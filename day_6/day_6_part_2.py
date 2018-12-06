import pprint

def main():
    coordinates = []
    maxX = 0
    maxY = 0
    with open('input.txt') as file:
        for i, line in enumerate(file):
            tmp = line.split(',')
            coordinates.append((i, int(tmp[0]), int(tmp[1])))
            maxX = int(tmp[0]) if int(tmp[0]) > maxX else maxX
            maxY = int(tmp[1]) if int(tmp[1]) > maxY else maxY

    print(maxX, maxY)

    matrix = [[(0) for x in range(maxX + 2)] for y in range(maxY + 2)]

    for point in coordinates:
        for x in range(maxX + 2):
            for y in range(maxY + 1):
                mDistance = getManhattenDistance(point, (x, y))
                matrix[x][y] += mDistance

    under_points = []
    for x in range(maxX + 2):
        for y in range(maxY + 1):
            if(matrix[x][y] < 10000):
                under_points.append((x, y, matrix[x][y]))

    print(sorted(under_points, key=lambda x : x[2], reverse=True))
    print(len(under_points))


def getManhattenDistance(startingPoint, desiredPoint):
    return abs(startingPoint[1] - desiredPoint[0]) + abs(startingPoint[2] - desiredPoint[1])

if __name__ == "__main__":
    main()