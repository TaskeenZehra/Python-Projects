import heapq
import tkinter as tk
from tkinter import ttk
import sys

class NavigationApp:
    def __init__(self, master, lis=None):
        self.master = master
        self.master.title("Karachi City Navigation System")

        self.graph = {
            'AZIZABAD': { 'SHARIFABAD': 2, 'FEDERAL B AREA': 2},
            'NAZIMABAD': { 'Sharifabad':3,'NORTH-NAZIMABAD':3},
            'SHARIFABAD': { 'HUSSAINABAD':1,'AZIZABAD':2,'FEDERAL B AREA': 3,'NAZIMABAD':3},
            'NORTH-NAZIMABAD': { 'NAZIMABAD':3,'NORTH-KARACHI':6,'SAKHI-HASSAN':4},
            'GULBERG': {'FEDERAL B AREA': 3, 'SAKHI-HASSAN': 5},
            'BUFFER-ZONE': { 'FEDERAL B AREA': 5,'NAGAN': 2},
            'SAKHI-HASSAN': {'NORTH-NAZIMABAD': 4,'NAGAN': 2,'GULBERG': 5},
            'SURJANI TOWN': { 'NEW-KARACHI': 6},
            'NEW-KARACHI': { 'NORTH-KARACHI': 3, 'SURJANI TOWN': 6},
            'HUSSAINABAD': { 'SHARIFABAD': 1,  'FEDERAL B AREA': 2 },
            'FEDERAL B AREA': {'SHARIFABAD': 3, 'AZIZABAD': 2, 'GULBERG': 3,  'BUFFER-ZONE': 5,'FEDERAL B AREA': 2},
            'NORTH-KARACHI': { 'NORTH-NAZIMABAD': 6,'NEW-KARACHI': 3},
            'NAGAN': {'SAKHI-HASSAN': 2, 'BUFFER-ZONE': 2}

        }

        ttk.Label(master, text="Select Start Location:").pack(pady=5)

        self.start_var = tk.StringVar()
        self.start_combobox = ttk.Combobox(master, textvariable=self.start_var)
        self.start_combobox['values'] = list(lis or [])
        self.start_combobox.pack(pady=5)

        ttk.Label(master, text="Select End Location:").pack(pady=5)

        self.end_var = tk.StringVar()
        self.end_combobox = ttk.Combobox(master, textvariable=self.end_var)
        self.end_combobox['values'] = list(lis or [])
        self.end_combobox.pack(pady=5)

        ttk.Button(master, text="Find Shortest Path", command=self.find_shortest_path).pack(pady=10)

        self.result_text = tk.Text(master, height=10, width=40)
        self.result_text.pack(pady=10)


    def dijkstra(self, start, end):
        distances = {node.upper(): float('inf') for node in self.graph}

        start = start.upper()
        end = end.upper()

        distances[start] = 0

        priority_queue = [(0, start)]  # Format(distance, node)

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_node in distances and current_distance <= distances[current_node]:
                for neighbor, weight in self.graph[current_node].items():
                    neighbor = neighbor.upper()
                    new_distance = current_distance + weight

                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        heapq.heappush(priority_queue, (new_distance, neighbor))

        return distances[end]

    def find_shortest_path(self):
        start_location = self.start_var.get().upper()
        end_location = self.end_var.get().upper()

        if start_location not in self.graph or end_location not in self.graph:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Invalid locations. Please select valid start and end locations.")
        else:
            shortest_distance = self.dijkstra(start_location, end_location)

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END,f"Shortest Distance from {start_location} to {end_location}: {shortest_distance} Km")


if __name__ == "__main__":

    graph = {
        'AZIZABAD': {'SHARIFABAD': 2, 'FEDERAL B AREA': 2},
        'NAZIMABAD': {'Sharifabad': 3, 'NORTH-NAZIMABAD': 3},
        'SHARIFABAD': {'HUSSAINABAD': 1, 'AZIZABAD': 2, 'FEDERAL B AREA': 3, 'NAZIMABAD': 3},
        'NORTH-NAZIMABAD': {'NAZIMABAD': 3, 'NORTH-KARACHI': 6, 'SAKHI-HASSAN': 4},
        'GULBERG': {'FEDERAL B AREA': 3, 'SAKHI-HASSAN': 5},
        'BUFFER-ZONE': {'FEDERAL B AREA': 5, 'NAGAN': 2},
        'SAKHI-HASSAN': {'NORTH-NAZIMABAD': 4, 'NAGAN': 2, 'GULBERG': 5},
        'SURJANI TOWN': {'NEW-KARACHI': 6},
        'NEW-KARACHI': {'NORTH-KARACHI': 3, 'SURJANI TOWN': 6},
        'HUSSAINABAD': {'SHARIFABAD': 1, 'FEDERAL B AREA': 2},
        'FEDERAL B AREA': {'SHARIFABAD': 3, 'AZIZABAD': 2, 'GULBERG': 3, 'BUFFER-ZONE': 5, 'FEDERAL B AREA': 2},
        'NORTH-KARACHI': {'NORTH-NAZIMABAD': 6, 'NEW-KARACHI': 3},
        'NAGAN': {'SAKHI-HASSAN': 2, 'BUFFER-ZONE': 2}

    }

    def bubble_sort(keys):
        n = len(keys)
        for i in range(n):
            for j in range(0, n - i - 1):
                if keys[j] > keys[j + 1]:
                    keys[j], keys[j + 1] = keys[j + 1], keys[j]
        return keys


    def sort_keys():
        keys = list(graph.keys())
        sorted_keys = bubble_sort(keys)
        return tuple(sorted_keys)


    start = tk.Tk()
    l = sort_keys()
    app = NavigationApp(start, l)
    start.mainloop()
