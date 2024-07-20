"""
Project Management
Estimate: 60 minutes
Actual:   -- minutes
"""

from prac_07.project import Project

FILENAME = 'projects.txt'
MENU = ('- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n'
        '- (A)dd new project\n- (U)pdate project\n- (Q)uit')


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'L':
            projects = load_new_projects()
        elif choice == 'S':
            proceed_saving_task(projects)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            pass
        elif choice == 'A':
            add_project(projects)
        elif choice == 'U':
            update_projects(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()


def load_projects(filename):
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects


def save_projects(projects, filename):
    with open(filename, 'w') as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t"
                           f"{project.cost_estimate}\t{project.completion_percentage}\n")


def load_new_projects():
    filename = input("Filename to load: ")
    projects = load_projects(filename)
    projects.sort()
    return projects


def proceed_saving_task(projects):
    filename = input("Filename to save: ")
    save_projects(projects, filename)


def display_projects(projects):
    if not projects:
        print("No projects to display")
    else:
        completed_projects = []
        incomplete_projects = []
        for project in projects:
            if project.is_completed():
                completed_projects.append(project)
            else:
                incomplete_projects.append(project)
        print("Incomplete projects: ")
        for project in sorted(incomplete_projects):
            print(f'  {project}')
        print("Completed projects: ")
        for project in sorted(completed_projects):
            print(f'  {project}')


def add_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = get_valid_number("Priority: ", int, 1, 999)
    cost_estimate = get_valid_number("Cost estimate: ", float, 0.0, 999999999.9)
    completion_percentage = get_valid_number("Percent complete: ", int, 0, 100)
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)


def get_valid_number(prompt, number_type, minimum, maximum):
    while True:
        try:
            number = number_type(input(prompt))
            if number < minimum or number > maximum:
                print(f"Number must be between {minimum} and {maximum} inclusive.")
            else:
                break
        except ValueError:
            print("Invalid input")
    return number


def update_projects(projects):
    if not projects:
        print("No projects to update")
    else:
        for i, project in enumerate(projects):
            print(f"{i} {project}")

        while True:
            try:
                project_index = int(input("Project choice: "))
                while project_index not in range(len(projects)):
                    print("Invalid index")
                    project_index = int(input("Project choice: "))
                break
            except ValueError:
                print("Invalid input - please enter a valid number")
        print(projects[project_index])

        try:
            if projects[project_index].is_completed():
                print("Project already completed")
            else:
                new_percentage = int(input("New Percentage: "))
                while new_percentage <= projects[project_index].completion_percentage or new_percentage > 100:
                    print(f"New percentage should be greater than {projects[project_index].completion_percentage}, "
                          f"up to 100")
                    new_percentage = int(input("New Percentage: "))
                projects[project_index].update_percentage(new_percentage)
        except ValueError:
            pass

        try:
            new_priority = int(input("New Priority: "))
            while new_priority <= 0:
                print("Invalid priority")
                new_priority = int(input("New Priority: "))
            projects[project_index].update_priority(new_priority)
        except ValueError:
            pass


main()
