import tkinter as tk
from tkinter import messagebox, Toplevel
import random
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
        self.auto_click_cost = 50
        self.upgrade_level = 1
        self.clicks_per_second = 0
        self.bonus = 0
        self.temp_bonus_active = False
        self.temp_bonus_duration = 0

        # Достижения
        self.achievements = {
            "Первый клик": False,
            "100 кликов": False,
            "500 кликов": False,
            "1000 кликов": False,
        }

        self.label = tk.Label(root, text="Клики: 0", font=("Helvetica", 24), bg="white")
        self.label.pack(pady=20)

        # Кнопка достижений
        self.achievements_button = tk.Button(root, text="Достижения", command=self.show_achievements)
        self.achievements_button.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=10)

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
        self.update_upgrade_button()
        self.generate_temp_bonus()

    def increment_clicks(self):
        self.click_count += self.click_value + self.bonus
        self.label.config(text=f"Клики: {self.click_count}")
        self.check_achievements()

    def check_achievements(self):
        if self.click_count >= 1 and not self.achievements["Первый клик"]:
            self.achievements["Первый клик"] = True
            messagebox.showinfo("Достижение!", "Вы получили достижение: Первый клик!")

        if self.click_count >= 100 and not self.achievements["100 кликов"]:
            self.achievements["100 кликов"] = True
            messagebox.showinfo("Достижение!", "Вы получили достижение: 100 кликов!")

        if self.click_count >= 500 and not self.achievements["500 кликов"]:
            self.achievements["500 кликов"] = True
            messagebox.showinfo("Достижение!", "Вы получили достижение: 500 кликов!")

        if self.click_count >= 1000 and not self.achievements["1000 кликов"]:
            self.achievements["1000 кликов"] = True
            messagebox.showinfo("Достижение!", "Вы получили достижение: 1000 кликов!")

    def upgrade_click(self):
        if self.click_count >= self.upgrade_cost:
            self.click_count -= self.upgrade_cost
            self.click_value += 1
            self.upgrade_level += 1
            self.upgrade_cost = int(self.upgrade_cost * 1.5)  # Увеличиваем стоимость следующего улучшения
            self.update_upgrade_button()
            self.label.config(text=f"Клики: {self.click_count}")
        else:
            messagebox.showwarning("Недостаточно ресурсов", f"Не хватает {self.upgrade_cost - self.click_count} очков для улучшения кликов!")

    def upgrade_auto_click(self):
        if self.click_count >= self.auto_click_cost:
            self.click_count -= self.auto_click_cost
            self.clicks_per_second += 1
            self.auto_click_cost += 50  # Увеличиваем стоимость следующего улучшения
            self.label.config(text=f"Клики: {self.click_count}")
            self.update_auto_click_button()
        else:
            messagebox.showwarning("Недостаточно ресурсов", f"Не хватает {self.auto_click_cost - self.click_count} очков для улучшения автокликера!")

    def update_auto_clicks(self):
        self.click_count += self.clicks_per_second
        self.label.config(text=f"Клики: {self.click_count}")
        self.root.after(1000, self.update_auto_clicks)  # Обновляем каждую секунду

    def reset_game(self):
        if self.click_count >= 2000:
            self.bonus += 1
        
        self.click_count = 0
        self.click_value = 1
        self.upgrade_cost = 10
        self.auto_click_cost = 50
        self.upgrade_level = 1
        self.clicks_per_second = 0
        
        self.label.config(text="Клики: 0")
        self.update_upgrade_button()
        self.update_auto_click_button()

    def update_upgrade_button(self):
        self.upgrade_button.config(text=f"Улучшить клики ({self.upgrade_cost} очков)")

    def update_auto_click_button(self):
        self.auto_click_button.config(text=f"Автокликер ({self.auto_click_cost} очков)")

    def show_achievements(self):
        achievements_window = Toplevel(self.root)
        achievements_window.title("Достижения")
        achievements_window.geometry("300x400")

    def update_upgrade_button(self):
        self.upgrade_button.config(text=f"Улучшить клики ({self.upgrade_cost} очков)")

    def update_auto_click_button(self):
        self.auto_click_button.config(text=f"Автокликер ({self.auto_click_cost} очков)")

    def generate_temp_bonus(self):
        if random.random() < 0.3:  # 30% шанс на появление бонуса
            self.activate_temp_bonus()
        self.root.after(10000, self.generate_temp_bonus)  # Проверяем каждые 10 секунд

    def activate_temp_bonus(self):
        self.temp_bonus_active = True
        self.temp_bonus_duration = 10  # Длительность бонуса в секундах
        messagebox.showinfo("Временный бонус!", "Вы получили временный бонус! Дополнительные клики на 10 секунд.")
        self.root.after(1000, self.decrement_temp_bonus)

    def decrement_temp_bonus(self):
        if self.temp_bonus_duration > 0:
            self.temp_bonus_duration -= 1
            if self.temp_bonus_duration == 0:
                self.temp_bonus_active = False
                messagebox.showinfo("Бонус завершен", "Ваш временный бонус закончился.")
        self.root.after(1000, self.decrement_temp_bonus)
    

        for achievement, unlocked in self.achievements.items():
            status_color = "black" if unlocked else "gray"
            label = tk.Label(achievements_window, text=achievement, fg=status_color)
            label.pack(anchor='w')

if __name__ == "__main__":
    root = tk.Tk()
    game = ClickerGame(root)
    root.mainloop()