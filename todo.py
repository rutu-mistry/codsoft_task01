from tkinter import *
from tkinter import ttk

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do List')
        self.root.geometry('650x410+300+150')

        self.label = Label(self.root, text='To-Do List App', 
                           font='Arial, 25 bold', width=10, bd=5, bg='orange', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add Task', 
                            font='Arial, 18 bold', width=10, bd=5, bg='orange', fg='black')
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text='Tasks', 
                            font='Arial, 18 bold', width=10, bd=5, bg='orange', fg='black')
        self.label3.place(x=320, y=54)

        self.main_text = Listbox(self.root, height=9, width=23, font="Arial, 20 italic bold")
        self.main_text.place(x=280, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font='Arial, 10 bold')
        self.text.place(x=20, y=120)

        self.load_tasks()

        self.button = Button(self.root, text="Add", font='Arial, 20 bold italic',
                             width=10, bd=5, bg='orange', fg='black', command=self.add)
        self.button.place(x=30, y=180)

        self.button2 = Button(self.root, text="Delete", font='Arial, 20 bold italic',
                              width=10, bd=5, bg='orange', fg='black', command=self.delete)
        self.button2.place(x=30, y=280)

    def add(self):
        content = self.text.get(1.0, END).strip()
        if content:
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content + "\n")
            self.text.delete(1.0, END)

    def delete(self):
        try:
            selected_index = self.main_text.curselection()[0]
            self.main_text.delete(selected_index)
            with open('data.txt', 'r+') as file:
                lines = file.readlines()
                file.seek(0)
                for i, line in enumerate(lines):
                    if i != selected_index:
                        file.write(line)
                file.truncate()
        except IndexError:
            pass

    def load_tasks(self):
        try:
            with open('data.txt', 'r') as file:
                for line in file:
                    self.main_text.insert(END, line.strip())
        except FileNotFoundError:
            open('data.txt', 'w').close()

def main():
    root = Tk()
    app = ToDoList(root)
    root.mainloop()

if __name__ == "__main__":
    main()
