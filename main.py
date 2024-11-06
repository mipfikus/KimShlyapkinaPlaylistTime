# Импорт необходимых модулей

import random
from datetime import timedelta

# Структура данных для плейлистов
playlist_d = [
           ("The Flute Tune", "Voodoo People", "Galvanize", "Miami Disco", "Komarovo", "Wild Frontier", "Check It Out", "Seasons", "These Things Will Come To Be"),
           (5.23, 5.07, 7.34, 4.31, 2.26, 4.28, 2.09, 4.25, 4.56),
       ]
playlist_b = {
           'Портофино': 3.32,
           'Снег': 4.35,
           'Попытка №5': 3.23,
           'Тополиный Пух': 3.53,
           'Если хочешь остаться': 4.48,
           'Зеленоглазое такси': 5.52,
           'Ты не верь слезам': 3.1,
           'Nowhere to Run': 2.58,
           'Салют, Вера': 4.44,
           'Улетаю': 3.24,
           'Опять метель': 3.37,
       }

# Функция вычисления времени звучания
def calculate_duration(playlist, songs):
           if isinstance(playlist, list) and len(playlist) == 2:
               indices = [playlist[0].index(song) for song in songs]
               return sum(playlist[1][i] for i in indices)
           elif isinstance(playlist, dict):
               return sum(playlist[song] for song in songs)
           else:
               raise ValueError("Неверный формат плейлиста")

# Функция выбора случайных песен
def select_random_songs(playlist, n):
           if isinstance(playlist, list) and len(playlist) == 2:
               return random.sample(list(zip(*playlist)[0]), n)
           elif isinstance(playlist, dict):
               return random.sample(list(playlist.keys()), n)
           else:
               raise ValueError("Неверный формат плейлиста")

def calculate_duration():
    # Вызов функций get_duration() и select_random_songs()
    # Вывод ответа