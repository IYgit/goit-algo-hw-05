import timeit
from boyer_module import boyer_moore_search
from kmp_module import kmp_search
from rabin_karp_module import rabin_karp_search
import requests
import matplotlib.pyplot as plt

# Функція для отримання вмісту файлу з URL
def get_text_from_url(doc_id):
    url = f"https://drive.usercontent.google.com/u/0/uc?id={doc_id}&export=download"
    response = requests.get(url)
    text = response.text
    return text

# Отримання вмісту файлу
text1 = get_text_from_url("18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh")
text2 = get_text_from_url("13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ")


# Функція для вимірювання часу виконання певного алгоритму пошуку підрядка
def measure_time(algorithm, text, pattern):
    def wrapper():
        algorithm(text, pattern)
    execution_time = timeit.timeit(wrapper, number=1)
    return execution_time

# Задаємо підрядки
real_pattern_text1 = "Алгоритми – це послідовність точно визначених дій"  
real_pattern_text2 = "Було проведено дослідження різних структур даних" 
random_pattern = "random_pattern"  # Вигаданий підрядок

# Вимірюємо час виконання для кожного алгоритму та кожного типу підрядка
algorithms = [boyer_moore_search, kmp_search, rabin_karp_search]
for algorithm in algorithms:
    real_time_text1 = measure_time(algorithm, text1, real_pattern_text1)
    random_time_text1 = measure_time(algorithm, text1, random_pattern)
    real_time_text2 = measure_time(algorithm, text2, real_pattern_text2)
    random_time_text2 = measure_time(algorithm, text2, random_pattern)

    print(f"Algorithm: {algorithm.__name__}")
    print("Real pattern in text1:", real_time_text1)
    print("Random pattern in text1:", random_time_text1)
    print("Real pattern in text2:", real_time_text2)
    print("Random pattern in text2:", random_time_text2)
    print()
