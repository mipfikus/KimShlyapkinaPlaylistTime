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
        indices = []
        for song in songs:
            if song in playlist[0]:
                indices.append(playlist[0].index(song))
        # Convert minutes to seconds for playlist_d
        total_duration = sum(playlist[1][i] * 60 + playlist[1][i] % 1 * 100 for i in indices)  
        return total_duration
    elif isinstance(playlist, dict):
        # No conversion needed for playlist_b (already in seconds)
        return sum(playlist[song] * 60 + playlist[song] % 1 * 100 for song in songs if song in playlist) 
    else:
        raise ValueError("Неверный формат плейлиста")

# Функция выбора случайных песен
def select_random_songs(playlist, n):
    if isinstance(playlist, list) and len(playlist) == 2:
        return random.sample(playlist[0], n) 
    elif isinstance(playlist, dict):
        return random.sample(list(playlist.keys()), n)
    else:
        raise ValueError("Неверный формат плейлиста")

# Итоговая функция 
def get_duration(playlist, n):
    selected_songs = select_random_songs(playlist, n)
    total_duration = calculate_duration(playlist, selected_songs)
    hours = int(total_duration // 3600)
    minutes = int((total_duration % 3600) // 60)
    seconds = int(total_duration % 60)
    return timedelta(hours=hours, minutes=minutes, seconds=seconds)

# вывод
print(get_duration(playlist_d, 5))