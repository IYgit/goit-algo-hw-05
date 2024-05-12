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

real_times_text1 = []
random_times_text1 = []
real_times_text2 = []
random_times_text2 = []

# Вимірюємо час виконання для кожного алгоритму та кожного типу підрядка
algorithms = [boyer_moore_search, kmp_search, rabin_karp_search]
for algorithm in algorithms:
    real_times_text1.append(measure_time(algorithm, text1, real_pattern_text1))
    random_times_text1.append(measure_time(algorithm, text1, random_pattern))
    real_times_text2.append(measure_time(algorithm, text2, real_pattern_text2))
    random_times_text2.append(measure_time(algorithm, text2, random_pattern))

#  Назви алгоритмів для легенди графіку
algorithm_names = [algorithm.__name__ for algorithm in algorithms]

# Побудова графіку
plt.figure(figsize=(10, 6))

plt.plot(algorithm_names, real_times_text1, label='Real pattern in text1', marker='o')
plt.plot(algorithm_names, random_times_text1, label='Random pattern in text1', marker='o')
plt.plot(algorithm_names, real_times_text2, label='Real pattern in text2', marker='o')
plt.plot(algorithm_names, random_times_text2, label='Random pattern in text2', marker='o')

plt.yscale('log')  # Встановлюємо логарифмічну шкалу по вертикалі

plt.xlabel('Algorithm')
plt.ylabel('Execution Time (log scale)')
plt.title('Comparison of Substring Search Algorithms')
plt.legend()
plt.xticks(rotation=45)  # Обертаємо назви алгоритмів для кращої читабельності

plt.tight_layout()
plt.show()
