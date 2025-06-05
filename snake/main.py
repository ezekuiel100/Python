from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Snake game")
window.resizable(False, False)

height = window.winfo_screenheight()
width = window.winfo_screenwidth()

window.geometry(f"{width}x{height}")

canvas = Canvas(width=width, height=height , background='gray75')

tamanho_bloco = 20 
colunas = int(width / tamanho_bloco)
linhas = int(height / tamanho_bloco)

for linha in range(linhas):
    for coluna in range(colunas):
        x1 = coluna * tamanho_bloco  
        y1 = linha * tamanho_bloco
        x2 = x1  + tamanho_bloco 
        y2 = y1 + tamanho_bloco
        canvas.create_rectangle(x1, y1, x2 , y2, outline="white")


snake = canvas.create_rectangle(20, 20, 40, 40, fill='blue')
canvas.create_oval(40, 40, 60, 60, fill='red')


def change_direction(event):
      if(event.keysym == 'Up'):
         canvas.move(snake , 0 , -20)
      if(event.keysym == 'Down'):
         canvas.move(snake , 0 , +20)
      if(event.keysym == 'Left'):
         canvas.move(snake , -20, 0 )
      if(event.keysym == 'Right'):
         canvas.move(snake ,+20, 0)
     
           
     
window.bind("<Key>" , change_direction)


canvas.pack()
window.mainloop()