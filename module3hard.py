def calculate_structure_sum(input_list):
    sum = 0
    for item in input_list:
        if isinstance(item, list):
            sum += calculate_structure_sum(item)
        elif isinstance(item, tuple):
            sum += calculate_structure_sum(item)
        elif isinstance(item, dict):
            for value in item.values():
                if isinstance(value, dict):
                    sum += calculate_structure_sum(value)
                else:
                    sum += value
            for key in item.keys():
                if isinstance(key, dict):
                    sum += calculate_structure_sum(key)
                else:
                    sum += int(len(key))
        elif isinstance(item, (int, float)):
            sum += item
        elif isinstance(item, str):
            sum += int(len(item))
        else:
            sum += calculate_structure_sum(item)

    return sum



data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(calculate_structure_sum(data_structure))

print(*data_structure)

