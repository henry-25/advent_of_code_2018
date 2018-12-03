def main():

    # Claim object should have four points top left, top right, bottom left, bottom right
    claims_array = []
    # Conflict array should list points where conflicts have occurred
    used_area_array = []

    with open('input.txt') as input_file:
        for line in input_file:
            tmp = {}
            line = line[line.index("@") + 2:]
            line = line.split(':')
            upper_right = line[0].split(',') # upper_right[0] is dimension from left edge, upper_right[1] is dimension from top edge 
            width_height = line[1].split('x') # width_height[0] is width, width_height[1] is height
            # Each corner is a tuple (x, y)
            tmp['upper_left'] = {'x': int(upper_right[0]), 'y': int(upper_right[1])}
            tmp['upper_right'] = {'x': int(upper_right[0]) + int(width_height[0]), 'y': int(upper_right[1])}
            tmp['bottom_left'] = {'x': int(upper_right[0]), 'y': int(upper_right[1]) + int(width_height[1])}
            tmp['bottom_right'] = {'x': int(upper_right[0]) + int(width_height[0]), 'y': int(upper_right[1]) + int(width_height[1])}
            claims_array.append(tmp)

    for i, claim in enumerate(claims_array):
        # print(i)
        check_for_intersect(claim, claims_array[i:])


#     used_area_array.append(claims_array[0])
#     iterclaims = iter(claims_array)
#     next(iterclaims)
#     for claim in iterclaims:
#         print('Newly claimed:', claim)
#         check_for_intersect(claim, used_area_array)

def check_for_intersect(claim, other_claims):
    count = 0
    for j, c in enumerate(other_claims):
        print(j)
        count += 1
    print(count)



if __name__ == "__main__":
    main()