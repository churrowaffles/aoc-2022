from ast import literal_eval

def main(file):
    signal = parse_file(file)
    sum_of_indices = 0

    # Iterate through the list of packets to compare each pair
    for index, packets in enumerate(signal):
        if compare_elements(packets[0], packets[1]):
            sum_of_indices += index + 1
    print("Part 1:", sum_of_indices)


def parse_file(text):
    # Parse input into an ordered list of packets pair
    # Each element of the list should contain 2 list (both packets) - first/left/A + second/right/B
    with open(text, 'r') as file:
        signal = file.read().split('\n\n')
        signal = [line.split('\n') for line in signal]

    # Convert string input to lists
    for i in range(len(signal)):
        a, b = signal[i][0], signal[i][1]
        signal[i][0], signal[i][1] = literal_eval(a), literal_eval(b)
    return signal


def compare_elements(a, b):
    '''
    If both are integers, if A < B = True || A > B = False; continue comparison if values are the same
    If one is integer and the other is list, convert integer into a list with single element
    If both are lists, recursively call this function to compare their elements
      - If List A runs out before conclusion, it is in the right order
      - If List B runs out before conclusion, it is in the wrong order
    '''
    
    i = 0
    while i < max(len(a), len(b)):
        try:
            if isinstance(a[i], int) and isinstance(b[i], int):
                if a[i] > b[i]:
                    return False
                if a[i] < b[i]:
                    return True
                i += 1
                continue
            
            if isinstance(a[i], int):
                a[i] = [a[i]]

            elif isinstance(b[i], int):
                b[i] = [b[i]]
                
            check_inner_list = compare_elements(a[i], b[i])
            if check_inner_list is not None:
                return check_inner_list
            i += 1
                
        except IndexError:
            return len(a) < len(b)
    


main('day13.txt')