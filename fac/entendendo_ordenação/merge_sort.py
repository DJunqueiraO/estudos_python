numbers = [25, 57, 48, 37, 12, 92, 86, 33]

def merge_sort(current_elements):
    elements = current_elements.copy()
    def merge(left, right):
        merged = []
        while left and right:
            if left[0] < right[0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))
        merged.extend(left or right)
        return merged
    def divide(elements):
        if len(elements) <= 1:
            return elements
        mid = len(elements) // 2
        left = divide(elements[:mid])
        right = divide(elements[mid:])
        return merge(left, right)
    return divide(elements)


print(merge_sort(numbers))
print(numbers)
