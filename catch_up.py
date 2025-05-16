#qweq
import tkinter as tk

class ClickerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Clicker Game")
        self.root.geometry("400x600")
        
        # Установка фона
        self.bg_image = tk.PhotoImage(file="fon.png")  # Замените на свой файл
        self.background_label = tk.Label(root, image=self.bg_image)
        self.background_label.place(relwidth=1, relheight=1)

        self.click_count = 0
        self.click_value = 1
        self.upgrade_cost = 10
        self.upgrade_level = 1
        self.clicks_per_second = 0
        self.bonus = 0

        self.label = tk.Label(root, text="Клики: 0", font=("Helvetica", 24), bg="white")
        self.label.pack(pady=20)

        # Загрузка изображений для кнопок
        self.click_image = tk.PhotoImage(file="b_1.png")  # Замените на свой файл
        self.upgrade_image = tk.PhotoImage(file="b_2.png")  # Замените на свой файл
        self.auto_click_image = tk.PhotoImage(file="Blue-Button-PNG-Image.png")  # Замените на свой файл
        self.reset_image = tk.PhotoImage(file="b_4.png")  # Замените на свой файл

        # Кнопки с изображениями
        self.click_button = tk.Button(root, image=self.click_image, command=self.increment_clicks, bg="black", borderwidth=0)
        self.click_button.pack(pady=10)

        self.upgrade_button = tk.Button(root, image=self.upgrade_image, command=self.upgrade_click, bg="black", borderwidth=0)
        self.upgrade_button.pack(pady=10)

        self.auto_click_button = tk.Button(root, image=self.auto_click_image, command=self.upgrade_auto_click, bg="black", borderwidth=0)
        self.auto_click_button.pack(pady=10)

        self.reset_button = tk.Button(root, image=self.reset_image, command=self.reset_game, bg="black", borderwidth=0)
        self.reset_button.pack(pady=10)

        self.update_auto_clicks()

    def increment_clicks(self):
        self.click_count += self.click_value + self.bonus
        self.label.config(text=f"Клики: {self.click_count}")

    def upgrade_click(self):
        if self.click_count >= self.upgrade_cost:
            self.click_count -= self.upgrade_cost
            self.click_value += 1
            self.upgrade_level += 1
            self.upgrade_cost *= 2  # Увеличиваем стоимость следующего улучшения
            self.upgrade_button.config(text=f"Улучшить клики ({self.upgrade_cost} очков)")
            self.label.config(text=f"Клики: {self.click_count}")

    def upgrade_auto_click(self):
        if self.click_count >= 50:  # Стоимость улучшения кликов в секунду
            self.click_count -= 50
            self.clicks_per_second += 1
            self.label.config(text=f"Клики: {self.click_count}")

    def update_auto_clicks(self):
        self.click_count += self.clicks_per_second
        self.label.config(text=f"Клики: {self.click_count}")
        self.root.after(1000, self.update_auto_clicks)  # Обновляем каждую секунду

    def reset_game(self):
        if self.click_count >= 2000:
            self.bonus += 1

        
        self.click_count = 0
        self.click_value = 1
        self.upgrade_cost += 2000
        self.upgrade_level = 50
        self.clicks_per_second = 10
        
        self.label.config(text="Клики: 0")

if __name__ == "__main__":
    root = tk.Tk()
    game = ClickerGame(root)
    root.mainloop()
