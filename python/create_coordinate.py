import pandas as pd
import json

VIZ_list_for_heatmap = [
        [2,7],[2,6],[3,5],[3,4],[4,3],[4,2],[5,1],[6,2],[6,3],[7,4],[7,5],[8,6],[8,7],
        [11,7],[12,7],[13,7],[12,6],[12,5],[12,4],[12,3],[12,2],[11,1],[12,1],[13,1],
        [16,7],[17,7],[18,7],[19,7],[20,7], [20,6],[19,5],[18,4],[17,3],[16,2],[16,1],[17,1],[18,1],[19,1],[20,1]
    ]

VIZ_list_for_A = [
    [23,1],[25,8],[27,1],[26,4.5],[24,4.5]
]

VIZ_list_for_R = [
    [29,8],[29,1],[29,4.5],[32.5,1]
]

VIZ_list_for_R_curve =[
    [29,8],[30,7.95],[31,7.7],[32,6.25],[31,4.8],[30,4.55],[29,4.5]
]

VIZ_list_for_D = [
    [35,8],[35,1]
]

VIZ_list_for_D_curve =[
    [35,8],[36,7.95],[37,7.7],[38,7],[38.5,6],[38.75,4.5],[38.5,3],[38,2],[37,1.3],[36,1.05],[35,1]
]


def create_coordinates_for_line(list,alphabet,curve=0):
    coordinates = []
    for coordinate in list:
        coordinates.append({'x':coordinate[0]+1, 'y':coordinate[1], 'alphabet':alphabet, 'heatmap':0, 'curve':curve})

    return coordinates

def create_coordinates_for_heatmap(X,Y):

    coordinates = []
    Xs = list(range(0,X))
    Ys = list(range(0,Y))
    for x in Xs:
        for y in Ys:
            if [x,y] in VIZ_list_for_heatmap:
                y_adj= y+1
                coordinates.append({'x':x, 'y':y_adj, 'alphabet':1, 'heatmap':1})
            else:
                y_adj= y+1
                coordinates.append({'x':x, 'y':y_adj, 'alphabet':0, 'heatmap':1})

    print(Xs)
    print(Ys)
    return coordinates


def main():
    # coordinates for heatmap
    coordinates = create_coordinates_for_heatmap(23,9)
    coordinates_A = create_coordinates_for_line(VIZ_list_for_A,'A')
    coordinates_R = create_coordinates_for_line(VIZ_list_for_R,'R') + create_coordinates_for_line(VIZ_list_for_R_curve,'R',1)
    coordinates_D = create_coordinates_for_line(VIZ_list_for_D,'D') + create_coordinates_for_line(VIZ_list_for_D_curve,'D',1)

    coordinates = coordinates + coordinates_A + coordinates_R + coordinates_D
    # encode_viz(coordinates)
    with open('../data/viz_coordinates.json','w') as file:
        file.write(json.dumps(coordinates))
    print('finish')

main()