from customtkinter import *
from tkinter import messagebox
from tkinter import ttk


class SearchPage(CTkFrame):

    def __init__(self, parent, db):

        super().__init__(parent, fg_color="transparent")

        self.db = db
        self.selected_id = None
        self.selected_card = None

        # =========================================================
        # MAIN GRID
        # =========================================================

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=1)

        # =========================================================
        # SEARCH AREA
        # =========================================================

        self.search_student = CTkFrame(
            self,
            fg_color="transparent"
        )

        self.search_student.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=15,
            pady=(15, 5),
            sticky="ew"
        )

        # Search frame columns
        self.search_student.columnconfigure(0, weight=0)
        self.search_student.columnconfigure(1, weight=0)
        self.search_student.columnconfigure(2, weight=0)
        self.search_student.columnconfigure(3, weight=0)

        # ---------------------------------------------------------
        # Search By
        # ---------------------------------------------------------

        search_by = CTkLabel(
            self.search_student,
            text="Search By",
            text_color="#fbff29",
            font=("Arial Black", 15)
        )

        search_by.grid(
            row=0,
            column=0,
            padx=15,
            pady=(15, 5),
            sticky="w"
        )

        self.search_stu = CTkOptionMenu(
            self.search_student,
            width=150,
            height=35,
            values=[
                "ID",
                "Name",
                "Class",
                "Phone No"
            ],
            font=("Arial Black", 15),
            text_color="#eeeee4",
            fg_color="#12263f",
            button_color="#1f3a5f"
        )

        self.search_stu.grid(
            row=1,
            column=0,
            padx=15,
            pady=(15, 5),
            sticky="w"
        )

        # ---------------------------------------------------------
        # Enter Value
        # ---------------------------------------------------------

        enter = CTkLabel(
            self.search_student,
            text="Enter Value",
            text_color="#fbff29",
            font=("Arial Black", 15)
        )

        enter.grid(
            row=0,
            column=1,
            padx=15,
            pady=15,
            sticky="w"
        )

        self.enter_value = CTkEntry(
            self.search_student,
            width=550,
            height=35,
            text_color="#eeeee4",
            fg_color="#05377e",
            placeholder_text="Type Here...",
            font=("Arial Black", 15)
        )

        self.enter_value.grid(
            row=1,
            column=1,
            padx=15,
            pady=15,
            sticky="w"
        )

        # ---------------------------------------------------------
        # Search Button
        # ---------------------------------------------------------

        self.button = CTkButton(
            self.search_student,
            width=80,
            height=20,
            text="🔍 Search",
            fg_color="#05377e",
            text_color="#eeeee4",
            font=("Arial Black", 15),
            command=self.search_button
        )

        self.button.grid(
            row=1,
            column=2,
            padx=15,
            pady=15,
            sticky="w"
        )

        # ---------------------------------------------------------
        # Clear Button
        # ---------------------------------------------------------

        self.clear = CTkButton(
            self.search_student,
            width=80,
            height=20,
            text="🔄 Clear",
            text_color="#eeeee4",
            fg_color="#05377e",
            font=("Arial Black", 15),
            command=self.clear_button
        )

        self.clear.grid(
            row=1,
            column=3,
            padx=15,
            pady=15,
            sticky="w"
        )

        # =========================================================
        # QUICK FILTER
        # =========================================================

        quick_filter = CTkLabel(
            self.search_student,
            text="Quick Filter",
            text_color="#fbff29",
            font=("Arial Black", 15)
        )

        quick_filter.grid(
            row=2,
            column=0,
            padx=15,
            pady=(15, 5),
            sticky="w"
        )

        self.filter_frame = CTkFrame(
            self.search_student,
            fg_color="transparent"
        )

        self.filter_frame.grid(
            row=3,
            column=0,
            columnspan=4,
            padx=15,
            pady=15,
            sticky="w"
        )

        # ---------------------------------------------------------
        # All Students
        # ---------------------------------------------------------

        self.alstudent_filt = CTkButton(
            self.filter_frame,
            width=80,
            height=20,
            text="All Students",
            hover_color="#05377e",
            text_color="#eeeee4",
            font=("Arial Black", 15),
            command=self.load_students
        )

        self.alstudent_filt.grid(
            row=0,
            column=0,
            padx=15,
            pady=15
        )

        # ---------------------------------------------------------
        # By Class
        # ---------------------------------------------------------

        self.byclass_filt = CTkOptionMenu(
            self.filter_frame,
            width=120,
            height=20,
            values=[
                "By Class",
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
                "12"
            ],
            fg_color="#05377e",
            text_color="#eeeee4",
            font=("Arial Black", 15),
            command=self.class_filter
        )

        self.byclass_filt.grid(
            row=0,
            column=1,
            padx=15,
            pady=15
        )

        # ---------------------------------------------------------
        # By Status
        # ---------------------------------------------------------

        self.by_status_filt = CTkButton(
            self.filter_frame,
            width=80,
            height=20,
            text="By Status",
            hover_color="#05377e",
            text_color="#eeeee4",
            font=("Arial Black", 15),
            command=self.by_status_filter
        )

        self.by_status_filt.grid(
            row=0,
            column=2,
            padx=15,
            pady=15
        )

        # ---------------------------------------------------------
        # By Pending
        # ---------------------------------------------------------

        self.bypending_filt = CTkButton(
            self.filter_frame,
            width=80,
            height=20,
            text="By Pending",
            hover_color="#05377e",
            text_color="#eeeee4",
            font=("Arial Black", 15),
            command=self.by_pending_filter
        )

        self.bypending_filt.grid(
            row=0,
            column=3,
            padx=15,
            pady=15
        )

        # =========================================================
        # TREEVIEW STYLE
        # =========================================================

        style = ttk.Style()

        style.theme_use("clam")

        style.configure(
            "Treeview",
            background="#0b1a2e",
            foreground="white",
            fieldbackground="#0b1a2e",
            rowheight=32,
            font=("Arial", 10)
        )

        style.configure(
            "Treeview.Heading",
            background="#0b1a2e",
            foreground="white",
            relief="solid",
            borderwidth=1,
            font=("Arial", 10)
        )

        style.map( "Treeview",
        background=[("selected", "#1f3a5f")],
        foreground=[("selected", "white")])

        # =========================================================
        # TREEVIEW
        # =========================================================

        self.tree = ttk.Treeview(
            self,
            columns=(
                "ID",
                "Name",
                "Class",
                "Phone No",
                "Monthly Fee",
                "Status"
            ),
            show="headings"
        )

        # Headings

        self.tree.heading(
            "ID",
            text="ID"
        )

        self.tree.heading(
            "Name",
            text="Name"
        )

        self.tree.heading(
            "Class",
            text="Class"
        )

        self.tree.heading(
            "Phone No",
            text="Phone No"
        )

        self.tree.heading(
            "Monthly Fee",
            text="Monthly Fee"
        )

        self.tree.heading(
            "Status",
            text="Status"
        )

        # Columns

        self.tree.column(
            "ID",
            width=50,
            stretch=False,
            anchor="center"
        )

        self.tree.column(
            "Name",
            width=200,
            stretch=False
        )

        self.tree.column(
            "Class",
            width=100,
            stretch=False,
            anchor="center"
        )

        self.tree.column(
            "Phone No",
            width=200,
            stretch=False
        )

        self.tree.column(
            "Monthly Fee",
            width=200,
            stretch=False,
            anchor="center"
        )

        self.tree.column(
            "Status",
            width=150,
            stretch=True,
            anchor="center"
        )

        # =========================================================
        # TREEVIEW POSITION
        # =========================================================

        self.tree.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=(15, 0),
            pady=(15, 15)
        )

        # =========================================================
        # SCROLLBAR
        # =========================================================

        scroll = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(
            yscrollcommand=scroll.set
        )

        scroll.grid(
            row=2,
            column=1,
            sticky="ns",
            padx=(0, 10),
            pady=(15, 15)
        )

        # =========================================================
        # TAG COLORS
        # =========================================================

        
        # =========================================================
        # LOAD DATA
        # =========================================================

        self.load_students()

    # =============================================================
    # LOAD ALL STUDENTS
    # =============================================================

    def load_students(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        # Row colors
        self.tree.tag_configure("even", background="#351852")

        self.tree.tag_configure( "odd", background="#001d43")

        # Status colors
        self.tree.tag_configure( "paid", foreground="#00ff66")

        self.tree.tag_configure("pending",foreground="#c80000")

        rows = self.db.get_all_students()

        print("REPORT LOAD - row count:", len(rows))

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

    # =============================================================
    # SEARCH
    # =============================================================

    def search_button(self):

        entry = self.enter_value.get().strip()

        stu = self.search_stu.get().strip()

        # Empty value

        if not entry:

            messagebox.showerror(
                "Nothing Selected",
                "Enter value for a search"
            )

            return

        # Search field mapping

        element = {
            "ID": "id",
            "Name": "name",
            "Class": "class",
            "Phone No": "phone"
        }

        if stu not in element:

            messagebox.showerror(
                "Invalid Field",
                "Select a valid search field"
            )

            return

        column = element[stu]

        # Search database

        try:

            rows = self.db.search_student(
                column,
                entry
            )

        except Exception as e:

            messagebox.showerror(
                "Search Error",
                str(e)
            )

            return

        # No result

        if not rows:

            messagebox.showinfo(
                "Search",
                "No student found"
            )

            return

        # Display result

        self.populate_tree(rows)

    # =============================================================
    # POPULATE TREE
    # =============================================================

    def populate_tree(self, rows):

        # Clear old rows

        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert new rows

        for i, row in enumerate(rows):

            row_tag = (
                "even"
                if i % 2 == 0
                else "odd"
            )

            status_display = (
                "Paid"
                if row[5] == "P"
                else "Pending"
            )

            status_tag = (
                "paid"
                if status_display == "Paid"
                else "pending"
            )

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
                tags=(
                    row_tag,
                    status_tag
                )
            )

    # =============================================================
    # CLEAR
    # =============================================================

    def clear_button(self):

        self.enter_value.delete(
            0,
            "end"
        )

        self.search_stu.set("ID")

        self.load_students()

    # =============================================================
    # BY CLASS
    # =============================================================

    def class_filter(self, selected_class):

        if selected_class == "By Class":
            return

        try:

            rows = self.db.search_student(
                "class",
                selected_class
            )

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

            return

        if not rows:

            messagebox.showinfo(
                "Search",
                "No student in this class"
            )

            return

        self.populate_tree(rows)

    # =============================================================
    # BY STATUS
    # =============================================================

    def by_status_filter(self):

        try:

            rows = self.db.get_all_students()

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

            return

        # Show only Paid students

        paid_rows = [
            row for row in rows
            if row[5] == "P"
        ]

        if not paid_rows:

            messagebox.showinfo(
                "Search",
                "No paid student"
            )

            return

        self.populate_tree(
            paid_rows
        )

    # =============================================================
    # BY PENDING
    # =============================================================

    def by_pending_filter(self):

        try:

            rows = self.db.get_pending_student()

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

            return

        if not rows:

            messagebox.showinfo(
                "Search",
                "No pending student"
            )

            return

        self.populate_tree(rows)