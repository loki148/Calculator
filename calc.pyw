import tkinter, math, time

win = tkinter.Tk()
win.title('CALCULATOR')
canvas = tkinter.Canvas(win, width=295, height=430, bg='grey')
canvas.pack()

canvas.create_rectangle(10,10,290,60,fill='white')
x = 0
a = 0
a_t= ['(', 7, 4,1,0,')', 8,5,2,'+','Fac',9,6,3,'-','DEL','.', '/','*','=']
for i in range(4):
    y=0
    for j in range(5):
        canvas.create_rectangle(10+x, 70+y, 60+x, 120+y, fill='#C0C0C0', tags= 'sq'+str(a_t[a]))
        canvas.create_text(35+x ,95+y , text = a_t[a], font='arial 17')
        #print(str(x+10), str(x+60),str(y+70),str(y+120))
        a += 1
        y += 76
    x += 76
Txt_formula = ''
def smthng(sur):
    canvas.delete('rslt')
    global Txt_formula
    x = sur.x
    y = sur.y
    print(x,y)
    if 10<x<60 and 70<y<120:
        a = '('
        Txt_formula = Txt_formula + a
        canvas.itemconfig('sq(', fill="gold")
        canvas.update()
        time.sleep(0.16)
        canvas.itemconfig('sq(', fill="#C0C0C0")
    elif 10<x<60 and 146<y<196:
        a = '7'
        Txt_formula = Txt_formula + a
        canvas.itemconfig('sq7', fill="gold")
        canvas.update()
        time.sleep(0.16)
        canvas.itemconfig('sq7', fill="#C0C0C0")
    elif 10<x<60 and 222<y<272:
        a = '4'
        Txt_formula = Txt_formula + a
        canvas.itemconfig('sq4', fill="gold")
        canvas.update()
        time.sleep(0.16)
        canvas.itemconfig('sq4', fill="#C0C0C0")
    elif 10<x<60 and 298<y<348:
        a = '1'
        Txt_formula = Txt_formula + a
        canvas.itemconfig('sq1', fill="gold")
        canvas.update()
        time.sleep(0.16)
        canvas.itemconfig('sq1', fill="#C0C0C0")
    elif 10<x<60 and 374<y<424:
        a = '0'
        Txt_formula = Txt_formula + a
        canvas.itemconfig('sq0', fill="gold")
        canvas.update()
        time.sleep(0.16)
        canvas.itemconfig('sq0', fill="#C0C0C0")
    elif 86<x<136 and 70<y<120:
        a = ')'
        Txt_formula = Txt_formula + a
        canvas.itemconfig('sq)', fill="gold")
        canvas.update()
        time.sleep(0.16)
        canvas.itemconfig('sq)', fill="#C0C0C0")
    elif 86<x<136 and 146<y<196:
        a = '8'
        Txt_formula = Txt_formula + a
        canvas.itemconfig('sq8', fill="gold")
        canvas.update()
        time.sleep(0.16)
        canvas.itemconfig('sq8', fill="#C0C0C0")
    elif 86<x<136 and 222<y<272:
        a = '5'
        Txt_formula = Txt_formula + a
        canvas.itemconfig('sq5', fill="gold")
        canvas.update()
        time.sleep(0.16)
        canvas.itemconfig('sq5', fill="#C0C0C0")
    elif 86<x<136 and 298<y<348:
        a = '2'
        Txt_formula = Txt_formula + a
        canvas.itemconfig('sq2', fill="gold")
        canvas.update()
        time.sleep(0.16)
        canvas.itemconfig('sq2', fill="#C0C0C0")
    elif 86<x<136 and 374<y<424:
        a = '+'
        Txt_formula = Txt_formula + a
        canvas.itemconfig('sq+', fill="gold")
        canvas.update()
        time.sleep(0.16)
        canvas.itemconfig('sq+', fill="#C0C0C0")
    elif 162<x<212 and 70<y<120:
        a='!'
        b = math.factorial(int(Txt_formula))
        Txt_formula = ''
        
        canvas.create_text(200,40, text=b,font='arial 15', tags='rslt')
        canvas.itemconfig('sqFac', fill="gold")
        canvas.update()
        time.sleep(0.16)
        canvas.itemconfig('sqFac', fill="#C0C0C0")
    elif 162<x<212 and 146<y<196:
        a = '9'
        Txt_formula = Txt_formula + a
        canvas.itemconfig('sq9', fill="gold")
        canvas.update()
        time.sleep(0.16)
        canvas.itemconfig('sq9', fill="#C0C0C0")
    elif 162<x<212 and 222<y<272:
        a = '6'
        Txt_formula = Txt_formula + a
        canvas.itemconfig('sq6', fill="gold")
        canvas.update()
        time.sleep(0.16)
        canvas.itemconfig('sq6', fill="#C0C0C0")
    elif 162<x<212 and 298<y<348:
        a = '3'
        Txt_formula = Txt_formula + a
        canvas.itemconfig('sq3', fill="gold")
        canvas.update()
        time.sleep(0.16)
        canvas.itemconfig('sq3', fill="#C0C0C0")
    elif 162<x<212 and 374<y<424:
        a = '-'
        Txt_formula = Txt_formula + a
        canvas.itemconfig('sq-', fill="gold")
        canvas.update()
        time.sleep(0.16)
        canvas.itemconfig('sq-', fill="#C0C0C0")
    elif 238<x<288 and 70<y<120:
        Txt_formula = ''
        
        canvas.itemconfig('sqDEL', fill="gold")
        canvas.update()
        time.sleep(0.16)
        canvas.itemconfig('sqDEL', fill="#C0C0C0")
    elif 238<x<288 and 146<y<196:
        a = '.'
        Txt_formula = Txt_formula + a
        canvas.itemconfig('sq.', fill="gold")
        canvas.update()
        time.sleep(0.16)
        canvas.itemconfig('sq.', fill="#C0C0C0")
    elif 238<x<288 and 222<y<272:
        a = '/'
        Txt_formula = Txt_formula + a
        canvas.itemconfig('sq/', fill="gold")
        canvas.update()
        time.sleep(0.16)
        canvas.itemconfig('sq/', fill="#C0C0C0")
    elif 238<x<288 and 298<y<348:
        a = '*'
        Txt_formula = Txt_formula + a
        canvas.itemconfig('sq*', fill="gold")
        canvas.update()
        time.sleep(0.16)
        canvas.itemconfig('sq*', fill="#C0C0C0")
    elif 238<x<288 and 374<y<424:
        Txt_formula
        rslt = eval(Txt_formula)
        canvas.create_text(200,40, text=rslt,font='arial 15', tags='rslt')
        a = '='
        Txt_formula = Txt_formula + a
        canvas.itemconfig('sq=', fill="gold")
        canvas.update()
        time.sleep(0.16)
        canvas.itemconfig('sq=', fill="#C0C0C0")
    else:
        pass
    canvas.delete('form')
    canvas.create_text(120,25, text=Txt_formula,font='arial 15', tags='form')

canvas.bind_all("<Button-1>", smthng)

win.mainloop()
