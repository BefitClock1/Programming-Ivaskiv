from Lab5 import que
test_queue = que()
test_queue.insert("A", 5)
test_queue.insert("B", 2)
test_queue.insert("C", 8)
test_queue.insert("D", 1)
test_queue.insert("E", 3)

print("Черга після вставки:")
test_queue.show_queue()
print(test_queue.get_max_priority)
print("Deleted:", test_queue.del_max_priority())

test_queue.show_queue()