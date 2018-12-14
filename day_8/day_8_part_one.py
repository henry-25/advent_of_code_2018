import sys

def main():

    sys.setrecursionlimit(15000)

    entries = []

    with open('input.txt') as input_file:
        for line in input_file:
            entries = line.split(' ')

    for i in range(len(entries)):
        entries[i] = int(entries[i])
    
    # entries[0] is number of child nodes 
    # entries[1] is the quantity of metadata entries

    # total, value, remaining = parse(entries)

    # print('part 1:', total)
    # print('part 2:', value)

    print(getMetadataSum(entries))

def getMetadataSum(entries):
    print(entries)
    num_children, num_metadata_entries = entries[:2]
    entries = entries[2:]
    all_total = 0

    for i in range(num_children):
        child_total, entries = getMetadataSum(entries)
        all_total += child_total

    all_total += sum(entries[:num_metadata_entries])

    if num_children == 0:
        return (all_total, entries[num_metadata_entries:]) 
    else:
        return (all_total, entries[num_metadata_entries:])

if __name__ == "__main__":
    main()