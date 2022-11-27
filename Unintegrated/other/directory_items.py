import os


def get_files_from_dataset(file_type):
    path = 'audio/dataset/'
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file[-3:] == file_type:
                file_list.append(os.path.join(root, file))
    return file_list


file_list = get_files_from_dataset('txt')

# print(f'all files from: {path}')
# for file in file_list:
#     print(file)

# open text file and read it and save to data
with open(file_list[0], 'r') as file:
    data = file.readlines()

# remove \n
data = [i.strip() for i in data]

print('value of the first text')
print(data)
