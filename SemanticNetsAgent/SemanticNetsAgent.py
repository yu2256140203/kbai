class State:
    def __init__(self, left_sheep, left_wolves, left_boat, right_sheep, right_wolves, right_boat):
        self.left_sheep = left_sheep
        self.left_wolves = left_wolves
        self.left_boat = left_boat
        self.right_sheep = right_sheep
        self.right_wolves = right_wolves
        self.right_boat = right_boat
        self.initial_sheep = self.left_sheep + self.right_sheep
        self.initial_wolves = self.left_wolves + self.right_wolves
        self.parent = None

    def to_tuple(self):
        return (self.left_sheep, self.left_wolves, self.left_boat, self.right_sheep, self.right_wolves, self.right_boat)

    def __eq__(self, other):
        return self.left_sheep == other.left_sheep and self.left_wolves == other.left_wolves and self.left_boat == other.left_boat and self.right_sheep == other.right_sheep and self.right_wolves == other.right_wolves and self.right_boat == other.right_boat

    def is_success(self):
        return self.left_sheep == 0 and self.left_wolves == 0 and self.left_boat == 0 and self.right_sheep == self.initial_sheep and self.right_wolves == self.initial_wolves and self.right_boat == 1

    def is_valid(self):
        if self.left_sheep < 0 or self.left_wolves < 0 or self.right_sheep < 0 or self.right_wolves < 0:
            return False
        if self.left_sheep > self.initial_sheep or self.left_wolves > self.initial_wolves or self.right_sheep > self.initial_sheep or self.right_wolves > self.initial_wolves:
            return False
        if self.left_sheep < self.left_wolves and self.left_sheep > 0:
            return False
        if self.right_sheep < self.right_wolves and self.right_sheep > 0:
            return False
        return True


    def get_children(self):
        children = []
        if self.left_boat == 1:
            for i in range(0, 3):
                for j in range(0, 3):
                    if i == 0 and j == 0:
                        continue
                    if i + j > 2:
                        continue
                    new_state = State(self.left_sheep - i, self.left_wolves - j, 0, self.right_sheep + i,
                                      self.right_wolves + j, 1)
                    if new_state.is_valid():
                        new_state.parent = self
                        children.append(new_state)
        else:
            for i in range(0, 3):
                for j in range(0, 3):
                    if i == 0 and j == 0:
                        continue
                    if i + j > 2:
                        continue
                    new_state = State(self.left_sheep + i, self.left_wolves + j, 1, self.right_sheep - i,
                                      self.right_wolves - j, 0)
                    if new_state.is_valid():
                        new_state.parent = self
                        children.append(new_state)
        return children

class SemanticNetsAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass

    def solve(self, initial_sheep, initial_wolves):
        #Add your code here! Your solve method should receive
        #the initial number of sheep and wolves as integers,
        #and return a list of 2-tuples that represent the moves
        #required to get all sheep and wolves from the left
        #side of the river to the right.
        #
        #If it is impossible to move the animals over according
        #to the rules of the problem, return an empty list of
        #moves.

        def _bfs(root):
            queue = []
            visited = []
            queue.append(root)
            visited.append(root)
            while queue:
                current = queue.pop(0)
                if current.is_success():
                    return current
                for child in current.get_children():
                    if child not in visited:
                        queue.append(child)
                        visited.append(child)
            return None

        def _get_path(state):
            path = []
            state_path = []
            while state.parent:
                path.append((abs(state.left_sheep - state.parent.left_sheep), abs(state.left_wolves - state.parent.left_wolves)))
                state_path.append(state.to_tuple())
                state = state.parent
            path.reverse()
            # state_path.append(state.to_tuple())
            # state_path.reverse()
            # print("PATH:"+str(state_path))
            return path

        start = State(initial_sheep, initial_wolves, 1, 0, 0, 0)
        solution = _bfs(start)
        if solution:
            return _get_path(solution)
        else:
            return []







