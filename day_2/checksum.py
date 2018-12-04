def main():
    num_two = 0
    num_three = 0
    with open('input.txt') as input_file:
        for line in input_file:
            letter_freq = dict()
            two_occurred = False
            three_occurred = False
            for letter in line:
                try:
                    letter_freq[letter] = letter_freq[letter] + 1

                except:
                    letter_freq[letter] = 1
            for key in letter_freq:
                if(letter_freq[key] == 2 and not two_occurred):
                    num_two += 1
                    two_occurred = True
                if(letter_freq[key] == 3 and not three_occurred):
                    num_three += 1
                    three_occurred = True
    print(num_two * num_three)

if __name__ == "__main__":
    main()