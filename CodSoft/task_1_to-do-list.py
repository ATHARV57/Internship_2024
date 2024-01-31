from tkinter import *
from tkinter import ttk
class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do-List')
        self.root.geometry('1000x750+300+150')
        self.label = Label(self.root, text = 'To-Do-List', font = ("Helvetica", 36), width = 20, bd = 5, bg = 'white', fg = 'black')
        self.label.pack(side = 'top', fill = BOTH)

        self.label2 = Label(self.root, text = 'Type Here', font = ("Helvetica", 20), width = 15, bd = 5, bg = 'white', fg = 'black')
        self.label2.place(x = 130, y = 100)

        self.label3 = Label(self.root, text = 'Tasks', font = ("Helvetica", 20), width = 15, bd = 5, bg = 'white', fg = 'black')
        self.label3.place(x = 600 , y = 100)

        self.main_text = Listbox(self.root, height = 40, bd = 5, width = 50, font = ("Helvetica", 10))
        self.main_text.place(x = 550, y = 150)

        self.text = Text(self.root, bd = 5, height = 2, width = 25, font = ("Helvetica", 10))
        self.text.place(x = 150, y = 150)

        def add(): 
            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content)
                file.seek (0) 
                file.close()
            self.text.delete(1.0, END)
        def delete():
            delete_ = self.main_text.curselection()
            look = self.main_text.get(delete_)
            with open('data.txt', 'r+') as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    item = str(look)
                    if item not in line: 
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)

        with open('data.txt', 'r') as file:
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(END, ready)
            file.close()


        self.button = Button(self.root, text = 'Add', font = ("Helvetica", 20), width = 10, bd = 5, bg = 'silver', fg = 'black', command = add)
        self.button.place(x = 150, y = 250)
        self.button2 = Button(self.root, text = 'Delete', font = ("Helvetica", 20), width = 10, bd = 5, bg = 'silver', fg = 'black', command = delete)
        self.button2.place(x = 150, y = 350)




def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()


if __name__ == "__main__":
    main()