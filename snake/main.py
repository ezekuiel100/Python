from tkinter import *
from tkinter import ttk

snake_direction = "Down"
snake_parts = []


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

def create_food(): 
 pass


def change_snake_direction(event):
   global snake_direction

   if(event.keysym == 'Up'):
       snake_direction = "Up"
   if(event.keysym == 'Down'):
     snake_direction = "Down"
   if(event.keysym == 'Left'):
     snake_direction = "Left"
   if(event.keysym == 'Right'):
     snake_direction = "Right"
     

def move_snake(): 
   head_coords = canvas.coords(snake_parts[0])
   x1, y1, x2, y2 = head_coords


   if(snake_direction == "Up"):      
      y1 -= 20
      y2 -= 20
   elif(snake_direction == "Down"):
       y1 += 20
       y2 += 20
   elif(snake_direction == "Left"):
       x1 -= 20
       x2 -= 20
   elif( snake_direction == "Right"):
       x1 += 20
       x2 += 20
   
   new_part = canvas.create_rectangle(x1, y1, x2, y2 , fill='green')
   snake_parts.insert(0,new_part)

   food_coords = canvas.coords(food)
   if head_coords[0] == food_coords[0] and head_coords[1] == food_coords[1]:
      create_food()
   else:
      tail = snake_parts.pop()
      canvas.delete(tail)


   window.after(100, move_snake)

     

window = Tk()
window.title("Snake game")
window.resizable(False, False)

screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()
window.geometry(f"{screen_width}x{screen_height}")

canvas = Canvas(window, width=screen_width, height=screen_height , background='gray75')    
           
snake = canvas.create_rectangle(20, 20, 40, 40, fill='blue')
snake_parts.append(snake)

food = canvas.create_oval(40, 40, 60, 60, fill='red')

window.bind("<Key>" , change_snake_direction)

draw_canvas()
move_snake()
canvas.pack()
window.mainloop()