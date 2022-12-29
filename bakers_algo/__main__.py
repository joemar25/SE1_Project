# total matrix is given
# process. allocation matrix. max need matrix. are also given

import numpy as np


def str_fix(a_string):
    a_string = str(a_string)
    for character in '[,]':
        a_string = a_string.replace(character, '')

    return a_string


def display_matrix(array) -> None:
    '''
        ### Displaying Array of Processes
        - requires 1 parameter which is the array
        - get that array
        - and display the array
    '''

    # processes display
    print('  id      alloc        max        avail        need')
    for data in array:
        id = data[0]
        allocated_matrix = data[1]
        max_need = data[2]
        available_matrix = data[3]
        need_matrix = data[4]

        # printing
        print(' ', id, '   ', str_fix(allocated_matrix), '   ', str_fix(max_need),
              '   ', str_fix(available_matrix), '   ', str_fix(need_matrix), '   ')


def get_total_allocation(array) -> object:
    # total allocation
    total_allocation = np.array(
        [0, 0, 0, 0],
        dtype=object,
        copy=False,
        order='K',
        subok=False,
        ndmin=0
    )
    for data in array:

        # get allocation matrix
        allocated_matrix = data[1]

        # get processes
        a = allocated_matrix[0]
        b = allocated_matrix[1]
        c = allocated_matrix[2]
        d = allocated_matrix[3]

        # calculate total allocation
        total_allocation[0] += a
        total_allocation[1] += b
        total_allocation[2] += c
        total_allocation[3] += d

    return total_allocation


def main():

    # total matrix (all of the process)
    total_matrix = np.array(
        [3, 17, 16, 12],
        dtype=object,
        copy=False,
        order='K',
        subok=False,
        ndmin=0
    )
    # all processes need to handle
    processes = np.array(
        [
            # ['id', [allocation matrix], [max need matrix], [available matrix], [need matrix]]
            ['P1', [0, 1, 1, 0], [0, 2, 1, 0], [0, 22, 0, 0], [0, 0, 0, 0]],
            ['P2', [1, 2, 3, 1], [1, 6, 5, 2], [0, 0, 0, 0], [0, 0, 0, 0]],
            ['P3', [1, 3, 6, 5], [2, 3, 6, 6], [0, 0, 0, 0], [0, 0, 0, 0]],
            ['P4', [0, 6, 3, 2], [0, 6, 5, 2], [0, 0, 0, 0], [0, 0, 66, 0]],
            ['P5', [0, 0, 1, 4], [0, 6, 5, 6], [0, 0, 0, 0], [0, 0, 0, 0]],
        ],
        dtype=object,
        copy=False,
        order='K',
        subok=False,
        ndmin=0
    )

    # total allocation
    total_allocation = np.array(
        get_total_allocation(processes),
        dtype=object,
        copy=False,
        order='K',
        subok=False,
        ndmin=0
    )

    # max - alloc = need
    for data in processes:

        # get allocation matrix
        allocated_matrix = data[1]
        # get max matrix
        max_need = data[2]

        # set need matrix
        data[4] = np.subtract(max_need, allocated_matrix)

    # initialized available matrix from total available matrix minus total allocation
    init_available_matrix = np.subtract(total_matrix, total_allocation)
    processes[0][3] = init_available_matrix

    # disp
    display_matrix(processes)

    # TODO  bankers algo


if __name__ == "__main__":
    main()


# useful learning materials
# numpy       - https://numpy.org/doc/stable/reference/generated/numpy.array.html
# numpy array - https://www.geeksforgeeks.org/python-numpy/
# numpy array - https://www.educba.com/numpy-arrays/
