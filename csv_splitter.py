#!/usr/bin/env python
# coding: utf-8

# In[586]:


from tkinter import *
#from math import ceil
import pandas as pd
import os
import csv
#import time


# In[587]:


filepath = ''
pypath = ''
rows = 0
test = 0


# In[588]:


def filepath_enter(entry, output_text, size_button, files_button, row_button):
    global filepath
    global pypath
    filepath = entry.get()
    pypath = filepath.replace('\\','\\')
    filesize = 0
    output_text.config(state = NORMAL)
    output_text.delete(1.0,END)
    output_text.insert(1.0,f'Accessing {filepath}...\n')
    output_text.config(state = DISABLED)
    if os.path.exists(pypath) == True and os.path.isfile(pypath) == True:
        if pypath.endswith('.csv'):
            output_text.config(state = NORMAL)
            output_text.insert(END,f'Accessed {filepath}\n')
            output_text.config(state = DISABLED)
            filepath_entry = 1
            output_text.config(state = NORMAL)
            output_text.insert(END,'You may now split the file basing on number of rows, number of output files to be created or sizes of output files by clicking on \'Split by Size\', \'Split by Rows\' or \'Split by Files\'.\n')
            output_text.config(state = DISABLED)
            size_button.config(state = NORMAL)
            files_button.config(state = NORMAL)
            row_button.config(state = NORMAL)
        
        else:
            output_text.config(state = NORMAL)
            output_text.insert(END,f'The file entered is not a csv file.\n')
            output_text.config(state = DISABLED)
            entry.delete(0,END)
        
    elif os.path.isfile(pypath) == False and os.path.isdir(pypath) == True:
        output_text.config(state = NORMAL)
        output_text.insert(END,f'The filepath entered leads to a folder, please include the file along with the extension in the filepath\n')
        output_text.config(state = DISABLED)
        entry.delete(0,END)
        
    else:
        output_text.config(state = NORMAL)
        output_text.insert(END,f'File not found, please check if the filepath entered is correct and includes the file along with the extension.\n')
        output_text.config(state = DISABLED)
        entry.delete(0,END)
        #sleep(1)
        #output_text.delete(0,END)'''
    


# In[589]:


def rows_enter(entry, output_text, row_win):
    global rows
    global pypath
    global rows
    filenum = 1
    #filename = input('Please enter  the file name: ')
    #rows = int(input('enter number of rows required in each file: '))
    try:
        rows = int(entry.get())
        output_text.config(state = NORMAL)
        output_text.insert(END,'Working on it...\n')
        output_text.config(state = DISABLED)
        chunks = pd.read_csv(pypath, chunksize = rows)
        for chunk in chunks:
            with open(f'{pypath}[{filenum}].csv', mode = 'w') as wrfile:
                    chunk.to_csv(wrfile)
            filenum += 1
    except:
        output_text.config(state = NORMAL)
        output_text.insert(END,'Please enter a valid positive integer.\n')
        output_text.config(state = DISABLED)
    else:
        output_text.config(state = NORMAL)
        output_text.insert(END,'Output created!\nYou may check the output files by accessing the location you entered in filepath\n')
        output_text.config(state = DISABLED)
    #entry.delete(0, END)
        row_win.destroy()
        output_text.config(state = NORMAL)
        output_text.insert(END,'Split by Rows closed.\n')
        output_text.config(state = DISABLED)
    
def rows_split(output_text):
    output_text.config(state = NORMAL)
    output_text.insert(END,'Split by Rows selected\n')
    output_text.config(state = DISABLED)
    row_win = Toplevel()
    row_win.title('CSV splitter - Split by Rows')
    row_frame = Frame(row_win)
    row_frame.pack(padx = 20, pady = 20)
    row_label = Label(row_frame, text = 'Enter number of rows required in each file:')
    row_label.grid(row = 0, column = 0 )
    rows_entry = Entry(row_frame, width = 15)
    rows_entry.grid(row = 1, column = 0)
    rows_entry_button = Button(row_frame, text = 'Enter', command = lambda:rows_enter(rows_entry,output_text,row_win))
    rows_entry_button.grid(row = 2, column = 0)
    row_win.mainloop()

def files_enter(entry, output_text, files_win):
    try:
        global test
        test = 0
        #output_text.config(state = NORMAL)
        #output_text.insert(END,'Files_entry called\n')
        #output_text.config(state = DISABLED)'''
        output_text.config(state = NORMAL)
        output_text.insert(END,'Working on it...\n')
        output_text.config(state = DISABLED)
        while test == 0:
            try:
                #n = int(input('Please enter the maximum number of files, the csv file is to be split into: '))
                n = int(entry.get())
            except ValueError:
                output_text.config(state = NORMAL)
                output_text.insert(END,'Please enter a valid number\n')
                output_text.config(state = DISABLED)
                test = 0
            else:
                test = 1
                break
        filenum = 1
        #size = filesize/n
    except:
        contents = pd.read_csv(pypath)
        total_rows = len(contents)
        #output_text.config(state = NORMAL)
        #output_text.insert(END,f'total_rows = {total_rows}\nn = {n}\n')
        #output_text.config(state = DISABLED)'''
        #rows = math.ceil(total_rows/n)
        while total_rows%n != 0:
            total_rows -= 1
        rows = total_rows/n
        #output_text.config(state = NORMAL)
        #output_text.insert(END,f'rows = {rows}\n')
        #output_text.config(state = DISABLED)'''
        chunks = pd.read_csv(pypath, chunksize = rows)
        for chunk in chunks:
            with open(f'{pypath}[{filenum}].csv', mode = 'w') as file: 
                chunk.to_csv(file)
            filenum += 1
        output_text.config(state = NORMAL)
        output_text.insert(END,'Please enter a valid positive integer.\n')
        output_text.config(state = DISABLED)
    else:
        output_text.config(state = NORMAL)
        output_text.insert(END,'Output created!\nYou may check the output files by accessing the location you entered in filepath\n')
        output_text.config(state = DISABLED)
        #entry.delete(0,END)
        files_win.destroy()
        output_text.config(state = NORMAL)
        output_text.insert(END,'Split by Files closed.\n')
        output_text.config(state = DISABLED)
    
def files_split(output_text):
    output_text.config(state = NORMAL)
    output_text.insert(END,'Split by Files selected.\n')
    output_text.config(state = DISABLED)
    files_win = Toplevel()
    files_win.title('CSV splitter - Split by Files')
    files_frame = Frame(files_win)
    files_frame.pack(padx = 20, pady = 20)
    files_label = Label(files_frame, text = 'Enter the number of files, the csv file is to be split into: ')
    files_label.grid(row = 0, column = 0)
    files_entry = Entry(files_frame, width = 15)
    files_entry.grid(row = 1, column = 0)
    files_entry_button = Button(files_frame, text = "Enter", command = lambda:files_enter(files_entry, output_text, files_win))
    files_entry_button.grid(row = 2, column = 0)
    files_note_label = Label(files_frame, text = 'Please note that the number of files produced may vary by one file depending on the divisibility of number of rows to be divided and number of files requested.')
    files_note_label.grid(row = 3, column = 0)


# In[591]:


def size_enter(entry, output_text, size_win): 
    global filepath
    global filesize
    global pypath
    global test
    size_list = []
    size = 0
    test = 0
    #output_text.insert(END,'size_enter called\n')
    #filename = input('Please enter  the file name: ')
    filesize = os.path.getsize(pypath)
    filenum = 1
    index = 0
    m = 'w'
    output_text.config(state = NORMAL)
    output_text.insert(END,'Working on it...\n')
    output_text.config(state = DISABLED)
    if filesize > 0:
        try:
            while test == 0:
                try:
                    raw_size_list = entry.get()
                    #print(raw_size_list,'raw_size_list')
                    size_list = [int(item)*1024 for item in raw_size_list.split(';')]
                    #print(size_list,'size_list')
                    #output_text.insert(END,f'raw_size_list: {raw_size_list} size_list: {size_list}')

                except ValueError:
                    output_text.config(state = NORMAL)
                    output_text.insert(END,'Invalid entry, please enter only integers separated by \' ; \'.\n ')
                    output_text.config(state = DISABLED)
                    entry.delete(first = 0, last = 'end')
                    size_list = []
                    test = 0
                    break

                else:
                    test = 1
                    break

        
            with open(f'{pypath}') as rfile:
                read = csv.reader(rfile)
                #output_text.insert(END,f'Opened {pypath}')
                for line in read:
                    with open(f'{pypath}[{filenum}].csv', mode = m) as file:
                        write = csv.writer(file)
                        write.writerow(line)
                        #output_text.insert(END,f'Opened {pypath}{filenum}.csv')
                        index += 1
                        m = 'a'
                    if os.path.getsize(f'{pypath}[{filenum}].csv') > size_list[filenum-1]:            
                        filenum += 1
                        m = 'w'
                    if filenum > len(size_list):
                        break
            output_text.config(state = NORMAL)
            output_text.insert(END,'Output created!\nYou may check the output files by accessing the location you entered in filepath\n')
            output_text.config(state = DISABLED)
            #entry.delete(0,END)
            size_win.destroy()
            output_text.config(state = NORMAL)
            output_text.insert(END,'Split by Size closed.\n')
            output_text.config(state = DISABLED)
        except IndexError:
            if sum(size_list) < filesize:
                output_text.config(state = NORMAL)
                output_text.insert(END,"\n\nOutput created, you may check the output files by accessing the location you entered in the filepath, but the sum of the file sizes entered is less than the size of the input file, some of the content from the input file may be missing in the output file(s), please check the sizes you entered and retry entering greater size(s) if this is not the output you desire.\n\n")
                output_text.config(state = DISABLED)
                #entry.delete(0,END)
                size_win.destroy()
                output_text.config(state = NORMAL)
                output_text.insert(END,'Split by Size closed.\n')
                output_text.config(state = DISABLED)
                
        except PermissionError:
            output_text.config(state = NORMAL)
            output_text.insert(END,'Permission denied to access the file.\n')
            output_text.config(state = DISABLED)
    else:
        output_text.config(state = NORMAL)
        output_text.insert(END,'File size is 0.\n')
        output_text.config(state = DISABLED)
        
def size_split(output_text):
    output_text.config(state = NORMAL)
    output_text.insert(END,'Split by Size selected\n')
    output_text.config(state = DISABLED)
    size_win = Toplevel()
    size_win.title('CSV splitter - Split by Size')
    size_frame = Frame(size_win)
    size_frame.pack(padx = 20, pady = 20)
    size_label = Label(size_frame, text = 'Enter the sizes(in kb) of the files you wish to create, in integers separated by a \' ; \' :')
    size_label.grid(row = 0, column = 0)
    size_entry = Entry(size_frame, width = 45)
    size_entry.grid(row = 1, column = 0)
    size_entry_button = Button(size_frame, text = 'Enter', width = 38, command = lambda:size_enter(size_entry, output_text, size_win))
    size_entry_button.grid(row = 2, column = 0)

# In[592]:


def label(text_entry):
    return Label(main, text = text_entry)

def button(text_entry, function, para1):
    return Button(main, text = text_entry, width = 10, command = lambda:function(para1))


# In[593]:


root = Tk()
root.geometry('700x700')
root.title('CSV splitter')
#root.resizable(0,0)
main = Frame(root)
main.pack(padx = 20, pady = 20)

Label(main).grid(row = 0, column = 0, columnspan =2)

filepath_label = Label(main, text = 'Filepath(including the file with extension):')
filepath_label.grid(row = 1, column = 0, sticky = 'W')
filepath_entry = Entry(main, width = 45)
filepath_entry.grid(row = 2, column = 0, sticky = 'W')
filepath_enter_button = Button(main, text = 'Enter', width = 38, command = lambda:filepath_enter(filepath_entry, output_text, size_button, files_button, row_button) )
filepath_enter_button.grid(row =3, column = 0, sticky = 'W')

output_text = Text(main, wrap = WORD)


Label(main).grid(row = 4, column = 0, columnspan = 2)

size_label = label("If you wish to split the file by entering the sizes of the output files, click the 'split by size' button:")
size_label.grid(row = 5, column = 0, sticky = 'W')
size_button = button( "split by size".title(), size_split, output_text)
size_button.grid(row= 5, column = 1)
size_button.config(state = DISABLED)



Label(main).grid(row = 6, column = 0, columnspan = 2)

row_label = label('If you wish to split the file by specifying fixed number of rows per file, click the \'split by rows\' button:')
row_label.grid(row = 7, column = 0, sticky = 'W')
row_button = button('split by rows'.title(), rows_split, output_text)
row_button.grid(row = 7, column = 1)
row_button.config(state = DISABLED)

Label(main).grid(row = 8, column = 0, columnspan = 2)

files_label = label('If you wish to split the file by specifying number of output files, click the \'split by files\' button:')
files_label.grid(row = 9, column = 0, sticky = 'W')
files_button = button('split by files'.title(), files_split, output_text)
files_button.grid(row = 9, column = 1)
files_button.config(state = DISABLED)

Label(main).grid(row = 10, column = 0, columnspan = 2)

output_text_label = label('Status Report:')
output_text_label.grid(row = 11, column = 0, sticky = 'W')
output_text.grid(row = 12, column = 0, columnspan = 2)
output_text.config(state = DISABLED)

#xscroll = Scrollbar(main, orient = HORIZONTAL)
#xscroll.config(command = output_text.xview)
#xscroll.grid(sticky = 'S')'''

yscroll = Scrollbar(main)
yscroll.config(command = output_text.yview)
yscroll.grid(row = 12, column = 2, sticky = 'ns')

output_text.config(yscrollcommand = yscroll.set)

main.mainloop()
