def read_from_file(file_name, task_list):
    try:
        input_file = open("text_files\\" + file_name + ".txt", "r")
    except:
        print(file_name + ".txt couldn't be found, please make sure it exists in text_files directorty")
    else:
        for line in input_file:
            task_list.append(line.strip())
            #print("read line successfully")
        input_file.close()

def write_to_file(file_name, task_list):
    try:
        output_file = open("text_files\\" + file_name + ".txt", "w")
    except:
        print(file_name + ".txt couldn't be found, please make sure it exists in text_files directorty")
    else:
        for task in task_list:
            print(task, file = output_file)
            #print("wrote line successfully")
        output_file.close()

def add_to_list(task ,task_list):
    task_list.append(task)
    print("added task successfully")


def remove_from_list(task, task_list):
    if task in task_list: task_list.remove(task)
    print("removed task successfully")