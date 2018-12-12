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

    print(getMetadataSum(entries))


def getMetadataSum(entries):
    if(len(entries) == 0):
        return 0
    if(entries[0] == 0):
        # print('Metadata entries', entries)
        numMetaData = entries[1]
        metadataSum = 0
        for i in entries[2:2 + entries[1]]:
            metadataSum += i
        return metadataSum + getMetadataSum(entries[2 + numMetaData:])
    else:
        entries[0] = 0
        # print('Entries', entries)
        child_array = entries[2:len(entries) - entries[1]]
        parent_array = entries[:2] + entries[len(entries) - entries[1]:]
        # print('Child', child_array)
        # print('Parent', parent_array)
        return getMetadataSum(child_array) + getMetadataSum(parent_array) 


if __name__ == "__main__":
    main()