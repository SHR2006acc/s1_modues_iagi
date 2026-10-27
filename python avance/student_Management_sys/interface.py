
import tkinter as tk


def check_status(status): 
    if status.get() :
        print("BOX ON")
    else : print("BOX OFF")
        
def main():
    window = tk.Tk()
    window.geometry("800x500")
    

    window.title("Python ++")
    status = tk.IntVar()
    
    check = tk.Checkbutton(
    window,
    text="Click Box",
    variable=status
                         )
    check.pack()
    # v1 = tk.IntVar()
    button = tk.Button(window,text="Click",command=lambda: check_status(status),padx=30,pady=20,background="grey")
    button.pack()


    window.mainloop()


if __name__ == "__main__":
    main()