class player:
    def __init__(self,id,name,position,possession,points):
        self.id = id
        self.name = name
        self.position = position
        self.possession = possession
        self.points = points

    def get_points(self):
        """Return the current points of the agent."""
        return self.points

    def add_points(self, points):
        """Add points to the agent's total."""
        self.points += points

    def add_possession(self, resource_id):
        """Add a resource ID to the agent's possession."""
        if resource_id not in self.possession:
            self.possession.append(resource_id)

    def get_pos(self):
        """Return the current position of the agent."""
        return self.position

    def update_pos(self, new_position):
        """Update the agent's position."""
        self.position = new_position

    def get_possession(self):
        """Return the list of resource IDs in possession."""
        return self.possession

    def get_best_resource(self, resources):
        """Return the best resource based on some criteria."""
        # Placeholder implementation; you can define your own criteria
        return max(resources, key=lambda r: r.value)  # Assuming 'resources' have a 'value' attribute

    def get_pos_to_resource(self, resource):
        """Return the position coordinates of the given resource."""
        return resource.position  # Assuming 'resource' has a 'position' attribute