import tkinter as tk
def submit():
    amount= int(Entry1.get())
    rate = float(Entry2.get())
    time = int(Entry3.get())
    CI = amount*(pow(1+rate/100,time))
    Entry4.insert(10, CI)

def clear():
    Entry1.delete(0, 20)
    Entry2.delete(0, 20)
    Entry3.delete(0, 20)
    Entry4.delete(0, 20)
    Entry1.focus_set()

if __name__== "__main__":
    root = tk.Tk()
    root.config(background="Light Green")
    label1= tk.Label(root, text="Principle amount:", fg="black", bg="red")
    label2= tk.Label(root, text="Rate:", fg="black", bg="red")
    label3= tk.Label(root, text="Time:", fg="black", bg="red")
    label4= tk.Label(root, text="Compund Interest:", fg="black", bg="red")
    label1.grid(row = 1, column = 0, padx = 10, pady = 10)
    label2.grid(row = 2, column = 0, padx = 10, pady = 10)
    label3.grid(row = 3, column = 0, padx = 10, pady = 10)
    label4.grid(row = 5, column = 0, padx = 10, pady = 10)

    Entry1 = tk.Entry(root)
    Entry2 = tk.Entry(root)
    Entry3 = tk.Entry(root)
    Entry4 = tk.Entry(root)
    Entry1.grid(row = 1, column = 1, padx = 10, pady = 10)
    Entry2.grid(row = 2, column = 1, padx = 10, pady = 10)
    Entry3.grid(row = 3, column = 1, padx = 10, pady = 10)
    Entry4.grid(row = 5, column = 1, padx = 10, pady = 10)

    button1= tk.Button(root, text="Submit", fg="black", bg="red", command=submit)
    button2= tk.Button(root, text="Clear", fg="black", bg="red", command=clear)
    button1.grid(row = 4, column = 1, padx = 10, pady = 10)
    button2.grid(row = 6, column = 1, padx = 10, pady = 10)
    root.mainloop()