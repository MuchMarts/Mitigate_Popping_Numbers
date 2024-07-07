class Player:
    def __init__(self):
        self.points = 0

    def increase_points(self, points):
        self.points += points
        print(f"You gained: {points} points")

    def show_points(self):
        return self.points

