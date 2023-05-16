import requests
import json
import tkinter as tk
from tkinter import messagebox

def get_gender_information():
    name = entry.get()

    if not name:
        messagebox.showwarning("Error", "Please enter a name.")
        return

    content = requests.get(f"https://api.genderize.io/?name={name}").text
    data = json.loads(content)

    if "gender" in data and "probability" in data:
        gender = data["gender"]
        probability = data["probability"]
        new_probability = probability * 100

        result_text.set(f"With a probability of: {new_probability}% \n {name} is a '{gender}'")
    else:
        result_text.set("Unable to determine the gender.")

# Create the main window
window = tk.Tk()
window.title("Gender Information")
window.geometry("400x200") 

# Create a label and an entry field for the name
name_label = tk.Label(window, text="Name:")
name_label.pack()
entry = tk.Entry(window)
entry.pack()

# Create a button to retrieve the gender information
button = tk.Button(window, text="Get Gender", command=get_gender_information)
button.place(x=165, y=50)  # Adjust the coordinates to position the button

# Create a label to display the result
result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text, wraplength=300)
result_label.pack()
result_label.place(x=90,y=100)
result_label.configure(font=("Calibri", 14))  # Adjust the font attributes as desired


# Start the Tkinter event loop
window.mainloop()
