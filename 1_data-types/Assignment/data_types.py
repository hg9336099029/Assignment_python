
"""
data_types.py

Simple, clear examples and short comments for common Python data types.
"""

# Classification: primitive vs non-primitive
# Primitive: int, float, complex, bool, str, bytes, None
# Non-primitive: list, tuple, range, set, dict

def _show(name, val):
	print(f"{name}: {repr(val)} -> {type(val).__name__}")


# Numeric types
int_var = 42
float_var = 3.14
complex_var = 1 + 2j

# Text and boolean
str_var = "Hello, world!"
bool_var = True

# Sequences
list_var = [1, 2, 3]
tuple_var = (1, 2, 3)
range_var = range(5)

# Set and mapping
set_var = {1, 2, 3}
dict_var = {"a": 1, "b": 2}

# Special types
none_var = None
bytes_var = b"abc"


if __name__ == "__main__":
	items = [
		("int", int_var),
		("float", float_var),
		("complex", complex_var),
		("str", str_var),
		("bool", bool_var),
		("list", list_var),
		("tuple", tuple_var),
		("range", range_var),
		("set", set_var),
		("dict", dict_var),
		("none", none_var),
		("bytes", bytes_var),
	]

	print("Python data types demo:\n")
	for name, val in items:
		_show(name, val)

	# Small, practical examples
	print("\nTuple unpacking:")
	a, b, c = tuple_var
	print(a, b, c)

	print("\nSwapping using tuple assignment:")
	x, y = 1, 2
	print("before:", x, y)
	x, y = y, x
	print("after:", x, y)

	print("\nMutability demo:")
	print("original list:", list_var)
	list_var.append(4)
	print("after append:", list_var)
	try:
		tuple_var[0] = 0
	except TypeError as exc:
		print("tuple immutability:", exc)

	print("\nConversions:")
	print("list(tuple):", list(tuple_var))
	print("tuple(list):", tuple(list_var))
	print("set(list):", set(list_var))



