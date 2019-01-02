import math, pprint

class four_dim_point: 
    def __init__(self, new_x, new_y, new_z, new_t):
        self.x_coord = new_x
        self.y_coord = new_y
        self.z_coord = new_z
        self.t_coord = new_t

    def __str__(self):
        return '(' + str(self.x_coord) + ', ' + str(self.y_coord) + ', ' + str(self.z_coord) + ', ' + str(self.t_coord) + ')'

    def calc_manhatten_distance(self, other_point):
        x_accum = abs(self.x_coord - other_point.x_coord)
        y_accum = abs(self.y_coord - other_point.y_coord)
        z_accum = abs(self.z_coord - other_point.z_coord)
        t_accum = abs(self.t_coord - other_point.t_coord)
        return (x_accum + y_accum + z_accum + t_accum)

def main():
    coordinates_list = list()
    constellation_list = dict()
    num_constellations = 1

    with open('input_example_2.txt') as input_file:
        for line in input_file:
            coordinates = [int(coord.strip()) for coord in line.split(',')]
            adding = four_dim_point(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
            coordinates_list.append(adding)

    for new_coord in coordinates_list:
        const_added_too = list() #If 1 added to one constellation, if greater than 1 added to two constellation (a linking coordinate, we need to join the two or more constellations)
        for key in constellation_list.keys():
            print('New coord:', new_coord, 'Key:', key)
            for i in constellation_list[key]:
                print(i)
            print(type(constellation_list[key]), 'length', len(constellation_list[key]))
            for exist_coord in constellation_list[key]:
                print('Comparing exist_coord:', exist_coord, 'to', new_coord, 'has manhatten distance', exist_coord.calc_manhatten_distance(new_coord))
                if(exist_coord.calc_manhatten_distance(new_coord)) < 4:
                    print('Adding', new_coord, 'to', exist_coord)
                    constellation_list[key].append(new_coord)
                    const_added_too.append(key)
                break
        # Create a new constellation if there isn't one to add to
        if len(const_added_too) == 0:
            constellation_list[num_constellations] = [new_coord]
            num_constellations += 1
        # Combine multiple constellations
        elif len(const_added_too) > 1:
            constellation_list[num_constellations] = []
            for i in const_added_too:
                for coord in constellation_list[i]:
                    constellation_list[num_constellations].append(coord)
                # constellation_list[num_constellations].append(constellation_list[i])
                del constellation_list[i]
            num_constellations += 1
    
    # for key in constellation_list.keys():
    #     print(key, ':')
    #     for i in constellation_list[key]:
    #         print(i)
    #     print('\n')

    # print(coordinates_list[0])
    # print(coordinates_list[1])
    # print(coordinates_list[0].calc_manhatten_distance(coordinates_list[1]))

if __name__ == "__main__":
    main()