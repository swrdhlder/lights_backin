from math import *
import copy

def press(x, y, dim, nuevo):
    nuevo[x][y] = 0 if nuevo[x][y] else 1

    if (x-1) >= 0:
        nuevo[x-1][y] = 0 if nuevo[x-1][y] else 1
    if (x+1) < dim:
        nuevo[x+1][y] = 0 if nuevo[x+1][y] else 1
    if (y-1) >= 0:
        nuevo[x][y-1] = 0 if nuevo[x][y-1] else 1
    if (y+1) < dim:
        nuevo[x][y+1] = 0 if nuevo[x][y+1] else 1
    return nuevo

def print_tablero(tablero):
    for fila in range(dim):
        for item in tablero[fila]:
            print("x" if item else "-", end=" ")
        print()
    print()

def check(tablero):
    suma = 0
    for fila in tablero:
        suma += sum(fila)
    return suma == 0

def follow_the_lights(nuevo):
    count = 0
    for fila in range(1, dim):
        for item in range(dim):
            if nuevo[fila-1][item] == 1:
                nuevo = press(fila, item, dim, nuevo) 
                count+=1
    
    return nuevo, check(nuevo)

def try_one(tablero_nuevo):
    print("Trying combinations of 1 cells")
    combos = list(range(dim))
    for combo in combos:
        nuevo = copy.deepcopy(tablero_nuevo)
        nuevo = press(0, combo, dim, nuevo)
        nuevo, sol = follow_the_lights(nuevo)
        print("Buttons pressed: ", combo+1)

        # print_tablero(nuevo)
        if sol:
            print("Solution found")
            return sol, [combo+1]
    return sol, []

def try_two(tablero_nuevo):
    print("Trying combinations of 2 cells")
    combos = list(range(dim))
    for combo in combos:
        nuevo = copy.deepcopy(tablero_nuevo)
        nuevo = press(0, combo, dim, nuevo)
        for combo2 in combos:
            if combo2 > combo:
                nuevo = press(0, combo2, dim, nuevo)
                nuevo, sol = follow_the_lights(nuevo)

                print("Buttons pressed: ", combo+1, combo2+1)

                # print_tablero(nuevo)
                if sol:
                    print("Solution found")
                    return sol, [combo+1, combo2+1]
    return sol, []

def try_three():
    print("Trying combinations of 3 cells")
    combos = list(range(dim))
    for combo in combos:
        nuevo = press(0, combo, dim)
        for combo2 in combos:
            if combo2 > combo:
                nuevo = press(0, combo2, dim)
                for combo3 in combos:
                    if combo3 > combo2:
                        nuevo = press(0, combo3, dim)
                        follow_the_lights()
                        print("Buttons pressed: ", combo+1, combo2+1, combo3 + 1)
                        print_tablero(nuevo)
                        if check(nuevo):
                            print("Solution Found")
                            exit()

def try_four():
    print("Trying combinations of 4 cells")
    combos = list(range(dim))
    for combo in combos:
        nuevo = press(0, combo, dim)
        for combo2 in combos:
            if combo2 > combo:
                nuevo = press(0, combo2, dim)
                for combo3 in combos:
                    if combo3 > combo2:
                        nuevo = press(0, combo3, dim)
                        for combo4 in combos:
                            if combo4 > combo3:
                                nuevo = press(0, combo4, dim)
                                follow_the_lights()
                                print("Buttons pressed: ", combo+1, combo2+1, combo3 + 1, combo4+1)
                                print_tablero(nuevo)
                                if check(nuevo):
                                    print_tablero(nuevo)
                                    exit()

def try_five():
    print("Trying combinations of 5 cells")
    combos = list(range(dim))
    for combo in combos:
        nuevo = press(0, combo, dim)
        for combo2 in combos:
            if combo2 > combo:
                nuevo = press(0, combo2, dim)
                for combo3 in combos:
                    if combo3 > combo2:
                        nuevo = press(0, combo3, dim)
                        for combo4 in combos:
                            if combo4 > combo3:
                                nuevo = press(0, combo4, dim)
                                for combo5 in combos:
                                    if combo5 > combo4:
                                        nuevo = press(0, combo5, dim)
                                        follow_the_lights()
                                        print("Buttons pressed: ", combo+1, combo2+1, combo3 + 1, combo4+1, combo5+1)
                                        print_tablero(nuevo)
                                        if check(nuevo):
                                            print_tablero(nuevo)
                                            exit()

def turn_90_degrees(tablero_nuevo):
    print("Turning the board 90 degrees.")
    nuevo = copy.deepcopy(tablero_nuevo)
    for fila in range(dim):
        for columna in range(dim):
            nuevo[dim-columna-1][fila] = tablero_nuevo[fila][columna]
    return nuevo

def tryout_sols():

    giros = 0
    combo = ()
    # 1. Try to follow lights normally
    # 2. Try every combination of top lights
    # 3. Try turning 
    #   4. Repeat previous two steps
    for i in range(4):
        tablero_nuevo = copy.deepcopy(tablero)
        if i > 0:
            for _ in range(i):
                tablero_nuevo = turn_90_degrees(tablero_nuevo)
            # print_tablero(tablero_nuevo)
            giros = i
        
        tablero_nuevo, sol = follow_the_lights(tablero_nuevo)
        if sol:
            print("0 giros, 0 additional buttons")
            exit()
        # print_tablero(tablero_nuevo)
        sol, buts = try_one(tablero_nuevo)
        if sol:
            print(str(giros) + " giros, additional buttons: " + str(buts))
            exit()

        sol, buts = try_two(tablero_nuevo)
        if sol:
            print(str(giros) + " giros, additional buttons: " + str(buts))
            exit()
        # try_three(tablero_nuevo)
        # try_four(tablero_nuevo)
        # try_five(tablero_nuevo)
            
    
            

def main():
    global tablero
    global dim
    dim = int(input())
    tablero = [[0 for _ in range(dim)] for _ in range(dim) ]
    for i in range(dim):
        tablero[i] = list(map(int, input().strip().split()))
    # dim = 6
    # tablero[0] = [0, 0, 0, 0, 0, 1]
    # tablero[1] = [1, 0, 1, 0, 0, 1]
    # tablero[2] = [0, 1, 1, 1, 1, 0]
    # tablero[3] = [1, 1, 1, 1, 0, 1]
    # tablero[4] = [1, 0, 1, 1, 1, 0]
    # tablero[5] = [1, 1, 0, 0, 1, 0]



    print_tablero(tablero)
    tryout_sols()

    # nuevo = press(3, 4, dim)
    
    # turn_90_degrees()


    # follow_the_lights()
    # print_tablero(tablero)
    # try_one()
    # try_two()
    # try_three()
    # try_four()
    # try_five()


    # print(check(nuevo))

main()