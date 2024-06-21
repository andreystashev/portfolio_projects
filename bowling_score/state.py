from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def strike(self):
        pass

    @abstractmethod
    def spare(self):
        pass

    @staticmethod
    def count(element):
        if element == '-':
            return 0
        if element != '0':
            return int(element)


class Bowling:
    def __init__(self):
        self.state = None
        self.move_counter = 0
        self.total_score = 0

    def change_state(self, state):
        self.state = state

    def char_state(self, element):
        if element == 'X':
            self.total_score += self.state.strike()
        elif element == '/':
            self.total_score += self.state.spare()
        elif element.isdigit() or element == '-':
            self.total_score += self.state.count(element)

    def split(self, game_result):
        frame = game_result[self.move_counter] + game_result[self.move_counter + 1] \
            if game_result[self.move_counter] != 'X' else game_result[self.move_counter]
        yield frame
        self.move_counter += 1 if len(frame) == 2 else 0

    def switch(self, game_result):
        while self.move_counter < len(game_result):
            frame_generation = self.split(game_result)
            for frame in frame_generation:
                if len(frame) == 1:
                    self.change_state(FirstMove())
                    self.char_state(frame[0])
                elif frame[1] == '/' and frame[0].isdigit() and frame[0] != '0':
                    self.change_state(SecondMove())
                    self.char_state(frame[1])
                else:
                    self.change_state(FirstMove())
                    self.char_state(frame[0])
                    self.change_state(SecondMove())
                    self.char_state(frame[1])
                self.move_counter += 1


class FirstMove(State):
    def strike(self):
        return 20

    def spare(self):
        pass


class SecondMove(State):
    def strike(self):
        pass

    def spare(self):
        return 15


class MarketMove1(FirstMove):
    def strike(self):
        return 10

    def spare(self):
        raise ValueError('В первом броске не может быть спэра')


class MarketMove2(SecondMove):
    def strike(self):
        raise ValueError('Во втором броске не может быть страйка')

    def spare(self):
        return 10


class MarketBowling(Bowling):

    def __init__(self):
        super().__init__()
        self.frame_count = 0

    def split(self, game_result):
        if self.move_counter + 1 == len(game_result) and game_result[self.move_counter] == 'X':
            frame = game_result[self.move_counter]
        elif self.move_counter + 2 == len(game_result) and (
                game_result[self.move_counter + 1] == '/' or game_result[self.move_counter + 1] == 'X'):
            frame = game_result[self.move_counter] + game_result[self.move_counter + 1]
        else:
            frame = game_result[self.move_counter] + game_result[self.move_counter + 1] + game_result[
                self.move_counter + 2] \
                if game_result[self.move_counter] == 'X' or game_result[self.move_counter + 1] == '/' \
                else game_result[self.move_counter] + game_result[self.move_counter + 1]
        self.frame_count += 1
        if self.frame_count > 10:
            raise ValueError('Нельзя играть больше 10 фреймов')
        yield frame
        if self.move_counter != len(game_result):
            if len(frame) == 2 and frame != 'XX' or game_result[self.move_counter] == '/':
                self.move_counter += 1
        else:
            self.move_counter += 0

    def switch(self, game_result):
        while self.move_counter < len(game_result):
            frame_generation = self.split(game_result)
            for frame in frame_generation:
                if len(frame) == 3:
                    if frame[0] == 'X' and frame[2] == '/':
                        self.change_state(MarketMove1())
                        self.char_state(frame[0])
                        self.change_state(MarketMove2())
                        self.char_state(frame[2])
                    elif frame[1] == '/' and frame[0].isdigit() and frame[0] != '0':
                        self.change_state(MarketMove2())
                        self.char_state(frame[1])
                        self.change_state(MarketMove1())
                        self.char_state(frame[2])
                    else:
                        self.change_state(MarketMove1())
                        self.char_state(frame[0])
                        self.char_state(frame[1])
                        self.char_state(frame[2])
                elif len(frame) == 1:
                    self.change_state(MarketMove1())
                    self.char_state(frame[0])
                elif frame[1] == '/' and frame[0].isdigit() and frame[0] != '0':
                    self.change_state(MarketMove2())
                    self.char_state(frame[1])
                elif frame[0] == 'X' and frame[1] == 'X':
                    self.change_state(MarketMove1())
                    self.char_state(frame[0])
                    self.char_state(frame[1])
                else:
                    if frame[0].isdigit() and frame[1].isdigit():
                        if int(frame[0]) + int(frame[1]) >= 10:
                            pass

                    self.change_state(FirstMove())
                    self.char_state(frame[0])
                    self.change_state(SecondMove())
                    self.char_state(frame[1])
                self.move_counter += 1
