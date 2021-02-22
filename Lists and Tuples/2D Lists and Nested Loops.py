
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[1][0])

# nested loops, should come under loops but, eh.
for row in number_grid:
    for col in row:
        print(col)
