import os

# path = "/Users/Bhupe/Downloads/P1/testdir
path = os.getcwd()
improper_path = "/Users//Bhupe/Downloads/P1//folder/dir"
non_existent_file = "/Users//Bhupe/Downloads/P1/testdir/A1.c"

print("Current Directory is:", path)
os.chdir(path)
recog_data = []


def find_files(path_directory):
    if not os.path.isfile(path_directory) and os.path.exists(path_directory):
        for file in os.listdir(path_directory):
            name = os.path.basename(file)
            if os.path.isdir(path_directory + '/' + file):
                find_files(path_directory + '/' + name)
            elif os.path.isfile(path_directory + '/' + file):
                if name.endswith('.c'):
                    recog_data.append(path_directory + '/' + name)

        return recog_data

    else:
        return 'Error: Not Found!'


print("\n", *find_files(path), sep='\n')  # Should find all the files ending with ".c"

print('\n' + find_files(improper_path))  # Should print error because path isn't proper

print(find_files(non_existent_file))  # Should print error because no such file as "A1.c" exists in the directory
