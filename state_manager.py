class StateManager:
    is_adding_new_points: bool

    def __init__(self):
        self.is_adding_new_points = False

    def switch_adding(self) -> None:
        self.is_adding_new_points = not self.is_adding_new_points
