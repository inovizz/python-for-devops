import os

FILE_LOC = "data.txt"

# color related code for better view on terminal
colors = {
    'DANGER': '\033[91m',
    'WARNING': '\033[33m',
    'MILD': '\033[94m',
    'OK': '\033[92m',
    'RESET': '\033[0m',
    'BLUE': '\033[94m',
    'CYAN': '\033[96m',
}

format = {0: 5, 1:25, 2:10, 3:25, 4:5}

# function to get the colored text
def color(text, text_color):
    if text_color in colors:
        return ''.join([colors[text_color], text, colors['RESET']])
    return text

# the help text
print("""Usage of the ToDo App CLI\nWe support following commands as of now\n""")
print('Command List')
print("\t" + color("Add item", 'CYAN') + "               " + color('--add', 'OK'))
# print("\t" + color("Add due date", 'CYAN') + "           " + color('--due', 'OK'))
print("\t" + color("Remove an Item", 'CYAN') + "         " + color('--remove', 'OK'))
print("\t" + color("Mark item done", 'CYAN') + "         " + color('--done', 'OK'))
print("\t" + color("Mark item not done", 'CYAN') + "     " + color('--undone', 'OK'))
print("\t" + color("View items", 'CYAN') + "             " + color('--view', 'OK'))

cmd = input("Enter the command ")

if cmd:
    # Add the item
    if cmd == "--add":
        print(color("Add your task in following format", 'BLUE'))
        print(color("'Title', 'Due Date', 'Description'\n", 'CYAN'))
        data = input()
        data = data.split(",")
        data = ", ".join(data)
        if data:
            with open(FILE_LOC, 'r+') as f:
                last_line = f.readlines()[-1]
                if last_line:
                    try:
                        count = int(last_line.split(",")[0])+1
                    except ValueError:
                        count = 1
                    f.write(str(count)+", "+data+", [ ]""\n")
                print(color("Item successfully added!", 'CYAN'))
    # remove the item
    elif cmd == "--remove":
        print("\n"+color("Remove your task by providing the id of the task", 'BLUE'))
        try:
            id = int(input("Enter the id of the task you want to delete "))
        except ValueError:
            raise("Please enter the correct id value")
        with open(FILE_LOC, 'r') as f:
            lines = f.readlines()
        with open(FILE_LOC, 'w+') as f:
            count = 0
            for line in lines:
                if count == 0:
                    f.write(line)
                    count += 1
                    continue
                no = int(line.split(", ")[0])
                if no != id:
                    f.write(line)
                count += 1
        print(color("Item successfully removed!", 'CYAN')) 
    # mark the item as done            
    elif cmd == "--done":
        print("\n"+color("Mark your task as done by providing the id of the task", 'BLUE'))
        try:
            id = int(input("Enter the id of the task you want to mark as done "))
        except ValueError:
            raise("Please enter the correct id value")
        with open(FILE_LOC, 'r') as f:
            lines = f.readlines()
        with open(FILE_LOC, 'w+') as f:
            count = 0
            for line in lines:
                if count == 0:
                    f.write(line)
                    count += 1
                    continue
                no = int(line.split(", ")[0])
                if no == id:
                    line_text = line.split(", ")
                    line_text[-1] = "[x]\n"
                    line = ", ".join(line_text)
                    f.write(line)
                else:
                    f.write(line)
                count += 1
        print(color("Item successfully updated!", 'CYAN')) 
    # mark the item as undone
    elif cmd == "--undone":
        print("\n"+color("Mark your task as undone by providing the id of the task", 'BLUE'))
        try:
            id = int(input("Enter the id of the task you want to mark as undone "))
        except ValueError:
            raise("Please enter the correct id value")
        with open(FILE_LOC, 'r') as f:
            lines = f.readlines()
        with open(FILE_LOC, 'w+') as f:
            count = 0
            for line in lines:
                if count == 0:
                    f.write(line)
                    count += 1
                    continue
                no = int(line.split(", ")[0])
                if no == id:
                    line_text = line.split(", ")
                    line_text[-1] = "[ ]\n"
                    line = ", ".join(line_text)
                    f.write(line)
                else:
                    f.write(line)
                count += 1
        print(color("Item successfully updated!", 'CYAN')) 
    # list all the todo items
    elif cmd == "--view":
        with open(FILE_LOC, 'r') as f:
            lines = f.readlines()
            count = 0
            for line in lines:
                data = []
                line = line.split(", ")
                for i in range(len(line)):
                    data.append(line[i].strip().ljust(format[i]))
                if count == 0:
                    print(color(" ".join(data), 'OK'))
                else:
                    print(color(" ".join(data), 'RESET'))
                count += 1   
    else:
        print("Command not found, please run the script again and check the help")
