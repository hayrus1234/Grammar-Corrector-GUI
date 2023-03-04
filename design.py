import tkinter as tk
import os
import openai


root=tk.Tk()
root.title("Grammar Corrector")
root.geometry("600x600")
root.resizable(0,0)

#define colors and fonts
sky_color="#76c3ef"
grass_color="#aad207"
output_color="#dcf0fb"
input_color="#ecf2ae"
large_font=('SimSun',14)

#functions
def opena():
    openai.api_key ='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'
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Correct this to standard English:{e.get('1.0','end')}",
    temperature=0,
    max_tokens=2000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
    global x
    x=response['choices'][0]['text']

def check():
    opena()
    output.config(text=x)
    
root.config(background='#DCAE96')
display_frame=tk.Frame(width=510,height=520)
display_frame.grid(row=0,column=0,padx=45,pady=50)


input_frame=tk.Frame(display_frame,bg=sky_color,width=510,height=520)
input_frame.grid()
e=tk.Text(input_frame,width=55,height=7)
e.place(x=30,y=25)
title=tk.Label(root,text="Enter your Sentence",font=large_font)
title.place(x=210,y=10)

but=tk.Button(input_frame,text='Correct',font=large_font,command=check)
but.place(x=210,y=195)

output=tk.Label(input_frame,font=large_font,bg=sky_color,wraplength=500)
output.place(x=20,y=300)


root.mainloop()
