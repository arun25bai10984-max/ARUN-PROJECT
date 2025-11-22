import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def _init_(self, root):
        self.root = root
        self.root.title("My To-Do List")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Title label
        title_label = tk.Label(
            root,
            text="📝 To-Do List",
            font=("Arial", 20, "bold"),
            bg="#4CAF50",
            fg="white",
            pady=10
        )
        title_label.pack(fill=tk.X)
        
        # Frame for input
        input_frame = tk.Frame(root, bg="#f0f0f0", pady=10)
        input_frame.pack(fill=tk.X)
        
        # Entry widget
        self.task_entry = tk.Entry(
            input_frame,
            font=("Arial", 12),
            width=30
        )
        self.task_entry.pack(side=tk.LEFT, padx=10)
        self.task_entry.bind("<Return>", lambda e: self.add_task())
        
        # Add button
        add_button = tk.Button(
            input_frame,
            text="Add",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            command=self.add_task,
            width=8
        )
        add_button.pack(side=tk.LEFT)
        
        # Frame for listbox and scrollbar
        list_frame = tk.Frame(root)
        list_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listbox
        self.task_listbox = tk.Listbox(
            list_frame,
            font=("Arial", 12),
            selectmode=tk.SINGLE,
            yscrollcommand=scrollbar.set,
            height=15
        )
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.task_listbox.yview)
        
        # Button frame
        button_frame = tk.Frame(root, bg="#f0f0f0", pady=10)
        button_frame.pack(fill=tk.X)
        
        # Delete button
        delete_button = tk.Button(
            button_frame,
            text="Delete Task",
            font=("Arial", 11),
            bg="#f44336",
            fg="white",
            command=self.delete_task,
            width=15
        )
        delete_button.pack(side=tk.LEFT, padx=10)
        
        # Clear all button
        clear_button = tk.Button(
            button_frame,
            text="Clear All",
            font=("Arial", 11),
            bg="#ff9800",
            fg="white",
            command=self.clear_all,
            width=15
        )
        clear_button.pack(side=tk.LEFT, padx=10)
        
    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")
    
    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete!")
    
    def clear_all(self):
        if self.task_listbox.size() > 0:
            result = messagebox.askyesno("Confirm", "Delete all tasks?")
            if result:
                self.task_listbox.delete(0, tk.END)
        else:
            messagebox.showinfo("Info", "No tasks to clear!")

if _name_ == "_main_":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()