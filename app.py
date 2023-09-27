import tkinter as tk
from tkinter import messagebox

contacts = {}  # Dictionary to store contacts

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    if name and phone:
        contacts[name] = phone
        update_listbox()
        clear_entries()
    else:
        messagebox.showwarning("Missing Information", "Please enter both name and phone number.")

def remove_contact():
    selected_contact = contacts_listbox.get(contacts_listbox.curselection())
    if selected_contact:
        # Extract the contact name from the selected item
        name, _ = selected_contact.split(":")
        if name in contacts:
            del contacts[name]
            update_listbox()

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

def update_listbox():
    contacts_listbox.delete(0, tk.END)
    for name, phone in contacts.items():
        contacts_listbox.insert(tk.END, f"{name}: {phone}")

def on_resize(event):
    # Adjust the width of listbox and buttons based on window size
    listbox_width = event.width - 40
    contacts_listbox.config(width=listbox_width)
    add_button.config(width=(listbox_width // 2))
    remove_button.config(width=(listbox_width // 2))

root = tk.Tk()
root.title("Contact Management System")

# Labels and Entry fields
name_label = tk.Label(root, text="Name:", bg="lightblue" ,font=("Helvetica", 13))
name_label.pack(fill=tk.X, padx=20, pady=5)

name_entry = tk.Entry(root)
name_entry.pack(fill=tk.X, padx=25, pady=5)

phone_label = tk.Label(root, text="Phone:", bg="lightblue", font=("Helvetica", 13))
phone_label.pack(fill=tk.X, padx=20, pady=5)

phone_entry = tk.Entry(root)
phone_entry.pack(fill=tk.X, padx=25, pady=5)

# Buttons
add_button = tk.Button(root, text="Add Contact", command=add_contact, bg="green", fg="white", font=("Helvetica", 12))
add_button.pack(fill=tk.X, padx=10, pady=5)

remove_button = tk.Button(root, text="Remove Contact", command=remove_contact, bg="red", fg="white", font=("Helvetica", 12))
remove_button.pack(fill=tk.X, padx=10, pady=5)

# Listbox
contacts_listbox = tk.Listbox(root, selectmode=tk.SINGLE,bg="lightyellow" ,font=("Helvetica", 14))
contacts_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# Populate the listbox with existing contacts
update_listbox()

# Configure the listbox and buttons for resizing
root.bind("<Configure>", on_resize)

root.mainloop()
