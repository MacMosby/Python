import tkinter
#
#
# def button_clicked():
#     print("I got clicked!")
#     my_label.config(text=input.get())
#
#
# window = tkinter.Tk()
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)
# window.config(padx=20, pady=20)
#
# # Label
#
# my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "italic"))
#
# my_label["text"] = "New text"
# my_label.config(text="Run")
#
# my_label.grid(column=0, row=0)
#
# # Button
#
# button = tkinter.Button(text="Click me!", command=button_clicked)
# button.grid(column=1, row=1)
#
# button2 = tkinter.Button(text="Any text")
# button2.grid(column=2, row=0)
#
# # Entry
#
# input = tkinter.Entry()
# input.grid(column=3, row=2)


def button_clicked():
    distance_in_km.config(text=f"{float(entry.get())*1.609}")


window = tkinter.Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

entry = tkinter.Entry(width=7)
entry.grid(column=1, row=0)

miles = tkinter.Label(text="Miles")
miles.grid(column=2, row=0)

is_equal_to = tkinter.Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

distance_in_km = tkinter.Label(text="0")
distance_in_km.grid(column=1, row=1)

km = tkinter.Label(text="Km")
km.grid(column=2, row=1)

button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)






window.mainloop()
