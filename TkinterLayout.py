import tkinter as tk

root = tk.Tk()
root.title("Fix Grid Layout")
root.geometry("400x400")

# Configure row and column weights for expansion
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(6, weight=1)

# Place widget 1 at row 0, column 2
label1 = tk.Label(root, text="Label 1", bg="lightblue")
label1.grid(row=0, column=2, padx=5, pady=5)

# Place widget 2 at row 1, column 6
label2 = tk.Label(root, text="Label 2", bg="lightgreen")
label2.grid(row=1, column=6, padx=5, pady=5)

root.mainloop()
