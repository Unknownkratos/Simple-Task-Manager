import tkinter as tk

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.tasks = []

        # Task Name Entry
        self.task_name_label = tk.Label(root, text="Task Name:")
        self.task_name_label.pack()
        self.task_name_entry = tk.Entry(root)
        self.task_name_entry.pack()

        # Task Description Entry
        self.task_desc_label = tk.Label(root, text="Task Description:")
        self.task_desc_label.pack()
        self.task_desc_entry = tk.Entry(root)
        self.task_desc_entry.pack()

        # Add Task Button
        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack()

        # Task List
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.task_listbox.pack()

        # Delete Task Button
        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack()

    def add_task(self):
        task_name = self.task_name_entry.get()
        task_desc = self.task_desc_entry.get()

        if task_name:
            self.tasks.append((task_name, task_desc))
            self.update_task_list()

    def delete_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            index = selected_task[0]
            del self.tasks[index]
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task[0])

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
