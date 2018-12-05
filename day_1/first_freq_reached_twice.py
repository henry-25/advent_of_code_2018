def main():
    input_list = []
    with open('input.txt') as input_file:
        for line in input_file:
            input_list.append(int(line))

    totals_reached = [0]
    # tmp_array = []
    curr_total = 0
    i = 0
    while i < len(input_list):
        curr_total += int(input_list[i])
        if(curr_total in totals_reached):
            i = len(input_list) + 1
        totals_reached.append(curr_total)
    #     tmp_array.append(curr_total)
        i += 1
        if(i == len(input_list)):
            i = 0
            for i in totals_reached:
                if i < (curr_total - 227):
                    totals_reached.remove(i)
            print(len(totals_reached))
            print('Rerun')

    print(curr_total)

if __name__ == "__main__":
    main()