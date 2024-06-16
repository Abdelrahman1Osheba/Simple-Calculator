import customtkinter
from tkinter import *
from tkinter import messagebox

app = customtkinter.CTk()
app.title("Calculator")
app.geometry("260x290")
app.resizable(False, False)
app.config(bg="#c7d4cd")
font = ("Times New Roman", 20, "bold")


def on_click(num):
    Display.insert(END, num)


def clear():
    Display.delete(0, END)


def back_space():
    length = len(Display.get())
    Display.delete(length - 1, END)


def Equal():
    try:
        num = Display.get()
        new_num = num.replace('X', '*')
        results = eval(new_num)
        clear()
        Display.insert(0, results)
    except ZeroDivisionError:
        messagebox.showerror("Forbidden", "Can not Divide By Zero")
    except:
        messagebox.showerror("Empty", "Enter Values")


Display = customtkinter.CTkEntry(app, font=font, text_color="#000000", fg_color="#8ad132", border_color="#000000",
                                 bg_color="#c7d4cd", width=240, height=50)
Display.place(x=10, y=10)
n0_button = customtkinter.CTkButton(app, text="0", font=font, command=lambda: on_click('0'), text_color="#000000",
                                    fg_color="#ffffff", hover_color="#3bb8b8", bg_color="#c7d4cd",
                                    border_color="#000000", border_width=4, cursor="hand2", width=60)
n0_button.place(x=10, y=80)
n1_button = customtkinter.CTkButton(app, text="1", font=font, command=lambda: on_click('1'), text_color="#000000",
                                    fg_color="#ffffff", hover_color="#3bb8b8", bg_color="#c7d4cd",
                                    border_color="#000000", border_width=4, cursor="hand2", width=60)
n1_button.place(x=10, y=120)
n4_button = customtkinter.CTkButton(app, text="4", font=font, command=lambda: on_click('4'), text_color="#000000",
                                    fg_color="#ffffff", hover_color="#3bb8b8", bg_color="#c7d4cd",
                                    border_color="#000000", border_width=4, cursor="hand2", width=60)
n4_button.place(x=10, y=160)
n7_button = customtkinter.CTkButton(app, text="7", font=font, command=lambda: on_click('7'), text_color="#000000",
                                    fg_color="#ffffff", hover_color="#3bb8b8", bg_color="#c7d4cd",
                                    border_color="#000000", border_width=4, cursor="hand2", width=60)
n7_button.place(x=10, y=200)
n2_button = customtkinter.CTkButton(app, text="2", font=font, command=lambda: on_click('2'), text_color="#000000",
                                    fg_color="#ffffff", hover_color="#3bb8b8", bg_color="#c7d4cd",
                                    border_color="#000000", border_width=4, cursor="hand2", width=60)
n2_button.place(x=70, y=120)
n5_button = customtkinter.CTkButton(app, text="5", font=font, command=lambda: on_click('5'), text_color="#000000",
                                    fg_color="#ffffff", hover_color="#3bb8b8", bg_color="#c7d4cd",
                                    border_color="#000000", border_width=4, cursor="hand2", width=60)
n5_button.place(x=70, y=160)
n8_button = customtkinter.CTkButton(app, text="8", font=font, command=lambda: on_click('8'), text_color="#000000",
                                    fg_color="#ffffff", hover_color="#3bb8b8", bg_color="#c7d4cd",
                                    border_color="#000000", border_width=4, cursor="hand2", width=60)
n8_button.place(x=70, y=200)
n3_button = customtkinter.CTkButton(app, text="3", font=font, command=lambda: on_click('3'), text_color="#000000",
                                    fg_color="#ffffff", hover_color="#3bb8b8", bg_color="#c7d4cd",
                                    border_color="#000000", border_width=4, cursor="hand2", width=60)
n3_button.place(x=130, y=120)
n6_button = customtkinter.CTkButton(app, text="6", font=font, command=lambda: on_click('6'), text_color="#000000",
                                    fg_color="#ffffff", hover_color="#3bb8b8", bg_color="#c7d4cd",
                                    border_color="#000000", border_width=4, cursor="hand2", width=60)
n6_button.place(x=130, y=160)
n9_button = customtkinter.CTkButton(app, text="9", font=font, command=lambda: on_click('9'), text_color="#000000",
                                    fg_color="#ffffff", hover_color="#3bb8b8", bg_color="#c7d4cd",
                                    border_color="#000000", border_width=4, cursor="hand2", width=60)
n9_button.place(x=130, y=200)
d_button = customtkinter.CTkButton(app, text=".", font=font, command=lambda: on_click('.'), text_color="#000000",
                                   fg_color="#ffffff", hover_color="#214ab0", bg_color="#c7d4cd",
                                   border_color="#000000", border_width=4, cursor="hand2", width=60)
d_button.place(x=70, y=80)
c_button = customtkinter.CTkButton(app, text="C", font=font, command=clear, text_color="#000000",
                                   fg_color="#ffffff", hover_color="#9c1c1c", bg_color="#c7d4cd",
                                   border_color="#000000", border_width=4, cursor="hand2", width=60)
c_button.place(x=130, y=80)
E_button = customtkinter.CTkButton(app, text="=", font=font, command=Equal, text_color="#000000",
                                   fg_color="#ffffff", hover_color="#05b314", bg_color="#c7d4cd",
                                   border_color="#000000", border_width=4, cursor="hand2", width=60, height=115)
E_button.place(x=190, y=80)
plus = customtkinter.CTkButton(app, text="+", font=font, command=lambda: on_click('+'), text_color="#000000",
                               fg_color="#ffffff", hover_color="#214ab0", bg_color="#c7d4cd", border_color="#000000",
                               border_width=4, cursor="hand2", width=60)
plus.place(x=10, y=240)
minus = customtkinter.CTkButton(app, text="-", font=font, command=lambda: on_click('-'), text_color="#000000",
                                fg_color="#ffffff", hover_color="#214ab0", bg_color="#c7d4cd", border_color="#000000",
                                border_width=4, cursor="hand2", width=60)
minus.place(x=70, y=240)
multiply = customtkinter.CTkButton(app, text="X", font=font, command=lambda: on_click('X'), text_color="#000000",
                                   fg_color="#ffffff", hover_color="#214ab0", bg_color="#c7d4cd",
                                   border_color="#000000", border_width=4, cursor="hand2", width=60)
multiply.place(x=130, y=240)
divide = customtkinter.CTkButton(app, text="/", font=font, command=lambda: on_click('/'), text_color="#000000",
                                 fg_color="#ffffff", hover_color="#214ab0", bg_color="#c7d4cd", border_color="#000000",
                                 border_width=4, cursor="hand2", width=60)
divide.place(x=190, y=240)

Delete = customtkinter.CTkButton(app, text="B", font=font, command=lambda: back_space(), text_color="#000000",
                                 fg_color="#ffffff", hover_color="#9c1c1c", bg_color="#c7d4cd", border_color="#000000",
                                 border_width=4, cursor="hand2", width=60)
Delete.place(x=190, y=200)
app.mainloop()
