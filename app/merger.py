import tkinter as tk
from tkinter import filedialog
import ui

# Function to open file dialog and let the user select PDF files
def choose_files():
    filetypes = [('PDF', '*.pdf')]
    paths = filedialog.askopenfilenames(title='Choose file', filetypes=filetypes)
    update_file_display(paths)

# Function to update the UI with the selected file paths in the listbox
def update_file_display(locations):
    for location in locations:
        ui.listbox_files.insert(tk.END, location)

# Function to retrieve the entered file name from the name entry field
def get_file_name():
    name = ui.entry_name.get()
    return name

# Function to open a folder dialog and update the location entry field
def get_file_location():
    file_path = filedialog.askdirectory(
        title="Choose where to save the merged PDF",
    )
    update_location(file_path)

# Function to update the location entry field with the selected directory
def update_location(directory):
    ui.entry_location.config(state="normal")         # Temporarily allow editing
    ui.entry_location.delete(0, tk.END)              # Clear previous text
    ui.entry_location.insert(0, directory)           # Insert new directory
    ui.entry_location.config(state="readonly")       # Set back to read-only