numbers = [26, 47, 38, 11, 95]


def bubble_sort(current_elements):
    elements = current_elements.copy()
    for i in range(len(elements) - 1):
        swapped = False
        for j in range(1, len(elements) - i):
            if elements[j] < elements[j - 1]:
                elements[j], elements[j - 1] = elements[j - 1], elements[j]
                swapped = True
        if not swapped:
            break
    return elements


print(numbers)
print(bubble_sort(numbers))
