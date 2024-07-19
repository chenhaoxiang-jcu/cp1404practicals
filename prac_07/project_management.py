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
            pass
        elif choice == 'U':
            pass
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


main()
