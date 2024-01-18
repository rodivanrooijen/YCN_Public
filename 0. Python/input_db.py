import tkinter as tk
import mysql.connecto
r
from tkinter import messagebox

# Define the submit function
def submit():
    name = name_entry.get()
    description = description_entry.get()
    price = price_entry.get()
    img = img_entry.get()
    mainpage = mainpage_var.get()

    # Check if any of the fields are empty
    if not name or not description or not price or not img:
        messagebox.showerror("Error", "Alle velden moeten ingevuld zijn")
        return

    # Convert price to int
    try:
        price = int(price)
    except ValueError:
        messagebox.showerror("Error", "Prijs moet een getal zijn")
        return

    # Construct the SQL statement
    sql = "INSERT INTO airplane_models (id, mainpage, name, description, price, img) VALUES (NULL, %s, %s, %s, %s, %s)"

    # Execute the SQL statement
    try:
        conn = mysql.connector.connect(
            host='db.dutch-aviation.com',
            user= 'md188183db669067',
            password='Bolle031097!',
            database= 'md188183db669067'
        )
        cursor = conn.cursor()

        # Execute the SQL statement with the values as a tuple
        cursor.execute(sql, (mainpage, name, description, price, img))
        conn.commit()

        cursor.close()
        conn.close()

        # Show success message
        messagebox.showinfo("Success", "Data inserted successfully")

        print("Connected to MySQL")

    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Database error: {str(e)}")

# Rest of your code



    # Show alert message
    #messagebox.showinfo("Alert", "Denk er aan dat je de foto's met de juiste naam doorgeeft aan Rodi!")

# Create the GUI
root = tk.Tk()
root.geometry("500x250")  # Set the size of the window
root.title("Nieuw vliegtuig toevoegen")  # Set the title of the window

# Create a frame for the form
form_frame = tk.Frame(root)
form_frame.pack(pady=20)

# Create labels and entry fields
name_label = tk.Label(form_frame, text="Titel:")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(form_frame)
name_entry.grid(row=0, column=1, padx=10, pady=5)

description_label = tk.Label(form_frame, text="Omschrijving:")
description_label.grid(row=1, column=0, padx=10, pady=5)
description_entry = tk.Entry(form_frame)
description_entry.grid(row=1, column=1, padx=10, pady=5)

price_label = tk.Label(form_frame, text="Prijs (Zonder punt of komma ):")
price_label.grid(row=2, column=0, padx=10, pady=5)
price_entry = tk.Entry(form_frame)
price_entry.grid(row=2, column=1, padx=10, pady=5)

img_label = tk.Label(form_frame, text="Image_url (incl .jpeg):")
img_label.grid(row=3, column=0, padx=10, pady=5)
img_entry = tk.Entry(form_frame)
img_entry.grid(row=3, column=1, padx=10, pady=5)

mainpage_label = tk.Label(form_frame, text="Moet het vliegtuig op de hoofdpagina?:")
mainpage_label.grid(row=4, column=0, padx=10, pady=5)
mainpage_var = tk.BooleanVar()
mainpage_checkbox = tk.Checkbutton(form_frame, variable=mainpage_var)
mainpage_checkbox.grid(row=4, column=1, padx=10, pady=5)

# Create a submit button
submit_button = tk.Button(root, text="Toevoegen aan de website", command=submit)
submit_button.pack(pady=10)

root.mainloop()
