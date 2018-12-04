def main():
    with open('input.txt') as input_file:
        for i, line in enumerate(input_file):
            with open('input.txt') as tmp_file:
                for x in xrange(i):
                    tmp_file.next()
                for line in tmp_file:
                    


if __name__ == "__main__":
    main()