import random
import stddraw
from color import Color

def bubble_sort(numbers):
    n = len(numbers)
    for sweep in range(n):
        for pair in range(0, n - 1 - sweep):
            if numbers[pair] > numbers[pair+1]:
                numbers[pair], numbers[pair + 1] = numbers[pair+1], numbers[pair]

def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

def insertion_sort(numbers):
    n = len(numbers)
    for i in range(1, n):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key

def draw_bars(numbers, selected=()):
    stddraw.clear()
    n = len(numbers)
    bar_width = 10.0 / n
    
    for i, number in enumerate(numbers):
        x = i * bar_width + bar_width / 2
        color = Color(255, 90, 90) if i in selected else Color(70, 130, 220)
        stddraw.setPenColor(color)
        stddraw.filledRectangle(x - bar_width / 2, 0, bar_width * 0.9, number)
    stddraw.show(100)

def bubble_sort_animated(numbers):
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)
    n = len(numbers)
    
    for sweep in range(n):
        swapped = False
        for pair in range(0, n - 1 - sweep):
            draw_bars(numbers, selected=(pair, pair+1))
            if numbers[pair] > numbers[pair+1]:
                numbers[pair], numbers[pair + 1] = numbers[pair+1], numbers[pair]
                swapped = True
            draw_bars(numbers, selected=(pair, pair+1))
            
        if not swapped:
            break
        
    draw_bars(numbers)
    stddraw.show()

def selection_sort_animated(numbers):
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)
    n = len(numbers)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            # Animamos la comparación del mínimo actual con el elemento j
            draw_bars(numbers, selected=(min_idx, j))
            if numbers[j] < numbers[min_idx]:
                min_idx = j
                
        # Intercambio físico y animación de la acción
        draw_bars(numbers, selected=(i, min_idx))
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
        draw_bars(numbers, selected=(i, min_idx))
        
    draw_bars(numbers)
    stddraw.show()

def insertion_sort_animated(numbers):
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)
    n = len(numbers)
    
    for i in range(1, n):
        key = numbers[i]
        j = i - 1
        
        while j >= 0 and numbers[j] > key:
            # Animamos los elementos que se están comparando y desplazando
            draw_bars(numbers, selected=(j, j + 1))
            numbers[j + 1] = numbers[j]
            draw_bars(numbers, selected=(j, j + 1))
            j -= 1
            
        numbers[j + 1] = key
        draw_bars(numbers)
        
    draw_bars(numbers)
    stddraw.show()

# INPUT
# Generate a list of 10 random numbers between 0 and 100
numbers_to_sort = [random.randint(0, 100) for _ in range(10)]
print(f"Original list: {numbers_to_sort}")

# PROCESS
# You can swap this call for selection_sort_animated or insertion_sort_animated to test them out!
#bubble_sort_animated(numbers_to_sort)
selection_sort_animated(numbers_to_sort)
#insertion_sort_animated(numbers_to_sort)
# OUTPUT
# Display final results in the console
print(f"Sorted list: {numbers_to_sort}")