import tkinter as tk
from tkinter import messagebox
import random

stack = []

root = tk.Tk()
root.title("Енгізу терезесі")
root.geometry("700x700")
root.config(bg="lightblue")


label1 = tk.Label(root, text="Сан енгізіңіз", font=("Times New Roman", 16, "bold italic"))
label1.pack(pady=50)

def open_second_window():
    second_window = tk.Toplevel(root)
    second_window.title("Жұмыс істеу терезесі")
    second_window.geometry("700x700")

    label = tk.Label(second_window, text="Жұмыс істеу терезесі")
    label.pack(pady=20)

    canvas = tk.Canvas(second_window, width=500, height=400, bg="white")
    canvas.pack(pady=10)

    def update_canvas():
        canvas.delete("all")  
        rect_width = 80  
        rect_height = 30  
        y_offset = 400  

        for i, row in enumerate(reversed(stack)):  
            for j, value in enumerate(row):
                x1 = 200  
                x2 = x1 + rect_width  
                y1 = y_offset - rect_height  
                y2 = y_offset  

                canvas.create_rectangle(x1, y1, x2, y2, fill="skyblue", outline="black")  
                canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=str(value), font=("Arial", 12))  

                y_offset = y1 

    matrix_text = "\n".join(str(row) for row in stack)
    matrix_label = tk.Label(second_window, text="Матрица:\n" + matrix_text)
    matrix_label.pack(pady=10)
    
    def push():
        if stack:  
            new_value = random.randint(1, 100) 
            stack[-1].append(new_value)  
            messagebox.showinfo("Успех", f"Қосылған элемент: {new_value}")
        else:
            new_value = random.randint(1, 100)
            stack.append([new_value])
            messagebox.showinfo("Успех", f"Создана новая строка с элементом: {new_value}")
        update_canvas() 

    def pop():
        if stack: 
            if stack[-1]:  
                removed_value = stack[-1].pop()  
                messagebox.showinfo("Успех", f"Өшірілген элемент: {removed_value}")
            if not stack[-1]: 
                stack.pop()
        else:
            messagebox.showerror("Ошибка", "Матрица пуста! Нечего удалять.")
        update_canvas()  
   
    button_push = tk.Button(second_window, text="Push", command=push, font=("Times New Roman", 14, "bold italic"))
    button_push.pack(pady=10)

    
    button_pop = tk.Button(second_window, text="Pop", command=pop, font=("Times New Roman", 14, "bold italic"))
    button_pop.pack(pady=10)

    update_canvas()

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

def add_row_to_stack():
    entered_text = entry.get()
    if entered_text.isdigit():
        cols = int(entered_text)
        row = [random.randint(1, 100) for _ in range(cols)]  
        stack.append(row)
        messagebox.showinfo("Успех", f"Қосылған матрица: {row}") 
    else:
        messagebox.showerror("Қате", "Тек сан енгізіңіз!")

button_submit = tk.Button(root, text="Қосылатын элементтер", command=add_row_to_stack, font=("Times New Roman", 14, "bold italic"))
button_submit.pack(pady=10)

button_visualize = tk.Button(root, text="Визуализация", command=open_second_window, font=("Times New Roman", 14, "bold italic"))
button_visualize.pack(pady=10)

root.mainloop()