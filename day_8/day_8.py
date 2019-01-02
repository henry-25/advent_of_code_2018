import sys

def main():

    entries = []

    with open('input.txt') as input_file:
        for line in input_file:
            entries = line.split(' ')

    for i in range(len(entries)):
        entries[i] = int(entries[i])

    print(getMetadataSum(entries))

def getMetadataSum(entries):
    num_children, num_metadata_entries = entries[:2]
    entries = entries[2:]
    scores = []
    all_total = 0

    for i in range(num_children):
        child_total, score, entries = getMetadataSum(entries)
        all_total += child_total
        scores.append(score)

    all_total += sum(entries[:num_metadata_entries])

    if num_children == 0:
        return (all_total, sum(entries[:num_metadata_entries]),entries[num_metadata_entries:]) 
    else:
        return (
            all_total,
            sum(scores[k - 1] for k in entries[:num_metadata_entries] if k > 0 and k <= len(scores)), 
            entries[num_metadata_entries:]
        )

if __name__ == "__main__":
    main()