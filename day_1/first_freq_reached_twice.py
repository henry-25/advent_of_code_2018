def main():
    input_list = []
    with open('input.txt') as input_file:
        for line in input_file:
            input_list.append(int(line))
        
    prev_freq = [0]
    repeat = True
    curr_value = 0

    while(repeat):
        for entry in input_list:
            if(curr_value in prev_freq):
                print(curr_value)
                repeat = False
            if(curr_value > 50000)
            prev_freq.append(prev_freq[len(prev_freq) - 1] + entry)
            print('Running')

    seen = set()
    uniq = []
    for x in prev_freq:
        if x not in seen:
            uniq.append(x)
            seen.add(x)
        else: 
            print(x)

    # print(prev_freq)

    # totals_reached = [0]
    # # tmp_array = []
    # curr_total = 0
    # i = 0
    # while i < len(input_list):
    #     curr_total += int(input_list[i])
    #     if(curr_total in totals_reached):
    #         i = len(input_list) + 1
    #     totals_reached.append(curr_total)
    # #     tmp_array.append(curr_total)
    #     i += 1
    #     if(i == len(input_list)):
    #         i = 0
    #         for i in totals_reached:
    #             if i < (curr_total - 227):
    #                 totals_reached.remove(i)
    #         print(len(totals_reached))
    #         print('Rerun')

    # print(prev_freq)

if __name__ == "__main__":
    main()