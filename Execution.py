import Functions
import Construction
import Navigation
import time
def construction_from_list(task_list):
    sub_list = []
    for task in task_list:
        #Case 1, the command is for fields
        if "field" in task:
            field_no = task.split("_", 1)[1]
            success = Construction.field(field_no)
            if success == True:
                sub_list.append(task)
                sleep_time = 0
                print(task + " done!!")
            elif success == False:
                print(task + " failed!!")
                break
        #Case 2, the command is for buildings
        elif "building" in task:
            building_no = task.split("_", 1)[1]
            success = Construction.building(building_no)
            if success == True:
                sub_list.append(task)
                sleep_time = 0
                print(task + " done!!")
            elif success == False:
                print(task + " failed!!")
                break
    #Removing the successful tasks from the list
    for task in sub_list:
        Functions.remove_from_list(task, task_list)
        print(task + " removed!!")


def cosntruction_sleep(construction_sleep_time):
    sleep_t = int(construction_sleep_time)
    if sleep_t > 4:
        sleep_t = sleep_t - 4
        print("sleeping for " + str(sleep_t) + " mins .....")
        time.sleep((sleep_t * 60) + 30)
        Construction.inst_complete()
        print("instat complete done !!")
    else:
        Construction.inst_complete()
        print("instat complete done !!")