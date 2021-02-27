import re
import json
from csv import writer
from decimal import Decimal
from datetime import datetime

remaining_time = Decimal('123456.0987654321')
field_names = ['current_location', 'current_experience', 'current_date']


class Enemy:

    def __init__(self, enemy):
        enemy_initialization = r'(Mob|Boss)_exp(\d+)_tm(\d+)'
        finding_enemy = re.findall(enemy_initialization, enemy)
        self.name = enemy
        self.health = int(finding_enemy[0][1])
        self.kill_time = Decimal(finding_enemy[0][2])

    def kill_self(self):
        self.health = 0


class Hero(object):

    def __init__(self, remaining_time):
        self.state = 0
        self.current_experience = 0
        self.elapsed_time = 0
        self.remaining_time = remaining_time

    def spent_time(self, time):
        self.elapsed_time += time
        self.remaining_time -= time

    def kill_enemy(self, enemy):
        self.current_experience += enemy.health
        self.spent_time(enemy.kill_time)
        enemy.kill_self()


class Location:

    def __init__(self):
        self.file_data = None
        self.current_location = None
        self.locations = []
        self.read_JSON()

    def change(self, location):
        location_initialization = r'(Location_\w+|Hatch)_tm([\d+|\d/.]+)'
        finding_location = re.findall(location_initialization, location)
        name_location = finding_location[0][0]
        throw_time = Decimal(finding_location[0][1])
        self.current_location = name_location
        return name_location, throw_time

    def go_to_location(self, index):
        self.branching = self.locations[index]

    def read_JSON(self):
        with open('rpg.json', 'r', encoding='utf8') as rpg:
            self.branching = json.load(rpg)

    def save_csv(self, csv_names):
        with open('dungeon.csv', 'a', newline='', encoding='utf8') as csv_file:
            csv_writer = writer(csv_file, )
            csv_writer.writerow(csv_names)


class Game:
    def __init__(self, remaining_time, csv_names):
        self.enemies = []
        self.hero = Hero(remaining_time)
        self.location_class = Location()
        self.location_class.save_csv(csv_names)

    def choising(self, action_length):
        available_choices = [str(i + 1) for i in range(action_length)]
        while True:
            option = input('Какое действие выберете? : ')
            if option in available_choices:
                break
        return int(option)

    def list_enemies(self):
        print('Доступные для уничтожения враги:')
        attacking_enemies = []
        for i in range(len(self.enemies)):
            attacking_enemies.append(str(i + 1) + '.' + self.enemies[i].name)
        print(*attacking_enemies, sep='\n')

    def kill_enemy(self):
        self.list_enemies()
        choose = self.choising(len(self.enemies))
        self.hero.kill_enemy(self.enemies[choose - 1])

    def show_state_info(self):
        # clear()
        print(f" Вы сейчас в {self.location_class.current_location} и у вас {self.hero.current_experience} опыта. ")
        print(f"До наводнения {self.hero.remaining_time} секунд.")
        print(f"{self.hero.elapsed_time} времени уже прошло.")
        showing_enemies = list(map(lambda enm: '- Враг: ' + enm.name, self.enemies))
        showing_locations = list(
            map(lambda loc: '- Вход в локацию: ' + list(loc.keys())[0], self.location_class.locations))
        print("Перед вами:")
        print(*showing_enemies, sep='\n')
        print(*showing_locations, sep='\n')

    def turning(self, killed_enemies):
        self.location_class.locations = []
        self.enemies = []
        for current_location, environment_in in self.location_class.branching.items():
            if environment_in == "You are winner":
                return 'You are winner'
            for item in environment_in:
                if isinstance(item, dict):
                    self.location_class.locations.append(item)
                elif isinstance(item, str) and not killed_enemies:
                    self.enemies.append(Enemy(item))
            self.location_class.current_location = current_location

    def current_state(self):
        with open('dungeon.csv', 'a', newline='', encoding='utf8') as csv_file:
            csv_writer = writer(csv_file, )
            available_actions = []
            if self.enemies:
                available_actions.append("Уничтожить врага")
            if self.location_class.locations:
                available_actions.append("Сходить в другую локацию")
            available_actions.append("Выиграть игру")
            csv_writer.writerow([self.location_class.current_location, self.hero.current_experience, datetime.now()])
            self.show_state_info()
            print(f"Пришло время выбора:")
            available_actions = list(map(lambda act:
                                         str(available_actions.index(act) + 1)
                                         + '.'
                                         + act,
                                         available_actions))
            print(*available_actions, sep='\n')
            return available_actions

    def get_locations_for_action(self):
        return \
            list(map(lambda x:
                     str(self.location_class.locations.index(x) + 1)
                     + '.Пройти в локацию: '
                     + list(x.keys())[0],
                     self.location_class.locations))

    def step_into_location(self, locations):
        locations_for_action = self.get_locations_for_action()
        print('Доступные для входа локации:')
        print(*locations_for_action, sep='\n')
        choose = self.choising(len(self.location_class.locations))
        curr_location, tm = self.location_class.change(locations_for_action[int(choose) - 1])
        self.hero.spent_time(tm)
        return choose

    def process(self):
        killed_enemies = False
        self.location_class.read_JSON()

        while True:
            turn = self.turning(killed_enemies)
            if turn == 'You are winner':
                if self.hero.current_experience >= 280:
                    print(turn)
                    return "win"
                else:
                    print('Вы слишком быстро добрались до выхода и чтобы доказать своё превосходство решаете '
                          'вернуться к началу и еще раз всех уничтожить')
                    return
            else:
                if not self.location_class.locations or self.hero.remaining_time <= 0:
                    print('Вы слишком быстро добрались до выхода и чтобы доказать своё превосходство решаете '
                          'вернуться к началу и еще раз всех уничтожить')
                    return
                todo_choice = self.current_state()
                action = self.choising(len(todo_choice))
                action = todo_choice[int(action) - 1][2:]

                if action == 'Уничтожить врага':
                    self.kill_enemy()
                    killed_enemies = True

                elif action == 'Сходить в другую локацию':
                    location_choice = int(self.step_into_location(self.location_class.locations)) - 1
                    self.location_class.go_to_location(location_choice)
                    killed_enemies = False
                    self.enemies = []
                elif action == 'Выиграть игру':
                    print('Вы решили подождать наводнения и волной вас вынесло к выходу.')
                    return 'exit'

    def go(self):
        while True:
            win = self.process()
            if win in ['win', 'exit']:
                print('Прекрасная игра! Вы выходите победителем. Времени в запасе у вас осталось: ',
                      self.hero.remaining_time)
                break


game = Game(remaining_time=remaining_time, csv_names=field_names)
game.go()
