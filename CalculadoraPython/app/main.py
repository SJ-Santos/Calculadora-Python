from tkinter import *
from tkinter import ttk 

janela = Tk()
janela.title("Calculadora")
janela.geometry("445x460")

#Frame do resultado
frm = Frame(janela,bg="black",width=445,height=80)
frm.grid(column=0,row=0)
#Frame dos botões 
frm2 = Frame(janela,width=500,height=420)
frm2.grid(column=0,row=1)

#Label calculo
valor=StringVar()

calculo_label=Label(frm,textvariable=valor,width=64,height=5,relief=FLAT,justify=RIGHT,fg="purple")
calculo_label.place(x=0,y=0)

total = ''
def calculo(event):
   global total 
   total = total +str(event)
   valor.set(total)


def result():
   global total
   resultado= eval(total) 
   valor.set(resultado)
   total = valor.get()
   


def limpar():
    global total
    total=''
    valor.set('') 



#Botões
btn_c = Button(frm2,command=limpar,text="C",width=45,height=4)
btn_c.place(x=0,y=0)

btn0 = Button(frm2,text="0",width=14,height=4,command=lambda:calculo("0"))
btn0.place(x=110,y=76*4)

btn1 = Button(frm2,text="1",width=14,height=4,command=lambda:calculo("1"))
btn1.place(x=0,y=76*3)

btn2 = Button(frm2,text="2",width=14,height=4,command=lambda:calculo("2"))
btn2.place(x=110,y=76*3)

btn3 = Button(frm2,text="3",width=14,height=4,command=lambda:calculo("3"))
btn3.place(x=110*2,y=76*3)

btn4 = Button(frm2,text="4",width=14,height=4,command=lambda:calculo("4"))
btn4.place(x=0,y=76*2)

btn5 = Button(frm2,text="5",width=14,height=4,command=lambda:calculo("5"))
btn5.place(x=110,y=76*2)

btn6 = Button(frm2,text="6",width=14,height=4,command=lambda:calculo("6"))
btn6.place(x=110*2,y=76*2)

btn7 = Button(frm2,text="7",width=14,height=4,command=lambda:calculo("7"))
btn7.place(x=0,y=76)

btn8 = Button(frm2,text="8",command=lambda:calculo("8"),width=14,height=4)
btn8.place(x=110,y=76)

btn9 = Button(frm2,text="9",command=lambda:calculo("9"),width=14,height=4)
btn9.place(x=110*2,y=76)

btn_mais = Button(frm2,text="+",command=lambda:calculo("+"),width=14,height=4)
btn_mais.place(x=110*3,y=0)

btn_menos = Button(frm2,text="-",command=lambda:calculo("-"),width=14,height=4)
btn_menos.place(x=110*3,y=76)

btn_dividir = Button(frm2,text="/",command=lambda:calculo("/"),width=14,height=4)
btn_dividir.place(x=110*3,y=76*2)

btn_multiplicar=Button(frm2,text="*",command=lambda:calculo("*"),width=14,height=4)
btn_multiplicar.place(x=110*3,y=76*3)



btn_ponto = Button(frm2,command=lambda:calculo("."),text=".",width=14,height=4)
btn_ponto.place(x=0,y=76*4)

btn_igual = Button(frm2,text="=",command=result,width=30,height=4)
btn_igual.place(x=110*2,y=76*4)

#loop da janela
janela.mainloop()