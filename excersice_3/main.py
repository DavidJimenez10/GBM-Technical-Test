from typing import List

def jump_forward(cur_position, k):
    return cur_position + k

def calculate_minimum_jump(target_points: int) -> str:
    """
    the algorithm is really simple
    you can reach any point using three cases
    1) you only jump forward and get to the point in this case it takes k jumps
    2) you only jump forward and get to the point + 1, so you jump backward and get to the point, in this case it takes k + 1 jumps
    3) you can reach any point between sum(k) - 2 and sum(k-1) + 1, making a backward jump in the k jumps
    for example: 
        target_point = 7
        k = 3 you get to 6
        k = 4 you get to 10
        if you jump backwards on the second jump for k = 4 you get 7
        k=1
        1 (-1)
        k=2
        0 (+3)
        k=3
        3 (+4)
        k=4
        7
    
    """
    output = ''
    for point in range(1, target_points+1):
        point = int(point)
        cur_position = 0
        k = 0
        while cur_position < point:
            k += 1
            cur_position = jump_forward(cur_position, k)
        
        if cur_position == point:
            pass
        elif cur_position - 1 == point:
            k += 1
        elif cur_position - k + 1 < point:
            pass
        output += str(k)
        output += '\n'
        #print(k)
    return output

if __name__ == "__main__":
    target_points = input('Por favor ingrese el número de pruebas: ')
    print(calculate_minimum_jump(int(target_points)))

