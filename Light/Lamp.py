import tkinter as tk
from PIL import Image, ImageTk

def tkloop():
    root.mainloop()

def toggle_image():
    global current_image_index
    current_image_index = (current_image_index + 1) % len(images)
    image_label.config(image=images[current_image_index])


root = tk.Tk()
root.title("Дедлайн")
root.resizable(height=False, width= False)
#root.attributes("-toolwindow", 1)
 
# Загрузка изображений
image1 = Image.open("on.png")
image2 = Image.open("off.png")
image1 = image1.resize((200, 200), Image.ANTIALIAS)
image2 = image2.resize((200, 200), Image.ANTIALIAS)

# Преобразование изображений в формат, подходящий для Tkinter
image1_tk = ImageTk.PhotoImage(image1)
image2_tk = ImageTk.PhotoImage(image2)


images = [image1_tk, image2_tk]
current_image_index = 0

# Создание метки для изображений
image_label = tk.Label(root, image=image1_tk)
image_label.pack(pady=10)

# Создание кнопки для смены изображений

#button = tk.Button(root, text="Сменить изображение", command=toggle_image)
#button.pack()
