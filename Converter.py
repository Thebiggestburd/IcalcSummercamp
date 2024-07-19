from tkinter import *
from tkinter import ttk

class CurrencyConverter:
    def __init__(self):
        self.currencies = dict()
        with open('Currency.py') as file:
            for line in file:
                line = line.rstrip('\n')
                currency, rate = line.split(':')
                self.currencies[currency] = float(rate)

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != "USD":
            amount = amount/self.currencies[to_currency]
        amount = round(amount * self.currencies[to_currency],2)
        return amount
my_converter = CurrencyConverter()
print(my_converter.convert("USD","CAD",50))
print(my_converter.convert("CAD","USD",50))


class App(Tk):
    def __init__(self, converter):
        Tk.__init__(self)
        self.my_converter = converter
        self.config(bg='orange')
        self.geometry("800x400")
        #Title
        self.title = Label(self,text="Currency Converter")
        self.title.config(font=('Arial',20,'bold'))
        self.title.place(x=300,y=5)
        # Entry Box
        self.entry_box = Entry(self,bd=3,justify=CENTER)
        self.entry_box.place(x=350,y=80)
        # DropDown list
        self.from_currency_list = Stringvar(self)
        self.to_currency_list.set('CAD')
        self.from_currency_list = Stringvar(self)
        self.to_currency_list.set('USD')
        font = ("Arial",12)
        self.option_add('*TCombobox*Listbox.font',font)
        self.from_currency_dropdown = ttk.Combobox(self,textvariable=self.from_currency_list,value=list(self.my_currency.currencies.keys()))
        self.to_currency_dropdown = ttk.Combobox(
            self,
            textvariable=self.to_currency_list,
            value=list(self.my_converter.currencies.keys()),
            )
        self.from_currency_dropdown.play(x=250,y=50)
        self.to_currency_dropdown.place(x=400,y=50)
            #result message
        self.result = Label(self,text='')
        self.result.config(font=("Arial",12,'bold'))
        self.result.place(x=380,y=120)

            #convert button
        self.convert_button = button(self,text="Convert",bg='green',command=self)
        self.convert_button.config(font=("Arial",10))
        self.convert_button.place(x=380,y=120)

        def do_convert(self):
            amount = self.entry_box.get()
            from_currency = self.from_currency_dropdown.get()
            to_currency = self.to_currency_dropdown.get()
            result = self.my_converter.convert(from_currency,to_currency,amount)
            self.result.config(text=str(converted_amount))


# Launch the App
my_converter = CurrencyConverter()
App(my_converter)
mainloop()
