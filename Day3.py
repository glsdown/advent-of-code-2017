location = 312051
square = 25  # 560
grid = [[0 for i in range(square)] for j in range(square)]


# Round 1
def spiral(X, Y):
    x = y = 0
    dx = 0
    dy = -1
    for i in range(max(X, Y) ** 2):
        if i == location - 1:
            print(abs(x) + abs(y))
        if (-X / 2 < x <= X / 2) and (-Y / 2 < y <= Y / 2):
            grid[((square // 2) + x) % square][((square // 2) + y) % square] = i + 1
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy


# Round 2
def spiral2(X, Y):
    x = y = 0
    dx = 0
    dy = -1
    for i in range(max(X, Y) ** 2):
        if (-X / 2 < x <= X / 2) and (-Y / 2 < y <= Y / 2):
            total = 0
            current_x = ((square // 2) + x) % square
            current_y = ((square // 2) + y) % square

            if i == 0:
                grid[current_x][current_y] = 1
            else:
                for j in range(-1, 2):
                    for k in range(-1, 2):
                        try:
                            if current_x + j >= 0 and current_y + k >= 0:
                                total += grid[current_x + j][current_y + k]
                        except:
                            pass
                if total < location:
                    grid[current_x][current_y] = total
                else:
                    print(total)
                    input()
                    quit()
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy


spiral(square, square)
spiral2(square, square)
