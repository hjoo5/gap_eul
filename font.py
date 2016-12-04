def choose_font():
    global m, text # I hate to use global, but for simplicity

    t = tkinter.Toplevel(root)
    font_name = tkinter.Label(t, text='Font Name: ')
    font_name.grid(row=0, column=0, sticky='nsew')
    enter_font = tkinter.Entry(t)
    enter_font.grid(row=0, column=1, sticky='nsew')
    font_size = tkinter.Label(t, text='Font Size: ')
    font_size.grid(row=1, column=0, sticky='nsew')
    enter_size = tkinter.Entry(t)
    enter_size.grid(row=1, column=1, sticky='nsew')

    # associating a lambda with the call to text.config()
    # to change the font of text (a Text widget reference)
    ok_btn = tkinter.Button(t, text='Apply Changes',
                       command=lambda: text.config(font=(enter_font.get(), 
                       enter_size.get())))
    ok_btn.grid(row=2, column=1, sticky='nsew')

    # just to make strechable widgets
    # you don't strictly need this
    for i in range(2):
        t.grid_rowconfigure(i, weight=1)
        t.grid_columnconfigure(i, weight=1)
    t.grid_rowconfigure(2, weight=1)


text = tkinter.Text(root)
text.pack(expand=1, fill='both')
chooser = tkinter.Button(root, text='Choose Font', command=choose_font)
chooser.pack(side='bottom')