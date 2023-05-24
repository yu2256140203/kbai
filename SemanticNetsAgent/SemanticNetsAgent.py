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
        #to #the rules of the problem, return an empty list of
        #moves.
        pass

        class State:
            def __init__(self, left_sheep, left_wolves, left_boat, right_sheep, right_wolves, right_boat):
                self.left_sheep = left_sheep
                self.left_wolves = left_wolves
                self.left_boat = left_boat
                self.right_sheep = right_sheep
                self.right_wolves = right_wolves
                self.right_boat = right_boat
                self.parent = None

            def to_tuple(self):
                return (self.left_sheep, self.left_wolves, self.left_boat, self.right_sheep, self.right_wolves, self.right_boat)

            def goal_test(self):
                return self.left_sheep == 0 and self.left_wolves == 0 and self.left_boat == 0 and self.right_sheep == initial_sheep and self.right_wolves == initial_wolves and self.right_boat == 1

            def valid_state(self):
                if self.left_sheep < 0 or self.left_wolves < 0 or self.right_sheep < 0 or self.right_wolves < 0:
                    return False
                if self.left_sheep > initial_sheep or self.left_wolves > initial_wolves or self.right_sheep > initial_sheep or self.right_wolves > initial_wolves:
                    return False
                if self.left_sheep < self.left_wolves and self.left_sheep > 0:
                    return False
                if self.right_sheep < self.right_wolves and self.right_sheep > 0:
                    return False
                return True

        def get_children(state):
            children = []
            if state.left_boat == 1:
                for i in range(0, 2):
                    for j in range(0, 2):
                        if i == 0 and j == 0:
                            continue
                        new_state = State(state.left_sheep - i, state.left_wolves - j, 0, state.right_sheep + i, state.right_wolves + j, 1)
                        if new_state.valid_state():
                            new_state.parent = state
                            children.append(new_state)
            else:
                for i in range(0, 2):
                    for j in range(0, 2):
                        if i == 0 and j == 0:
                            continue
                        new_state = State(state.left_sheep + i, state.left_wolves + j, 1, state.right_sheep - i, state.right_wolves - j, 0)
                        if new_state.valid_state():
                            new_state.parent = state
                            children.append(new_state)
            return children

        def bfs():
            queue = []
            visited = []
            start = State(initial_sheep, initial_wolves, 1, 0, 0, 0)
            queue.append(start)
            visited.append(start)
            while queue:
                current = queue.pop(0)
                if current.goal_test():
                    return current
                for child in get_children(current):
                    if child not in visited:
                        queue.append(child)
                        visited.append(child)
            return None

        def get_path(state):
            path = []
            state_path = []
            while state.parent:
                path.append((abs(state.left_sheep - state.parent.left_sheep), abs(state.left_wolves - state.parent.left_wolves)))
                state_path.append(state.to_tuple())
                state = state.parent
            path.reverse()
            #print("PATH:"+str(state_path))
            return path

        solution = bfs()
        if solution:
            return get_path(solution)
        else:
            return []






