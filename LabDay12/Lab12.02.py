# 02. Write a program that implements a Matrix class and performs addition, multiplication and transpose operations on 3x3 matrices.

class Matrix:
    def __init__(self, data):
        if len(data) != 3 or any(len(row) != 3 for row in data):
            raise ValueError("Only 3x3 matrices are supported.")
        self.data = data

    def get_matrix_input(matrix_num):
        print(f"\nEnter elements for Matrix {matrix_num} (3x3):-")
        matrix = []
        for i in range(3):
            row = list(map(int, input(f"Row {i+1} (space-separated 3 integers): ").split()))
            if len(row) != 3:
                raise ValueError("Each row must contain exactly 3 integers.")
            matrix.append(row)
        return Matrix(matrix)    

    def display(self):
        for row in self.data:
            print(row)

    def add(self, other):
        result = [[self.data[i][j] + other.data[i][j] for j in range(3)] for i in range(3)]
        return Matrix(result)

    def multiply(self, other):
        result = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)

    def transpose(self):
        result = [[self.data[j][i] for j in range(3)] for i in range(3)]
        return Matrix(result)


# Main Program
try:
    matrix1 = Matrix.get_matrix_input(1)
    matrix2 = Matrix.get_matrix_input(2)

    print("\nMatrix 1:")
    matrix1.display()

    print("\nMatrix 2:")
    matrix2.display()

    # Addition
    print("\nAddition of Matrix 1 and Matrix 2:")
    matrix1.add(matrix2).display()

    # Multiplication
    print("\nMultiplication of Matrix 1 and Matrix 2:")
    matrix1.multiply(matrix2).display()

    # Transpose
    print("\nTranspose of Matrix 1:")
    matrix1.transpose().display()

except ValueError as e:
    print("Error:", e)