# 3. To-Do List App (Text-Based)
# Build a to-do list manager that:
# Allows users to add tasks with priorities (e.g., "Buy milk - high").
# Lets them view the current list, delete tasks by number, and mark tasks as complete.
# Keeps looping until the user types “exit”.
# Shows a summary at the end: number of completed tasks vs pending.
# Skills practiced: lists, string parsing, loops, input, CRUD basics
print("Welcome to a to do list App!")
completed_task={}
pending_task={}
while True:
     
     task = input("please enter your to do list with priorities e.g (Buy milk - high)")
     if task=="exit":
        break
     pending_task[len(pending_task)+1]=task
     print("here's your current to do list \n",pending_task )
     number = int(input("please enter number to delete the pending item "))
     if  len(pending_task)>=number:
         completed_task[len(completed_task)+1]= pending_task.get(number)
         pending_task.pop(number)
     else:
         print("please enter a valid number ")
    
print(f"number of completed task :\n{completed_task} , \npending task :\n{pending_task}")
     
     