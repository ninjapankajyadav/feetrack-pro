from customtkinter import *
                                                                                                                         
from tkinter import ttk
                                                               
from tkinter import messagebox
                                                                                                                                                   
from Tuitionfee_DB import tuitionDB
                                                                    
                                   
db = tuitionDB()


class StudentPage(CTkFrame):
                                                    
    def __init__(self, parent, db):
                                                                  
        super().__init__(parent, fg_color="transparent")
                                                                               
        self.db = db
                                                                               
        self.selected_id = None

                    
                                                                               
        self.grid_columnconfigure(0, weight=1)
                                                                               
        self.grid_columnconfigure(1, weight=3)
                                                                               
        self.grid_columnconfigure(2, weight=0)
                                                                               
        self.grid_rowconfigure(0, weight=0)                                    
                                                                               
        self.grid_rowconfigure(1, weight=1)                                
                                                                               
        self.grid_rowconfigure(2, weight=0)                 


                                                                                                                            
        
                                                        
        add_frame = CTkFrame(
                                                                      
            self,
                                                        
            fg_color="#0b1a2e",
                                                        
            corner_radius=25,
                                                        
            border_width=5,
                                                        
            border_color="#1f3a5f",
                                                                            
        )
                                                                      
        add_frame.grid(row=0, column=0, rowspan=2, padx=25, pady=(15, 5), sticky="nsew")

                                                        
        CTkLabel(
                                                                      
            add_frame,
                                                        
            text="ADD STUDENT",
                                                        
            font=("Arial Black", 16),
                                                        
            text_color="#eeeee4",
                                                                      
        ).pack(pady=(15, 5))

                                                                               
        self.nameentry = CTkEntry(add_frame, placeholder_text="NAME", width=200)
                                                                               
        self.nameentry.pack(pady=5)

                                                      
        clas = [
                                                                      
            "SELECT CLASS",
                                                                      
            "1",
                                                                      
            "2",
                                                                      
            "3",
                                                                      
            "4",
                                                                      
            "5",
                                                                      
            "6",
                                                                      
            "7",
                                                                      
            "8",
                                                                      
            "9",
                                                                      
            "10",
                                                                      
            "11",
                                                                      
            "12",
                                                                            
        ]
                                                                               
        self.classentry = CTkOptionMenu(add_frame, values=clas, width=200)
                                                                               
        self.classentry.pack(pady=5)

                                                                               
        self.phonentry = CTkEntry(add_frame, placeholder_text="PHONE", width=200)
                                                                               
        self.phonentry.pack(pady=5)

                                                                               
        self.feeentry = CTkEntry(add_frame, placeholder_text="FEE", width=200)
                                                                               
        self.feeentry.pack(pady=5)

                                  
                                                        
        CTkLabel(
                                                                      
            add_frame,
                                                        
            text="Fee Status:",
                                                        
            text_color="#eeeee4",
                                                        
            font=("Arial Black", 12),
                                                                      
        ).pack(pady=(8, 2))

                                                                               
        self.status_var = StringVar(value="UN")
                                                        
        radio_frame = CTkFrame(add_frame, fg_color="transparent")
                                                                      
        radio_frame.pack()
                                                        
        CTkRadioButton(
                                                                      
            radio_frame,
                                                        
            text="Paid",
                                                        
            variable=self.status_var,
                                                        
            value="P",
                                                        
            text_color="white",
                                                                      
        ).pack(side="left", padx=10)
                                                        
        CTkRadioButton(
                                                                      
            radio_frame,
                                                        
            text="Pending",
                                                        
            variable=self.status_var,
                                                        
            value="UN",
                                                        
            text_color="white",
                                                                      
        ).pack(side="left", padx=10)

                                                        
        CTkButton(
                                                                      
            add_frame,
                                                        
            text=" Save Student",
                                                        
            width=200,
                                                        
            fg_color="#f78222",
                                                        
            hover_color="#d4691a",
                                                        
            text_color="black",
                                                        
            font=("Arial Black", 13),
                                                        
            command=self.save_student,
                                                                      
        ).pack(pady=15)

                                                                                                                     
                                                    
        style = ttk.Style()
                                                                  
        style.theme_use("clam")
                                                                  
        style.configure(
                                                                      
            "Treeview",
                                                        
            background="#0b1a2e",
                                                        
            foreground="white",
                                                        
            fieldbackground="#0b1a2e",
                                                        
            rowheight=32,
                                                                            
        )
                                                                  
        style.configure(
                                                                      
            "Treeview.Heading",
                                                        
            background="#12263f",
                                                        
            foreground="white",
                                                        
            relief="solid",
                                                        
            borderwidth=1,
                                                                            
        )
                                                                  
        style.map(
                                                                      
            "Treeview",
                                                          
            background=[("selected", "#1f3a5f")],
                                                          
            foreground=[("selected", "white")],
                                                                            
        )

                                                                               
        self.tree = ttk.Treeview(
                                                                      
            self,
                                                        
            columns=("id", "name", "class", "phone", "fee", "status"),
                                                        
            show="headings",
                                                                            
        )
                                                                               
        self.tree.heading("id", text="ID")
                                                                               
        self.tree.heading("name", text="Name")
                                                                               
        self.tree.heading("class", text="Class")
                                                                               
        self.tree.heading("phone", text="Phone")
                                                                               
        self.tree.heading("fee", text="Fee")
                                                                               
        self.tree.heading("status", text="Status")

                                                                               
        self.tree.column("id", width=50, stretch=False)
                                                                               
        self.tree.column("name", width=130, stretch=True)
                                                                               
        self.tree.column("class", width=70, stretch=False)
                                                                               
        self.tree.column("phone", width=120, stretch=True)
                                                                               
        self.tree.column("fee", width=90, stretch=False)
                                                                               
        self.tree.column("status", width=90, stretch=False)

                                                                               
        self.tree.grid(row=1, column=1, sticky="nsew", padx=(0, 0), pady=5)
                                                                               
        self.tree.bind("<<TreeviewSelect>>", self.on_row_select)

                                                    
        scroll = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
                                                                               
        self.tree.configure(yscrollcommand=scroll.set)
                                                                      
        scroll.grid(row=1, column=2, sticky="ns", padx=(0, 5), pady=5)

                                                                                                                

                                                        
        search_bar = CTkFrame(self, fg_color="#0b1a2e", corner_radius=10)
                                                                      
        search_bar.grid(row=0, column=1, columnspan=2, sticky="ew", padx=(0, 5), pady=(10, 2))

                                                                               
        self.search_entry = CTkEntry(
                                                                      
            search_bar, placeholder_text="Search...", width=220,
                                                        
            fg_color="#12263f", border_color="#1f3a5f", text_color="white"
                                                                            
        )
                                                                               
        self.search_entry.pack(side="left", padx=(10, 5), pady=8)
                                                                               
        self.search_entry.bind("<Return>", lambda e: self.search_students())

                                                                               
        self.filter_var = StringVar(value="Name")
                                                                  
        CTkOptionMenu(
                                                                      
            search_bar,
                                                          
            values=["Name", "Class", "Phone"],
                                                        
            variable=self.filter_var,
                                                        
            width=110,
                                                        
            fg_color="#12263f",
                                                        
            button_color="#1f3a5f",
                                                        
            text_color="white",
                                                                      
        ).pack(side="left", padx=5)

                                                        
        CTkButton(
                                                                      
            search_bar, text="Search", width=90,
                                                        
            fg_color="#f78222", hover_color="#d4691a",
                                                        
            text_color="black", font=("Arial Black", 12),
                                                        
            command=self.search_students,
                                                                      
        ).pack(side="left", padx=5)



                                                                                                                                  

                                                        
        bottom_panel = CTkFrame(self, fg_color="#0b1a2e", corner_radius=15)
                                                                      
        bottom_panel.grid(row=2, column=0, columnspan=3, sticky="ew", padx=10, pady=10)
        
                                                        
        CTkLabel(bottom_panel,
                                                        
            text="SELECTED STUDENT DETAILS",
                                                        
            font=("Arial Black", 14),
                                                        
            text_color="#eeeee4",
                                                                      
        ).pack(pady=(10, 5))

                                                        
        result_frame = CTkFrame(bottom_panel, fg_color="transparent")
                                                                      
        result_frame.pack(padx=10, pady=5, fill="x")

                      
                                                      
        fields = ["Name", "Class", "Phone", "Fee", "Status"]
                                                            
        for i, field in enumerate(fields):
                                                            
            CTkLabel(
                                                                          
                result_frame,
                                                            
                text=field + ":",
                                                            
                font=("Arial Black", 12),
                                                            
                text_color="#aaaaaa",
                                                                          
            ).grid(row=0, column=i * 2, sticky="w", padx=(20, 2))

                      
                                                                               
        self.result_name = CTkLabel(result_frame, text="-", text_color="white")
                                                                               
        self.result_class = CTkLabel(result_frame, text="-", text_color="white")
                                                                               
        self.result_phone = CTkLabel(result_frame, text="-", text_color="white")
                                                                               
        self.result_fee = CTkLabel(result_frame, text="-", text_color="white")
                                                                               
        self.result_status = CTkLabel(result_frame, text="-", text_color="orange")

                                                      
        result_values = [
                                                                                   
            self.result_name,
                                                                                   
            self.result_class,
                                                                                   
            self.result_phone,
                                                                                   
            self.result_fee,
                                                                                   
            self.result_status,
                                                                            
        ]
                                                            
        for i, val in enumerate(result_values):
                                                                          
            val.grid(row=1, column=i * 2, sticky="w", padx=(20, 2), pady=4)

                               
                                                        
        btn_frame = CTkFrame(bottom_panel, fg_color="transparent")
                                                                      
        btn_frame.pack(pady=(5, 12))

                                                        
        CTkButton(
                                                                      
            btn_frame,
                                                        
            text="EDIT",
                                                        
            width=120,
                                                        
            fg_color="transparent",
                                                        
            border_color="#00bcd4",
                                                        
            border_width=2,
                                                        
            text_color="#00bcd4",
                                                        
            hover_color="#0b2a2e",
                                                        
            command=self.edit_student,
                                                                      
        ).pack(side="left", padx=15)

                                                        
        CTkButton(
                                                                      
            btn_frame,
                                                        
            text=" DELETE",
                                                        
            width=120,
                                                        
            fg_color="transparent",
                                                        
            border_color="#f44336",
                                                        
            border_width=2,
                                                        
            text_color="#f44336",
                                                        
            hover_color="#2e0b0b",
                                                        
            command=self.delete_student,
                                                                      
        ).pack(side="left", padx=15)

                            
                                                                               
        self.load_students()

                                                                                                         



                                                         
    def load_students(self):
                                                                  
        """Fetch all students from DB and populate treeview."""

                                                            
        for row in self.tree.get_children():
                                                                                   
            self.tree.delete(row)

                                                                               
        self.tree.tag_configure("paid", foreground="#00ff66")
                                                                               
        self.tree.tag_configure("pending", foreground="#fb542b")
                                                                               
        self.tree.tag_configure("odd", background="#0b1a2e")
                                                                               
        self.tree.tag_configure("even", background="#0f2238")

                                                    
        rows = self.db.get_all_students()
                                                            
        for i, row in enumerate(rows):
                                                        
            row_tag = "even" if i % 2 == 0 else "odd"
                                                        
            status_display = "Paid" if row[5] == "P" else "Pending"
                                                        
            status_tag = "paid" if status_display == "Paid" else "pending"
                                                                                   
            self.tree.insert(
                                                                          
                "",
                                                                          
                "end",
                                                            
                values=(row[0], row[1], row[2], row[3], row[4], status_display),
                                                            
                tags=(row_tag, status_tag),
                                                                                
            )

                                                         
    def on_row_select(self, event):
                                                                  
        """Fill detail panel when a row is clicked."""
                                                    
        selected = self.tree.selection()
                                                                                
        if not selected:
                                                          
            return
                                                    
        values = self.tree.item(selected[0], "values")
                                                                               
        self.selected_id = values[0]
                                                                               
        self.result_name.configure(text=values[1])
                                                                               
        self.result_class.configure(text=values[2])
                                                                               
        self.result_phone.configure(text=values[3])
                                                                               
        self.result_fee.configure(text=values[4])
                                                                               
        self.result_status.configure(text=values[5])

                                                        
    def save_student(self):
                                                                  
        """Insert new student into DB."""
                                                    
        name = self.nameentry.get().strip()
                                                    
        cls = self.classentry.get()
                                                    
        phone = self.phonentry.get().strip()
                                                    
        fee = self.feeentry.get().strip()
                                                    
        status = self.status_var.get()

                                                                                
        if not name or cls == "SELECT CLASS" or not phone or not fee:
                                                      
            messagebox.showerror("Error", "All fields are required!")
                                                          
            return

                                                                   
        try:
                                                                                   
            self.db.insert_student(name, int(cls), int(phone), int(fee), status)
                                                             
            messagebox.showinfo("Success", "Student saved successfully!")
                                                                                   
            self.nameentry.delete(0, "end")
                                                                                   
            self.phonentry.delete(0, "end")
                                                                                   
            self.feeentry.delete(0, "end")
                                                                                   
            self.classentry.set("SELECT CLASS")
                                                                                   
            self.status_var.set("UN")
                                                                                   
            self.load_students()
                                                        
        except Exception as e:
                                                      
            messagebox.showerror("DB Error", str(e))

                                                        
    def edit_student(self):
                                                                  
        """Open edit dialog for selected student."""
                                                                                
        if not self.selected_id:
                                                                      
            messagebox.showwarning("Warning", "Please select a student first!")
                                                          
            return

                    
                                                    
        dialog = CTkToplevel()
                                                                  
        dialog.title("Edit Student")
                                                                  
        dialog.geometry("320x380")
                                                                  
        dialog.grab_set()
                                                                  
        dialog.after(200, lambda: dialog.iconbitmap("openinglogo.ico"))
       
                                                                      
        CTkLabel(dialog, text="EDIT STUDENT", font=("Arial Black", 14)).pack(pady=10)

                                                        
        name_e = CTkEntry(dialog, width=250, placeholder_text="Name")
                                                                  
        name_e.insert(0, self.result_name.cget("text"))
                                                                      
        name_e.pack(pady=5)

                                                      
        clas = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
                                                    
        class_e = CTkOptionMenu(dialog, values=clas, width=250)
                                                                  
        class_e.set(self.result_class.cget("text"))
                                                                      
        class_e.pack(pady=5)

                                                        
        phone_e = CTkEntry(dialog, width=250, placeholder_text="Phone")
                                                                  
        phone_e.insert(0, self.result_phone.cget("text"))
                                                                      
        phone_e.pack(pady=5)

                                                        
        fee_e = CTkEntry(dialog, width=250, placeholder_text="Fee")
                                                                  
        fee_e.insert(0, self.result_fee.cget("text"))
                                                                      
        fee_e.pack(pady=5)

                                                    
        status_v = StringVar(
                                                        
            value="P" if self.result_status.cget("text") == "Paid" else "UN"
                                                                            
        )
                                                        
        r_frame = CTkFrame(dialog, fg_color="transparent")
                                                                      
        r_frame.pack(pady=5)
                                                                      
        CTkRadioButton(r_frame, text="Paid", variable=status_v, value="P").pack(
                                                        
            side="left", padx=10
                                                                            
        )
                                                                      
        CTkRadioButton(r_frame, text="Pending", variable=status_v, value="UN").pack(
                                                        
            side="left", padx=10
                                                                            
        )

                                                         
        def save_edit():
                                                                       
            try:
                                                                                       
                self.db.update_student(
                                                                                           
                    self.selected_id,
                                                                              
                    name_e.get().strip(),
                                                                              
                    class_e.get(),
                                                                              
                    phone_e.get().strip(),
                                                                              
                    float(fee_e.get().strip()),
                                                                              
                    status_v.get(),
                                                                                    
                )
                                                                 
                messagebox.showinfo("Updated", "Student updated!")
                                                                          
                dialog.destroy()
                                                                                       
                self.load_students()
                                                            
            except Exception as e:
                                                          
                messagebox.showerror("Error", str(e))

                                                        
        CTkButton(
                                                                      
            dialog,
                                                        
            text="Save Changes",
                                                        
            width=200,
                                                        
            fg_color="#f78222",
                                                        
            text_color="black",
                                                        
            command=save_edit,
                                                                      
        ).pack(pady=15)



    

                                                          
    def delete_student(self):
                                                                  
        """Delete selected student from DB."""
                                                                                
        if not self.selected_id:
                                                                      
            messagebox.showwarning("Warning", "Please select a student first!")
                                                          
            return

                                                    
        confirm = messagebox.askyesno(
                                                                      
            "Confirm Delete", f"Delete student '{self.result_name.cget('text')}'?"
                                                                            
        )
                                                                                
        if confirm:
                                                                       
            try:
                                                                                       
                self.db.delete_student(self.selected_id)
                                                                 
                messagebox.showinfo("Deleted", "Student deleted!")
                                                                                       
                self.selected_id = None
                                                                                       
                self.result_name.configure(text="-")
                                                                                       
                self.result_class.configure(text="-")
                                                                                       
                self.result_phone.configure(text="-")
                                                                                       
                self.result_fee.configure(text="-")
                                                                                       
                self.result_status.configure(text="-")
                                                                                       
                self.load_students()
                                                            
            except Exception as e:
                                                          
                messagebox.showerror("Error", str(e))
    

                                                           
    def search_students(self):
                                                    
        query = self.search_entry.get().strip()
                                                    
        filter_by = self.filter_var.get()
                                                                                
        if not query:
                                                                                   
            self.load_students()
                                                          
            return

                                                            
        column_map = {"Name": "name", "Class": "class", "Phone": "phone"}
                                                    
        col = column_map[filter_by]

                                                    
        rows = self.db.search_students(col, query)

                                                            
        for row in self.tree.get_children():
                                                                                   
            self.tree.delete(row)

                                                                               
        self.tree.tag_configure("paid", foreground="#00ff66")
                                                                               
        self.tree.tag_configure("pending", foreground="#fb542b")
                                                                               
        self.tree.tag_configure("odd", background="#0b1a2e")
                                                                               
        self.tree.tag_configure("even", background="#0f2238")

                                                            
        for i, row in enumerate(rows):
                                                        
            row_tag = "even" if i % 2 == 0 else "odd"
                                                        
            status_display = "Paid" if row[5] == "P" else "Pending"
                                                        
            status_tag = "paid" if status_display == "Paid" else "pending"
                                                                                   
            self.tree.insert("", "end",
                                                            
                values=(row[0], row[1], row[2], row[3], row[4], status_display),
                                                            
                tags=(row_tag, status_tag),
                                                                                    
                )