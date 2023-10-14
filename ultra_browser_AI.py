import webbrowser
import tkinter as tk
from tkinter import ttk

def search():
    value = entry_var1.get()
    
     
    
    
    for i in range(1):
        perpl= "https://www.perplexity.ai/search?q="
        open=value

        webbrowser.open_new(str(perpl) + str(open))
        e1.delete(0, 'end')
    
    
    
    
#
window=tk.Tk()
window.title("Браузер зі Штучним інтелектом")
window.geometry("640x480")
#
style = ttk.Style()
style.theme_use('vista')
#
entry_var1 = tk.StringVar()
#
l1=tk.Label(window,text="Напишіть свій пошуковий запит:",font=("Arial",10))
l1.grid(column=0,row=0,padx=10,pady=10)
#
e1=tk.Entry(window,font=("Arial",10), textvariable=entry_var1)
e1.grid(column=1,row=0,padx=10,pady=10)
#
#
bth2=ttk.Button(window,text="Шукати",command=search)
bth2.grid(column=0,row=3,padx=10,pady=10)
#
window.mainloop()