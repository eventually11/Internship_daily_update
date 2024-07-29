import tkinter as tk

class AdvancedCalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Advanced Calculator")

        self.equation = tk.StringVar()
        self.input_field = tk.Entry(master, textvariable=self.equation)
        self.input_field.grid(row=0, column=0, columnspan=4, sticky="nsew")

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            'C', '0', '=', '/'
        ]

        row = 1
        col = 0
        for button in buttons:
            tk.Button(self.master, text=button, command=lambda b=button: self.click(b)).grid(row=row, column=col, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Adjust column and row weights to make buttons expand
        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)
            self.master.grid_rowconfigure(i+1, weight=1)

    def click(self, button):
        current_equation = self.equation.get()
        if button == '=':
            try:
                self.equation.set(str(eval(current_equation)))
            except Exception as e:
                # If there is an error, display "error" in the entry field
                self.equation.set("error")
        elif button == 'C':
            self.equation.set("")
        else:
            # or any other button clicked, append the clicked button's text to the current input
            self.equation.set(current_equation + button)

if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedCalculatorApp(root)
    root.mainloop()