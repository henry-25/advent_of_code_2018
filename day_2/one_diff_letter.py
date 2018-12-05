def main():

    lines_array = []

    with open('input.txt') as input_file:
        for line in input_file:
            lines_array.append(line)

    lines_array = sorted(lines_array)

    first_half_array = []
    second_half_array = []

    for i in lines_array:
        first_half_array.append((i[:13].rstrip()))
        second_half_array.append((i[13:].rstrip()))

    one_diff_one_same = []

    for j in range(len(lines_array)):
        for k in range(j + 1, len(lines_array)):
            if(first_half_array[j] == first_half_array[k]):
                if(second_half_array[j] != second_half_array[k]):
                    one_diff_one_same.append((j, k, 2))
            else:
                if(second_half_array[j] == second_half_array[k]):
                    one_diff_one_same.append((j, k, 1))

    for pot_answer in one_diff_one_same:
        num_diff = 0
        if(pot_answer[2] == 1):
            for i in range(len(first_half_array[pot_answer[0]])):
                if first_half_array[pot_answer[0]]
            for char_outer in first_half_array[pot_answer[0]]:
                for char_inner in first_half_array[pot_answer[1]]:
                    print(char_inner, char_outer)
                    if(char_inner != char_outer):
                        num_diff += 1
                        
            if(num_diff == 1):
                print(pot_answer)
        if(pot_answer[2] == 2):
            for char_outer in second_half_array[pot_answer[0]]:
                for char_inner in second_half_array[pot_answer[1]]:
                    print(char_inner, char_outer)
                    if(char_inner != char_outer):
                        num_diff += 1
                        
            if(num_diff == 1):
                print(pot_answer)

    # print(one_diff_one_same)
    # print(len(one_diff_one_same))


if __name__ == "__main__":
    main()