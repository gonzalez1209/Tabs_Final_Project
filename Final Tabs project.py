import tkinter as tk

# The Event class represents an event and its properties
class Event:
    def __init__(self, name, date, time, location, description):
        # Initialize instance variables with provided arguments
        self.name = name
        self.date = date
        self.time = time
        self.location = location
        self.description = description
        self.invited_friends = []  # Start with an empty list of invited friends

# The EventPlanner class manages a list of events and provides methods to create new events and invite friends to an existing event
class EventPlanner:
    def __init__(self):
        self.events = []  # Initialize an empty list of events

    # Create a new event with the provided arguments and add it to the list of events
    def create_event(self, name, date, time, location, description):
        new_event = Event(name, date, time, location, description)
        self.events.append(new_event)

    # Add the provided friend to the list of invited friends for the provided event
    def invite_friend(self, event, friend):
        event.invited_friends.append(friend)

# The EventGUI class creates the GUI for the event planner and handles user input
class EventGUI:
    def __init__(self, planner):
        self.planner = planner  # Store the provided EventPlanner object

        self.window = tk.Tk()  # Create a new tkinter window
        self.window.title("Event Planner")  # Set the window title

        # Create labels and entry boxes for event information
        self.name_label = tk.Label(self.window, text="Event Name:")
        self.name_label.grid(row=0, column=0)

        self.name_entry = tk.Entry(self.window)
        self.name_entry.grid(row=0, column=1)

        self.date_label = tk.Label(self.window, text="Event Date:")
        self.date_label.grid(row=1, column=0)

        self.date_entry = tk.Entry(self.window)
        self.date_entry.grid(row=1, column=1)

        self.time_label = tk.Label(self.window, text="Event Time:")
        self.time_label.grid(row=2, column=0)

        self.time_entry = tk.Entry(self.window)
        self.time_entry.grid(row=2, column=1)

        self.location_label = tk.Label(self.window, text="Event Location:")
        self.location_label.grid(row=3, column=0)

        self.location_entry = tk.Entry(self.window)
        self.location_entry.grid(row=3, column=1)

        self.description_label = tk.Label(self.window, text="Event Description:")
        self.description_label.grid(row=4, column=0)

        self.description_entry = tk.Entry(self.window)
        self.description_entry.grid(row=4, column=1)

        # Create a button to create a new event and add it to the window
        self.create_button = tk.Button(self.window, text="Create Event", command=self.create_event)
        self.create_button.grid(row=5, column=0)

        # Create a label and listbox for selecting friends to invite
        self.invite_label = tk.Label(self.window, text="Invite Friends:")
        self.invite_label.grid(row=6, column=0)

        self.friend_listbox = tk.Listbox(self.window, selectmode=tk.MULTIPLE)
        self.friend_listbox.grid(row=7, column=0)

        # Create a button to invite selected friends to the most recently created event and add it to the window
        self.invite_button = tk.Button
