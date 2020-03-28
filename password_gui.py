from tkinter import *
from generate import *
from commands import *

# base
root = Tk()
root.geometry("600x400")
root.title('Password Manager')
root.resizable(0,0)
act = Commands()

# functions
def test():
    value = entry.get().upper()
    print(value)
    if value == 'LIST':
        data = act.list_all_platforms()
        box = Tk()
        box.title('Platforms')
        for x in data:
            msg = Label(box, text = x)
            msg.pack()
        
    elif value == 'SHOW ALL':
        data = act.get_all_accounts()
        box = Tk()
        box.title('All Accounts')
        for x in data:
            msg = Label(box, text = x)
            msg.pack()

    elif value == 'ADD':
        def add_account():
            data = [plat.get(), user.get(), passw.get()]
            act.add_account_gui(data)
            stop = True
            return stop
            
        box = Tk()
        plat = Entry(box)
        plat.pack()
        user = Entry(box)
        user.pack()
        passw = Entry(box)
        passw.pack()
        x = add_account()
        submit = Button(box, command = x,
        text = 'Add')
        submit.pack()

    
    elif value == 'VIEW':
        def view():
            temp = plat.get()
            val = act.get_account(temp.upper())
            show = Label(box, text = val)
            show.pack()
        box = Tk()
        plat = Entry(box)
        plat.pack()
        submit = Button(box, command = view,
        text = 'View')
        submit.pack()
        
        


# label
label = Label(root, 
text = "Password Manager", height = '2')
label.pack()

# show commands
commands = 'List of Commands\nView\nAdd\nList'
list_of_commands = Label(root, text = commands, height = '12')
list_of_commands.pack()

# input user
entry = Entry(root)
entry.pack()

# submit button
button = Button(root, text = 'Submit', height = '2',
command = test)
button.pack()

# main loop
root.mainloop()