def check_match(input_list, target_list):
    for sublist in target_list:
        if all(item in input_list for item in sublist):
            return True
    return False

# Example usage:
list_2d = [[(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)]]
input_tuples = [(1, 1), (1, 2), (0, 1), (1, 0)]

if check_match(input_tuples, list_2d):
    print("Match found!")
else:
    print("No match found.")