max(3, 2) == 3
min(3, 2) == 2
max([1, 2, 0, 3, 4]) == 4
min("hello") == "e"
max(2.2, 5.6, 5.9, key=int) == 5.6
min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]
