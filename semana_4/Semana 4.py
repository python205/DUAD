

my_variable = 3
my_other_variable3 = "My name is Jeff"

print (my_variable, my_other_variable3)

my_int = 5
my_other_int = 8
result = my_int + my_other_int
print (result)


my_float = 3.14
my_other_float = 8.23
result = my_float + my_other_float
print (result)

my_string = "Este es un string"
my_multiline_string = """
Este
es
un
string
de
multiples
"""

print(my_string)
print('Este es un string')
print(my_multiline_string)

other_string = "Bond"
concatenated_string = "My name is " + other_string
print(concatenated_string)

other_string2 = "Bond"
f_string = f"My name is {other_string2}"
print(f_string)

other_string = 'Bond'
template_string = 'My name is {name}'
formatted_string = template_string.format(name=other_string)

print(formatted_string)

my_false_boolean = False
my_true_boolean = True

print(my_false_boolean)
print(my_true_boolean)


my_first_list = [2, 5, 7, 8]

print(my_first_list[1])
print(my_first_list)

my_list = ["tent", "bag", "bed"]
print(my_list[1])

my_first_tuple = (2, 5, 7, 8)
print(my_first_tuple[1])

my_first_dictionary = {
	"key": 5,
	"other_key": "Hello again!",
	"final_key": 98,
}

print(my_first_dictionary["other_key"])

condo_houses = [
	{
		"number": 93,
		"area_m2": 125,
		"rooms": [
			"living_room",
			"kitchen",
			"main_sleeping_room",
			"second_sleeping_room",
			"bathroom",
		],
	},
	{
		"number": 95,
		"area_m2": 125,
		"rooms": [
			"living_room",
			"kitchen",
			"main_sleeping_room",
			"second_sleeping_room",
			"third_sleeping_room",
			"bathroom",
		],
	},
]

print(condo_houses[1]['rooms'][4])
