
class Matrix:
    def __init__(self, data):
        if not all(len(row) == len(data[0]) for row in data):
            raise ValueError("All rows must have the same number of columns.")
        self.data = data

    def __add__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrices must have the same dimensions for addition.")
        return Matrix([
            [self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))]
            for i in range(len(self.data))
        ])

    def __sub__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrices must have the same dimensions for subtraction.")
        return Matrix([
            [self.data[i][j] - other.data[i][j] for j in range(len(self.data[0]))]
            for i in range(len(self.data))
        ])

    def __repr__(self):
        return f"Matrix({self.data})"
