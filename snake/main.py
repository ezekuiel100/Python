from tkinter import *
from tkinter import ttk

def draw_canvas():
   tamanho_bloco = 20 
   colunas = int(screen_width / tamanho_bloco)
   linhas = int(screen_height / tamanho_bloco)

   for linha in range(linhas):
      for coluna in range(colunas):
        x1 = coluna * tamanho_bloco  
        y1 = linha * tamanho_bloco
        x2 = x1  + tamanho_bloco 
        y2 = y1 + tamanho_bloco
        canvas.create_rectangle(x1, y1, x2 , y2, outline="white")

def change_snake_direction(event):
      if(event.keysym == 'Up'):
         canvas.move(snake , 0 , -20)
      if(event.keysym == 'Down'):
         canvas.move(snake , 0 , +20)
      if(event.keysym == 'Left'):
         canvas.move(snake , -20, 0 )
      if(event.keysym == 'Right'):
         canvas.move(snake ,+20, 0)
     

window = Tk()
window.title("Snake game")
window.resizable(False, False)

screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()
window.geometry(f"{screen_width}x{screen_height}")

canvas = Canvas(window, width=screen_width, height=screen_height , background='gray75')    
           
snake = canvas.create_rectangle(20, 20, 40, 40, fill='blue')
canvas.create_oval(40, 40, 60, 60, fill='red')

window.bind("<Key>" , change_snake_direction)

draw_canvas()
canvas.pack()
window.mainloop()