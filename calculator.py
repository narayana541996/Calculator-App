from tkinter import *
#from time import sleep
import re

expression = ''


color2 = 'purple'
color1 = 'yellow'
color3 = 'green'
color4 = 'lightblue'
window = Tk()
#window.geometry('312x324')
window.title('Calcy')
window.resizable(0,0)

def btnclick(n):
    global expression
    expression = expression + str(n)
    screen.insert(INSERT,n)

def clear_button():
    global expression
    cleared_expression = expression[:-1]
    expression = cleared_expression
    screen.delete('1.0',END)
    screen.insert(INSERT,cleared_expression)

def clear_all_button():
    global expression
    expression = ''
    screen.delete('1.0',END)

def equal_button():
    global expression
    iop = screen.get('1.0',END)
    op = iop
    op = re.split('[+ - * / . ( ) ]',op)
    op = ''.join(op)
    op = op.strip()
    #print('op',op)
    #print('iop',iop)
    if op.isnumeric() == True:
        ans = eval(iop.strip())
        screen.delete('1.0',END)
        screen.insert(INSERT,ans)
    else:
        screen.delete('1.0',END)
        screen.insert(INSERT,'\nInvalid input\nclear the screen and try again')
        

ans_frame = Frame(window)
ans_frame.pack(fill = X)
btn_frame = Frame(window)
btn_frame.pack(side = BOTTOM)

screen = Text(ans_frame, font = 10, bg = color1, fg = color2, insertbackground = color2, width = 0, height = 5, padx = 10, pady = 10, relief = RIDGE)
screen.pack(fill = BOTH)
clear = Button(btn_frame, text = 'Clear', bg = color1, fg = color2,width = 10, height = 5, activebackground = color2, activeforeground = color1, command = lambda:clear_button()).grid(row = 1, column =3)
one = Button(btn_frame, text = '1', bg = color2, fg = color1,width = 10, height = 5, activebackground = color1, activeforeground = color2, command = lambda:btnclick(1)).grid(row = 2,column = 0)
two = Button(btn_frame, text = '2', bg = color2, fg = color1,width = 10, height = 5, activebackground = color1, activeforeground = color2, command = lambda:btnclick(2)).grid(row = 2, column = 1)
three = Button(btn_frame, text = '3', bg = color2, fg = color1,width = 10, height = 5, activebackground = color1, activeforeground = color2, command = lambda:btnclick(3)).grid(row = 2, column = 2)
four = Button(btn_frame, text = '4', bg = color2, fg = color1,width = 10, height = 5, activebackground = color1, activeforeground = color2, command = lambda:btnclick(4)).grid(row = 3,column = 0)
five = Button(btn_frame, text = '5', bg = color2, fg = color1,width = 10, height = 5, activebackground = color1, activeforeground = color2, command = lambda:btnclick(5)).grid(row = 3, column = 1)
six = Button(btn_frame, text = '6', bg = color2, fg = color1,width = 10, height = 5, activebackground = color1, activeforeground = color2, command = lambda:btnclick(6)).grid(row = 3, column = 2)
seven = Button(btn_frame, text = '7', bg = color2, fg = color1,width = 10, height = 5, activebackground = color1, activeforeground = color2, command = lambda:btnclick(7)).grid(row = 4, column = 0)
eight = Button(btn_frame, text = '8', bg = color2, fg = color1,width = 10, height = 5, activebackground = color1, activeforeground = color2, command = lambda:btnclick(8)).grid(row = 4, column = 1)
nine = Button(btn_frame, text = '9', bg = color2, fg = color1,width = 10, height = 5, activebackground = color1, activeforeground = color2, command = lambda:btnclick(9)).grid(row = 4, column = 2)
zero = Button(btn_frame, text = '0', bg = color2, fg = color1,width = 10, height = 5, activebackground = color1, activeforeground = color2, command = lambda:btnclick(0)).grid(row = 1, column = 1)
equal = Button(btn_frame, text = '=', bg = color1, fg = color2,width = 10, height = 5, activebackground = color2, activeforeground = color1, command = lambda:equal_button()).grid(row = 4, column = 3)
plus = Button(btn_frame, text = '+', bg = color1, fg = color2,width = 10, height = 5, activebackground = color2, activeforeground = color1, command = lambda:btnclick('+')).grid(row = 2, column = 3, sticky = W)
minus = Button(btn_frame, text = '-', bg = color1, fg = color2,width = 10, height = 5, activebackground = color2, activeforeground = color1, command = lambda:btnclick('-')).grid(row = 3, column = 3, sticky = W)
open_bracket = Button(btn_frame, text = '(', bg = color1, fg = color2,width = 10, height = 5, activebackground = color2, activeforeground = color1, command = lambda:btnclick('(')).grid(row = 1, column = 0)
closing_bracket = Button(btn_frame, text = ')', bg = color1, fg = color2,width = 10, height = 5, activebackground = color2, activeforeground = color1, command = lambda:btnclick(')')).grid(row = 1, column = 2)
multiply = Button(btn_frame, text = '*', bg = color1, fg = color2,width = 10, height = 5, activebackground = color2, activeforeground = color1, command = lambda:btnclick('*')).grid(row = 5, column = 0, sticky = N)
divide = Button(btn_frame, text = '/', bg = color1, fg = color2,width = 10, height = 5, activebackground = color2, activeforeground = color1, command = lambda:btnclick('/')).grid(row = 5, column = 1, sticky = N)
dot = Button(btn_frame, text = '.', bg = color1, fg = color2,width = 10, height = 5, activebackground = color2, activeforeground = color1, command = lambda:btnclick('.')).grid(row = 4, column = 0, sticky = NW)
clear_all = Button(btn_frame, text = 'Clear All', bg = color1, fg = color2, width = 10, height = 2, activebackground = color2, activeforeground = color1, command = lambda:clear_all_button()).grid(row = 5, column = 2, columnspan = 2, sticky = NSEW)
