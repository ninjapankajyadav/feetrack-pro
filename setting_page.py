from customtkinter import *
import webbrowser


class SettingPage(CTkFrame):
                                                    
    def __init__(self, parent, db):
                                                                  
        super().__init__(parent, fg_color="transparent")
                                                        
        CTkLabel( self, text="Setting Page", text_color="#eeeee4", font=("Arial Black", 20)).grid()

        
        self.selected_id = None
                                                                                       
        self.selected_card = None

        self.db = db

        self.scroll_frame = CTkScrollableFrame( self,fg_color="transparent")
        self.scroll_frame.grid(row=0,column=0,sticky="nsew")

        self.scroll_frame.grid_columnconfigure(0, weight=1)


      

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)  # single column, full width

        

        frame1 = CTkFrame(self.scroll_frame, fg_color="transparent")
        frame1.grid(row=0, column=0, padx=15, pady=9, sticky="ew")
        
 
        CTkLabel(frame1, text="⛯ Setting",
                text_color="#fbff29",
                font=("Segoe UI Emoji",25,"bold")
                ).grid(row=0, column=0, padx=18,
                pady=(0, 10),sticky="w")

        CTkLabel(frame1, text="Mange your Application Setting",
                text_color="#F8FAFC",font=("Segoe UI Emoji",15,"bold")
                ).grid(row=1, column=0, padx=15, 
                pady=(0, 10),sticky="w")
        
        frame2 =CTkFrame(self.scroll_frame, fg_color="#02445A",
                        width= 300, height = 120,corner_radius=5,)
       
        frame2.grid(row=1, column=0, padx=15, pady=9, sticky="ew")

        # Columns
        frame2.columnconfigure(0, weight=0)  # icon
        frame2.columnconfigure(1, weight=1)  # app name
        frame2.columnconfigure(2, weight=1)  # empty space
        frame2.columnconfigure(3, weight=0)  # info icon
        frame2.columnconfigure(4, weight=0)  # version

        CTkLabel(frame2,text="Appliction",
                text_color="#F8FAFC",font=("Arial Black",15,"bold")
                ).grid(row=0, column=0, padx=15, 
                pady=(0, 10),sticky="w")

        CTkLabel(frame2,text="🖥️",
                        text_color="#F8FAFC",font=("Segoe UI Emoji",35,"bold")
                        ).grid(row=1, column=0, padx=(18,25), 
                        pady=(0, 20),sticky="w")

        
        CTkLabel(frame2,text="Appliction Name",
                        text_color="#F8FAFC",font=("Arial Black",15,)
                        ).grid(row=1, column=1, padx=5, 
                        pady=(0, 8),sticky="sw")

        CTkLabel(frame2,text="FeeTrack Pro",
                        text_color="#F8FAFC",font=("Arial Black",15)
                        ).grid(row=2, column=1, padx=5, 
                        pady=(0, 15),sticky="nw")
        CTkLabel(
                frame2,
                text="ℹ",
                text_color="#F8FAFC",
                font=("Segoe UI Emoji", 35, "bold")
                ).grid(
                row=1,
                column=3,
                rowspan=2,
                padx=(20, 15),
                pady=(0, 15),
                sticky="n"
                )

        CTkLabel(
                frame2,
                text="Version",
                text_color="#F8FAFC",
                font=("Arial Black", 15)
                ).grid(
                row=1,
                column=4,
                padx=(5, 25),
                pady=(0, 8),
                sticky="sw"
                )

        CTkLabel(
                frame2,
                text="1.0.0",
                text_color="#F8FAFC",
                font=("Arial Black", 15)
                ).grid(
                row=2,
                column=4,
                padx=(5, 25),
                pady=(0, 15),
                sticky="nw"
        )


        frame3 = CTkFrame(self.scroll_frame, fg_color="#02445A",
                        width = 300, height = 120, corner_radius = 9,)
        frame3.grid(row=2, column=0, padx=15, pady=9, sticky="ew")

        # Columns
        frame3.columnconfigure(0, weight=0)  # icon
        frame3.columnconfigure(1, weight=1)  # app name
        frame3.columnconfigure(2, weight=1)  # empty space
        frame3.columnconfigure(3, weight=0)  # info icon
        frame3.columnconfigure(4, weight=0) 
        

        CTkLabel(frame3,
                text="Database",
                text_color="#F8FAFC",
                font=("Arial Black",15,"bold")
                ).grid(row=0, column=0, padx=15,pady=(0, 10),sticky="w")
        
        
        CTkLabel(frame3,text="🛢",
                fg_color = "transparent",
                font = ("Segoe UI Emoji",35,"bold")
                ).grid(row=1, column=0, padx = (18,25), pady=(0, 20),sticky="w")

        
        CTkLabel(frame3,
                text="Database Name",
                text_color="#F8FAFC",
                font=("Arial Black",15,"bold")
                ).grid(row=1, column=1, padx=(5, 25),
                 pady=(0, 8),sticky="sw")

        CTkLabel(frame3,
                text="tutionfee",
                text_color="#F8FAFC",
                font=("Arial Black",15,"bold")
                ).grid(row=2, column=1, padx=(5, 25),
                pady=(0, 8),sticky="nw")


        CTkLabel(frame3,
                text="🔗",
                fg_color = "transparent",
                font = ("Segoe UI Emoji",35,"bold"),
                ).grid(row=1, column=3, padx=(20, 15),
                pady=(0, 15),sticky="n")

        CTkLabel(frame3,
                text="Connection Stutus",
                text_color="#F8FAFC",
                font=("Arial Black",15,"bold")
                ).grid(row=1, column= 4, padx=(5, 25),
                pady=(0, 8),sticky="sw")

        CTkLabel(frame3,
                text="🟢 Connection",
                text_color="#00A71F",
                font=("Segoe UI Emoji",15)
                ).grid(row=2, column= 4, padx=(5, 25),
                pady=(0, 8),sticky="nw")

        frame4 = CTkFrame(self.scroll_frame, fg_color="#02445A",
                        width = 300, height = 100, corner_radius = 9,)
        frame4.grid(row=3, column=0, padx=15, pady=9, sticky="ew")

        frame4.columnconfigure(0,weight=0)
        frame4.columnconfigure(1,weight=0)
        frame4.columnconfigure(2,weight=1)


        CTkLabel(frame4,text="Appearance",
                text_color="#F8FAFC",
                font=("Arial Black",15,"bold")
                ).grid(row=0, column=0, padx=15,pady=(0, 10),sticky="w")
        

        CTkLabel(frame4,
                text="☀︎",
                text_color="#F8FAFC",
                font=("Segoe UI Emoji",30)
                ).grid(row=1, column= 0, padx=(5, 25),
                pady=(0, 8),sticky="w")

        
        CTkLabel(frame4,
                text="Theme",
                text_color="#F8FAFC",
                font=("Segoe UI Emoji",15,"bold")
                ).grid(row=1, column= 1, padx=(5, 25),
                pady=(0, 8),sticky="w")

        
        dark_theme = CTkButton(frame4,height=20,width=30,
                     text= "☀︎ Dark", text_color="#F8FAFC",fg_color="#022D3B",
                     font=("Segoe UI Emoji",15),hover_color="#CBCB2D")
        dark_theme.grid(row=2, column= 1, padx=5,pady=(0, 8),sticky="nw")


        light_theme = CTkButton(frame4,height=20,width=30,
                        text= "☾ Light", text_color="#F8FAFC",fg_color="#022D3B",
                        font=("Segoe UI Emoji",15),hover_color="#CBCB2D")
        light_theme.grid(row=2, column= 2, padx=(5, 25),pady=(0, 8),sticky="nw")

        
        frame5 = CTkFrame(self.scroll_frame, fg_color="#02445A",
                        width = 300, height = 200, corner_radius = 9,)
        frame5.grid(row=4, column=0, padx=15, pady=9, sticky="ew")

        frame5.columnconfigure(0,weight=0)
        frame5.columnconfigure(1,weight=0)
        frame5.columnconfigure(2,weight=0)
        frame5.columnconfigure(3,weight=0)

        CTkLabel(frame5,text="About",
                        text_color="#F8FAFC",
                        font=("Arial Black",15,"bold")
                ).grid(row=0, column=0, padx=15,pady=(0, 10),sticky="w")

        CTkLabel(frame5,
                text="ⓘ",
                text_color="#F8FAFC",
                font=("Segoe UI Emoji",30)
        ).grid(row=1, column= 0, padx=(5, 25),pady=(0, 8),sticky="w")

        CTkLabel(frame5,
                text="About",
                text_color="#F8FAFC",
                font=("Segoe UI Emoji",15,"bold")
        ).grid(row=1, column= 1, padx=(5, 25),pady=(0, 8),sticky="w")

        CTkLabel(frame5,
                text="💻 Developed by Pankaj Yadav\nPython Developer | BCA ",
                text_color="#04EBFC",
                font=("Segoe UI Emoji",15,"bold"),
        ).grid(row=1, column= 1, padx= (5, 25),pady=(0, 8),sticky="w")

        

       
        def open_link(url):
             webbrowser.open_new_tab(url)

        # ---- GitHub ----
        CTkLabel(frame5,
                text="🐙 GitHub",
                text_color="#F8FAFC",
                font=("Segoe UI Emoji", 15, "bold")
        ).grid(row=1, column=2, padx=(5, 25), pady=(0, 2), sticky="w")

        link1 = CTkLabel(frame5,
                        text="github.com/ninjapankajyadav",
                        text_color="#170477",
                        cursor="hand2",
                        font=("Segoe UI Emoji", 15, "bold"))
        link1.grid(row=2, column=2, padx=(5, 25), pady=(0, 8), sticky="w")
        link1.bind("<Button-1>", lambda e: open_link("https://github.com/ninjapankajyadav"))

        # ---- LinkedIn ----
        CTkLabel(frame5,
                text="in / LinkedIn",
                text_color="#F8FAFC",
                font=("Segoe UI Emoji", 15, "bold")
        ).grid(row=1, column=3, padx=(5, 25), pady=(0, 2), sticky="w")

        link2 = CTkLabel(frame5,
                        text="linkedin.com/in/pankaj-yadav-b564141b4",
                        text_color="#170477",
                        cursor="hand2",
                        font=("Segoe UI Emoji", 15, "bold"))
        link2.grid(row=2, column=3, padx=(5, 25), pady=(0, 8), sticky="w")
        link2.bind("<Button-1>", lambda e: open_link("https://linkedin.com/in/pankaj-yadav-b564141b4"))
            
            