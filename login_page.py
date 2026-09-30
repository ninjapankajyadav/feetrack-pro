                                                                     
from customtkinter import *
import os
from dotenv import load_dotenv

load_dotenv()
                                                           
from PIL import Image
                                                               
from tkinter import messagebox

                                                
def loginbox():
                                                                            
    if username.get() == "" or userpassword.get() == "":
                                                  
        messagebox.showerror("Error !!!!","user and password are required")
                                                                               
    elif username.get() == os.getenv("APP_USER") and userpassword.get() == os.getenv("APP_PASSWORD"):
                                                         
        messagebox.showinfo("Success","Successfully Done")
                                                                  
        ap.destroy()



                                                
ap = CTk()
                                                          
ap.geometry("428x579+500+100")
                                                          
ap.resizable(FALSE,FALSE)
                                                          
ap.title("Login Tuition fee")
                                                          
ap.iconbitmap("educational-investment_icon.ico")
                                                          
ap.grid_rowconfigure(0, weight=1)
                                                          
ap.grid_columnconfigure(0, weight=1)
                                                
image = CTkImage(Image.open("downloadlogin2.jpg"), size=(428, 579))
                                                
imagelabel = CTkLabel(ap, image=image, text="")
                                                              
imagelabel.grid(row=0, column=0, sticky="nsew")

                                                
heading_label = CTkLabel(
                                                              
    ap,
                                                
    width=200,
                                                
    height=75,
                                                
    text="FEE MANAGEMENT",
                                                
    bg_color="#A6A5A5",
                                                
    font=("Arial Black", 25, "bold"),
                                                
    corner_radius = 10,
                                                
    text_color="#016735"
                                                                    
)
                                                       
heading_label.place(x= 115,y= 90)

                                                
username = CTkEntry(
                                                              
    ap,
                                                
    bg_color="black",
                                                
    width=260,
                                                
    height=55,
                                                
    placeholder_text="Enter your Username",
                                                
    text_color="#000000",
                                                
    fg_color="#016533",
                                                
    font=("Segoe UI", 26),
                                                
    placeholder_text_color="#000000",
                                                
    corner_radius=5,
                                                
    border_width=2,

                                                                    
)
                                                       
username.place(x=135,y=225)

                                                
userpassword = CTkEntry(
                                                              
    ap,
                                                
    bg_color="black",
                                                
    width=260,
                                                
    height=55,
                                                
    placeholder_text="Enter your Password",
                                                
    text_color="#000000",
                                                
    fg_color="#016533",
                                                
    font=("Segoe UI", 26),
                                                
    placeholder_text_color="#000000",
                                                
    corner_radius=5,
                                                
    border_width=2,
                                                
    show= "*",

                                                                    
)
                                                       
userpassword.place(x=135,y=320)


                                                
userbutton = CTkButton(
                                                              
    ap,
                                                
    width=120,
                                                
    height=55,
                                                
    text="Login",
                                                
    hover_color="#064884",
                                                
    text_color="#000000",
                                                
    font=("Elephant",21),
                                                
    fg_color="#016533",
                                                
    border_color="#FFFFFF",
                                                
    corner_radius= 5,
                                                
    border_width= 2,
                                                
    cursor="hand2",
                                                
    command= loginbox

                                                                    
)

                                                       
userbutton.place(x= 195,y= 420)
                                                          
ap.mainloop()
