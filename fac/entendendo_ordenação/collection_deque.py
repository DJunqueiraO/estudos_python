from collections import deque

linked_list = deque()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

linked_list.appendleft(0)

linked_list.pop()
linked_list.popleft()

print(linked_list)
