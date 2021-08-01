import time
import Execution
import Functions
import Navigation
import Construction


total_slots = 3
construction_task_list = []
Functions.read_from_file("construction_tasks", construction_task_list)
tasks_no = len(construction_task_list)

if tasks_no > 0:
    Navigation.open_main_screen()
    while(tasks_no > 0):
        #Queue is empty
        if Construction.check_queue(total_slots) == True:
            Execution.construction_from_list(construction_task_list)
            construction_sleep_time = Construction.check_duration(total_slots)
            Functions.write_to_file("construction_tasks", construction_task_list)
            print("Task List Updated to the txt file")
            tasks_no = len(construction_task_list)
            print("Remaining tasks = " + str(tasks_no) + "tasks")
            Execution.cosntruction_sleep(construction_sleep_time)            
        #Queue is full    
        else:
            construction_sleep_time = Construction.check_duration(total_slots)
            print("Queue not empty...")
            Execution.cosntruction_sleep(construction_sleep_time)
    time.sleep(5)
    Navigation.close_connection()
else:
    print("No Tasks to do, make sure you added the tasks into the txt file")