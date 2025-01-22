


# from plyer import notification  # pip install plyer
# import time

# def notifyMe(title, message):
#     notification.notify(
#         title=title,
#         message=message,
#         app_icon=None,  # Use raw string or double backslashes
#         timeout=10,
#     )

# if __name__ == '__main__':
#     while True:
#         notifyMe("Hey User, take a break now !!", "You should follow the 20-20-20 rule to keep your eyes healthy")
#         time.sleep(1200)  # 1200 seconds = 20 minutes






import tkinter as tk
from tkinter import messagebox

# Dictionary to store event details: Event name -> list of participants
events = {}

# Function to add a new event
def add_event():
    event_name = event_name_entry.get()
    if event_name:
        if event_name not in events:
            events[event_name] = []
            messagebox.showinfo("Success", f"Event '{event_name}' added successfully. xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        else:
            messagebox.showwarning("Warning", "Event already exists.")
    else:
        messagebox.showwarning("Input Error", "Please enter an event name.")
    event_name_entry.delete(0, tk.END)

# Function to add a participant to an event
def add_participant():
    event_name = event_name_participant_entry.get()
    participant_name = participant_name_entry.get()
    contact = contact_entry.get()
    department = department_entry.get()
    
    if event_name and participant_name and contact and department:
        if event_name in events:
            events[event_name].append((participant_name, contact, department, "Not Attended"))
            messagebox.showinfo("Success", f"Participant '{participant_name}' added to '{event_name}'.")
        else:
            messagebox.showwarning("Event Not Found", f"Event '{event_name}' not found.")
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")
    
    event_name_participant_entry.delete(0, tk.END)
    participant_name_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    department_entry.delete(0, tk.END)

# Function to display participants of a specific event
def display_participants():
    event_name = event_name_display_entry.get()
    if event_name in events:
        participants = events[event_name]
        participants_list.delete(1.0, tk.END)
        for participant in participants:
            participants_list.insert(tk.END, f"{participant[0]} | {participant[1]} | {participant[2]} | {participant[3]}\n")
    else:
        messagebox.showwarning("Event Not Found", f"Event '{event_name}' not found.")
    event_name_display_entry.delete(0, tk.END)

# Function to mark attendance of a participant
def mark_attendance():
    event_name = event_name_attendance_entry.get()
    participant_name = participant_name_attendance_entry.get()
    
    if event_name in events:
        for i, participant in enumerate(events[event_name]):
            if participant[0] == participant_name:
                updated_participant = (participant_name, participant[1], participant[2], attendance_var.get())
                events[event_name][i] = updated_participant
                messagebox.showinfo("Success", f"Attendance for '{participant_name}' marked as {attendance_var.get()}.")
                break
        else:
            messagebox.showwarning("Participant Not Found", f"Participant '{participant_name}' not found in event '{event_name}'.")
    else:
        messagebox.showwarning("Event Not Found", f"Event '{event_name}' not found.")
    
    event_name_attendance_entry.delete(0, tk.END)
    participant_name_attendance_entry.delete(0, tk.END)

# Function to generate summary of participants in all events
def generate_summary():
    summary_list.delete(1.0, tk.END)
    for event_name, participants in events.items():
        summary_list.insert(tk.END, f"Event: {event_name} - Total Participants: {len(participants)}\n")
        for participant in participants:
            summary_list.insert(tk.END, f"  {participant[0]} | {participant[3]}\n")

# GUI Setup
root = tk.Tk()
root.title("College Event Management System")
root.configure(bg="lightblue")
root.geometry("800x800")

# Frames with Background Colors
frame1 = tk.Frame(root, bg="lightgreen", bd=2, relief="solid")
frame1.pack(padx=10, pady=10, fill="x")

frame2 = tk.Frame(root, bg="lightyellow", bd=2, relief="solid")
frame2.pack(padx=10, pady=10, fill="x")

frame3 = tk.Frame(root, bg="lightcoral", bd=2, relief="solid")
frame3.pack(padx=10, pady=10, fill="x")

frame4 = tk.Frame(root, bg="lightgray", bd=2, relief="solid")
frame4.pack(padx=10, pady=10, fill="x")

frame5 = tk.Frame(root, bg="lightseagreen", bd=2, relief="solid")
frame5.pack(padx=10, pady=10, fill="x")

# Event Name Entry
event_name_label = tk.Label(frame1, text="Event Name:", bg="lightgreen")
event_name_label.grid(row=0, column=0, padx=5, pady=5)
event_name_entry = tk.Entry(frame1)
event_name_entry.grid(row=0, column=1, padx=5, pady=5)

# Add Event Button
add_event_button = tk.Button(frame1, text="Add Event", command=add_event, bg="blue", fg="white")
add_event_button.grid(row=0, column=2, padx=5, pady=5)

# Participant Details Entry
event_name_participant_label = tk.Label(frame2, text="Event Name:", bg="lightyellow")
event_name_participant_label.grid(row=0, column=0, padx=5, pady=5)
event_name_participant_entry = tk.Entry(frame2)
event_name_participant_entry.grid(row=0, column=1, padx=5, pady=5)

participant_name_label = tk.Label(frame2, text="Participant Name:", bg="lightyellow")
participant_name_label.grid(row=1, column=0, padx=5, pady=5)
participant_name_entry = tk.Entry(frame2)
participant_name_entry.grid(row=1, column=1, padx=5, pady=5)

contact_label = tk.Label(frame2, text="Contact Number:", bg="lightyellow")
contact_label.grid(row=2, column=0, padx=5, pady=5)
contact_entry = tk.Entry(frame2)
contact_entry.grid(row=2, column=1, padx=5, pady=5)

department_label = tk.Label(frame2, text="Department:", bg="lightyellow")
department_label.grid(row=3, column=0, padx=5, pady=5)
department_entry = tk.Entry(frame2)
department_entry.grid(row=3, column=1, padx=5, pady=5)

# Add Participant Button
add_participant_button = tk.Button(frame2, text="Add Participant", command=add_participant, bg="green", fg="white")
add_participant_button.grid(row=4, column=1, padx=5, pady=5)

# Display Participants Entry
event_name_display_label = tk.Label(frame3, text="Event Name to Display Participants:", bg="lightcoral")
event_name_display_label.grid(row=0, column=0, padx=5, pady=5)
event_name_display_entry = tk.Entry(frame3)
event_name_display_entry.grid(row=0, column=1, padx=5, pady=5)

# Display Participants Button
display_participants_button = tk.Button(frame3, text="Display Participants", command=display_participants, bg="purple", fg="white")
display_participants_button.grid(row=0, column=2, padx=5, pady=5)

# Participants List Box
participants_list = tk.Text(frame3, width=50, height=10)
participants_list.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Attendance Marking Entry
event_name_attendance_label = tk.Label(frame4, text="Event Name:", bg="lightgray")
event_name_attendance_label.grid(row=0, column=0, padx=5, pady=5)
event_name_attendance_entry = tk.Entry(frame4)
event_name_attendance_entry.grid(row=0, column=1, padx=5, pady=5)

participant_name_attendance_label = tk.Label(frame4, text="Participant Name:", bg="lightgray")
participant_name_attendance_label.grid(row=1, column=0, padx=5, pady=5)
participant_name_attendance_entry = tk.Entry(frame4)
participant_name_attendance_entry.grid(row=1, column=1, padx=5, pady=5)

attendance_var = tk.StringVar(value="Not Attended")
attendance_radio1 = tk.Radiobutton(frame4, text="Attended", variable=attendance_var, value="Attended", bg="lightgray")
attendance_radio1.grid(row=2, column=0, padx=5, pady=5)
attendance_radio2 = tk.Radiobutton(frame4, text="Not Attended", variable=attendance_var, value="Not Attended", bg="lightgray")
attendance_radio2.grid(row=2, column=1, padx=5, pady=5)

# Mark Attendance Button (Placed at row 3, column 1)
mark_attendance_button = tk.Button(frame4, text="Mark Attendance", command=mark_attendance, bg="orange", fg="white")
mark_attendance_button.grid(row=3, column=1, padx=5, pady=5)

# Summary Section
generate_summary_button = tk.Button(frame5, text="Generate Event Summary", command=generate_summary, bg="darkblue", fg="white")
generate_summary_button.pack(padx=5, pady=5)

# Summary List Box
summary_list = tk.Text(frame5, width=60, height=10)
summary_list.pack(padx=5, pady=5)

root.mainloop()
