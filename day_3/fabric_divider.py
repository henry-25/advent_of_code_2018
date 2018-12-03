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
            tmp['tlc'] = {'x': int(upper_right[0]), 'y': int(upper_right[1])}
            tmp['width'] = int(width_height[0])
            tmp['height'] = int(width_height[1])
            # # Each corner is a tuple (x, y)
            # tmp['upper_left'] = {'x': int(upper_right[0]), 'y': int(upper_right[1])}
            # tmp['upper_right'] = {'x': int(upper_right[0]) + int(width_height[0]), 'y': int(upper_right[1])}
            # tmp['bottom_left'] = {'x': int(upper_right[0]), 'y': int(upper_right[1]) + int(width_height[1])}
            # tmp['bottom_right'] = {'x': int(upper_right[0]) + int(width_height[0]), 'y': int(upper_right[1]) + int(width_height[1])}
            claims_array.append(tmp)

    used_area_array.append(claims_array[0])
    iterclaims = iter(claims_array)
    next(iterclaims)
    for claim in claims_array:
        check_for_intersect(claim, used_area_array)

def check_for_intersect(claim, used_area_array):
    for aca in used_area_array:
        if()

# def check_for_intersect(claim, other_claims):
#     for previously_used in other_claims:
#         if(claim['upper_left']['x'] < previously_used['upper_left']['x'] and claim['upper_left']['y'] < previously_used['upper_left']['y']):
#             if(claim['upper_right']['x'] > previously_used['upper_right']['x'] and claim['upper_right']['y'] < previously_used['upper_right']['y']):
#                 if(claim['bottom_left']['x'] < previously_used['bottom_left']['x'] and claim['bottom_left']['y'] > previously_used['bottom_left']['y']):
#                     if(claim['bottom_right']['x'] > previously_used['bottom_right']['x'] and claim['bottom_right']['y'] > previously_used['bottom_right']['y']):
#                         print(claim, 'Contains', previously_used)
    



if __name__ == "__main__":
    main()