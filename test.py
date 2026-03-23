# --- Basic Python Examples ---

# 1. Hello World
print("Hello, Python!")

# 2. Variables and Types
name = "World"  # String
age = 25        # Integer
height = 5.9    # Float
is_learning = True  # Boolean

# 3. Basic Arithmetic
sum_val = 10 + 5
product = 10 * 2
division = 10 / 2

# 4. Lists and Loops
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(f"Number: {num}")

# 5. List Comprehension (Advanced but common)
squares = [x**2 for x in numbers]
print(f"Squares: {squares}")

# 6. Functions
def greet(person):
    return f"Hello, {person}!"

print(greet("Alice"))
