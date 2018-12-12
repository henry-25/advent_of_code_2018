def main():
    reached_frequencies = []
    curr_value = 0
    no_doubles = True
    first_double = None
    while no_doubles:
        with open('input.txt') as input_file:
            for line in input_file:
                print(curr_value)
                for i in reached_frequencies:
                    if i == curr_value and no_doubles:
                        no_doubles = False
                        first_double = curr_value
                reached_frequencies.append(curr_value)
                if(line[:1] == '+'):
                    curr_value += int(line[1:])
                else:
                    curr_value -= int(line[1:])
                # reached_frequencies.append(curr_value)
                # curr_value += int(line)

    print(first_double)

if __name__ == "__main__":
    main()