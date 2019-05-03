from tkinter import *
from tkinter import messagebox

# background and font
bg = '#4B4B4C'
f = 'Arial Bold'
x = 5
y = 10


class FormApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Percentage Calculator')
        self.geometry('700x300+400+300')
        container = Frame(self)
        self.frames = {
            'form': MainScreen(self),
        }

        self.show_form_frame()
        container.config(bg=bg)
        container.pack(fill=BOTH, expand=True)

    def show_frame(self, name):
        frame = self.frames[name]
        frame.config(relief="groove", bg=bg)
        frame.place(width=700, height=300, relx=0.5, rely=0.5, anchor=CENTER)
        frame.tkraise()

    def show_form_frame(self):
        self.show_frame('form')

    def create_text(self, *args, **kw):
        """Create text with coordinates x1,y1."""
        return self._create('text', args, kw)


class MainScreen(Frame):
    def __init__(self, form):
        Frame.__init__(self, form)

        # title
        frame = Frame(self, bg=bg)
        Label(frame, text='Fill and Go!', font=(f, 20), pady=20, bg=bg, fg='#fc195d')\
            .grid(row=0, column=0, columnspan=2)

        self.v1 = IntVar()
        self.v2 = IntVar()
        self.v3 = IntVar()
        self.v4 = StringVar()

        # Labels
        Label(frame, text='Sum of Money', font=(f, 12), bd=10, bg=bg, fg='white').grid(row=1, column=0)
        e1 = Entry(frame, textvariable=self.v1).grid(row=1, column=1, pady=5)

        Label(frame, text='Percentage', font=(f, 12), bd=10, bg=bg, fg='white').grid(row=2, column=0)
        Entry(frame, textvariable=self.v2).grid(row=2, column=1, pady=5)

        Label(frame, text='Days/Months', font=(f, 12), bd=10, bg=bg, fg='white',).grid(row=3, column=0)
        Entry(frame, textvariable=self.v3).grid(row=3, column=1, pady=5)

        self.text_box = Text(frame, width=30, height=15)
        self.text_box.grid(row=0, column=2, rowspan=8, padx=30)

        # button Go
        self.go_btn = Button(frame, text='Go!', font=(f, 12), bg="#d11950", fg='white',\
                             highlightthickness=0, relief=FLAT, command=self.calc)
        self.go_btn.grid(row=5, column=0, columnspan=2, pady=10)

        self.lab = Label(frame, text='sum = ', font=(f, 20), bg=bg, bd=10, fg='#fc195d')

        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    # *****************************************************************
    # YOU CAN PUT IN THIS DO METHOD WHAT YOU WANT TO DO WITH VARIABLES!!
    # *****************************************************************
    def calc(self):
        run = True
        sums = self.v1.get()
        percentage = self.v2.get()
        time = self.v3.get()
        self.text_box.delete(1.0, "end-1c")

        i = 0
        if time == 0 or percentage == 0 or sums == 0:
            messagebox.showinfo("OOOPS", "  You probably forgot \nto put some number in.")
        else:
            while run == True:
                # calculation
                sums = sums + (sums * percentage / 100)
                i = i + 1
                # terminal output
                print('{}.total {:.2f}'.format(i, sums))
                # GUI output
                self.text_box.insert("end-1c", ('{}.total {:.2f}\n'.format(i, sums)))
                if i == time:
                    run = False


if __name__ == "__main__":
    app = FormApp()
    app.mainloop()
