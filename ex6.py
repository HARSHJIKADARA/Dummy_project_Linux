import tkinter as tk

root = tk.Tk()
root.title("Tkinter Geometry Managers Example")
root.geometry("800x600")

frame1 = tk.Frame(root, bg='blue')
frame1.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)


for i in range(2):
    button = tk.Button(frame1, text=f'Pack Button {i+1}')
    button.pack(pady=5)

frame2 = tk.Frame(root, bg='pink')
frame2.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

for i in range(3):
    button = tk.Button(frame2, text=f'Grid Button {i+1}')
    button.grid(row=i, column=0, padx=5, pady=5)

frame3 = tk.Frame(root, bg='red')
frame3.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

for i in range(4):
    button = tk.Button(frame3, text=f'Place Button {i+1}')
    button.place(x=10, y=(i * 30) + 10)  

root.mainloop()