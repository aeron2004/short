import heapq
import tkinter as tk
from tkinter import ttk


# Define your places and their coordinates
places = {
    "Entrance Gate": (500, 650),
    "Mid Str-2nd Flr": (500, 600),
    
    # EAST
    "Str1": (410, 600),
    "Student Center": (280, 600),
    "Str1-2nd Flr": (100, 600),
    "ADMINISTRATION": (100, 550),
    "BOARD ROOM": (180, 550),
    "UNIVERSITY PRES": (260, 550),
    "VP ADMIN": (340, 550),
    "VP ACAD": (410, 550),
    "VP RDE": (455, 550),
    "HRMO": (500, 550),
    "REGISTRAR": (590, 550),    
    
    "2 ways": (100, 500),
    "ACCOUNTING": (100, 415),
    "CASHER": (100, 365),
    "BUDGET": (100, 315),
    "COLLEGE PRES": (100, 265),
    "Str2-down": (165, 265),
    "CANTEEN": (165, 150),
    "Str3-2nd Flr": (100, 150),
    "CATERING": (270, 150),
    "Str4-2nd Flr": (360, 150),
    "way(2)": (425, 150),
    "USC Office": (425, 100),
    
    "LIBRARY": (500, 150),
    
    "Str1-down": (200, 500),
    "SUPPLY": (200, 450),
    "COA": (200, 380),
    "way(1)": (270, 500),
    "COA BODEGA": (270, 380),
    "ICT Office": (270, 250),
    
    "PARKING LOT": (500, 315),
    
    # WEST
    "Str2": (590, 600),
    "REGISTRAR": (590, 550),
    "Str2-2nd Flr": (900, 600),
    "PLANNING": (900, 550),
    "BUILDING & ESTATES": (900, 450),
    "EXIT GATE": (900, 315),
    "NSTP Office": (900, 250),
    "DRRMO": (800, 250),
    "FITNESS STUDIO": (700, 250),
    "DANCE STUDIO": (600, 250),
    "way(3)": (500, 250),
    
    "Str5-2nd Flr": (640, 150),
    "CLINIC": (690, 150),
    "GUIDANCE": (740, 150),
    "PLACEMENT": (800, 150),
    "SAO": (845, 150),
    "Str6-2nd Flr": (900,150),

    
}

# Define paths between locations
paths = [
    ("Entrance Gate", "Mid Str-2nd Flr"),
    ("Mid Str-2nd Flr", "Str1"),
    ("Mid Str-2nd Flr", "Str2"),
    
    # EAST
    ("Entrance Gate", "Str1"),
    ("Str1", "Student Center"),
    ("Str1", "VP ACAD"),
    ("Student Center", "Str1-2nd Flr"),
    ("Str1-2nd Flr", "ADMINISTRATION"),
    ("ADMINISTRATION", "2 ways"),
    ("ADMINISTRATION", "BOARD ROOM"),
    ("BOARD ROOM", "UNIVERSITY PRES"),
    ("UNIVERSITY PRES", "VP ADMIN"),
    ("VP ADMIN", "VP ACAD"),
    ("VP ACAD", "VP RDE"),
    ("VP RDE", "HRMO"),
    ("HRMO", "REGISTRAR"),
    
    ("2 ways", "ACCOUNTING"),
    ("ACCOUNTING", "CASHER"),
    ("CASHER", "BUDGET"),
    ("BUDGET", "COLLEGE PRES"),
    ("COLLEGE PRES","Str2-down"),
    ("Str2-down", "CANTEEN"),   
    ("CANTEEN", "CATERING"),
    ("CANTEEN", "Str3-2nd Flr"),
    ("CATERING", "Str4-2nd Flr"),
    ("Str4-2nd Flr", "way(2)"),
    ("way(2)", "USC Office"),
    
    ("way(2)","LIBRARY"),
    
    ("2 ways", "Str1-down"),
    ("Str1-down", "SUPPLY"),
    ("SUPPLY", "COA"),
    ("Str1-down", "way(1)"),
    ("way(1)", "COA BODEGA"),
    ("COA BODEGA", "ICT Office"),
    ("COA BODEGA", "PARKING LOT"),
    ("ICT Office", "PARKING LOT"),
    ("PARKING LOT", "way(3)"),
    
    ("way(3)", "LIBRARY"),
    
    # WEST
    ("Entrance Gate", "Str2"),
    ("Str2", "Str2-2nd Flr"),
    ("Str2", "REGISTRAR"),
    ("REGISTRAR", "PLANNING"),
    ("Str2-2nd Flr", "PLANNING"),
    ("PLANNING", "BUILDING & ESTATES"),
    ("BUILDING & ESTATES", "EXIT GATE"),
    ("EXIT GATE", "NSTP Office"),  
    ("NSTP Office", "DRRMO"),
    ("DRRMO", "FITNESS STUDIO"),
    ("FITNESS STUDIO", "DANCE STUDIO"),
    
    ("DANCE STUDIO", "way(3)"),
    ("way(3)", "PARKING LOT"),
    
    ("LIBRARY", "Str5-2nd Flr"),
    ("Str5-2nd Flr", "CLINIC"),
    ("CLINIC", "GUIDANCE"),
    ("GUIDANCE", "PLACEMENT"),
    ("PLACEMENT", "SAO"),
    ("SAO", "Str6-2nd Flr"),

]


# Create a grid to represent the map
grid = [[0] * 900 for _ in range(700)]  # Initialize grid with zeros

# Update grid to mark blocked locations
grid[places["Entrance Gate"][1]][places["Entrance Gate"][0]] = 1
grid[places["Mid Str-2nd Flr"][1]][places["Mid Str-2nd Flr"][0]] = 1
grid[places["2 ways"][1]][places["2 ways"][0]] = 1
grid[places["Str1"][1]][places["Str1"][0]] = 1
grid[places["Str2"][1]][places["Str2"][0]] = 1
grid[places["Str1-down"][1]][places["Str1-down"][0]] = 1
grid[places["way(2)"][1]][places["way(2)"][0]] = 1
grid[places["CANTEEN"][1]][places["CANTEEN"][0]] = 1

# Function to find the shortest path between two points
def shortest_path(start, goal):
    # Initialize the queue and visited set
    queue = [(0, start, [])]  # Include a list to store the path
    visited = set()

    # While the queue is not empty
    while queue:
        # Dequeue the current node, distance, and path
        dist, current, path = heapq.heappop(queue)

        # If this node has not been visited yet
        if current not in visited:
            # Mark this node as visited
            visited.add(current)

            # If this is the goal node, we are done
            if current == goal:
                return dist, path + [current]  # Return the path as well

            # Otherwise, enqueue all neighbors
            for neighbor in paths:
                if current == neighbor[0] and neighbor[1] not in visited:
                    heapq.heappush(queue, (dist + 1, neighbor[1], path + [current]))
                elif current == neighbor[1] and neighbor[0] not in visited:
                    heapq.heappush(queue, (dist + 1, neighbor[0], path + [current]))

    # If we get here, there is no path between the start and goal
    return None

# Define the main GUI window
root = tk.Tk()
#root.title("A Star Search Algorithm  ")
root.title("SNSU MAIN - GROUND FLOOR")
# Create a canvas to draw the map
canvas = tk.Canvas(root, width=1000, height=700)
canvas.pack()

# Draw paths
for start, end in paths:
    (x1, y1), (x2, y2) = places[start], places[end]
    canvas.create_line(x1, y1, x2, y2, fill="black")

# Draw places
for place, (x, y) in places.items():
    circle = canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="green")
    label = canvas.create_text(x, y + 20, text=place, anchor="w", font = ("Arial", 7))
    # Adjust the label's x-coordinate to center it below the circle
    label_bbox = canvas.bbox(label)
    label_width = label_bbox[2] - label_bbox[0]
    canvas.move(label, -label_width / 2, 0)

# Create a frame to hold the start and goal labels and entry fields
frame = ttk.Frame(root, padding="20")

# Place the frame at the bottom
#side = "bottom"
frame.pack() 

# Create labels for start and goal with Added Font Style and Size
start_label = ttk.Label(frame, text="Start:", font = ("Arial, 10"))
start_label.grid(row=0, column=0)

goal_label = ttk.Label(frame, text="Goal:", font = ("Arial, 10"))
goal_label.grid(row=1, column=0)

# Create drop-down menus for selecting start and goal locations
start_var = tk.StringVar()
start_dropdown = ttk.Combobox(frame, textvariable=start_var, values=list(places.keys()))
start_dropdown.grid(row=0, column=1)

goal_var = tk.StringVar()
goal_dropdown = ttk.Combobox(frame, textvariable=goal_var, values=list(places.keys()))
goal_dropdown.grid(row=1, column=1)

# Create a label to display the shortest path
shortest_path_label = ttk.Label(root, text="Shortest Path:")
shortest_path_label.pack()

# Create a label to display the places of the shortest path
shortest_path_places = tk.StringVar()
shortest_path_places_label = ttk.Label(root, textvariable=shortest_path_places)
shortest_path_places_label.pack()

# Create a button to find the shortest path
def animate_path():
    start = start_var.get()
    goal = goal_var.get()

    shortest_path_label.config(text="Searching...")
    root.update()

    result = shortest_path(start, goal)

    if result is not None:
        path_length, path = result
        shortest_path_label.config(text=f"Shortest Path Found: {path_length}")
        shortest_path_places.set(" -> ".join(path))  # Set the places of the shortest path
        canvas.delete("shortest_path")  # Clear previous path if any

        # Draw the shortest path in red
        for i in range(len(path) - 1):
            (x1, y1), (x2, y2) = places[path[i]], places[path[i + 1]]
            canvas.create_line(x1, y1, x2, y2, fill="red", tags="shortest_path")

    else:
        shortest_path_label.config(text="No path found")

# Create a button to find the shortest path
find_button = ttk.Button(frame, text="Find Shortest Path", command=animate_path)
find_button.grid(row=2, columnspan=2)

# Start the GUI main loop
root.mainloop()

