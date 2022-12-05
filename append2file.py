import os


import tkinter as tk
from pathlib import Path
master=tk.Tk()
master.title("Append2File")
master.geometry("300x250")
string_var=tk.StringVar()
input_substring_var=tk.StringVar()
output_substring_var=tk.StringVar()
def submit():
 
    stringEntry=string_var.get()
    print("The name is : " + stringEntry)
    
    if not stringEntry:
        print("Empty string entered. Exiting...")
    
    else:

        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        fileList=[]
        for f in files:
            fileList.append(f)
            

        print(fileList)

        for f in fileList:
            fileExt=Path(f).suffix
            fileName=str(f).removesuffix(fileExt)


            print(fileName+"then"+fileExt)
            
            if fileExt!='.py'and fileExt!='.exe':
                print("NO PYTHON FOUND")
                fileNameCat=''.join(fileName)+"_"+stringEntry+fileExt
                os.rename(f,fileNameCat)
                



        
    print("Reached end")
    master.destroy()


def replaceString():
    inputSubStringEntry=input_substring_var.get()
    outputSubStringEntry=output_substring_var.get()

    if not inputSubStringEntry:
        print("Empty string entered. Exiting...")
    else:
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        fileList=[]
        for f in files:
            fileList.append(f)
            

        print(fileList)

        for f in fileList:
            if inputSubStringEntry in f:
                result=str(f).replace(inputSubStringEntry,outputSubStringEntry)
                os.rename(f,result)
        
    print("Reached end")
    master.destroy()

    








stringKey_label=tk.Label(master=master,text="Enter string here",font=('arial',10))
stringKey_entry=tk.Entry(master=master,textvariable = string_var, font=('arial',10,'normal'))
append_btn=tk.Button(master=master,text = 'Append', command = submit)

substringInput_label=tk.Label(master=master,text="Enter substring to replace here (case sensitive)",font=('arial',10))
substringInput_entry=tk.Entry(master=master,textvariable = input_substring_var, font=('arial',10,'normal'))
substringOutput_label=tk.Label(master=master,text="Enter new substring here (case sensitive)",font=('arial',10))
substringOutput_entry=tk.Entry(master=master,textvariable = output_substring_var, font=('arial',10,'normal'))
replace_btn=tk.Button(master=master,text = 'Replace', command = replaceString)

empty_label= tk.Label(master, text='     \n   ')

stringKey_label.grid(row=0,column=0)
stringKey_entry.grid(row=1,column=0)
append_btn.grid(row=3,column=0)
empty_label.grid(row=4,column=0)
substringInput_label.grid(row=5,column=0)
substringInput_entry.grid(row=6,column=0)
substringOutput_label.grid(row=7,column=0)
substringOutput_entry.grid(row=8,column=0)
replace_btn.grid(row=9,column=0)



 

master.mainloop()




