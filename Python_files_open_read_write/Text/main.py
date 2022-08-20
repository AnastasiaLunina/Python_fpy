import os

base_path = os.getcwd()
path_first = '1.txt'
path_second = '2.txt'
path_third = '3.txt'
full_path_first = os.path.join(base_path, path_first)
full_path_second = os.path.join(base_path, path_second)
full_path_third = os.path.join(base_path, path_third)

with open('1.txt', 'r', encoding='utf-8') as f:
    file_1 = f.readlines()

with open('2.txt', 'r', encoding='utf-8') as f:
    file_2 = f.readlines()

with open('3.txt', 'r', encoding='utf-8') as f:
    file_3 = f.readlines()

max_len = (len(file_1), len(file_2), len(file_3))
print(max_len)

with open('combined.txt', 'w', encoding='utf-8') as f_combined:
    f_combined.write('This is a first article' + '\n')
    f_combined.write('Total lines: ' + str(len(file_1)) + '\n')
    f_combined.writelines(file_1)
    f_combined.write('\n')

with open('combined.txt', 'a', encoding='utf-8') as f_combined:
    f_combined.write('This is a second article' + '\n')
    f_combined.write('Total lines: ' + str(len(file_2)) + '\n')
    f_combined.writelines(file_2)
    f_combined.write('\n')
    f_combined.write('\n')

with open('combined.txt', 'a', encoding='utf-8') as f_combined:
    f_combined.write('This is a third article' + '\n')
    f_combined.write('Total lines: ' + str(len(file_3)) + '\n')
    f_combined.writelines(file_3)
    f_combined.write('\n')



