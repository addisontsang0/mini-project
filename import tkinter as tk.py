import tkinter as tk
from tkinter import messagebox
result = messagebox.askyesno(
    title = "Yes No Demo",
    messgae = " Start new order?",
    detail = "Click NO to Exit"
)

if not result:
    exit()
    