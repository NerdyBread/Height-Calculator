import tkinter as tk


class Window:
    def __init__(self, height, length, title, other_text, submit):
        self.height = height
        self.length = length
        self.other_text = other_text
        self.submit = submit
        self.root = tk.Tk()
        self.root.geometry(f"{height}x{length}")
        self.root.title = title

    def create_widgets(self):
        title_widget = tk.Label(self.root, text="Height Calulator")
        other_text = tk.Label(self.root, text=self.other_text)
        if self.submit:
            self.unit_options = ["cm", "in"]
            self.menu = tk.StringVar(self.root)
            self.menu.set("Choose units")
            self.unit_selector = tk.OptionMenu(
                self.root, self.menu, *self.unit_options)

            self.text_box = tk.Entry(self.root, width=10)
            self.calc_button = tk.Button(self.root, text="Calculate",
                                         command=self.callback)

            self.text_box.place(x=120, y=120)
            self.unit_selector.place(x=184, y=114)
            self.calc_button.place(x=20, y=180)

        title_widget.place(x=20, y=20)
        other_text.place(x=20, y=120)

    def callback(self):
        try:
            height = int(self.text_box.get())
        except ValueError:
            pass
        else:
            unit = self.menu.get()
            if unit in self.unit_options:
                height_str = f"{self.text_box.get()}{self.menu.get()}"
                self.result_win = Window(300, 200, "Results",
                                         f"You are {height_str} tall", False)
                self.result_win.create_widgets()
                self.result_win.run()

    def run(self):
        self.root.mainloop()
