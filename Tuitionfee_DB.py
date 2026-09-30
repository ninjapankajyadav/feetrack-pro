from decimal import Decimal, InvalidOperation
import os
from dotenv import load_dotenv

load_dotenv()

                                                                                               
import mysql.connector as connector


                                                                       
class tuitionDB:
                                                    
    def __init__(self):
                                                                               
        self.con = connector.connect(
                                                        
            host="localhost", user="root", password=os.getenv("DB_PASSWORD"), database="tuitionfee"
                                                                            
        )
                                                                               
        self.cursor = self.con.cursor()
                       

                           

                                                    
        query = """CREATE TABLE IF NOT EXISTS student (
        student_id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(100) NOT NULL,
        class INT NOT NULL,
        phone BIGINT NOT NULL,
        fee INT NOT NULL,
        status ENUM('P', 'UN') DEFAULT 'UN') """

                                                                               
        self.cursor.execute(query)
                                                            
        print("Student Table created successfully")

                           

                                                    
        query2 = """create table if not exists invoice(
        invoice_id int primary key auto_increment,
        student_id int,
        month varchar(100) NOT NULL,
        amount decimal(10,2) NOT NULL,
        payment_states ENUM('P','UN') DEFAULT 'UN' NOT NULL,
        payment_date DATE,
        receipt_no VARCHAR(20) UNIQUE,
        payment_method VARCHAR(50),
        note TEXT,
        FOREIGN KEY (student_id) REFERENCES student(student_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
        )"""
                                                    
        cur = self.con.cursor()
                                                   
        cur.execute(query2)
                                                                               
        self.ensure_invoice_columns()
                                                            
        print("Invoice Table created successfully")

                                                                  
    def ensure_invoice_columns(self):
                                                    
        cur = self.con.cursor()
                                                            
        columns = {
                                                                      
            "payment_method": "VARCHAR(50)",
                                                                      
            "note": "TEXT",
                                                                      
            "updated_at": "DATETIME NULL",
                                                                      
            "edit_summary": "TEXT",
                                                                            
        }

                                                            
        for col_name, col_type in columns.items():
                                                                       
            try:
                                                           
                cur.execute(f"ALTER TABLE invoice ADD COLUMN {col_name} {col_type}")
                                                            
            except connector.Error as e:
                                                            
                msg = str(e).lower()
                                                                                        
                if "duplicate column" not in msg and "already exists" not in msg:
                                                                              
                    raise

                        
                                                    
        query3 = """create table if not exists fee(
        id INT AUTO_INCREMENT PRIMARY KEY,
        student_id INT,
        amount INT,
        month VARCHAR(15),
        year INT,
        status CHAR(3),  -- P / UN
        date_paid DATE,
        FOREIGN KEY (student_id) REFERENCES student(student_id))"""
                                                                               
        self.cursor.execute(query3)
                                                            
        print("fee Table created successfully")



                             

                                                          
    def insert_student(self, name, student_class, phone, fee, status):
                                                    
        query = """INSERT INTO student (name, class,phone, fee, status) VALUES (%s, %s, %s, %s, %s)"""
                                                    
        values = (name, student_class, phone, fee, status)
                                                    
        cur = self.con.cursor()
                                                   
        cur.execute(query, values)
                                                                               
        self.con.commit()
                                                            
        print("Student data added successfully")

                         

                                                          
    def insert_invoice(self, student_id, month, payment_states, payment_method, note, payment_date):
                                                    
        cur = self.con.cursor()

                                                   
        cur.execute("SELECT fee FROM student WHERE student_id = %s", (student_id,))
                                                        
        result = cur.fetchone()

                                                                                
        if result is None:
                                                                
            print("Student not found")
                                                          
            return
                                                    
        amount = result[0]



                                                    
        query = """INSERT INTO invoice (student_id, month, amount, payment_states, payment_date, payment_method, note)
            VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                                                   
        cur.execute(query, (student_id, month, amount, payment_states, payment_date, payment_method, note))
                                                                               
        self.con.commit()

                                                    
        invoice_id = cur.lastrowid
                                                    
        receipt_no = f"RCP-{invoice_id:05d}"

                                                   
        cur.execute("UPDATE invoice SET receipt_no=%s WHERE invoice_id=%s", (receipt_no, invoice_id))
                                                   
        cur.execute("UPDATE student SET status=%s WHERE student_id=%s", (payment_states, student_id))
                                                                               
        self.con.commit()

                                                            
        print("Invoice added successfully, Amount:", amount, "Receipt:", receipt_no)


        

          
                                                       
    def get_student(self, student_id):
                                                    
        query1 = """SELECT * FROM student WHERE student_id= %s"""
                                                                               
        self.cursor.execute(query1, (student_id,))
                                                      
        return self.cursor.fetchone()


                                                            
    def get_student_fees(self, student_id):
                                                    
        query2 = """SELECT month, year, amount, status FROM fee WHERE student_id= %s"""
                                                                               
        self.cursor.execute(query2, (student_id,))
                                                      
        return self.cursor.fetchall()


                                                   
    def add_fee(self, student_id, amount, month, year, status):
                                                    
        query = """INSERT INTO fee (student_id, amount, month, year, status)
                VALUES (%s, %s, %s, %s, %s)"""
                                                                               
        self.cursor.execute(query, (student_id, amount, month, year, status))
                                                                               
        self.con.commit()

                         
                                                            
    def get_all_students(self):

        query = "SELECT * FROM student"

        cur = self.con.cursor()
        cur.execute(query)

        rows = cur.fetchall()

        for row in rows:
            print("Student ID:", row[0])
            print("Name:", row[1])
            print("Class:", row[2])
            print("Phone:", row[3])
            print("Fee:", row[4])
            print("Status:", row[5])

        return rows
                                         

                                                        
    def view_student(self):
                                                    
        query = " select * from student "
                                                    
        cur = self.con.cursor()
                                                   
        cur.execute(query)
                                                            
        for row in cur:
                                                                
            print("***********************")
                                                                
            print("STUDENT ID = ", row[0])
                                                                
            print("STUDENT NAME = ", row[1])
                                                                
            print("STUDENT CLASS = ", row[2])
                                                                
            print("STUDENT PHONE = ", row[3])
                                                                
            print("STUDENT FEE = ", row[4])
                                                                
            print("STUDENT STATUS = ", row[5])
                                                                
            print("************************")

                         

                                                        
    def view_invoice(self):
                                                    
        query = " select * from invoice "
                                                    
        cur = self.con.cursor()
                                                   
        cur.execute(query)
                                                            
        for row in cur:
                                                                
            print("***********************")
                                                                
            print("INVOICE ID = ", row[0])
                                                                
            print("STUDENT ID = ", row[1])
                                                                
            print("MONTH = ", row[2])
                                                                
            print("AMOUNT = ", row[3])
                                                                
            print("PAYMENT STATES = ", row[4])
                                                                
            print("PAYMENT DATE = ", row[5])
                                                                
            print("************************")

                                                               
    def get_recent_invoices(self, limit=10):
                                                    
        query = """
            SELECT i.invoice_id, s.student_id, s.name, s.class, s.phone, i.amount,
                   i.month, i.payment_states, i.payment_date, i.receipt_no,
                   i.payment_method, i.note, i.updated_at, i.edit_summary
            FROM invoice i
            INNER JOIN student s ON s.student_id = i.student_id
            ORDER BY i.invoice_id DESC
            LIMIT %s
        """
                                                    
        cur = self.con.cursor()
                                                   
        cur.execute(query, (limit,))
                                                      
        return cur.fetchall()

                                                          
    def count_invoices(self):
                                                    
        cur = self.con.cursor()
                                                   
        cur.execute("SELECT COUNT(*) FROM invoice")
                                                        
        result = cur.fetchone()
                                                      
        return result[0] if result else 0

                           

                                                          
    def update_student(self, student_id, new_name, new_class, new_phone, new_fee, new_status):
                                                    
        query = """UPDATE student SET name = %s, class = %s,
        phone = %s, fee = %s, status = %s WHERE student_id = %s"""
                                                    
        values = (new_name, new_class, new_phone, new_fee, new_status, student_id)
                                                    
        cur = self.con.cursor()
                                                   
        cur.execute(query, values)
                                                                               
        self.con.commit()
                                                            
        print("** UPDATED **")

                           

                                                          
    def update_invoice(self, invoice_id, new_student_id=None, new_month=None, new_amount=None,
                                                                  
                      new_payment_states=None, new_payment_date=None,
                                                                  
                      new_payment_method=None, new_note=None):
                                                    
        cur = self.con.cursor()

                                                   
        cur.execute(
                                                                      
            "SELECT student_id, month, amount, payment_states, payment_date," \
            " payment_method, note FROM invoice WHERE invoice_id = %s",
                                                                      
            (invoice_id,),
                                                                            
        )
                                                        
        current = cur.fetchone()
                                                                                
        if current is None:
                                                                      
            raise ValueError("Invoice not found")

                                                                                
        if new_student_id is None:
                                                        
            new_student_id = current[0]
                                                                                
        if new_month is None:
                                                        
            new_month = current[1]
                                                                                
        if new_amount is None:
                                                        
            new_amount = current[2]
                                                                                
        if new_payment_states is None:
                                                        
            new_payment_states = current[3]
                                                                                
        if new_payment_date is None:
                                                        
            new_payment_date = current[4]
                                                                                
        if new_payment_method is None:
                                                        
            new_payment_method = current[5]
                                                                                
        if new_note is None:
                                                        
            new_note = current[6]

                                                    
        field_names = (
                                                                      
            "Student ID",
                                                                      
            "Month",
                                                                      
            "Amount",
                                                                      
            "Status",
                                                                      
            "Payment Date",
                                                                      
            "Method",
                                                                      
            "Note",
                                                                            
        )
                                                    
        new_values = (
                                                                      
            new_student_id,
                                                                      
            new_month,
                                                                      
            new_amount,
                                                                      
            new_payment_states,
                                                                      
            new_payment_date,
                                                                      
            new_payment_method,
                                                                      
            new_note,
                                                                            
        )
                                                      
        changes = []
                                                            
        for field, old, new in zip(field_names, current, new_values):
                                                        
            old_text = "" if old is None else str(old)
                                                        
            new_text = "" if new is None else str(new)
                                                                                    
            if field == "Amount":
                                                                           
                try:
                                                                
                    changed = Decimal(old_text) != Decimal(new_text)
                                                                
                except (InvalidOperation, ValueError):
                                                                
                    changed = old_text != new_text
                                                                      
            else:
                                                            
                changed = old_text != new_text

                                                                                    
            if changed:
                                                                          
                changes.append(f"{field}: {old_text} -> {new_text}")

                                                    
        edit_summary = "; ".join(changes) if changes else "No changes"

                                                    
        query = """
            UPDATE invoice
            SET student_id = %s,
                month = %s,
                amount = %s,
                payment_states = %s,
                payment_date = %s,
                payment_method = %s,
                note = %s,
                updated_at = NOW(),
                edit_summary = %s
            WHERE invoice_id = %s
        """
                                                    
        values = (
                                                                      
            new_student_id,
                                                                      
            new_month,
                                                                      
            new_amount,
                                                                      
            new_payment_states,
                                                                      
            new_payment_date,
                                                                      
            new_payment_method,
                                                                      
            new_note,
                                                                      
            edit_summary,
                                                                      
            invoice_id,
                                                                            
        )
                                                   
        cur.execute(query, values)
                                                                               
        self.con.commit()
                                                            
        print("** UPDATED **")
                                                      
        return edit_summary

                          

                                                          
    def delete_student(self, student_id):
                                                    
        query = """ delete from student where student_id = %s """
                                                    
        values = (student_id,)
                                                            
        print(query, values)
                                                    
        cur = self.con.cursor()
                                                   
        cur.execute(query, values)
                                                                               
        self.con.commit()
                                                            
        print("!!! DELETED !!!")

    def get_recent_invoice_2(self, limit=10):
        query = """
            SELECT i.invoice_id, s.name, s.class, i.month, i.amount,
                i.payment_states, i.payment_date
            FROM invoice i
            INNER JOIN student s ON s.student_id = i.student_id
            ORDER BY i.invoice_id DESC
            LIMIT %s
        """
        cur = self.con.cursor()
        cur.execute(query, (limit,))
        return cur.fetchall()
                        

                                                           
    def search_student(self, column, value):
                                                    
        cur = self.con.cursor()

                                                                                
        if column not in ("id", "name", "phone", "class"):
                                                                      
            raise ValueError("invalid column")

                                                                                
        if column =="id":
                                                       
            cur.execute("SELECT * FROM STUDENT WHERE student_id = %s",(value,))
                
                                                                                   
        elif column == "class":
                                                       
            cur.execute("SELECT * FROM student WHERE class = %s", (value,))
                                                                  
        else:
                                                       
            cur.execute(f"SELECT * FROM student WHERE {column} LIKE %s", (f"%{value}%",))
                                                      
        return cur.fetchall()

                          

                                                          
    def delete_invoice(self, invoice_id):
                                                    
        cur = self.con.cursor()
                                                   
        cur.execute("SELECT student_id FROM invoice WHERE invoice_id = %s", (invoice_id,))
                                                        
        row = cur.fetchone()
                                                    
        student_id = row[0] if row else None

                                                    
        query = "delete from invoice where invoice_id = %s"
                                                   
        cur.execute(query, (invoice_id,))

                                                                                
        if student_id is not None:
                                                       
            cur.execute(
                                                                          
                "SELECT COUNT(*) FROM invoice WHERE student_id = %s AND payment_states = 'P'",
                                                                          
                (student_id,),
                                                                                
            )
                                                            
            paid_count = cur.fetchone()[0]
                                                        
            new_status = "P" if paid_count > 0 else "UN"
                                                       
            cur.execute("UPDATE student SET status = %s WHERE student_id = %s", (new_status, student_id))

                                                                               
        self.con.commit()
                                                            
        print("!!! DELETED !!!")

                      
                                                            
    def view_full_report(self):
                                                    
        query = '''
            SELECT 
                student.name,
                student.class,
                invoice.month,
                invoice.amount,
                invoice.payment_states,
                invoice.payment_date
            FROM student
            INNER JOIN invoice
            ON student.student_id = invoice.student_id;
        '''

                                                    
        cur = self.con.cursor()
                                                   
        cur.execute(query)

                                                               
        rows = cur.fetchall()

                                                            
        for row in rows:
                                                                
            print(row)
        
                           
    def get_student1(self, student_id=None, name=None, student_class=None, phone=None, fee=None, status=None):
        conditions = []
        values = []

        if student_id is not None:
            conditions.append("student_id = %s")
            values.append(student_id)
        if name is not None:
            conditions.append("name = %s")
            values.append(name)
        if student_class is not None:
            conditions.append("class = %s")
            values.append(student_class)
        if phone is not None:
            conditions.append("phone = %s")
            values.append(phone)
        if fee is not None:
            conditions.append("fee = %s")
            values.append(fee)
        if status is not None:
            conditions.append("status = %s")
            values.append(status)

        if not conditions:
            raise ValueError("At least one filter required")

        query = f"SELECT * FROM student WHERE {' AND '.join(conditions)}"
        self.cursor.execute(query, tuple(values))
        return self.cursor.fetchall()
                                                                  
    def get_student_by_status(self, status):
                                                    
        query = "SELECT * FROM student WHERE status = %s"
                                                                               
        self.cursor.execute(query, (status,))
                                                      
        return self.cursor.fetchall()

    def get_pending_student(self):
        self.cursor.execute("SELECT * FROM student WHERE status != 'P'")
        return self.cursor.fetchall()
                                                        
    def mark_as_paid(self, invoice_id):
                                                    
        cur = self.con.cursor()

                                                    
        query = """
        UPDATE invoice
        SET payment_states = 'P',
            payment_date = CURDATE()
        WHERE invoice_id = %s
        AND payment_states = 'UN'
        """

                                                   
        cur.execute(query, (invoice_id,))
                                                                               
        self.con.commit()

                                                                                
        if cur.rowcount > 0:
                                                                
            print("Payment marked as PAID")
                                                                  
        else:
                                                                
            print("Already paid or invoice not found")
    
                             

    def search_students(self, column, value):
        allowed_columns = {"id", "class", "name", "phone"}
        if column not in allowed_columns:
            raise ValueError("Invalid search column")
        if column == "name":
            query = "SELECT * FROM student WHERE LOWER(name) LIKE %s"
            param = f"%{value.lower()}%"
        else:
            query = f"SELECT * FROM student WHERE {column} = %s"
            param = value
        self.cursor.execute(query, (param,))
        return self.cursor.fetchall()
                                                                               
    
    def load_reportdata(self):

        cur = self.con.cursor(dictionary=True)

        cur.execute("""
            SELECT payment_states, COUNT(*) AS total
            FROM invoice
            GROUP BY payment_states
        """)

        rows = cur.fetchall()

        paid = 0
        unpaid = 0

        for row in rows:
            if row["payment_states"] == "P":
                paid = row["total"]
            elif row["payment_states"] == "UN":
                unpaid = row["total"]
        return {
            "paid": paid,
            "unpaid": unpaid
        }
                                 
                            
                                 
                               
                                      
               
                                                               

                                   
    
                                     
                     
                                                                              
                        
                                                       
                                       
                                                
             

                                 
                            
                                  

                         
                                                       
               
                                                            
                                 
                                              
                                        
                                         
                                                 
                                                        
                
                                                                        
if __name__ == "__main__":
                                                
    db = tuitionDB()
                                                              
    db.view_student()
    
