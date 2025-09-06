import random
import time
import sys

#ЫЫЫЫЫЫЫ

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20
    
    def attack(self, other):
        # US-9: Случайный разброс урона (attack_power ± 15)
        damage = random.randint(self.attack_power - 15, self.attack_power + 15)
        other.health -= damage
        return damage
    
    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self):
        # US-5: Запрос имени игрока
        player_name = self.get_player_name()
        
        # US-8: Случайное имя для компьютера
        computer_name = self.generate_computer_name()
        
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)
    
    def get_player_name(self):
        """US-5: Получение имени игрока с валидацией"""
        while True:
            try:
                name = input("Введите имя вашего героя: ").strip()
                if name:
                    return name
                else:
                    print("Имя не может быть пустым! Попробуйте снова.")
            except EOFError:
                print("\nВвод завершен. Используется имя по умолчанию 'Воин'.")
                return "Воин"
            except KeyboardInterrupt:
                print("\n\nИгра прервана.")
                sys.exit(0)
    
    def generate_computer_name(self):
        """US-8: Генерация случайного имени для компьютера"""
        names = ["Гаргона", "Дракула", "Тёмный Властелин", "Орк", "Призрак", 
                "Демон", "Вампир", "Зомби", "Ведьмак", "Гоблин"]
        return random.choice(names)
    
    def print_status(self):
        """Вывод текущего статуса боя"""
        print(f"{self.player.name}: {max(0, self.player.health)} HP")
        print(f"{self.computer.name}: {max(0, self.computer.health)} HP")
        print("-" * 30)
    
    def start(self):
        """US-2, US-3: Основной игровой цикл"""
        print(f"=== БИТВА ГЕРОЕВ ===")
        print(f"{self.player.name} vs {self.computer.name}")
        print("=" * 30)
        
        round_number = 1
        
        # US-2: Игровой цикл
        while self.player.is_alive() and self.computer.is_alive():
            print(f"--- Раунд {round_number} ---")
            self.print_status()
            
            # Ход игрока
            print(f"Ход {self.player.name}...")
            damage = self.player.attack(self.computer)
            print(f"{self.player.name} атакует {self.computer.name} и наносит {damage} урона!")
            
            # US-7: Задержка для чтения
            time.sleep(1.5)
            
            # Проверка победы после хода игрока
            if not self.computer.is_alive():
                break
            
            # Ход компьютера
            print(f"Ходитда {self.computer.name}...")
            damage = self.computer.attack(self.player)
            print(f"{self.computer.name} атакует {self.player.name} и наносит {damage} урона!")
            
            time.sleep(1.5)
            round_number += 1
        
        # US-4: Объявление победителя
        self.print_final_result()
    
    def print_final_result(self):
        """US-4: Вывод финального результата игры"""
        print("=" * 40)
        print("=== БИТВА ЗАВЕРШЕНА! ===")
        self.print_status()
        
        if self.player.is_alive():
            print(f"ПОБЕДИЛ {self.player.name}!")
        else:
            print(f"ПОБЕДИЛ {self.computer.name}!")
        print("=" * 40)

def main():
    """US-10: Точка входа в приложение"""
    try:
        print("Добро пожаловать в игру 'Битва Героев'!")
        print("Подготовьтесь к эпическому сражению!\n")
        
        # US-7: Небольшая пауза перед началом
        time.sleep(1)
        
        game = Game()
        game.start()
        
        # Предложение сыграть еще раз
        while True:
            try:
                replay = input("\nХотите сыграть еще раз? (да/нет): ").strip().lower()
                if replay in ['да', 'д', 'yes', 'y']:
                    print("\n" + "=" * 40)
                    game = Game()
                    game.start()
                elif replay in ['нет', 'н', 'no', 'n']:
                    print("\nСпасибо за игру! До свидания!")
                    break
                else:
                    print("Пожалуйста, введите 'да' или 'нет'.")
            except (KeyboardInterrupt, EOFError):
                print("\n\nИгра завершена.")
                break
                
    except KeyboardInterrupt:
        print("\n\nИгра прервана пользователем.")
    except Exception as e:
        print(f"\nПроизошла unexpected ошибка: {e}")

# US-10: Проверка на прямой запуск файла
if __name__ == "__main__":
    main()