import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfWriter
import os

# Global list to store user-selected PDF file paths
selected_paths = []

# References to UI widgets (bound at runtime via `bind_ui_elements`)
listbox_files = None
entry_location_widget = None
entry_name_widget = None


def bind_ui_elements(listbox, entry_location, entry_name):
    """
    Injects UI widget references from the main UI module.
    This decouples UI creation from logic and avoids circular imports.
    """
    global listbox_files, entry_location_widget, entry_name_widget
    listbox_files = listbox
    entry_location_widget = entry_location
    entry_name_widget = entry_name


def choose_files():
    """
    Opens a file dialog for the user to select multiple PDF files.
    Updates the global `selected_paths` and refreshes the file display.
    """
    global selected_paths
    filetypes = [('PDF', '*.pdf')]
    selected_paths = filedialog.askopenfilenames(title='Choose file', filetypes=filetypes)
    update_file_display(selected_paths)


def update_file_display(locations):
    """
    Clears and repopulates the file list UI with the selected file paths.
    """
    listbox_files.delete(0, tk.END)
    for location in locations:
        listbox_files.insert(tk.END, location)


def get_file_name():
    """
    Returns the trimmed user input for the output file name.
    """
    return entry_name_widget.get().strip()


def get_file_location():
    """
    Opens a directory chooser and updates the location field in the UI.
    """
    file_path = filedialog.askdirectory(title="Choose where to save the merged PDF")
    if file_path:
        update_location(file_path)


def update_location(directory):
    """
    Inserts the selected output directory into the location entry widget.
    This is done by temporarily making the widget editable.
    """
    entry_location_widget.config(state="normal")
    entry_location_widget.delete(0, tk.END)
    entry_location_widget.insert(0, directory)
    entry_location_widget.config(state="readonly")


def merge_pdfs():
    """
    Merges the selected PDF files into a single output file.
    Validates inputs, writes the merged file using `pypdf`,
    and provides user feedback via message boxes.
    """
    file_name = get_file_name()
    directory = entry_location_widget.get().strip()

    # Input validation
    if not file_name:
        messagebox.showerror("Missing File Name", "Please enter a name for the merged PDF file.")
        return
    if not directory:
        messagebox.showerror("Missing Location", "Please choose a location to save the merged PDF.")
        return
    if not selected_paths:
        messagebox.showerror("No Files Selected", "Please select PDF files to merge.")
        return

    output_path = os.path.join(directory, f"{file_name}.pdf")

    try:
        merger = PdfWriter()
        for path in selected_paths:
            merger.append(path)
        merger.write(output_path)
        merger.close()
        messagebox.showinfo("Success", f"PDF successfully saved to:\n{output_path}")
    except Exception as e:
        # Surface any unexpected I/O or parsing issues
        messagebox.showerror("Merge Failed", f"An error occurred while merging the PDFs:\n{e}")