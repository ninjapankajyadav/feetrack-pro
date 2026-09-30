from customtkinter import *

from tkinter import ttk

from Tuitionfee_DB import tuitionDB

db = tuitionDB()

class HomePage(CTkFrame):
    def __init__(self, parent, db, show_page):
        super().__init__(parent, fg_color="transparent")
        self.controller = parent   # ya jo bhi variable naam do
        self.db = db
        self.show_page = show_page
                               
        self.selected_id = None
                                                                                            
        self.selected_card = None

        # scroll frame

        self.scroll_frame = CTkScrollableFrame( self,fg_color="transparent")
        self.scroll_frame.pack(fill="both", expand=True)



        
        self.columnconfigure(0, weight=1)   # single column, full width

        

        self.frame1 = CTkFrame(self.scroll_frame, fg_color="transparent")
        self.frame1.grid(row=0, column=0, padx=15, pady=9, sticky="ew")
  

        self.frame1.grid_columnconfigure(0, weight=1) 


        title_label = CTkLabel(self.frame1, text="👨‍🎓 FeeTrack Pro",
                                text_color="#fbff29", font=("Segoe UI Emoji",20,"bold"))
        
        title_label.grid(row=0, column=0, padx=15, pady=(15,0))

        subtitle_label = CTkLabel(self.frame1, text="Manage Student . Generate Invoice . Keep Record",
                                text_color="#003ca3", font=("Segoe UI Emoji",15,"bold"))
        
        subtitle_label.grid(row=1, column=0, padx=15, pady=(0,15))


        self.frame2 = CTkFrame(self.scroll_frame, fg_color="transparent")
        self.frame2.grid(row=1, column=0, padx=15, pady=9, sticky="ew")


        welcome_bar = CTkLabel(self.frame2,text="Welcome Back, Admin! 👋",
                            text_color="#EAF2FB", font=("Segoe UI Emoji",20,"bold"))
        welcome_bar.grid(row= 0,column= 0,padx=15, pady=(15,0),sticky = "w")
        

        text_lab = CTkLabel(self.frame2,text="Manage Your Student, Create Invoice,Keep Track Of All the Payment ─── All In one Place",
                            text_color="#4FA3E3", font=("Arial Black", 12))
        text_lab.grid(row= 1,column= 0,padx= 4,pady=(0,15),sticky = "w")


        self.frame3 = CTkFrame(self.scroll_frame, fg_color="transparent")
        self.frame3.grid(row=2, column=0, padx=15, pady=9, sticky="ew")

        
        for i in range(4):
            self.frame3.grid_columnconfigure(i, weight=1)

        self.quick_label = CTkLabel(self.frame3, text="Quick Action",
                             text_color="#fbff29",font=("Segoe UI Emoji",20,"bold"))
        
        self.quick_label.grid(row=0, column=0, padx=15, pady=(15,0), sticky="w")


        self.student_page = CTkButton(self.frame3,
                            width=280, height=90,
                            text="➕ 👨‍🎓 Add Student\n Register a New Student",
                            text_color="#0e439f",
                            fg_color="#12263f",
                            hover_color="#1f3a5f",
                            font=("Segoe UI Emoji",20,"bold"),
                            command=lambda: self.show_page("StudentPage"))
        self.student_page.grid(row=1,column= 0,padx=15, pady=(15,0),sticky = "w")


        self.invoice_page = CTkButton(self.frame3,
                            width=280, height=90,
                            text="📝 Generate Invoice \n Create Invoice for Payment",
                            text_color="#148B2E",
                            fg_color="#12263f",
                            hover_color="#1f3a5f",
                            font=("Segoe UI Emoji",20,"bold"),
                            command=lambda: self.show_page("InvoicePage"))
        self.invoice_page.grid(row= 1,column= 1,padx=15, pady=(15,0),sticky = "w")


        self.view_page = CTkButton(self.frame3,
                            width=280, height=90, 
                            text="📊 View Report \n Check Payment & Report",
                            text_color="#420f6c",
                            fg_color="#12263f",
                            hover_color="#1f3a5f",
                            font=("Segoe UI Emoji",20,"bold"),
                            command=lambda: self.show_page("ReportPage"))
        self.view_page.grid(row=1,column= 2,padx=15, pady=(15,0),sticky = "w")


        self.setting_page = CTkButton(self.frame3,
                            width=220, height=90, 
                            text="⛯ Settings \n Configure Application",
                            text_color="#5d5458",
                            fg_color="#12263f",
                            hover_color="#1f3a5f",
                            font=("Segoe UI Emoji",20,"bold"),
                            command=lambda: self.show_page("SettingPage"))

        self.setting_page.grid(row=1,column= 3,padx=15, pady=(15,0),sticky = "w")

# ------------------------------------- Treeview ----------------------------------------

        self.columnconfigure(1,weight=1)
        self.rowconfigure(3,weight=0)

        self.frame4 = CTkFrame(self.scroll_frame, fg_color="transparent")
        self.frame4.grid(row=3, column=0, padx=15, pady=9, sticky="nsew")

        self.frame4.grid_columnconfigure(0, weight=1) 

        CTkLabel(self.frame4, text="Recent Invoice ",
                text_color="#fbff29",
                font=("Segoe UI Emoji", 25)).grid(row=0,
                column=0, padx=15,
                pady=(15, 0))
        
        self.frame4.rowconfigure(1,weight=1)
        self.frame4.columnconfigure(0,weight=1)

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Home.Treeview",
                        background="#0b1a2e",
                        foreground="white",
                        rowheight=32,
                        fieldbackground="#0b1a2e",
                        font=("Arial Black", 11))
        
        style.configure("Home.Horizontal.TScrollbar",
                        background="#1f3a5f",
                        troughcolor="#0b1a2e",
                        arrowcolor="white",
                        bordercolor="#0b1a2e")

        style.configure("Home.Treeview.Heading",
                        background="#0b1a2e",
                        foreground="white",
                        relief="solid",
                        font=("Arial Black", 11),
                        borderwidth=1)

        style.map("Home.Treeview",
                background=[("selected", "#1f3a5f")],
                foreground=[("selected", "white")])

        self.tree = ttk.Treeview(self.frame4,
                                columns=("invoice_no", "student_name",
                                "class_", "month", "amount", "status", "date"),
                                show="headings",
                                style="Home.Treeview")

        self.tree.heading("invoice_no", text="Invoice No.")
        self.tree.heading("student_name", text="Student Name")
        self.tree.heading("class_", text="Class")
        self.tree.heading("month", text="Month")
        self.tree.heading("amount", text="Amount (₹)")
        self.tree.heading("status", text="Status")
        self.tree.heading("date", text="Date")

        self.frame4.grid_columnconfigure(1, minsize=20)

        self.tree.column("invoice_no", width=125, minwidth=100, stretch=True)
        self.tree.column("student_name", width=150, minwidth=120, stretch=True)
        self.tree.column("class_", width=80, minwidth=70, stretch=True)
        self.tree.column("month", width=100, minwidth=90, stretch=True)
        self.tree.column("amount", width=100, minwidth=90, stretch=True)
        self.tree.column("status", width=100, minwidth=90, stretch=True)
        self.tree.column("date", width=130, minwidth=110, stretch=True)

        self.tree.grid(row=1, column=0, sticky="nsew", padx=(0, 0), pady=5)

        scroll = ttk.Scrollbar(self.frame4, orient="horizontal",
                    command=self.tree.xview,
                    style="Home.Horizontal.TScrollbar")
        
        scroll.grid(row=2, column=0, sticky="ew")

        self.tree.configure(xscrollcommand=scroll.set)

        self.recent_invoices()

    def recent_invoices(self):
        rows = self.db.get_recent_invoice_2()

        print("DEBUG rows:", rows)

        for row in rows:
            item = self.tree.insert(
                "",
                "end",
                values=(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6]
                )
            )
            print("Inserted item:", item)
            print("Values:", self.tree.item(item)["values"])

        print("All Treeview items:", self.tree.get_children())


