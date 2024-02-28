"""
We are going to use arrays to optimize execution time
"""
import numpy as np
from typing import Dict

def get_winner(path: str) -> int:
    with open(path) as file:
        output = ''
        while (lines := file.readline()) != '0 0':
            """
            lines = file.readline()
            if lines == '0 0':
                exit()
            """
            
            grand_prix, participants = lines.strip().split(" ")

            base_position_arrray = build_position_array(int(grand_prix), int(participants), file)

            num_score_system = file.readline()
            
            #print(base_position_arrray)
            for _ in range(int(num_score_system)):
                dict_scores = build_dict_scores(file)
                #print(dict_scores)
                result_array = calculate_score(base_position_arrray, dict_scores)
                winner = np.argwhere(result_array == np.amax(result_array)) + 1
                output += ', '.join([str(i) for i in winner.squeeze(axis=1).tolist()])
                output += '\n'
                #print(', '.join([str(i) for i in winner.squeeze(axis=1).tolist()]))
    return output


def build_position_array(grand_prix, participants, file) -> np.ndarray:
    position_arrray = np.empty((grand_prix,participants))
    for i in range(grand_prix):
        position_arrray[i,:] = file.readline().split(" ")
    return position_arrray

def calculate_score(base_position_arrray, dict_scores) -> np.ndarray:
    result_array = np.zeros_like(base_position_arrray)
    for key,value in dict_scores.items():
        assign_score_array = base_position_arrray.copy()
        assign_score_array[assign_score_array != key] = 0
        assign_score_array[assign_score_array == key] = value
        result_array = np.vstack((result_array,assign_score_array))

    return np.sum(result_array,axis=0)


def build_dict_scores(file) -> Dict[str,str]:
    score_info = file.readline().strip().split(" ")
    score_positions = int(score_info.pop(0))
    if score_positions == len(score_info):
        return {i+1:int(score) for i,score in enumerate(score_info)}

if __name__ == "__main__":
    path = input('Por favor ingrese la ruta del archivo: ')
    print(get_winner(path))