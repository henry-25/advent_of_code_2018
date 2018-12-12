import pprint

def main():
    collect_data = []
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

    new_dict = {}
    for k in sorted(step_prequisites, key=lambda k : len(step_prequisites[k])):
        # print(k, ord(k) - 4)
        new_dict[k] = {'time' : (ord(k) - 4), 'step_pre' :  step_prequisites[k]}

    with open('dict.txt', 'a') as f:
        print(new_dict, file=f)

    workers_available = 5
    seconds_passed = 0
    current_steps = []
    steps_done = []

    while len(new_dict):
        # If workers available assign them a task
        if(workers_available):
            steps_available_to_complete = []

            # Sort the array and any steps without prequisites are available to be completed
            for k in new_dict:
                if len(new_dict[k]['step_pre']) == 0 and not k in current_steps:
                    steps_available_to_complete.append(k)

            # If there are steps available to complete sort them to find the first one alphabetically
            if(steps_available_to_complete):
                steps_available_to_complete = sorted(steps_available_to_complete)

                # print('Steps available to complete', steps_available_to_complete)

                # While there are still workers available and steps to complete assign a worker to the step, 
                # remove it from the available steps, reduce the number of available workers, add the step to the currently being worked on steps
                while workers_available and len(steps_available_to_complete) > 0:
                    workers_available -= 1
                    step_working_on = steps_available_to_complete[0]
                    steps_available_to_complete.remove(step_working_on)
                    current_steps.append(step_working_on)

        # print('New dict:', new_dict)
        # print('Current steps:', current_steps)
        
        with open('file_output.txt', 'a') as f:
            print((seconds_passed, current_steps, steps_done), file=f)

        # For each step currently being worked on reduce the time remaining by one second
        for i in current_steps:
            new_dict[i]['time'] -= 1
            # If step is completed, remove it from the current steps, remove it from the available steps to work on,
            # increment the number of available workers, remove step from preq of previous steps
            if new_dict[i]['time'] == 0:
                current_steps.remove(i)
                new_dict.pop(i)
                steps_done.append(i)
                workers_available += 1

                for k in new_dict:
                    if i in new_dict[k]['step_pre']:
                        new_dict[k]['step_pre'].remove(i)
                        
        seconds_passed += 1

    print(seconds_passed)

    # answer = ''

    # while len(step_prequisites):
    #     array_least_required = []
    #     curr_len = 999
    #     for k in sorted(step_prequisites, key=lambda k : len(step_prequisites[k])):
    #         if len(step_prequisites[k]) < curr_len:
    #             curr_len = len(step_prequisites[k])
        
    #     for k in step_prequisites:
    #         if len(step_prequisites[k]) == curr_len:
    #             array_least_required.append(k)

    #     array_least_required = sorted(array_least_required)
    #     value_removed = array_least_required[0]

    #     for k in step_prequisites:
    #         if value_removed in step_prequisites[k]:
    #             step_prequisites[k].remove(value_removed)
        
    #     step_prequisites.pop(value_removed)
    #     answer += value_removed

    # print(answer)

if __name__ == "__main__":
    main()