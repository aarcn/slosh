import tkinter as tk

# Creates the main application window
root = tk.Tk()
root.title("Slosh GUI")
root.geometry("800x600")

# label widget
title_label = tk.Label(root, text="Slosh Application", font=("Calibri", 26))
title_label.pack(pady=20)


# Example of adding a button that will later be used to interact with your card counting logic
def on_button_click():
    print("Button clicked!")


action_button = tk.Button(root, text="Start Counting", command=on_button_click)
action_button.pack(pady=10)

# If you need a canvas to display cards, you can create one:
canvas = tk.Canvas(root, width=600, height=400, bg="green")
canvas.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
