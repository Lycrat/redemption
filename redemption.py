# list comprehension
powers = [x**x for x in range(5)]

#Unicode chars
unicode_str = "\u2665"

#String splitting
welcome_panya = "hello panya"
arr_welcome_panya = welcome_panya.split()

#String splicing
welcome_bryan = "hello bryan"
sliced_welcome_bryan = welcome_bryan[:5]

#String methods
name = "Osterley"
name_scream = name.upper()

#Functions
def eat(name: str = "chocolate") -> str:
    return f"I want some {name}, miam miam..."

if __name__ == "__main__":
    print(powers)
    print(unicode_str)
    print(welcome_panya)
    print(arr_welcome_panya)
    print(eat())