import tkinter as tk
from socketClient import recieve


root = tk.Tk()
root.title("Не гори")
root.resizable(height=False, width=False )
#root.attributes("-toolwindow", 1)
ip = input('ip: ')
port = int(input('port: '))

button = tk.Button(root, text="click me", command=lambda: recieve(ip,port))
button.pack()

root.mainloop()
