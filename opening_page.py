                                                                     
from customtkinter import *
                                                           
from PIL import Image
                                                                                                                 
from Tuitionfee_DB import tuitionDB
                                                                    
from home_page import HomePage

from student_page import StudentPage

from invoice_page import InvoicePage

from search_page import SearchPage

from report_page import ReportPage

from setting_page import SettingPage

                                            
db = tuitionDB()

                                              
                                                
win = CTk(fg_color="#000000")
                                                          
win.geometry("1380x760")
                                                          
win.minsize(1200, 700)
                                                          
win.iconbitmap("openinglogo.ico")
                                                          
win.title("FeeTrack Pro")
                                                          
win.resizable(TRUE, TRUE)
                                                          
win.grid_rowconfigure(0, weight= 1)
                                                          
win.grid_rowconfigure(1, weight= 1)
                                                          
win.grid_columnconfigure(0, weight=0)
                                                          
win.grid_columnconfigure(1, weight= 1)
              
                                           
header_frame = CTkFrame(win, fg_color="#05377e", height=50, corner_radius=0)
                                                              
header_frame.grid(row=0, column=1, sticky="ew", padx=2, pady=0)
                                                          
header_frame.grid_propagate(False)
                                                          
header_frame.grid_columnconfigure(1, weight=1)

            
                                                
page_title = CTkLabel(header_frame, text="Home", font=("Arial Black", 16), text_color="#fbff29")
                                                              
page_title.grid(row=0, column=0, padx=20, sticky="w")

                
                                                
clock_label = CTkLabel(header_frame, text="",text_color="#D4FF00" ,font=("Segoe UI Emoji",15,"bold"))
                                                              
clock_label.grid(row=0, column=1, sticky = "e")

             
                                                              
CTkLabel(header_frame, text="👨‍💼 Admin", font=("Segoe UI Emoji",15,"bold"), 
        text_color="#e2eb3a").grid(row=0, column=2, padx=20, sticky="e")

                                                    
def update_clock():
                                                                               
    import datetime
                                                
    now = datetime.datetime.now().strftime(""" %b %d %Y  
      %I:%M %p """)
                                                              
    clock_label.configure(text=now)
                                                              
    win.after(1000, update_clock)

                                                          
update_clock()


                                                        
def switch_indicator(active_indicator):
               
                                                        
    for ind in [
                                                                  
        hom_indicator,
                                                                  
        stud_indicator,
                                                                  
        invo_indicator,
                                                                  
        report_indicator,
                                                                  
        searh_indicator,
                                                                  
        sett_indicator,
                                                                        
    ]:
                                                                  
        ind.configure(fg_color="#05377e")

                      
                                                              
    active_indicator.configure(fg_color="#b77b14")

     
                                                
page_frame = CTkFrame(win, fg_color="#0b1a2e")
                                                              
page_frame.grid(row=1, column=1, sticky="nsew", padx=(0, 5), pady=(0, 5))
                                                          
page_frame.grid_rowconfigure(0, weight=1)
                                                          
page_frame.grid_columnconfigure(0, weight=1)

def show_page(name):
    pages[name].tkraise()
    page_title.configure(text=page_titles[name])
                                                    
pages = {}
                                                          
pages["HomePage"] = HomePage(page_frame,db, show_page)
                                                          
pages["StudentPage"] = StudentPage(page_frame, db)
                                                          
pages["InvoicePage"] = InvoicePage(page_frame, db)
                                                          
pages["ReportPage"] = ReportPage(page_frame,db)
                                                          
pages["SearchPage"] = SearchPage(page_frame, db)
                                                          
pages["SettingPage"] = SettingPage(page_frame,db)



                                                    
page_titles = {
                                                              
    "HomePage": "Home",
                                                              
    "StudentPage": "Student Management",
                                                              
    "InvoicePage": "Invoice",
                                                              
    "ReportPage": "Reports",
                                                              
    "SearchPage": "Search",
                                                              
    "SettingPage": "Settings",
                                                                    
}
                                                    
for page in pages.values():
                                                                  
    page.grid(row=0, column=0, sticky="nsew")

                                                 
def show_page(name):
                                                              
    pages[name].tkraise()
                                                              
    page_title.configure(text=page_titles[name])

                                                          
show_page("HomePage")

                                                    


                                            
menucolour = "#05377e"

                                                
menubarframe = CTkFrame(
                                                              
    win, fg_color="#05377e", width=150, height=450, corner_radius=20
                                                                    
)

                                                              
menubarframe.grid(
                                                
    row=0,
                                                
    sticky="NS",
                                                
    rowspan=7,
                                                
    pady=00,
                                                
    padx=5,
                                                                    
)
                                                          
menubarframe.grid_propagate(FALSE)
                                                          
menubarframe.configure(fg_color="#05377e")


                       


                                                    
common_style = {
                                                              
    "fg_color": "transparent",
                                                              
    "hover_color": "#ab7420",
                                                              
    "width": 230,
                                                              
    "height": 50,
                                                              
    "corner_radius": 10,
                                                              
    "anchor": "w",
                                                              
    "compound": "left",
                                                                    
}


                                                
def load_img(path):
                                                  
    return CTkImage(light_image=Image.open(path), size=(40, 40))


                                     
                                            
home_img = load_img("home.png")
                                            
stud_img = load_img("student2.png")
                                            
invoice_img = load_img("invoice 2.png")
                                            
report_img = load_img("report2.png")
                                            
search_img = load_img("search2.png")
                                            
setting_img = load_img("setting2.png")


                                                        

                                                
logo_img = CTkImage(light_image=Image.open("dashbord2.png"), size=(45, 50))

                                                
logo_img_but = CTkButton(
                                                              
    menubarframe,
                                                
    image=logo_img,
                                                
    text="FeeTrack ",

    text_color="#e2eb3a",

    font=("Georgia", 18),
                                                
    fg_color="transparent",
                                                
    hover_color="#1a1a1a",# 1f3a5f
                                                
    width=240,
                                                
    height=50,
                                                
    corner_radius=10,
                                                
    anchor="w",
                                                
    compound="left",
                                                
    command=lambda: (switch_indicator(hom_indicator), show_page("HomePage")),
                                                                    
)

                                                
home_but = CTkButton(
                                                              
    menubarframe,
                                                
    image=home_img,
                                                              
    **common_style,
                                                
    text="HOME",
                                                
    font=("Arial Black", 14),
                                                
    text_color="#fbff29",
                                                
    command=lambda: (switch_indicator(hom_indicator), show_page("HomePage")),
                                                                    
)

                                                
hom_indicator = CTkLabel(menubarframe, fg_color="#f78222", text="")

                                                              
hom_indicator.grid(row=1, padx=5, pady=1, ipady=4, ipadx=3, sticky="W")

                                                
stud_but = CTkButton(
                                                              
    menubarframe,
                                                
    image=stud_img,
                                                              
    **common_style,
                                                
    text="STUDENT",
                                                
    font=("Arial Black", 14),
                                                
    text_color="#fbff29",
                                                
    command=lambda: (switch_indicator(stud_indicator), show_page("StudentPage")),
                                                                    
)


                                                
stud_indicator = CTkLabel(menubarframe, fg_color="#f78222", text="")

                                                              
stud_indicator.grid(row=2, padx=5, pady=1, ipady=4, ipadx=3, sticky="W")

                                                
invoice_but = CTkButton(
                                                              
    menubarframe,
                                                
    image=invoice_img,
                                                              
    **common_style,
                                                
    text="INVOICE",
                                                
    font=("Arial Black", 14),
                                                
    text_color="#fbff29",
                                                
    command=lambda: (switch_indicator(invo_indicator), show_page("InvoicePage")),
                                                                    
)


                                                
invo_indicator = CTkLabel(menubarframe, fg_color="#f78222", text="")

                                                              
invo_indicator.grid(row=3, padx=5, pady=1, ipady=4, ipadx=3, sticky="W")

                                                
report_but = CTkButton(
                                                              
    menubarframe,
                                                
    image=report_img,
                                                              
    **common_style,
                                                
    text="REPORT",
                                                
    font=("Arial Black", 14),
                                                
    text_color="#fbff29",
                                                
    command=lambda: (switch_indicator(report_indicator), show_page("ReportPage")),
                                                                    
)


                                                
report_indicator = CTkLabel(menubarframe, fg_color="#fc9516", text="")

                                                              
report_indicator.grid(row=4, padx=5, pady=1, ipady=4, ipadx=3, sticky="W")

                                                
search_but = CTkButton(
                                                              
    menubarframe,
                                                
    image=search_img,
                                                              
    **common_style,
                                                
    text="SEARCH",
                                                
    font=("Arial Black", 14),
                                                
    text_color="#fbff29",
                                                
    command=lambda: (switch_indicator(searh_indicator), show_page("SearchPage")),
                                                                    
)


                                                
searh_indicator = CTkLabel(menubarframe, fg_color="#f78222", text="")
                                                              
searh_indicator.grid(row=5, padx=5, pady=1, ipady=4, ipadx=3, sticky="W")

                                                
setting_but = CTkButton(
                                                              
    menubarframe,
                                                
    image=setting_img,
                                                              
    **common_style,
                                                
    text="SETTING",
                                                
    font=("Arial Black", 14),
                                                
    text_color="#fbff29",
                                                
    command=lambda: (switch_indicator(sett_indicator), show_page("SettingPage")),
                                                                    
)


                                                
sett_indicator = CTkLabel(menubarframe, fg_color="#f78222", text="")
                                                              
sett_indicator.grid(row=6, padx=5, pady=1, ipady=4, ipadx=3, sticky="W")

                                                              
logo_img_but.grid(row=0, column=0, pady=25, padx=5, sticky="n")
                                                              
home_but.grid(row=1, column=0, pady=10)
                                                              
stud_but.grid(row=2, column=0, pady=10)
                                                              
invoice_but.grid(row=3, column=0, pady=10)
                                                              
report_but.grid(row=4, column=0, pady=10)
                                                              
search_but.grid(row=5, column=0, pady=10)
                                                              
setting_but.grid(row=6, column=0, pady=10)
                                                        
win.mainloop()
