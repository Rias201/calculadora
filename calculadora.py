from tkinter import *
import pyperclip as clipboard

FONT_TYPE = "Verdana"
FONT_SIZE = 18
MAIN_BG_COLOR = "#8861b4"
OP_BG_COLOR = "#bb91da"
OP_FG_COLOR = "Black"
NUM_BG_COLOR = "#a179c7"
NUM_FG_COLOR = "Black"
SPECIAL_BG_COLOR = "#d4a8ec"
SPECIAL_FG_COLOR = "Black"
ENTRY_BG_COLOR = "#edc0ff"
ENTRY_FG_COLOR = "Black"

def borrar():
    global index
    op = inp.get()
    clear()
    inp.insert(index,op[:-1])
    index += len(inp.get())

def calcular():
    global index
    resultado = inp.get()
    clear()
    try:
        inp.insert(index,eval(resultado))
    except SyntaxError:
        inp.insert(index,"SyntaxError")
    except ZeroDivisionError:
        inp.insert(index,"MATH Error")
    except:
        print("Error desconocido")
        exit(1)
    index += len(inp.get())

def clear():
    global index
    inp.delete(0,END)
    index = 0

def copiar():
    clipboard.copy(inp.get())

def digitar(val):
    global index
    inp.insert(index,val)
    index += 1

def pegar():
    global index
    clear()
    inp.insert(index, clipboard.paste())
    index += len(inp.get())

index = 0

main = Tk()
# Configuración ventana principal
main.title("Calculadora")
# main.geometry("240x360")
main.resizable(0,0)
main.configure(bg=MAIN_BG_COLOR)

# Donde sale el resultado
inp = Entry(main,font=(FONT_TYPE,FONT_SIZE*2),bg=ENTRY_BG_COLOR,fg=ENTRY_FG_COLOR,width=12,justify=RIGHT)

# Botones con números
btn_0 = Button(main,text="0",font=(FONT_TYPE,FONT_SIZE),bg=NUM_BG_COLOR,fg=NUM_FG_COLOR,width=11,height=1,command=lambda:digitar(0))
btn_1 = Button(main,text="1",font=(FONT_TYPE,FONT_SIZE),bg=NUM_BG_COLOR,fg=NUM_FG_COLOR,width=5,height=1,command=lambda:digitar(1))
btn_2 = Button(main,text="2",font=(FONT_TYPE,FONT_SIZE),bg=NUM_BG_COLOR,fg=NUM_FG_COLOR,width=5,height=1,command=lambda:digitar(2))
btn_3 = Button(main,text="3",font=(FONT_TYPE,FONT_SIZE),bg=NUM_BG_COLOR,fg=NUM_FG_COLOR,width=5,height=1,command=lambda:digitar(3))
btn_4 = Button(main,text="4",font=(FONT_TYPE,FONT_SIZE),bg=NUM_BG_COLOR,fg=NUM_FG_COLOR,width=5,height=1,command=lambda:digitar(4))
btn_5 = Button(main,text="5",font=(FONT_TYPE,FONT_SIZE),bg=NUM_BG_COLOR,fg=NUM_FG_COLOR,width=5,height=1,command=lambda:digitar(5))
btn_6 = Button(main,text="6",font=(FONT_TYPE,FONT_SIZE),bg=NUM_BG_COLOR,fg=NUM_FG_COLOR,width=5,height=1,command=lambda:digitar(6))
btn_7 = Button(main,text="7",font=(FONT_TYPE,FONT_SIZE),bg=NUM_BG_COLOR,fg=NUM_FG_COLOR,width=5,height=1,command=lambda:digitar(7))
btn_8 = Button(main,text="8",font=(FONT_TYPE,FONT_SIZE),bg=NUM_BG_COLOR,fg=NUM_FG_COLOR,width=5,height=1,command=lambda:digitar(8))
btn_9 = Button(main,text="9",font=(FONT_TYPE,FONT_SIZE),bg=NUM_BG_COLOR,fg=NUM_FG_COLOR,width=5,height=1,command=lambda:digitar(9))

# Botones con operadores
btn_suma = Button(main,text="+",font=(FONT_TYPE,FONT_SIZE),bg=OP_BG_COLOR,fg=OP_FG_COLOR,width=5,height=1,command=lambda:digitar("+"))
btn_resta = Button(main,text="-",font=(FONT_TYPE,FONT_SIZE),bg=OP_BG_COLOR,fg=OP_FG_COLOR,width=5,height=1,command=lambda:digitar("-"))
btn_mult = Button(main,text="*",font=(FONT_TYPE,FONT_SIZE),bg=OP_BG_COLOR,fg=OP_FG_COLOR,width=5,height=1,command=lambda:digitar("*"))
btn_div = Button(main,text="/",font=(FONT_TYPE,FONT_SIZE),bg=OP_BG_COLOR,fg=OP_FG_COLOR,width=5,height=1,command=lambda:digitar("/"))
btn_igual = Button(main,text="=",font=(FONT_TYPE,FONT_SIZE),bg=SPECIAL_BG_COLOR,fg=SPECIAL_FG_COLOR,width=11,height=1,command=lambda:calcular())

# Botones especiales
btn_punto = Button(main,text=".",font=(FONT_TYPE,FONT_SIZE),bg=OP_BG_COLOR,fg=OP_FG_COLOR,width=5,height=1,command=lambda:digitar("."))
btn_par_open = Button(main,text="(",font=(FONT_TYPE,FONT_SIZE),bg=OP_BG_COLOR,fg=OP_FG_COLOR,width=5,height=1,command=lambda:digitar("("))
btn_par_close = Button(main,text=")",font=(FONT_TYPE,FONT_SIZE),bg=OP_BG_COLOR,fg=OP_FG_COLOR,width=5,height=1,command=lambda:digitar(")"))
btn_clear = Button(main,text="C",font=(FONT_TYPE,FONT_SIZE),bg=SPECIAL_BG_COLOR,fg=SPECIAL_FG_COLOR,width=5,height=1,command=lambda:clear())
btn_borrar = Button(main,text="⬅",font=(FONT_TYPE,FONT_SIZE),bg=OP_BG_COLOR,fg=OP_FG_COLOR,width=11,height=1,command=lambda:borrar())
btn_copy = Button(main,text="📝",font=(FONT_TYPE,FONT_SIZE),bg=OP_BG_COLOR,fg=OP_FG_COLOR,width=5,height=1,command=lambda:copiar())
btn_paste = Button(main,text="📋",font=(FONT_TYPE,FONT_SIZE),bg=OP_BG_COLOR,fg=OP_FG_COLOR,width=5,height=1,command=lambda:pegar())

# Colocación de los items
inp.grid(row=0,column=0,columnspan=5,pady=5)

btn_clear.grid(row=1,column=0)
btn_par_open.grid(row=1,column=1)
btn_par_close.grid(row=1,column=2)
btn_borrar.grid(row=1,column=3,columnspan=2)

btn_7.grid(row=2,column=0)
btn_8.grid(row=2,column=1)
btn_9.grid(row=2,column=2)
btn_copy.grid(row=2,column=3)
btn_paste.grid(row=2,column=4)

btn_4.grid(row=3,column=0)
btn_5.grid(row=3,column=1)
btn_6.grid(row=3,column=2)
btn_mult.grid(row=3,column=3)
btn_div.grid(row=3,column=4)

btn_1.grid(row=4,column=0)
btn_2.grid(row=4,column=1)
btn_3.grid(row=4,column=2)
btn_suma.grid(row=4,column=3)
btn_resta.grid(row=4,column=4)

btn_0.grid(row=5,column=0,columnspan=2)
btn_punto.grid(row=5,column=2)
btn_igual.grid(row=5,column=3,columnspan=2)

# Mantiene la ventana abierta
main.mainloop()