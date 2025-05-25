import tkinter as tk
from main.python.be.vub.calculator.operations.OperationHandler import OperationHandler



class CalculatorApp(tk.Tk):


    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator")
        self.geometry("400x600")
        self.resizable(False, False)

        self.handler = OperationHandler()

        self._operation = None
        self._operand1 = None

        # Build GUI
        self._create_widgets()

    def _create_widgets(self):
        # Input entry (display for showing numbers)
        self.display = tk.Entry(self, justify='right', font=('Arial', 20))
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        # list of Unary operations (sin, cos,...)
        # Add Clear button
        unary_symbols = list(self.handler.unary_ops.keys()) + ['C']  

        #create buttons with text=text on the button, command=function on the button, 
        for idx, symbol in enumerate(unary_symbols):
            btn = tk.Button(self, text=symbol, font=('Arial', 14), command=lambda s=symbol: self._apply_unary_operation(s))
            #give you row and column for a specific symbol
            r, c = divmod(idx, 4)
            #a button is placed on a 4-column grid
            btn.grid(row=1 + r, column=c, padx=5, pady=5, sticky='nsew')

        # Numbers & Binary Operators
        items = [
            ('7', self._insert_char_to_display), ('8', self._insert_char_to_display), ('9', self._insert_char_to_display), ('/', self._prepare_binary_operator_input),
            ('4', self._insert_char_to_display), ('5', self._insert_char_to_display), ('6', self._insert_char_to_display), ('*', self._prepare_binary_operator_input),
            ('1', self._insert_char_to_display), ('2', self._insert_char_to_display), ('3', self._insert_char_to_display), ('-', self._prepare_binary_operator_input),
            ('0', self._insert_char_to_display), ('.', self._insert_char_to_display), ('=', self._apply_binary_operation), ('+', self._prepare_binary_operator_input),
            ('^', self._prepare_binary_operator_input)
        ]
        #create buttons for items symbols
        #put a button in a specific palce on the grid
        for idx, (text, handler) in enumerate(items):
            r = idx // 4 + 3
            c = idx % 4
            #command=lambda t=text, h=handler: h(t)  = this part is a lambda with 2 input parameter, and return value will be h(t)
            btn = tk.Button(self, text=text, font=('Arial', 18), command=lambda t=text, h=handler: h(t))
            btn.grid(row=r, column=c, padx=5, pady=5, sticky='nsew')

        # Grid weight
        total_rows = 3 + (len(items) - 1) // 4 + 1
        #map() returns a lazy iterable, so we are wrapping it in list(...)
        # it is like = for i in range(rows): self.grid_rowconfigure(i, weight=1) 
        list(map(lambda i: self.grid_rowconfigure(i, weight=1), range(total_rows)))
        list(map(lambda j: self.grid_columnconfigure(j, weight=1), range(4)))

    #disply selected number
    def _insert_char_to_display(self, char):
        self.display.insert(tk.END, char)

    #just fill two attributes=operand1,operation
    def _prepare_binary_operator_input(self, symbol):
        try:
            self._operand1 = float(self.display.get())
            self.display.delete(0, tk.END)
            self._operation = symbol
        except ValueError:
            self.display.delete(0, tk.END)

    # Apply the selected unary operation to the input number
    def _apply_unary_operation(self, symbol):
        if symbol == 'C':
            self.display.delete(0, tk.END)
            return
        try:
            val = float(self.display.get())
            result = self.handler.evaluate_unary(symbol, val)
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(0, 'Error')

    # Apply the selected binary operation to the input number
    def _apply_binary_operation(self, _=None):
        if not self._operation or self._operand1 is None:
            return
        try:
            b = float(self.display.get())
            answer = self.handler.evaluate_binary(self._operation, self._operand1, b)
            self.display.delete(0, tk.END)
            self.display.insert(0, answer)
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(0, 'Error')



