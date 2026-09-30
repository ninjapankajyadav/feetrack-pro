from customtkinter import *
from tkinter import ttk
from Tuitionfee_DB import tuitionDB
db = tuitionDB()




class ReportPage(CTkFrame):
                                                    
    def __init__(self, parent,db):
                                                                  
        super().__init__(parent, fg_color="transparent")
                                                        
        CTkLabel(self, text="Report Page", text_color="#eeeee4", font=("Arial Black", 20)
            ).grid()
        self.selected_id = None
                                                                                       
        self.selected_card = None

        self.db = db
       

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)

        self.top_bar =CTkFrame(self,fg_color="transparent")

        self.top_bar.grid(row=0,column=0,padx=15,pady=15,sticky= "ew")


        CTkLabel(self.top_bar,text="Class",text_color="#fbff29",
                 font=("Arial Black", 15)
                ).grid(row=0,column=0,padx=15,pady=15,sticky ="w")

        self.class_menu = CTkOptionMenu(self.top_bar,width=180,height=35,
                                        values=['All Classes','1','2','3','4','5','6',
                                            '7','8','9','10','11','12',],
                                        font=("Arial Black", 15),
                                        text_color="#eeeee4",
                                        fg_color="#12263f",
                                        button_color="#1f3a5f",)
        self.class_menu.grid(row=1,column=0,padx=15,pady=15,sticky ="w")

        CTkLabel(self.top_bar,text="Payment status",
                text_color="#fbff29",
                font=("Arial Black", 15)
        ).grid(row= 0,column= 1,pady= 15,padx= 15,sticky= "w")

        self.payment_status =CTkOptionMenu(self.top_bar,width=180,height=35,
                                           values=["All Status","Paid","Unpaid"],
                                            font=("Arial Black", 15),
                                            text_color="#eeeee4",
                                            fg_color="#12263f",
                                            button_color="#1f3a5f",)
        self.payment_status.grid(row=1,column=1,padx=15,pady=15,sticky ="w")

        self.search_button = CTkButton(self.top_bar,width=120,height=35,
                                    text="🔍︎Apply filter ",
                                    fg_color="#05377e",
                                    text_color="#eeeee4",
                                    font=("Arial Black", 15),)
        self.search_button.grid(row=1, column=2, padx=15, pady=15, sticky="w")

        self.reset = CTkButton(self.top_bar,width=120,height=35,
                                    text="⭯Reset ",
                                    fg_color="#05377e",
                                    text_color="#eeeee4",
                                    font=("Arial Black", 15),)
        self.reset.grid(row=1, column=3, padx=15, pady=15, sticky="w")

        self.export =CTkButton(self.top_bar,width=120,height=35,
                                    text="📊Export",
                                    fg_color="#05377e",
                                    text_color="#eeeee4",
                                    font=("Arial Black", 15),)
        self.export.grid(row=1, column=4, padx=15, pady=15, sticky="w")


#----------------------------------------- Treeview TK -----------------------------------------------
    
       
        
        self.rowconfigure(1,weight=1)

       
        tree_view = CTkFrame(
            self,
            fg_color="transparent"
        )

        tree_view.grid(
            row=1,
            column=0,
            padx=15,
            pady=15,
            sticky="nsew"
        )

        tree_view.grid_rowconfigure(1, weight=1)
        tree_view.grid_columnconfigure(0, weight=1)

        CTkLabel(
            tree_view,
            text="Report Over View",
            text_color="#fbff29",
            font=("Arial Black", 15)
        ).grid(
            row=0,
            column=0,
            padx=15,
            pady=(0, 10),
            sticky="w"
        )

        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Report.Treeview",
            background="#0b1a2e",
            foreground="white",
            fieldbackground="#0b1a2e",
            rowheight=32,
            font=("Arial", 11)
        )

        style.configure(
            "Report.Treeview.Heading",
            background="#0b1a2e",
            foreground="white",
            font=("Arial Black", 11),
            relief="solid"
        )

        style.map(
            "Report.Treeview",
            background=[("selected", "#1f3a5f")],
            foreground=[("selected", "white")]
        )

        self.tree = ttk.Treeview(
            tree_view,
            columns=(
                "ID",
                "Name",
                "Class",
                "Phone No",
                "Monthly Fee",
                "Status"
            ),
            show="headings",
            style="Report.Treeview",
            height=12
        )

        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Class", text="Class")
        self.tree.heading("Phone No", text="Phone No")
        self.tree.heading("Monthly Fee", text="Monthly Fee")
        self.tree.heading("Status", text="Status")

        self.tree.column("ID", width=70, anchor="center")
        self.tree.column("Name", width=200, anchor="center")
        self.tree.column("Class", width=100, anchor="center")
        self.tree.column("Phone No", width=180, anchor="center")
        self.tree.column("Monthly Fee", width=150, anchor="center")
        self.tree.column("Status", width=120, anchor="center")

        self.tree.grid(
            row=1,
            column=0,
            sticky="nsew"
        )

        scroll = ttk.Scrollbar(
            tree_view,
            orient="vertical",
            command=self.tree.yview
        )

        scroll.grid(
            row=1,
            column=1,
            sticky="ns"
        )

        self.tree.configure(
            yscrollcommand=scroll.set
        )


        self.load_student()
        self.class_menu.configure(command = lambda _: self.class_value())
        self.payment_status.configure(command = lambda _: self.class_value())
        self.search_button.configure(command = self.class_value)
        self.reset.configure(command = self.reset_button)



# ------------------------------- Method/Funtions ----------------------------------------


    def load_student(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        # Row colors
        self.tree.tag_configure(
            "even",
            background="#969696",
            foreground="black"
        )

        self.tree.tag_configure(
            "odd",
            background="#001d43",
            foreground="white"
        )

        # Status colors
        self.tree.tag_configure(
            "paid",
            foreground="#00ff66"
        )

        self.tree.tag_configure(
            "pending",
            foreground="#c80000"
        )

        rows = self.db.get_all_students()

        for i, row in enumerate(rows):

            row_tag = "even" if i % 2 == 0 else "odd"

            if row[5] == "P":
                status_display = "Paid"
                status_tag = "paid"
            else:
                status_display = "Pending"
                status_tag = "pending"

            self.tree.insert(
                "",
                "end",
                values=(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    status_display
                ),
                tags=(row_tag, status_tag)
            )

        

    def class_value(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        rows = self.db.get_all_students()
        selected_class = self.class_menu.get()
        selected_status = self.payment_status.get()

        for row in rows:
            if selected_class != "All Classes" and str(row[2]) != selected_class:
                continue

            if selected_status == "Paid" and row[5] != "P":
                continue
            if selected_status == "Unpaid" and row[5] == "P":
                continue

            status_display = "Paid" if row[5] == "P" else "Pending"
            tag = "paid" if row[5] == "P" else "pending"

            self.tree.insert(
                "",
                "end",
                values=(row[0], row[1], row[2], row[3], row[4], status_display),
                
                tags=(tag,),
                
            )
            print("REPORT tree children:", len(self.tree.get_children()))
   
    def reset_button(self):
       self.class_menu.set("All Classes")
       self.payment_status.set("All Status")
       self.load_student()
       
        



        


        
