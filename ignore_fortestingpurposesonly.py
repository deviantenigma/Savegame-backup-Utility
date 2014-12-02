import tkinter
import string
from ctypes import windll
import os

'''
for d in string.ascii_uppercase:
    if os.path.exists("%s:\\" % (d)):
        print("Drive letter '%s' is in use." % (d))
'''

'''
def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives
print(get_drives())
'''

'''
testLambda = (lambda boolInput: False if boolInput else True)

print(testLambda(True))
print(testLambda(False))
'''


top = tkinter.Tk()

#Testing out listbox in preparation to migrating game selection to a listbox as opposed to a bunch of check boxes
#because checkboxes aren't very scalable.
def click_button(event):
    # #this block works
    w = event.widget
    index = w.curselection()
    for x in index:
        value = w.get(x)
        print(value)

Lb1 = tkinter.Listbox(top,selectmode='extended')
#Lb1.bind('<<ListboxSelect>>', click_button)
Lb1.insert(0, "Python")
Lb1.insert(0, "Perl")
Lb1.insert(0, "C")
Lb1.insert(0, "PHP")
Lb1.insert(0, "JSP")
Lb1.insert(0, "Ruby")

def btnclick():
    values = [Lb1.get(x) for x in Lb1.curselection()]
    print(', '.join(values))

onlybutton = tkinter.Button(text='test', command=btnclick)

Lb1.pack()
onlybutton.pack()
top.mainloop()


