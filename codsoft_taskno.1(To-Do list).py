import tkinter as tk
import tkinter.messagebox

root=tkinter.Tk()
root.title("TO-DO List")
root.configure(bg="pink")
root.geometry("400x400")

main_Frame = tk.Label(root, text="TO DO LIST", font=("Arial Black", 24),fg="white", bg="black")
main_Frame.pack()


def task():
    mentioned_task=add_task.get()
    if mentioned_task:
        task_box.insert(tk.END,mentioned_task)
        add_task.delete(0,tk.END)
        

def clear_task():
    task_index_number=task_index.get()   
    try:
        if int(task_index_number)>=task_box.size():
            error_index.config(text="index exceeding") 
            task_index.delete(0,tk.END)           
    
        else:
            error_index.config(text="") 
            if task_index_number:
                task_box.delete(task_index_number)
                task_index.delete(0,tk.END)    
    except:
        error_index.config(text="enter crt index number")
        task_index.delete(0,tk.END)  
              

task_box=tk.Listbox(root,height=12,width=70)
task_box.pack()

add_task=tk.Entry(root,width=70)
add_task.pack()

b1=tk.Button(root,text="enter your tasks here",width=46,command=task)
b1.pack()

task_index=tk.Entry(root,width=70)
task_index.pack()

error_index = tk.Label(root, text="", fg="white",width=50,bg="black")
error_index.pack()


b2=tk.Button(root,text="enter clear task index(start from 0)",command=clear_task)
b2.pack()

root.mainloop()
