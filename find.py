def find_specific_cgg(filename):
    valid_positions = []

    with open(filename, 'r') as file:
        content = file.read()

        index = content.find('cgg')
        while index != -1:
            # Check the condition
            if index + 3 == len(content) or content[index + 3] != 't':
                valid_positions.append(index)
            index = content.find('cgg', index+1)

    return valid_positions

filename = "newprotein.txt"

positions = find_specific_cgg(filename)
if positions:
    print(f"'cgg' found at valid positions:", positions)
else:
    print(f"No valid 'cgg' sequences were found in the file.")

def count_specific_cgg(filename):
    count = 0

    with open(filename, 'r') as file:
        content = file.read()

        index = content.find('cgg')
        while index != -1:
            # Check the condition
            if index + 3 == len(content) or content[index + 3] != 't':
                count += 1
            index = content.find('cgg', index+1)

    return count

filename = "newprotein.txt"

cgg_count = count_specific_cgg(filename)
print(f"Number of valid 'cgg' sequences found: {cgg_count}")
