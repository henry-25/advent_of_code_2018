import sys

def main():
    input_string = ''
    with open('input.txt') as input_file:
        for line in input_file:
            input_string = line

    unit_types = []
    lowercase_all = input_string.lower()
    j = 0
    while j < len(lowercase_all) - 1:
        if not (lowercase_all[j], lowercase_all[j].swapcase()) in unit_types:
            unit_types.append((lowercase_all[j], lowercase_all[j].swapcase()))
        j += 1

    reduced_strings = []

    for unit in unit_types:
        print(unit)
        (t_string, t_string_len) = reduce_string_without_unit(unit, input_string)
        print(t_string_len)
        reduced_strings.append((t_string_len, unit[0]))
        # print(t_string)
        # print(t_string_len)

    print(reduced_strings)

def reduce_string_without_unit(unit, input_string):
    k = 0
    tmp_string = input_string.replace(unit[0], '').replace(unit[1], '')
    while k < len(tmp_string) - 1:
        if(tmp_string[k] == tmp_string[k+1].swapcase()):
            tmp_string = tmp_string[:k] + tmp_string[k+2:]
            k = 0
        else:
            k += 1
    return(tmp_string, len(tmp_string))


    
    # print(unit)
    # print(input_string)

    # final_answer = ''
    # i = 0
    # while i < len(input_string) - 2:
    #     if(input_string[i] == input_string[i+1].swapcase()):
    #         input_string = input_string[:i] + input_string[i+2:]
    #         i = 0
    #     else:
    #         i += 1
    # print(input_string)
    # print(len(input_string))

#     final_answer = eliminate_polarities(input_string)
#     print(final_answer)


# def eliminate_polarities(input_string):
#     if(len(input_string) == 1):
#         return ''
#     # print(input_string[0], input_string[1].swapcase())
#     if(input_string[0] == input_string[1].swapcase()):
#         return eliminate_polarities(input_string[1:])
#     else:
#         return input_string[0] + input_string[1] + eliminate_polarities(input_string[1:])

if __name__ == "__main__":
    main()