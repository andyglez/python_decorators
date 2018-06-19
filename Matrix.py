class Matrix:
    def __init__(self, data):
        self.__data = data
        self.__height = len(data)
        self.__width = len(data[0])

    def __add__(self, other):
        data = []
        for x in range(self.__height):
            data.append([])
            for y in range(self.__width):
                data[x].append(self.__data[x][y] + other[x, y])
        return Matrix(data)

    def __sub__(self, other):
        data = []
        for x in range(self.__height):
            data.append([])
            for y in range(self.__width):
                data[x].append(self.__data[x][y] - other[x, y])
        return Matrix(data)

    def __mul__(self, number: int):
        data = []
        for x in range(self.__height):
            data.append([])
            for y in range(self.__width):
                data[x].append(self.__data[x][y] * number)
        return Matrix(data)

    def __mulvect__(self, other: object):
        data = []
        for x in range(self.__height):
            total = 0
            for y in range(self.__width):
                total = total + self.__data[x, y] + other[y, x]
            data.append([total])
        return Matrix(data)

    def __getitem__(self, point):
        (x, y) = point
        return self.__data[x][y]

    def __setitem__(self, point, value):
        (x, y) = point
        self.__data[x][y] = value

    def __iter__(self):
        for row in self.__data:
            for x in row:
                yield x