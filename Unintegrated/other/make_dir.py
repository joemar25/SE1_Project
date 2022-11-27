import os

# make a directory if it doesn't exist


def emptydir(directory):

    # if the given directory is empty then return
    if(not (directory and not directory.isspace())):
        return

    # save path if the direcory contains mode than one folder
    path = ''
    for dir in directory.split('/'):
        path += dir+'/'
        if os.path.isdir(path) == False:
            os.mkdir(path)


PATH = 'a/b'

# create directory mar if not exit
# emptydir(PATH)


# Get the canonical path
# of the specified path
# by eliminating any symbolic links
# encountered in the path
real_path = os.path.realpath(PATH)

# Print the canonical path
print(real_path)
