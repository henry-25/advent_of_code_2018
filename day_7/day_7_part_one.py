def main():
    # dict of each step with array of its prequisites
    step_prequisites = {}
    with open('input.txt') as input_file:
        for line in input_file:
            line_split = line.split(' ')
            try :
                step_prequisites[line_split[7]].append(line_split[1])
            except :
                step_prequisites[line_split[7]] = [line_split[1]]
            if(not line_split[1] in step_prequisites):
                step_prequisites[line_split[1]] = []

    answer = ''

    while len(step_prequisites):
        array_least_required = []
        curr_len = 999
        for k in sorted(step_prequisites, key=lambda k : len(step_prequisites[k])):
            if len(step_prequisites[k]) < curr_len:
                curr_len = len(step_prequisites[k])
        
        for k in step_prequisites:
            if len(step_prequisites[k]) == curr_len:
                array_least_required.append(k)

        array_least_required = sorted(array_least_required)
        value_removed = array_least_required[0]

        for k in step_prequisites:
            if value_removed in step_prequisites[k]:
                step_prequisites[k].remove(value_removed)
        
        step_prequisites.pop(value_removed)
        answer += value_removed

    print(answer)

if __name__ == "__main__":
    main()