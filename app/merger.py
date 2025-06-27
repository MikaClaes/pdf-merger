import tkinter as tk
from tkinter import filedialog
import ui


# Function to open file dialog and let the user select PDF files
def choose_files():
    filetypes=[('PDF','*.pdf')]
    paths = filedialog.askopenfilenames(title='Choose file',filetypes=filetypes)
    update_file_display(paths)

# Function to update the UI with the selected file paths
def update_file_display(locations):
    for location in locations:
        ui.listbox_files.insert(tk.END, location)