import customtkinter # importing customtkinter module 
import tkinter # importing tkinter module
from tkinter import * # importing every class and subclasses from tkinter module
from deep_translator import GoogleTranslator # importing GoogleTranslator module from deep_translator module
from tkinter import messagebox as tmsg # importing message box to show message

root=customtkinter.CTk() # CTK() class instance
root.title("Ultimate Translator Hub") # title 
root.geometry("800x650") # geometry size defining
root.maxsize(800,650) # maxsize
root.minsize(800,650) # minsize
root.iconbitmap("c:\\Users\\user\\Downloads\\Ultimate Language Translator-logo.ico") # icon
root._set_appearance_mode("dark") # setting the apperance mode

# function for when clicking on the text box
def on_focus_in(event):
    # Hide the placeholder when focusing in
    placeholder_label.grid_forget()

# function for when not clicked on the text box
def on_focus_out(event):
    # Show the placeholder if the textbox is empty when losing focus
    if not event.widget.get(1.0, "end-1c").strip():
        placeholder_label.grid(row=2, column=2, sticky="nw", padx=10, pady=10)

# function for language option menu
def optionmenu_callback_translating(choice):
    try:
        # dictionary for language and their codes
        lang_dic = {
                    "Afrikaans": "af", "Arabic": "ar", "Bengali": "bn", "Catalan": "ca","Czech": "cs",
                    "Danish": "da", "German": "de", "Greek": "el", "English": "en", "Spanish": "es",
                    "Estonian": "et", "Finnish": "fi", "French": "fr", "Gujarati": "gu", "Hebrew": "he",
                    "Hindi": "hi", "Croatian": "hr", "Hungarian": "hu", "Indonesian": "id", "Italian": "it",
                    "Japanese": "ja", "Kannada": "kn", "Korean": "ko", "Latin": "la", "Latvian": "lv",
                    "Lithuanian": "lt", "Macedonian": "mk", "Malayalam": "ml", "Mongolian": "mn",
                    "Marathi": "mr", "Myanmar (Burmese)": "my", "Nepali": "ne", "Dutch": "nl",
                    "Norwegian": "no", "Polish": "pl", "Portuguese": "pt", "Punjabi": "pa", "Romanian": "ro",
                    "Russian": "ru", "Sinhala": "si", "Slovak": "sk", "Slovenian": "sl", "Samoan": "sm",
                    "Shona": "sn", "Somali": "so", "Albanian": "sq", "Serbian": "sr", "Sesotho": "st",
                    "Sundanese": "su", "Swedish": "sv", "Swahili": "sw", "Tamil": "ta", "Telugu": "te",
                    "Thai": "th", "Tagalog": "tl", "Turkish": "tr", "Ukrainian": "uk", "Urdu": "ur",
                    "Vietnamese": "vi", "Welsh": "cy", "Xhosa": "xh", "Yiddish": "yi", "Zulu": "zu"
                    }
        # getting the selected language code from the dictionary
        lang_code=lang_dic[f"{choice}"]
        # getting the text from the user
        lang=text_entry.get("1.0",END)
        # Translating the text
        translated_text = GoogleTranslator(source='auto', target=f"{lang_code}").translate(lang)
        # clearing the pre generated text 
        result_text.delete("1.0", END)
        # Insert system-generated text
        result_text.insert('1.0', translated_text)
    except Exception as e:
        tmsg.showerror("Error!","Your Entered language is not valid!\nor may be not available right now.")
#Help Menu options

#Rate menu
def RATE():
    def rmessage():
        # destroying the rate window
        rate_window.destroy()
        # if rating submitted then this message will be displayed
        tmsg.showinfo("Thank You!","Thank You! for your rating :)")
        
    #creating rate window
    rate_window=customtkinter.CTk() # CTk() class instance 
    rate_window.title("Rate Us") # title
    rate_window._set_appearance_mode("dark") # setting apperance mode dark
    rate_window.iconbitmap("c:\\Users\\user\\Downloads\\Ultimate Language Translator-logo.ico") # icon
    rate_window.geometry("300x310") # determining size
    rate_window.maxsize(300,310) # fixing max size
    rate_window.minsize(300,310) # fixing min size
    
    # upper frame
    uframe=customtkinter.CTkFrame(rate_window,fg_color="deeppink2",corner_radius=0)
    uframe.pack(fill=X)
    
    # show label to create extra spacing
    rshow0=customtkinter.CTkLabel(uframe,text="",font=("Calisto MT",15,"bold"))
    rshow0.pack()
    # title
    title=customtkinter.CTkLabel(uframe,text="Rate us here",font=("Calisto MT",25,"bold","underline"),text_color="purple",fg_color="white",corner_radius=10,padx=15,pady=8) 
    title.pack()
    # show label to create extra spacing
    rshow1=customtkinter.CTkLabel(uframe,text="",font=("Calisto MT",15,"bold"))
    rshow1.pack()
    
    #lower frame
    lframe=customtkinter.CTkFrame(rate_window,fg_color="purple",corner_radius=0,border_color="purple")
    lframe.pack(fill=BOTH,expand=True)
    
    # show label to create extra spacing
    rshow01=customtkinter.CTkLabel(lframe,text="",font=("Calisto MT",15,"bold"))
    rshow01.pack()
    
    # rate scale to rate 
    rate_scale=tkinter.Scale(lframe,from_=0, to=100, orient="horizontal",sliderlength=5,tickinterval=50,bg="deeppink2",fg="white",relief="flat",font=("poppins",10,"bold"))
    rate_scale.set(50) # initially setting the position to 50
    rate_scale.pack()
    
    # show label to create extra spacing
    rshow2=customtkinter.CTkLabel(lframe,text="",font=("Calisto MT",15,"bold"),fg_color="purple",text_color="purple")
    rshow2.pack()
    
    # lower frame
    lframe2=customtkinter.CTkFrame(rate_window,fg_color="deeppink2",corner_radius=0,border_color="deeppink2")
    lframe2.pack(fill=BOTH,expand=True)
    
    # show label to create extra spacing
    f_label2=customtkinter.CTkLabel(lframe2,text="\n",fg_color='deeppink2')#show label to create space
    f_label2.pack()
    
    # submit button
    s_button=customtkinter.CTkButton(lframe2,text="Submit",font=("poppins",20,"bold"),fg_color="light sea green",text_color="white",command=rmessage)
    s_button.pack()
    
    # show label to create extra spacing
    f_label1=customtkinter.CTkLabel(lframe2,text="\n",fg_color='deeppink2')#show label to create space
    f_label1.pack()
    
    rate_window.mainloop()# mainloop() to execute and show the rate window
    
#About us menu
def ABOUT():  
    # if clicked on about us then this message will be displayed
    tmsg.showinfo("About Us","This \"Ultimate Translator Hub\" is made by Soumyajeet Das.\nIt is created using custom tkinter module in Python.\nDate: 18/08/2024")

#Help Menu

help_menu=Menu(root)

#Inside help Menu
in_help_menu=Menu(help_menu,tearoff=0)
# help menu options
in_help_menu.add_command(label="Rate Us",command=RATE)
in_help_menu.add_separator()# separator
in_help_menu.add_command(label="About Us    ",command=ABOUT)
#config the sub help menu to change font size
in_help_menu.config(font=("Helvetica",12))#changing font of sub help menu to increase the menu size
# add_cascade the help menu
help_menu.add_cascade(label="   Help   ",menu=in_help_menu)
root.configure(menu=help_menu)#configuring help Menu
 
frame0=customtkinter.CTkFrame(root,fg_color="deeppink2",corner_radius=0,) # frame 0
frame0.pack(fill=BOTH)
# show label to create extra spacing
show0=customtkinter.CTkLabel(frame0,text="",font=("Calisto MT",20,"bold"))
show0.grid(row=1,column=1)
# show label to create extra spacing
show00=customtkinter.CTkLabel(frame0,text="\t\t   ",font=("Calisto MT",20,"bold"))
show00.grid(row=2,column=1)
# heading 
heading=customtkinter.CTkLabel(frame0,text="Ultimate Translator Hub",font=("Calisto MT",35,"bold","underline"),fg_color="white",text_color="purple",corner_radius=15,padx=20,pady=10)
heading.grid(row=2,column=2)
# show label to create extra spacing
show01=customtkinter.CTkLabel(frame0,text="\t",font=("Calisto MT",20,"bold"))
show01.grid(row=3,column=1)

frame1=customtkinter.CTkFrame(root,fg_color="purple",corner_radius=0) # frame 1
frame1.pack(fill=BOTH)

# show label to create extra spacing
show1=customtkinter.CTkLabel(frame1,text="",font=("Calisto MT",20,"bold"))
show1.grid(row=1,column=1)
# show label to create extra spacing
show2=customtkinter.CTkLabel(frame1,text="   ",font=("Calisto MT",20,"bold"))
show2.grid(row=2,column=1)
# text box for getting the text from the user
text_entry=customtkinter.CTkTextbox(frame1,fg_color="white",text_color="black",font=("poppins",20),height=200,width=770)
text_entry.grid(row=2, column=2)

# Create placeholder label
placeholder_label = customtkinter.CTkLabel(frame1, text="Enter your text here..", font=("poppins", 20), fg_color="white", text_color="grey", anchor="nw")

# Place the placeholder label over the textbox
placeholder_label.grid(row=2, column=2, sticky="nw", padx=10, pady=10)

# Bind events for showing/hiding the placeholder
text_entry.bind("<FocusIn>", on_focus_in)
text_entry.bind("<FocusOut>", on_focus_out)

frame2=customtkinter.CTkFrame(root,fg_color="purple",corner_radius=0) # frame 2
frame2.pack(fill=BOTH)
    
# languages list
lang_list=["Afrikaans", "Arabic", "Albanian", "Bengali", "Catalan", "Czech", "Danish", "German", 
           "Greek", "English", "Spanish", "Estonian", "Finnish", "French", "Gujarati", "Hebrew", 
           "Hindi", "Croatian", "Hungarian", "Indonesian", "Italian", "Japanese", "Kannada", 
           "Korean", "Latin", "Latvian", "Lithuanian", "Macedonian", "Malayalam", "Mongolian", 
           "Marathi", "Myanmar (Burmese)", "Nepali", "Dutch", "Norwegian", "Polish", "Portuguese", 
           "Punjabi", "Romanian", "Russian", "Sinhala", "Slovak", "Slovenian", "Samoan", "Shona",
           "Somali", "Serbian", "Sesotho", "Sundanese", "Swedish", "Swahili", "Tamil", "Telugu",
           "Thai", "Tagalog", "Turkish", "Ukrainian", "Urdu", "Vietnamese", "Welsh", "Xhosa", 
           "Yiddish", "Zulu"
          ]

# show label to create extra spacing
show4=customtkinter.CTkLabel(frame2,text="   ",font=("Calisto MT",5,"bold"))
show4.pack()
# language option menu
lang_optionmenu = customtkinter.CTkOptionMenu(frame2, values=lang_list, font=("Calisto MT",20,"bold"),text_color="black",fg_color="LightBlue1",button_color="light sea green",command=optionmenu_callback_translating)
lang_optionmenu.set(lang_list[0]) # setting the language at 0th index of lang_list[]
lang_optionmenu.pack()  # Add to the grid with some padding

frame3=customtkinter.CTkFrame(root,fg_color="purple",corner_radius=0) # frame 3
frame3.pack(fill=BOTH)

# show label to create extra spacing
show4=customtkinter.CTkLabel(frame3,text="   ",font=("Calisto MT",20,"bold"))
show4.grid(row=1,column=1)
# text box for getting the result text
result_text=customtkinter.CTkTextbox(frame3,fg_color="white",text_color="black",font=("poppins",20),height=200,width=770)
result_text.grid(row=2, column=2)

# show label to create extra spacing
show5=customtkinter.CTkLabel(frame3,text="   ",font=("Calisto MT",20,"bold"))
show5.grid(row=3,column=1)

root.mainloop() # mainloop to execute and show the window in the screen