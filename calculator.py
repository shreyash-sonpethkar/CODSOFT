from tkinter import *
class Calculator:
    def __init__(self, cal):
        cal.title("GUI Calculator")
        font, calbtn, btnArray, operator = ('arial', 20, "bold"), "789+456-123*0C=/", [], ""
        text_input = IntVar()
        def BtnClick(number):
            nonlocal operator
            operator = operator+str(number)
            text_input.set(operator)
        def Equal():
            nonlocal operator
            calculated = eval(operator)
            text_input.set(calculated)
            operator = ""
        def ClearEntry():
            nonlocal operator
            text_input.set(0)
            operator =""
        Entry(cal, textvariable=text_input, font=font, bg="powder blue", bd=30, justify="right").grid(columnspan=4)
        index = 0
        for row in range(4):
            for column in range(4):
                btnArray.append(Button(cal, text=calbtn[index], bg="powder blue", padx=16, pady=16, bd=8, font=font))
                btnArray[index].grid(row=row+1, column=column)
                btnArray[index]['command'] = Equal if calbtn[index] == "=" else ClearEntry if calbtn[index] == "C" else lambda x = calbtn[index] : BtnClick(x)
                index+=1
        cal.mainloop()
cal = Tk()
Calculator(cal)