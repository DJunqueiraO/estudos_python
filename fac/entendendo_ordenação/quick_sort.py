numbers = [25, 57, 48, 37, 12, 92, 86, 33]


# Função de ordenação Quick Sort
def quick_sort(current_elements):
    elements = current_elements.copy()
    def quick_sort_recursion(quick_sort_recursion_elements, low, high):
        def partition(partition_elements, partition_low, partition_high):
            partition_pivot = partition_elements[partition_high]
            i = partition_low - 1
            for j in range(partition_low, partition_high):
                current_element = partition_elements[j]
                if current_element <= partition_pivot:
                    i += 1
                    partition_elements[i], partition_elements[j] = partition_elements[j], partition_elements[i]
            partition_elements[i + 1], partition_elements[partition_high] = partition_elements[partition_high], partition_elements[i + 1]
            return i + 1
        if low < high:
            pivot = partition(quick_sort_recursion_elements, low, high)
            quick_sort_recursion(quick_sort_recursion_elements, low, pivot - 1)
            quick_sort_recursion(quick_sort_recursion_elements, pivot + 1, high)
        return quick_sort_recursion_elements

    return quick_sort_recursion(elements, 0, len(elements) - 1)


print(quick_sort(numbers))
print(numbers)
