import tkinter as tk
from pushupf import pushmadu
from squats import squat
from curlf import curl
from situps import situp

#function to be called when the pushup button is clicked
def pushup_window():
    pushmadu()
#function to be called when the pushup button is clicked
def squats_window():
    squat()
#function to be called when the pushup button is clicked
def curl_window():
    curl()
#function to be called when the pushup button is clicked
def situp_window():
    situp()
# Create a new window

root = tk.Tk()

# Set the window title
root.title("Exercise Tracker")

# Create a label to display instructions
instructions_label = tk.Label(root, text="Click on an exercise to track it:")
instructions_label.pack()

# Create a frame to hold the pushup and squats buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Load the image file for the Pushup button
pushup_image = tk.PhotoImage(file="img/push.png")
squat_image = tk.PhotoImage(file='img/squat.png')
situp_image = tk.PhotoImage(file = "img/situp.png")
curl_image = tk.PhotoImage(file = "img/curl.png")


# Create the Pushup button with the image and size
pushup_button = tk.Button(button_frame,text="push-up", image=pushup_image, compound=tk.TOP,command=pushup_window,borderwidth=10, relief="groove", bd=5, highlightthickness=5)
pushup_button.pack(side="left", padx=10, pady=10)

# Create the Squats button with default size
squats_button = tk.Button(button_frame, text="Squats", compound=tk.TOP, command=squats_window,image=squat_image,borderwidth=10, relief="groove", bd=5, highlightthickness=5)
squats_button.pack(side="left", padx=10, pady=10)

# Create a frame to hold the other three buttons
other_buttons_frame = tk.Frame(root)
other_buttons_frame.pack()

# Create the Situps button with default size
situps_button = tk.Button(other_buttons_frame, text="Situps", compound=tk.TOP,image=situp_image,command = situp_window,borderwidth=10, relief="groove", bd=5, highlightthickness=5)
situps_button.pack(side="left", padx=10, pady=10)

# Create the Curl button with default size
curl_button = tk.Button(other_buttons_frame, text="Curl", compound=tk.TOP,image=curl_image,borderwidth=10, command = curl_window,relief="groove", bd=5, highlightthickness=5)
curl_button.pack(side="left", padx=10, pady=10)

# Start the main event loop
root.mainloop()
