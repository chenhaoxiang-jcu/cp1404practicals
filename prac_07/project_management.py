"""
Project Management
Estimate: 60 minutes
Actual:   around 5-6 hours
"""

import datetime
from operator import attrgetter

from prac_07.project import Project

FILENAME = 'projects.txt'
MENU = ('- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n'
        '- (A)dd new project\n- (U)pdate project\n- (Q)uit')
DATE_FORMAT = '%d/%m/%Y'
LOWEST_PRIORITY = 1
HIGHEST_PRIORITY = 9
MINIMUM_PERCENTAGE = 0
MAXIMUM_PERCENTAGE = 100
MINIMUM_COST = 0.0
MAXIMUM_COST = 999999999.9


def main():
    """Menu-driven project management software with options to load, save, display, filter, add, and update projects."""
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
            filter_projects(projects)
        elif choice == 'A':
            add_project(projects)
        elif choice == 'U':
            update_projects(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    save_choice = input("Would you like to save to projects.txt? ").upper()
    if save_choice == 'Y':
        save_projects(projects, FILENAME)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from a file."""
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects


def save_projects(projects, filename):
    """Save projects to a file."""
    with open(filename, 'w') as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t"
                           f"{project.cost_estimate}\t{project.completion_percentage}\n")
    print(f"Saved {len(projects)} projects to {filename}")


def load_new_projects():
    """Load projects from a file that user input."""
    filename = input("Filename to load: ")
    projects = load_projects(filename)
    return projects


def proceed_saving_task(projects):
    """Save projects to a file that user input."""
    filename = input("Filename to save: ")
    save_projects(projects, filename)


def display_projects(projects):
    """Display priority-sorted incomplete and completed projects separately."""
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


def filter_projects(projects):
    """Ask the user for a date and display only projects that start after that date, sorted by date."""
    date_string = get_valid_date("Show projects that start after date (dd/mm/yy): ")
    date = datetime.datetime.strptime(date_string, DATE_FORMAT).date()

    filtered_projects = [project for project in projects
                         if datetime.datetime.strptime(project.start_date, DATE_FORMAT).date() >= date]

    for filtered_project in filtered_projects:
        filtered_project.start_date = datetime.datetime.strptime(filtered_project.start_date, DATE_FORMAT).date()
    filtered_projects.sort(key=attrgetter('start_date'))

    for filtered_project in filtered_projects:
        filtered_project.start_date = filtered_project.start_date.strftime(DATE_FORMAT)
        print(filtered_project)


def get_valid_date(prompt):
    """Get valid date with specific format."""
    while True:
        try:
            date_string = input(prompt)
            datetime.datetime.strptime(date_string, DATE_FORMAT).date()
            break
        except ValueError:
            print("Invalid date format")
    return date_string


def add_project(projects):
    """Ask the user for the inputs and add a new project to memory."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = get_valid_date("Start date (dd/mm/yy): ")
    priority = get_valid_number("Priority: ", int, LOWEST_PRIORITY, HIGHEST_PRIORITY)
    cost_estimate = get_valid_number("Cost estimate: $", float, MINIMUM_COST, MAXIMUM_COST)
    completion_percentage = get_valid_number("Percent complete: ", int, MINIMUM_PERCENTAGE, MAXIMUM_PERCENTAGE)
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)


def get_valid_number(prompt, number_type, minimum, maximum):
    """Validate the number user input."""
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
    """Choose a project, then modify the completion % and/or priority - leave blank to retain existing values"""
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

        if projects[project_index].is_completed():
            print("Project already completed")
        else:
            while True:
                try:
                    new_percentage = input("New Percentage: ")
                    if new_percentage != '':
                        new_percentage = int(new_percentage)
                        if (new_percentage <= projects[project_index].completion_percentage
                                or new_percentage > MAXIMUM_PERCENTAGE):
                            raise ValueError
                        else:
                            projects[project_index].update_percentage(new_percentage)
                    break
                except ValueError:
                    print(f"Invalid percentage, "
                          f"new percentage should be greater than {projects[project_index].completion_percentage}, "
                          f"up to {MAXIMUM_PERCENTAGE}")

        while True:
            try:
                new_priority = input("New Priority: ")
                if new_priority != '':
                    new_priority = int(new_priority)
                    if new_priority < LOWEST_PRIORITY or new_priority > HIGHEST_PRIORITY:
                        raise ValueError
                    else:
                        projects[project_index].update_priority(new_priority)
                break
            except ValueError:
                print(f"Invalid priority,should be a number and between {LOWEST_PRIORITY} - {HIGHEST_PRIORITY}.")


main()
