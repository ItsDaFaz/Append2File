import os


import tkinter as tk
from pathlib import Path
master=tk.Tk()
master.title("Append2File")
master.geometry("150x100")
string_var=tk.StringVar()
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
            #print(f)

        print(fileList)

        for f in fileList:
            #fileSplit = f.split()
            fileExt=Path(f).suffix
            fileName=str(f).removesuffix(fileExt)


            print(fileName+"then"+fileExt)
            #print("Filename only ",fileSplit[:-1],"extension",fileSplit[-1])
            #fileNameOnly=fileSplit[:-1]
            if fileExt!='.py'and fileExt!='.exe':
                print("NO PYTHON FOUND")
                fileNameCat=''.join(fileName)+"_"+stringEntry+fileExt
                os.rename(f,fileNameCat)
                #print(fileNameCat)



        
    print("Reached end")
    master.destroy()




    





master.bind('<Return>',submit)



stringKey_label=tk.Label(master=master,text="Enter string here",font=('arial',10))
stringKey_entry=tk.Entry(master=master,textvariable = string_var, font=('arial',10,'normal'))
sub_btn=tk.Button(master=master,text = 'Append', command = submit)

stringKey_label.grid(row=0,column=0)
stringKey_entry.grid(row=1,column=0)
sub_btn.grid(row=3,column=0)






 

master.mainloop()




