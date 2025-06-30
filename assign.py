# Python Data Types: Syntax, Documentation, and Usage

# -----------------------------
# 1. STRING
# -----------------------------

# Syntax
s1 = "Hello"
s2 = 'World'
s3 = '''Multiline\nString'''
s4 = """Another multiline
example"""
s5 = str(123)  # Convert number to string

# Documentation:
# - Type: str
# - Strings are immutable sequences of Unicode characters.
# - Enclosed using single (' '), double (" "), or triple quotes (''' ''' or """ """).
# - Strings support indexing and slicing.
# - Strings can be concatenated and repeated using + and *.

# Usage:
message = "  Hello Python  "
print(message.strip().upper())   # Output: HELLO PYTHON
print(message[2:7])              # Output: Hello
print("Py" + "thon")             # Output: Python
print("Hi! " * 3)                # Output: Hi! Hi! Hi!

# Common methods:
# .lower(), .upper(), .find(), .replace(), .split(), .strip(), .count(), .startswith(), .endswith()


# -----------------------------
# 2. LIST
# -----------------------------

# Syntax
my_list = [1, 2, 3, "apple", True]
nested_list = [[1, 2], [3, 4]]
empty_list = list()
from_range = list(range(5))

# Documentation:
# - Type: list
# - Ordered, mutable collection of items.
# - Supports mixed data types.
# - Can be nested.
# - Supports indexing, slicing, and iteration.

# Usage:
numbers = [4, 2, 9]
numbers.append(5)           # Add an element at the end
numbers.sort()              # Sorts the list in-place
print(numbers)              # Output: [2, 4, 5, 9]
numbers.insert(1, 10)       # Insert 10 at index 1
print(numbers[::2])         # Slicing with step

# Common methods:
# .append(), .insert(), .remove(), .pop(), .sort(), .reverse(), .extend(), .index(), .count(), len()


# -----------------------------
# 3. TUPLE
# -----------------------------

# Syntax
my_tuple = (10, 20, 30)
single_element = (5,)  # Comma is required for single-item tuples
converted = tuple([1, 2, 3])

# Documentation:
# - Type: tuple
# - Ordered, immutable sequence of elements.
# - Can contain different types.
# - Supports indexing and slicing.
# - Can be used as dictionary keys if all elements are hashable.

# Usage:
coordinates = (10.5, 20.6)
x, y = coordinates           # Tuple unpacking
print(f"X = {x}, Y = {y}")  # Output: X = 10.5, Y = 20.6

# Tuple packing and unpacking
a = 1
b = 2
t = (a, b)
a2, b2 = t

# Built-in functions:
# len(), max(), min(), sum() (if elements are numeric)


# -----------------------------
# 4. SET
# -----------------------------

# Syntax
my_set = {1, 2, 3}
empty_set = set()  # {} creates an empty dictionary
set_from_list = set([1, 2, 2, 3])

# Documentation:
# - Type: set
# - Unordered, mutable collection of unique elements.
# - Does not allow duplicates.
# - Cannot contain mutable items like lists.
# - Very fast for membership testing.

# Usage:
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))        # Output: {1, 2, 3, 4, 5}
print(a & b)             # Output: {3} (intersection)
print(a - b)             # Output: {1, 2} (difference)
print(2 in a)            # Output: True

# Common methods:
# .add(), .remove(), .discard(), .union(), .intersection(), .difference(), .clear(), .copy(), len()


# -----------------------------
# 5. DICTIONARY
# -----------------------------

# Syntax
my_dict = {"name": "Alice", "age": 30}
empty_dict = dict()
built_dict = dict(name="John", age=25)

# Documentation:
# - Type: dict
# - Unordered collection of key-value pairs.
# - Keys must be unique and immutable.
# - Values can be any data type.
# - Fast lookups by key.

# Usage:
student = {"name": "John", "marks": 85}
print(student["name"])         # Output: John
student["grade"] = "A"          # Add a new key-value pair
print(student.get("age", 0))   # Output: 0 (default value if key not found)

# Iterating:
for key, value in student.items():
    print(f"{key}: {value}")

# Common methods:
# .get(), .keys(), .values(), .items(), .update(), .pop(), .clear(), .copy(), len()
