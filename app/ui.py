import tkinter as tk
import merger

root = tk.Tk()
root.title("PDF Merger")
root.geometry("800x420")
root.resizable(False, False)
root.configure(bg="#061A40")

# Upload Section
label_files = tk.Label(root, text="Files:", font=("Arial", 12, "bold"), bg="#061A40", fg="#FF7B00")
label_files.place(x=20, y=20)

btn_upload = tk.Button(root, text="Upload file", width=15, command=merger.choose_files)
btn_upload.place(x=80, y=20)

# File Display Area
frame_files = tk.Frame(root, bd=2, relief="solid", width=300, height=325, bg="#FEFEFE")
frame_files.place(x=20, y=75)

listbox_files = tk.Listbox(frame_files, width=43, height=20, bg="#FFFFFF", fg="#000000", selectbackground="#FF7B00")
listbox_files.pack(padx=5, pady=5)

# Merged File Location
label_location = tk.Label(root, text="Location", font=("Arial", 12, "bold"), bg="#061A40", fg="#FF7B00")
label_location.place(x=378, y=120)

entry_location = tk.Entry(root, width=40, bg="#FEFEFE", state="readonly")
entry_location.place(x=380, y=150)

btn_choose = tk.Button(root, text="Choose location", width=15, command=merger.get_file_location)
btn_choose.place(x=630, y=146)

# File Name
label_name = tk.Label(root, text="Name", font=("Arial", 12, "bold"), bg="#061A40", fg="#FF7B00")
label_name.place(x=378, y=200)

entry_name = tk.Entry(root, width=40, bg="#FEFEFE")
entry_name.place(x=380, y=230)

label_ext = tk.Label(root, text=".pdf", font=("Arial", 12, "bold"), bg="#061A40", fg="#FF7B00")
label_ext.place(x=630, y=228)

# Submit Button
btn_submit = tk.Button(root, text="Submit", width=20, height=2, bg="#FF7B00", fg="#FEFEFE", activebackground="#FE6A00", activeforeground="#FEFEFE")
btn_submit.place(x=450, y=300)