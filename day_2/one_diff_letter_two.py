def main():
    i = 0
    lines_array = []
    with open('input.txt') as input_file:
        for line in input_file:
            lines_array.append(line)
    
    for i, entry in enumerate(lines_array):
        j = i
        while j < len(lines_array):
            u = zip(entry, lines_array[j])
            num_diff = 0
            for k, l in u:
                if k != l:
                    num_diff += 1
            if (num_diff == 1):
                print(entry, lines_array[j])
            j += 1


if __name__ == "__main__":
    main()