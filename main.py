"""
This is a simple calculator made in python, which uses tkinter GUI.
"""
from tkinter import *

color = {'black': '#000000', 'white': '#ffffff', 'lead1': '#1d1f1f', 'lead2': '#2b2b2b',
         'lead3': '#545454', 'cyan1': '#5db6f0', 'cyan2': '#92cbf0', 'cyan3': '#37d3ff', 'green1': '#8af2a5',
         'green2': '#c6f1d1', 'grey': '#bababa'}

# Numbers configurations
num_bt_width = 6
num_bt_height = 3
num_bt_bg = color['lead2']
num_bt_fg = color['white']
num_bt_activebackground = color['lead3']
num_bt_activeforeground = color['black']
num_bt_relief = FLAT
num_bt_border = 0
num_bt_highlightbackground = color['black']

# Operators Configurations
op_bt_width = 6
op_bt_height = 3
op_bt_bg = color['cyan1']
op_bt_fg = color['black']
op_bt_activebackground = color['cyan2']
op_bt_activeforeground = color['black']
op_bt_relief = FLAT
op_bt_border = 0
op_bt_highlightbackground = color['black']


class App:
    def __init__(self, toplevel):
        self.cursor = 0
        self.frame1 = Frame(toplevel, border=10, bg=color['lead1'])
        self.entry1 = Entry(self.frame1,
                            width=11,
                            justify='right',
                            font='Arial, 33',
                            bg=color['lead1'],
                            fg=color['white'],
                            relief=FLAT,
                            border=0,
                            highlightbackground=color['white'],
                            highlightcolor=color['white'],
                            insertbackground=color['white'])
        self.bt_ac = Button(self.frame1,
                            text='AC',
                            command=self.ac,
                            width=6,
                            height=3,
                            bg=color['green1'],
                            fg=color['black'],
                            activebackground=color['green2'],
                            activeforeground=color['black'],
                            relief=FLAT,
                            border=0,
                            highlightbackground=color['black'])
        self.bt_parentheses = Button(self.frame1,
                                     text='()',
                                     command=self.parentheses,
                                     width=op_bt_width,
                                     height=op_bt_height,
                                     bg=op_bt_bg,
                                     fg=op_bt_fg,
                                     activebackground=op_bt_activebackground,
                                     activeforeground=op_bt_activeforeground,
                                     relief=op_bt_relief,
                                     border=op_bt_border,
                                     highlightbackground=op_bt_highlightbackground)
        self.bt_percent = Button(self.frame1,
                                 text='%',
                                 command=self.percent,
                                 width=op_bt_width,
                                 height=op_bt_height,
                                 bg=op_bt_bg,
                                 fg=op_bt_fg,
                                 activebackground=op_bt_activebackground,
                                 activeforeground=op_bt_activeforeground,
                                 relief=op_bt_relief,
                                 border=op_bt_border,
                                 highlightbackground=op_bt_highlightbackground)
        self.bt_division = Button(self.frame1,
                                  text='/',
                                  command=self.division,
                                  width=op_bt_width,
                                  height=op_bt_height,
                                  bg=op_bt_bg,
                                  fg=op_bt_fg,
                                  activebackground=op_bt_activebackground,
                                  activeforeground=op_bt_activeforeground,
                                  relief=op_bt_relief,
                                  border=op_bt_border,
                                  highlightbackground=op_bt_highlightbackground)
        self.bt_times = Button(self.frame1,
                               text='x',
                               command=self.times,
                               width=op_bt_width,
                               height=op_bt_height,
                               bg=op_bt_bg,
                               fg=op_bt_fg,
                               activebackground=op_bt_activebackground,
                               activeforeground=op_bt_activeforeground,
                               relief=op_bt_relief,
                               border=op_bt_border,
                               highlightbackground=op_bt_highlightbackground)
        self.bt_minus = Button(self.frame1,
                               text='-',
                               command=self.minus,
                               width=op_bt_width,
                               height=op_bt_height,
                               bg=op_bt_bg,
                               fg=op_bt_fg,
                               activebackground=op_bt_activebackground,
                               activeforeground=op_bt_activeforeground,
                               relief=op_bt_relief,
                               border=op_bt_border,
                               highlightbackground=op_bt_highlightbackground)
        self.bt_plus = Button(self.frame1,
                              text='+',
                              command=self.plus,
                              width=op_bt_width,
                              height=op_bt_height,
                              bg=op_bt_bg,
                              fg=op_bt_fg,
                              activebackground=op_bt_activebackground,
                              activeforeground=op_bt_activeforeground,
                              relief=op_bt_relief,
                              border=op_bt_border,
                              highlightbackground=op_bt_highlightbackground)
        self.bt_equals = Button(self.frame1,
                                text='=',
                                command=self.equals,
                                width=op_bt_width,
                                height=op_bt_height,
                                bg=color['grey'],
                                fg=color['black'],
                                activebackground=color['white'],
                                activeforeground=color['black'],
                                relief=op_bt_relief,
                                border=op_bt_border,
                                highlightbackground=op_bt_highlightbackground)
        self.bt_dot = Button(self.frame1,
                             text='.',
                             command=self.dot,
                             width=num_bt_width,
                             height=num_bt_height,
                             bg=num_bt_bg,
                             fg=num_bt_fg,
                             activebackground=num_bt_activebackground,
                             activeforeground=num_bt_activeforeground,
                             relief=num_bt_relief,
                             border=num_bt_border,
                             highlightbackground=op_bt_highlightbackground)
        self.bt_backspace = Button(self.frame1,
                                   text='<x',
                                   command=self.backspace,
                                   width=num_bt_width,
                                   height=num_bt_height,
                                   bg=num_bt_bg,
                                   fg=num_bt_fg,
                                   activebackground=num_bt_activebackground,
                                   activeforeground=num_bt_activeforeground,
                                   relief=num_bt_relief,
                                   border=num_bt_border,
                                   highlightbackground=op_bt_highlightbackground)
        self.bt_zero = Button(self.frame1,
                              text='0',
                              command=self.zero,
                              width=num_bt_width,
                              height=num_bt_height,
                              bg=num_bt_bg,
                              fg=num_bt_fg,
                              activebackground=num_bt_activebackground,
                              activeforeground=num_bt_activeforeground,
                              relief=num_bt_relief,
                              border=num_bt_border,
                              highlightbackground=op_bt_highlightbackground)
        self.bt_one = Button(self.frame1, text='1',
                             width=num_bt_width,
                             command=self.one,
                             height=num_bt_height,
                             bg=num_bt_bg,
                             fg=num_bt_fg,
                             activebackground=num_bt_activebackground,
                             activeforeground=num_bt_activeforeground,
                             relief=num_bt_relief,
                             border=num_bt_border,
                             highlightbackground=op_bt_highlightbackground)
        self.bt_two = Button(self.frame1,
                             text='2',
                             command=self.two,
                             width=num_bt_width,
                             height=num_bt_height,
                             bg=num_bt_bg,
                             fg=num_bt_fg,
                             activebackground=num_bt_activebackground,
                             activeforeground=num_bt_activeforeground,
                             relief=num_bt_relief,
                             border=num_bt_border,
                             highlightbackground=op_bt_highlightbackground)
        self.bt_three = Button(self.frame1,
                               text='3',
                               command=self.three,
                               width=num_bt_width,
                               height=num_bt_height,
                               bg=num_bt_bg,
                               fg=num_bt_fg,
                               activebackground=num_bt_activebackground,
                               activeforeground=num_bt_activeforeground,
                               relief=num_bt_relief,
                               border=num_bt_border,
                               highlightbackground=op_bt_highlightbackground)
        self.bt_four = Button(self.frame1,
                              text='4',
                              command=self.four,
                              width=num_bt_width,
                              height=num_bt_height,
                              bg=num_bt_bg,
                              fg=num_bt_fg,
                              activebackground=num_bt_activebackground,
                              activeforeground=num_bt_activeforeground,
                              relief=num_bt_relief,
                              border=num_bt_border,
                              highlightbackground=op_bt_highlightbackground)
        self.bt_five = Button(self.frame1,
                              text='5',
                              command=self.five,
                              width=num_bt_width,
                              height=num_bt_height,
                              bg=num_bt_bg,
                              fg=num_bt_fg,
                              activebackground=num_bt_activebackground,
                              activeforeground=num_bt_activeforeground,
                              relief=num_bt_relief,
                              border=num_bt_border,
                              highlightbackground=op_bt_highlightbackground)
        self.bt_six = Button(self.frame1,
                             text='6',
                             command=self.six,
                             width=num_bt_width,
                             height=num_bt_height,
                             bg=num_bt_bg,
                             fg=num_bt_fg,
                             activebackground=num_bt_activebackground,
                             activeforeground=num_bt_activeforeground,
                             relief=num_bt_relief,
                             border=num_bt_border,
                             highlightbackground=op_bt_highlightbackground)
        self.bt_seven = Button(self.frame1,
                               text='7',
                               command=self.seven,
                               width=num_bt_width,
                               height=num_bt_height,
                               bg=num_bt_bg,
                               fg=num_bt_fg,
                               activebackground=num_bt_activebackground,
                               activeforeground=num_bt_activeforeground,
                               relief=num_bt_relief,
                               border=num_bt_border,
                               highlightbackground=op_bt_highlightbackground)
        self.bt_eight = Button(self.frame1,
                               text='8',
                               command=self.eight,
                               width=num_bt_width,
                               height=num_bt_height,
                               bg=num_bt_bg,
                               fg=num_bt_fg,
                               activebackground=num_bt_activebackground,
                               activeforeground=num_bt_activeforeground,
                               relief=num_bt_relief,
                               border=num_bt_border,
                               highlightbackground=op_bt_highlightbackground)
        self.bt_nine = Button(self.frame1,
                              text='9',
                              command=self.nine,
                              width=num_bt_width,
                              height=num_bt_height,
                              bg=num_bt_bg,
                              fg=num_bt_fg,
                              activebackground=num_bt_activebackground,
                              activeforeground=num_bt_activeforeground,
                              relief=num_bt_relief,
                              border=num_bt_border,
                              highlightbackground=op_bt_highlightbackground)

        self.frame1.grid()
        self.entry1.grid(row=0, columnspan=4, pady=10)
        self.bt_ac.grid(row=1, column=0, pady=3, padx=3)
        self.bt_parentheses.grid(row=1, column=1, pady=3, padx=3)
        self.bt_percent.grid(row=1, column=2, pady=3, padx=3)
        self.bt_division.grid(row=1, column=3, pady=3, padx=3)
        self.bt_times.grid(row=2, column=3, pady=3, padx=3)
        self.bt_minus.grid(row=3, column=3, pady=3, padx=3)
        self.bt_plus.grid(row=4, column=3, pady=3, padx=3)
        self.bt_equals.grid(row=5, column=3, pady=3, padx=3)
        self.bt_dot.grid(row=5, column=1, pady=3, padx=3)
        self.bt_backspace.grid(row=5, column=2, pady=3, padx=3)
        self.bt_zero.grid(row=5, column=0, pady=3, padx=3)
        self.bt_one.grid(row=4, column=0, pady=3, padx=3)
        self.bt_two.grid(row=4, column=1, pady=3, padx=3)
        self.bt_three.grid(row=4, column=2, pady=3, padx=3)
        self.bt_four.grid(row=3, column=0, pady=3, padx=3)
        self.bt_five.grid(row=3, column=1, pady=3, padx=3)
        self.bt_six.grid(row=3, column=2, pady=3, padx=3)
        self.bt_seven.grid(row=2, column=0, pady=3, padx=3)
        self.bt_eight.grid(row=2, column=1, pady=3, padx=3)
        self.bt_nine.grid(row=2, column=2, pady=3, padx=3)

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
            self.insert_text('x')

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
                y = str(int(x) / 100)
                self.entry1.insert(self.cursor, y)
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
            except (SyntaxError, TypeError, NameError):
                self.ac()
                self.insert_text('Expressão Inválida')


root = Tk()
root.title('Calculadora')
root.configure()
App(root)
root.mainloop()
