def main():

    # Claim object should have four points top left, top right, bottom left, bottom right
    claims_array = []
    # Conflict array should list points where conflicts have occurred
    used_area_array = []

    largest_x = 5
    largest_y = 5

    with open('input.txt') as input_file:
        for line in input_file:
            tmp = {}
            rect_number = line[:line.index("@")]
            line = line[line.index("@") + 2:]
            line = line.split(':')
            upper_right = line[0].split(',') # upper_right[0] is dimension from left edge, upper_right[1] is dimension from top edge 
            width_height = line[1].split('x') # width_height[0] is width, width_height[1] is height
            tmp['rect_number'] = rect_number
            tmp['tlc'] = {'x': int(upper_right[0]), 'y': int(upper_right[1])}
            tmp['width'] = int(width_height[0])
            tmp['height'] = int(width_height[1])
            if (int(upper_right[0]) + int(width_height[0])) > largest_x:
                largest_x = int(upper_right[0]) + int(width_height[0])
            if (int(upper_right[1]) + int(width_height[1])) > largest_y:
                largest_y = int(upper_right[1]) + int(width_height[1])
            # # Each corner is a tuple (x, y)
            # tmp['upper_left'] = {'x': int(upper_right[0]), 'y': int(upper_right[1])}
            # tmp['upper_right'] = {'x': int(upper_right[0]) + int(width_height[0]), 'y': int(upper_right[1])}
            # tmp['bottom_left'] = {'x': int(upper_right[0]), 'y': int(upper_right[1]) + int(width_height[1])}
            # tmp['bottom_right'] = {'x': int(upper_right[0]) + int(width_height[0]), 'y': int(upper_right[1]) + int(width_height[1])}
            claims_array.append(tmp)

    matrix = [[0 for x in range(largest_x + 1)] for y in range(largest_y + 1)]

    for claim in claims_array:
        print(claim)
        for i in range(claim['tlc']['x'], claim['tlc']['x'] + claim['width']):
                for j in range(claim['tlc']['y'], claim['tlc']['y'] + claim['height']):
                        matrix[i][j] += 1

    count = 0
    for i in range(largest_x):
        for j in range(largest_y):
                if(matrix[i][j] > 1):
                        count += 1
        
    for claim in claims_array:
        b = True
        for i in range(claim['tlc']['x'], claim['tlc']['x'] + claim['width']):
                for j in range(claim['tlc']['y'], claim['tlc']['y'] + claim['height']):
                        if(matrix[i][j] != 1):
                                b = False
        if(b): 
                print(claim['rect_number'])
#     print(matrix)


#     count = 0

#     used_area_array.append(claims_array[0])
#     iterclaims = iter(claims_array)
#     next(iterclaims)
#     for claim in claims_array:
#         count += check_for_intersect(claim, used_area_array)

#     print(count)

# def check_for_intersect(claim, used_area_array):
#     for aca in used_area_array:
#         if(claim['tlc']['x'] > aca['tlc']['x'] and claim['tlc']['y'] > aca['tlc']['y']) or (claim['tlc']['x'] < aca['tlc']['x'] and claim['tlc']['y'] < aca['tlc']['y']):
#                 return 1
#         else:
#                 return 0

# def check_for_intersect(claim, other_claims):
#     for previously_used in other_claims:
#         if(claim['upper_left']['x'] < previously_used['upper_left']['x'] and claim['upper_left']['y'] < previously_used['upper_left']['y']):
#             if(claim['upper_right']['x'] > previously_used['upper_right']['x'] and claim['upper_right']['y'] < previously_used['upper_right']['y']):
#                 if(claim['bottom_left']['x'] < previously_used['bottom_left']['x'] and claim['bottom_left']['y'] > previously_used['bottom_left']['y']):
#                     if(claim['bottom_right']['x'] > previously_used['bottom_right']['x'] and claim['bottom_right']['y'] > previously_used['bottom_right']['y']):
#                         print(claim, 'Contains', previously_used)
    



if __name__ == "__main__":
    main()