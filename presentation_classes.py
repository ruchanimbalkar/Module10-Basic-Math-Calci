#------------------------------------------------------------------------------------------------#
# Title: Basic Arithmetic Demo (Presentation Classes Script)
# Description: Multi-line Textbox that displays results of arithmetic operations on two operands
# ChangeLog (Who, When, What)
# Rucha Nimbalkar, 12/18/2024, Created Script
# Rucha Nimbalkar, 12/18/2024, Created MainWindow class
# Rucha Nimbalkar, 12/18/2024, Added code in the MainWindow class
# Rucha Nimbalkar, 12/18/2024, Created MathIO class
# Rucha Nimbalkar, 12/18/2024, Added methods in the MathIO class
#------------------------------------------------------------------------------------------------#
import tkinter as tk
from tkinter import ttk
import processing_classes as proc

class MainWindow(object):
    """
        Description: Creates the following UI objects:
        window__root(tk.Tk)
        lbl_math_info(ttk.label)
        txt_first_number (ttk.entry)
        txt_second_number (ttk.entry)
        mtx_results(ttk.textbox)
        btn_add(ttk.button)
        btn_subtract(ttk.button)
        btn_multiply(ttk.button)
        btn_divide(ttk.button)
    """

    @staticmethod
    def create_main_window():
        """Create and configure a root node object"""
        application_window = tk.Tk()
        application_window.geometry("500x250")
        application_window.title("Simple Math")

        lbl_math_results = ttk.Label(application_window, text = "Math Results")
        lbl_math_results.grid(row=1, column=1, sticky = tk.NW, padx= 10, pady=5)

        lbl_first_number = ttk.Label(
            application_window,
            text="First Number",
            width= 20,
            anchor= tk.E
        )
        lbl_first_number.grid(row=2,column=1, sticky = tk.E)
        txt_first_number = ttk.Entry(application_window, width=40)
        txt_first_number.grid(row=2, column=2, columnspan=3)
        txt_first_number.insert(0,"0.00")

        lbl_math_results = ttk.Label(application_window, text="Math Results")
        lbl_math_results.grid(row=1, column=1, sticky=tk.NW, padx=10, pady=5)

        lbl_second_number = ttk.Label(
            application_window,
            text="Second Number",
            width=20,
            anchor=tk.E
        )
        lbl_second_number.grid(row=3, column=1, sticky=tk.E)
        txt_second_number = ttk.Entry(application_window, width=40)
        txt_second_number.grid(row=3, column=2, columnspan=3)
        txt_second_number.insert(0, "0.00")

        #Adding a multiline textbox
        mtx_results = tk.Text(width=50, height=5)
        mtx_results.grid(row=4,
                         column=1,
                         sticky=tk.N,
                         columnspan=4,
                         padx=10,
                         pady=10
                         )

        #Adding buttons
        #addition button
        btn_add = ttk.Button(application_window, text ="+",width=3)
        btn_add.grid(row=5, column=1,sticky=tk.E, padx=15, pady=5)
        btn_add['command'] = lambda : MathIO.write_sum_to_textbox(
            float(txt_first_number.get()),
            float(txt_second_number.get()),
            mtx_results
        )

        #subtract button
        btn_subtract = ttk.Button(application_window, text="-", width=3)
        btn_subtract.grid(row=5, column=2, sticky=tk.E, padx=15, pady=5)
        btn_subtract['command'] = lambda: MathIO.write_difference_to_textbox(
            float(txt_first_number.get()),
            float(txt_second_number.get()),
            mtx_results
        )

        #multiplication button
        btn_multiply = ttk.Button(application_window, text="*", width=3)
        btn_multiply.grid(row=5, column=3, sticky=tk.E, padx=15, pady=5)
        btn_multiply['command'] = lambda: MathIO.write_product_to_textbox(
            float(txt_first_number.get()),
            float(txt_second_number.get()),
            mtx_results
        )

        #division button
        btn_divide = ttk.Button(application_window, text="/", width=3)
        btn_divide.grid(row=5, column=4, sticky=tk.E, padx=15, pady=5)
        btn_divide['command'] = lambda: MathIO.write_quotient_to_textbox(
            float(txt_first_number.get()),
            float(txt_second_number.get()),
            mtx_results
        )

        #clear button
        btn_clear = ttk.Button(application_window, text="CLEAR", width=6)
        btn_clear.grid(row=5, column=5, sticky=tk.E, padx=15, pady=5)
        btn_clear['command'] = lambda: MathIO.clear_textbox(mtx_results)
        return application_window
#End class

class MathIO(object):

    @staticmethod
    def clear_textbox(textbox):
        textbox['state'] = 'normal'
        textbox.delete(1.0,tk.END)
        textbox['state'] = 'disabled'

    @staticmethod
    def write_sum_to_textbox(n1,n2,textbox):
        textbox['state']= 'normal'
        text = str.format('The sum of {n1} and {n2} is {result}\n', n1=n1, n2=n2, result = proc.MathProcessor.add(n1,n2))
        textbox.insert(tk.END,text)
        textbox['state'] = 'disabled'

    @staticmethod
    def write_difference_to_textbox(n1,n2,textbox):
        textbox['state']= 'normal'
        text = str.format('The difference of {n1} and {n2} is {result}\n', n1=n1, n2=n2, result = proc.MathProcessor.subtract(n1,n2))
        textbox.insert(tk.END,text)
        textbox['state'] = 'disabled'

    @staticmethod
    def write_product_to_textbox(n1,n2,textbox):
        textbox['state']= 'normal'
        text = str.format('The product of {n1} and {n2} is {result}\n', n1=n1, n2=n2, result = proc.MathProcessor.multiply(n1,n2))
        textbox.insert(tk.END,text)
        textbox['state'] = 'disabled'

    @staticmethod
    def write_quotient_to_textbox(n1,n2,textbox):
        textbox['state']= 'normal'
        text = str.format('The quotient of {n1} and {n2} is {result}\n', n1=n1, n2=n2, result = proc.MathProcessor.divide(n1,n2))
        textbox.insert(tk.END,text)
        textbox['state'] = 'disabled'

#End class