# total matrix is given
# process. allocation matrix. max need matrix. are also given

import numpy as np

def display_matrix(array)-> None:
    
    '''
        ### Displaying Array of Processes
        - requires 1 parameter which is the array
        - get that array
        - and display the array
    '''
    
    # processes display
    print('  id          alloc            max           avail               need')
    for data in array:
        id = data[0]
        allocated_matrix = data[1]
        max_need = data[2]
        available_matrix = data[3]
        need_matrix = data[3]
        
        # printing
        print(' ', id, '   ' , allocated_matrix, '   ', max_need, '   ' , available_matrix, '   ' , need_matrix, '   ')
        
        a = allocated_matrix[0]
        
        print(a)

def main():
    
    # total matrix (all of the process)
    total_matrix = [3, 17, 16, 12]
    processes = [
        # ['id', [allocation matrix], [max need matrix], [available matrix], [need matrix]]
        ['P1', [0,1,1,0], [0,2,1,0],[0,0,0,0],[0,0,0,0]],
        ['P2', [1,2,3,1], [1,6,5,2],[0,0,0,0],[0,0,0,0]],
        ['P3', [1,3,6,5], [2,3,6,6],[0,0,0,0],[0,0,0,0]],
        ['P4', [0,6,3,2], [0,6,5,2],[0,0,0,0],[0,0,0,0]],
        ['P5', [0,0,1,4], [0,6,5,6],[0,0,0,0],[0,0,0,0]],
    ]
    
    # numpy array - https://www.educba.com/numpy-arrays/
    # numpy array - https://www.geeksforgeeks.org/python-numpy/
    array = np.array(
        processes,
        dtype=object,
        copy=False,
        order='K', 
        subok=False, 
        ndmin=0
    )

    # display
    # print("Numpy Array in python :", array)
    display_matrix(array)



if __name__ == "__main__":
    main()
    