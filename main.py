"""
This is a simple calculator made in python, which uses tkinter GUI.
"""
from tkinter import *

class App:
    def __init__(self, toplevel):
        self.frame1 = Frame(toplevel, border=10)
        self.entry1 = Entry(self.frame1, width=19, justify='right', font='Arial, 16')
        self.cursor = 0
        self.bt_ac = Button(self.frame1, text='AC', width=5, height=2, command=self.ac)
        self.bt_parentheses = Button(self.frame1, text='()', width=5, height=2, command=self.parentheses)
        self.bt_percent = Button(self.frame1, text='%', width=5, height=2, command=self.percent)
        self.bt_division = Button(self.frame1, text='/', width=5, height=2, command=self.division)
        self.bt_times = Button(self.frame1, text='x', width=5, height=2, command=self.times)
        self.bt_minus = Button(self.frame1, text='-', width=5, height=2, command=self.minus)
        self.bt_plus = Button(self.frame1, text='+', width=5, height=2, command=self.plus)
        self.bt_equals = Button(self.frame1, text='=', width=5, height=2, command=self.equals)
        self.bt_dot = Button(self.frame1, text='.', width=5, height=2, command=self.dot)
        self.bt_backspace = Button(self.frame1, text='<x', width=5, height=2, command=self.backspace)
        self.bt_zero = Button(self.frame1, text='0', width=5, height=2, command=self.zero)
        self.bt_one = Button(self.frame1, text='1', width=5, height=2, command=self.one)
        self.bt_two = Button(self.frame1, text='2', width=5, height=2, command=self.two)
        self.bt_three = Button(self.frame1, text='3', width=5, height=2, command=self.three)
        self.bt_four = Button(self.frame1, text='4', width=5, height=2, command=self.four)
        self.bt_five = Button(self.frame1, text='5', width=5, height=2, command=self.five)
        self.bt_six = Button(self.frame1, text='6', width=5, height=2, command=self.six)
        self.bt_seven = Button(self.frame1, text='7', width=5, height=2, command=self.seven)
        self.bt_eight = Button(self.frame1, text='8', width=5, height=2, command=self.eight)
        self.bt_nine = Button(self.frame1, text='9', width=5, height=2, command=self.nine)

        self.frame1.grid()
        self.entry1.grid(row=0, columnspan=4)
        self.bt_ac.grid(row=1, column=0)
        self.bt_parentheses.grid(row=1, column=1)
        self.bt_percent.grid(row=1, column=2)
        self.bt_division.grid(row=1, column=3)
        self.bt_times.grid(row=2, column=3)
        self.bt_minus.grid(row=3, column=3)
        self.bt_plus.grid(row=4, column=3)
        self.bt_equals.grid(row=5, column=3)
        self.bt_dot.grid(row=5, column=1)
        self.bt_backspace.grid(row=5, column=2)
        self.bt_zero.grid(row=5, column=0)
        self.bt_one.grid(row=4, column=0)
        self.bt_two.grid(row=4, column=1)
        self.bt_three.grid(row=4, column=2)
        self.bt_four.grid(row=3, column=0)
        self.bt_five.grid(row=3, column=1)
        self.bt_six.grid(row=3, column=2)
        self.bt_seven.grid(row=2, column=0)
        self.bt_eight.grid(row=2, column=1)
        self.bt_nine.grid(row=2, column=2)

    def get_cursor_position(self):
        self.cursor = self.entry1.index(INSERT)

    def backspace(self):
        self.get_cursor_position()
        self.entry1.delete(self.cursor - 1, self.cursor)

    def insert_text(self, text):
        self.get_cursor_position()
        self.entry1.insert(self.cursor, text)

    def ac(self):
        self.entry1.delete(0, 'end')

    def parentheses(self):
        opening = 0
        closure = 0
        self.get_cursor_position()
        for letter in self.entry1.get():
            if letter == '(':
                opening += 1
            if letter == ')':
                closure += 1
        if opening == closure:
            self.entry1.insert(self.cursor, '(')
        else:
            self.entry1.insert(self.cursor, ')')

    def percent(self):
        self.get_cursor_position()
        size = len(self.entry1.get())
        if size > 0 and self.entry1.get()[self.cursor - 1] in '+-x/.(%':
            self.backspace()
            self.insert_text('%')
        if size > 0 and self.entry1.get()[self.cursor - 1] != '%':
            self.insert_text('%')

    def division(self):
        self.get_cursor_position()
        size = len(self.entry1.get())
        if size > 0 and self.entry1.get()[self.cursor - 1] in '+-x/.':
            self.backspace()
            self.insert_text('/')
        if size > 0 and self.entry1.get()[self.cursor - 1] != '/':
            self.insert_text('/')

    def times(self):
        self.get_cursor_position()
        size = len(self.entry1.get())
        if size > 0 and self.entry1.get()[self.cursor - 1] in '+-x/.':
            self.backspace()
            self.insert_text('*')
        if size > 0 and self.entry1.get()[self.cursor - 1] != 'x':
            self.insert_text('*')

    def minus(self):
        self.get_cursor_position()
        size = len(self.entry1.get())
        if size == 0:
            self.insert_text('-')
        else:
            if self.entry1.get()[self.cursor - 1] in '+-x/.':
                self.backspace()
                self.insert_text('-')
            if size > 0 and self.entry1.get()[self.cursor - 1] != '-':
                self.insert_text('-')

    def plus(self):
        self.get_cursor_position()
        size = len(self.entry1.get())
        if self.entry1.get()[self.cursor - 1] in '+-x/.':
            self.backspace()
            self.insert_text('+')
        if size > 0 and self.entry1.get()[self.cursor - 1] != '+':
            self.insert_text('+')

    def dot(self):
        self.get_cursor_position()
        size = len(self.entry1.get())
        if size > 0:
            if self.entry1.get()[self.cursor - 1] in '+-x/.':
                self.backspace()
                self.insert_text('.')
        if size > 0 and self.entry1.get()[self.cursor - 1] != '.':
            self.insert_text('.')

    def zero(self):
        self.get_cursor_position()
        self.insert_text('0')

    def one(self):
        self.get_cursor_position()
        self.insert_text('1')

    def two(self):
        self.get_cursor_position()
        self.insert_text('2')

    def three(self):
        self.get_cursor_position()
        self.insert_text('3')

    def four(self):
        self.get_cursor_position()
        self.insert_text('4')

    def five(self):
        self.get_cursor_position()
        self.insert_text('5')

    def six(self):
        self.get_cursor_position()
        self.insert_text('6')

    def seven(self):
        self.get_cursor_position()
        self.insert_text('7')

    def eight(self):
        self.get_cursor_position()
        self.insert_text('8')

    def nine(self):
        self.get_cursor_position()
        self.insert_text('9')

    def fix_percent(self):
        print(self.entry1.get())
        x = ''
        self.cursor = len(self.entry1.get()) - 1
        while True:
            if self.entry1.get()[self.cursor] == '%':
                self.entry1.delete(self.cursor)
                self.entry1.insert(self.cursor, '*')
                self.cursor -= 2
                while True:
                    try:
                        if self.entry1.get()[self.cursor] in '+-*/.%()':
                            break
                        else:
                            x += self.entry1.get()[self.cursor]
                            self.entry1.delete(self.cursor)
                    except IndexError:
                        break
                print(x)
                y = str(int(x) / 100)
                self.entry1.insert(self.cursor, y)
                print(self.entry1.get())
            else:
                if self.cursor > 0:
                    self.cursor -= 1
                else:
                    break

    def equals(self):
        if len(self.entry1.get()) > 0:
            try:
                if '%' in self.entry1.get():
                    self.fix_percent()
                x = eval(self.entry1.get().replace('x', '*'))
                self.ac()
                self.insert_text(x)
            except (SyntaxError, TypeError):
                self.ac()
                self.insert_text('Expressão Inválida')

root = Tk()
root.title('Calculadora')
root.configure()
App(root)
root.mainloop()
