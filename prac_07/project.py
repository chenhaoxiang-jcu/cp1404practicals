class Project:
    """Represent information about a project."""

    def __init__(self, name='', start_date='', priority=0, cost_estimate=0.0, completion_percentage=0):
        """Initialize a Project object."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of the project."""
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Less than, using to sort projects by priority."""
        return self.priority < other.priority

    def is_completed(self):
        """Check whether the project completion percentage is 100."""
        return self.completion_percentage == 100

    def update_percentage(self, percentage):
        """Update the completion percentage of project."""
        self.completion_percentage = percentage

    def update_priority(self, priority):
        """Update the priority of project."""
        self.priority = priority
