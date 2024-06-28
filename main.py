import tkinter as tk
import math
import time

def update_clock():
    current_time = time.localtime()
    hours = current_time.tm_hour
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Calculate angles for hour, minute, and second hands
    hour_angle = math.radians(90 - (hours % 12 * 30 + minutes / 2))
    minute_angle = math.radians(90 - minutes * 6)
    second_angle = math.radians(90 - seconds * 6)

    # Clear canvas
    canvas.delete("all")

    # Draw clock face
    canvas.create_oval(50, 50, 250, 250, width=2)

    # Draw numbers
    for i in range(1, 13):
        angle = math.radians(90 - i * 30)
        x = 150 + 85 * math.cos(angle)
        y = 150 - 85 * math.sin(angle)
        canvas.create_text(x, y, text=str(i), font=("Arial", 12))

    # Draw hour hand
    hour_hand_length = 50
    hour_hand_x = 150 + hour_hand_length * math.cos(hour_angle)
    hour_hand_y = 150 - hour_hand_length * math.sin(hour_angle)
    canvas.create_line(150, 150, hour_hand_x, hour_hand_y, width=4, fill='blue')

    # Draw minute hand
    minute_hand_length = 70
    minute_hand_x = 150 + minute_hand_length * math.cos(minute_angle)
    minute_hand_y = 150 - minute_hand_length * math.sin(minute_angle)
    canvas.create_line(150, 150, minute_hand_x, minute_hand_y, width=3, fill='green')

    # Draw second hand
    second_hand_length = 80
    second_hand_x = 150 + second_hand_length * math.cos(second_angle)
    second_hand_y = 150 - second_hand_length * math.sin(second_angle)
    canvas.create_line(150, 150, second_hand_x, second_hand_y, width=1, fill='red')

    # Update every second
    root.after(1000, update_clock)

# Create main window
root = tk.Tk()
root.title("Analog Clock Simulation")

# Create canvas widget
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Start clock
update_clock()

# Run tkinter main loop
root.mainloop()
