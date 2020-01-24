import tkinter as tk

root = tk.Tk()

tk.Label(root, text = "Enter price").grid(row = 0, sticky = "W")
tk.Entry(root, width = 20).grid(row = 1, padx=10)
tk.Button(root, text = "Confirm").grid(row = 2)
