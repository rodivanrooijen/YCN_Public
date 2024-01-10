import tkinter as tk
import webbrowser

def reverse_image_search():
    search_query = entry.get()
    search_url = f"https://www.google.com/searchbyimage?image_url={search_query}"
    webbrowser.open(search_url)

root = tk.Tk()
root.title("Google Reverse Image Search")

label = tk.Label(root, text="Enter image URL:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Search", command=reverse_image_search)
button.pack()

root.mainloop()
