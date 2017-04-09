def fix_filenames(folder):
    import os
    folder = os.getcwd() + '/' + folder
    os.chdir(folder)
    name_list = os.listdir(folder)
    new_names = []

    for name in name_list:
        split_name = name.split('-')
        new_name = name
        extension = name.split('.')[1]

        if len(split_name) == 3 and extension == 'mp3' \
                and split_name[0].isdigit():
            new_name = split_name[2][:-4] + '-' + split_name[1] + '.mp3'
        new_names.append(new_name)

    index = 0
    for file in name_list:
        os.rename(file, new_names[index])
        index += 1
