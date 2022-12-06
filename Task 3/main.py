# Turimas "audi" dict.

# Parašykite funkciją "showObjectKeys", kuri kaip argumentą priims objektą 
# ir grąžins visus jo "values" list'e.

audi = {
    "make": 'audi',
    "model": 'A6',
    "year": 2005,
    "color": 'white',
}


def show_object_keys(dictionary):
    """Function takes dictionary and returns its values in a list."""
    return [value for key, value in dictionary.items()]
