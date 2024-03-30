import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from fake import manual_testing

def switch_to_input_frame():
    main_frame.pack_forget()
    input_frame.pack(fill="both", expand=True)

def switch_to_main_frame():
    input_frame.pack_forget()
    main_frame.pack(fill="both", expand=True)
def submit_news():
    news_input = news_entry.get("1.0", "end-1c")  # Get text from the text entry widget
    if news_input.strip():  # Check if the input is not empty
        result = manual_testing(news_input)  # Call the manual_testing function
        messagebox.showinfo("Result", f"The news is: {result}")  # Show the result in a message box
    else:
        messagebox.showwarning("Warning", "Please enter a news article.")  # Show a warning if input is empty


# Create the main window
root = tk.Tk()
root.title("Fake News API")

# Load the background image
background_image = Image.open(r"C:\Users\rohan\Downloads\_4fbc0c76-24dd-45b8-ba51-5da32a87f93c.jpg")  # Replace "background_image.jpg" with your image path
background_image = background_image.resize((1920, 1080), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(background_image)

backy=Image.open(r"C:\Users\rohan\Downloads\3840x2160-black-solid-color-background.jpg")
backy = backy.resize((1920, 1080), Image.ANTIALIAS)
backy = ImageTk.PhotoImage(backy)

# Determine the window size
window_width = 1920
window_height = 1080

# Create a frame for the initial screen
main_frame = tk.Frame(root, width=window_width, height=window_height)
main_frame.pack_propagate(False)  # Prevent frame from resizing
main_frame.pack(fill="both", expand=True)

# Add background image to the main frame
background_label = tk.Label(main_frame, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Create a button to switch to the input screen
enter_button = tk.Button(main_frame, text="Enter news articles", command=switch_to_input_frame, font=("Helvetica", 25), bg="gray")
enter_button.pack()
enter_button.place(x=600, y=690, width=300, height=65)

# Create a frame for the input screen
input_frame = tk.Frame(root, width=window_width, height=window_height)
input_frame.pack_propagate(False)  # Prevent frame from resizing

# Add background image to the input frame
input_background_label = tk.Label(input_frame, image=backy)
input_background_label.place(relwidth=1, relheight=1)

# Create a label for entering news
news_label = tk.Label(input_frame, text="Enter news article", font=("Helvetica", 16))
news_label.pack()
news_label.place(x=320, y=70,width=904)

# Create a text entry widget for entering news article
news_entry = tk.Text(input_frame, height=30, width=100, font=("Helvetica", 12))
news_entry.pack()
news_entry.place(x=320, y=100)

# Create a submit button
submit_button = tk.Button(input_frame, text="Submit", font=(25),command=submit_news)
submit_button.pack()
submit_button.place(x=888, y=700,width=80,height=35)

# Create a button to go back to the main screen
back_button = tk.Button(input_frame, text="Go back", command=switch_to_main_frame, font=(25))
back_button.pack()
back_button.place(x=600, y=700, width= 80, height= 35)

# Run the Tkinter event loop
root.mainloop()
