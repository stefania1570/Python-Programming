#ex 1: Write a Python class that simulates a Stack. The class should implement methods like push, pop, peek 
# (the last two methods should return None if no element is present in the stack).
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:", stack.items)

print("Pop:", stack.pop())
print("Stack after pop:", stack.items)

print("Peek:", stack.peek())

print("Is Empty:", stack.is_empty())
print("Stack size:", stack.size())

#ex 2: Write a Python class that simulates a Queue. The class should implement methods like push, pop, peek 
# (the last two methods should return None if no element is present in the queue).

class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

my_queue = Queue()
my_queue.push(1)
my_queue.push(2)
my_queue.push(3)

print(my_queue.pop())  # Output: 1
print(my_queue.peek())  # Output: 2
print(my_queue.pop())  # Output: 2
print(my_queue.pop())  # Output: 3
print(my_queue.pop())  # Output: None

#ex 3: Write a Python class that simulates a matrix of size NxM, with N and M provided at initialization. 
# The class should provide methods to access elements (get and set methods) and some methematical functions such as 
# transpose, matrix multiplication and a method that allows iterating through all elements form a matrix an apply a 
# transformation over them (via a lambda function).

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def get(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        else:
            raise IndexError("Index out of range")

    def set(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value
        else:
            raise IndexError("Index out of range")

    def transpose(self):
        transposed_matrix = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed_matrix.set(j, i, self.get(i, j))
        return transposed_matrix

    def matrix_multiply(self, other_matrix):
        if self.cols != other_matrix.rows:
            raise ValueError("Matrix dimensions are not compatible for multiplication")

        result_matrix = Matrix(self.rows, other_matrix.cols)
        for i in range(self.rows):
            for j in range(other_matrix.cols):
                dot_product = 0
                for k in range(self.cols):
                    dot_product += self.get(i, k) * other_matrix.get(k, j)
                result_matrix.set(i, j, dot_product)

        return result_matrix

    def apply_function(self, func):
        result_matrix = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result_matrix.set(i, j, func(self.get(i, j)))
        return result_matrix

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str

matrix1 = Matrix(2, 3)
matrix1.set(0, 0, 1)
matrix1.set(0, 1, 2)
matrix1.set(0, 2, 3)
matrix1.set(1, 0, 4)
matrix1.set(1, 1, 5)
matrix1.set(1, 2, 6)

print("Original matrix:")
print(matrix1)

# Transpose the matrix
transpose_matrix = matrix1.transpose()
print("Transposed matrix:")
print(transpose_matrix)


matrix2 = Matrix(3, 2)
matrix2.set(0, 0, 7)
matrix2.set(0, 1, 8)
matrix2.set(1, 0, 9)
matrix2.set(1, 1, 10)
matrix2.set(2, 0, 11)
matrix2.set(2, 1, 12)

print("Matrix 2:")
print(matrix2)

# Multiply
result_matrix = matrix1.matrix_multiply(matrix2)
print("Matrix multiplication result:")
print(result_matrix)

# lambda
transformed_matrix = matrix1.apply_function(lambda x: x * 2)
print("Transformed matrix:")
print(transformed_matrix)
