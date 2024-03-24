import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET

def fix_y_value(xml_file_path):
    # Load the XML file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Find all 'BendPoint' elements in the XML tree
    for bend_point in root.findall(".//BendPoint"):
        y_element = bend_point.find('Y')
        if y_element is not None:
            y_value = int(y_element.text)
            # Check if the Y value exceeds 2000 and fix it if necessary
            if y_value > 2000:
                y_element.text = '2000'

    # Save the modified XML back to the same file
    tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)
    return "File processed successfully."

def open_file_dialog():
    filepath = filedialog.askopenfilename(
        title="Open XML File", 
        filetypes=(("XML files", "*.xml"), ("All files", "*.*")))
    
    if filepath:
        message = fix_y_value(filepath)
        status_label.config(text=message)

# Create the main window
root = tk.Tk()
root.title("XML Y-Value Fixer")

# Create and pack a button to open the file dialog
open_button = tk.Button(root, text="Open XML File", command=open_file_dialog)
open_button.pack(pady=20)

# Status label to show messages
status_label = tk.Label(root, text="")
status_label.pack(pady=20)

# Start the GUI event loop
root.mainloop()
