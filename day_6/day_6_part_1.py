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

    matrix = [[(0, 999) for x in range(maxX + 2)] for y in range(maxY + 2)]

    for point in coordinates:
        for x in range(maxX + 2):
            for y in range(maxY + 1):
                mDistance = getManhattenDistance(point, (x, y))
                if(mDistance == matrix[x][y][1]):
                    matrix[x][y] = ('.', mDistance)
                if(mDistance < matrix[x][y][1]):
                    matrix[x][y] = (str(point[0]) + '*', mDistance)

    # matrix = matrix[:][:-1]

    infiniteAreaArrays = set('.')

    for x in range(maxX + 2):
        for y in range(maxY + 1):
            if(x == 0 or y == 0 or x == maxX + 1 or y == maxY):
                try:
                    infiniteAreaArrays.add(matrix[x][y][0])
                except:
                    print(x, y)

    areasNonInfinite = dict()

    for x in range(maxX + 2):
        for y in range(maxY + 1):
            try:
                if not matrix[x][y][0] in infiniteAreaArrays:
                    try:
                        areasNonInfinite[matrix[x][y][0]] += 1
                    except:
                        areasNonInfinite[matrix[x][y][0]] = 1
            except:
                print(x, y)


    print(areasNonInfinite)
    # print(matrix[0])
    # print(matrix[357])
    # print(infiniteAreaArrays)
    # print(matrx[][0])
    # print(matrix[][357])
    


def getManhattenDistance(startingPoint, desiredPoint):
    return abs(startingPoint[1] - desiredPoint[0]) + abs(startingPoint[2] - desiredPoint[1])

if __name__ == "__main__":
    main()