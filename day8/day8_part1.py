filename = 'test'

if __name__ == "__main__":

    total_meta = 0
    current_node = 0
    current_subnodes = 0
    current_meta_data_entries = 0
    state = 'header'
    line = open(filename, 'r').readlines()
    numbers = line[0].split(' ')
    for number in numbers.__iter__():
        print (number)
        if state == 'header':
            current_subnodes = number
            current_meta_data_entries = numbers.next()
            if current_subnodes:
                state == ''
