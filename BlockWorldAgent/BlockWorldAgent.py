from copy import deepcopy
class State:
    def __init__(self, list_of_stacks):
        self.list_of_stacks = deepcopy(list_of_stacks)
        self.list_of_stacks.sort(key = lambda x: x[0])
        self.map_block = {}
        self.children = []
        self.parent = None
        self.move_from_parent_record = None # eg. ("C", "Table"), the move that was made to get to this state from the parent state
        self._build_map_block()
        self.item_axis = {}
        self.create_item_axis()

    def _build_map_block(self):
        ### block map ###
        # the map describes an "is on top of" relationship between the key and value pair
        # e.g. map_block['B'] = 'A' means block B is on top of block A
        # e.g. map_block['A'] = 'Table' means block A is on top of Table
        map_block = {}
        if self.list_of_stacks == []:
            return
        for stack in self.list_of_stacks:
            for i in range(len(stack)):
                if i == 0:
                    map_block[stack[i]] = 'Table'
                else:
                    map_block[stack[i]] = stack[i-1]
        self.map_block = map_block

    def create_item_axis(self):
        item_axis = {}
        for block_idx, stack in enumerate(self.list_of_stacks):
            for idx, item in enumerate(stack):
                item_axis[item] = (block_idx, idx)
        self.item_axis = item_axis

    def __eq__(self, other):
        pass

    def __hash__(self):
        pass

    def list_possible_moves(self):
        possible_moves = []
        for idx, stack in enumerate(self.list_of_stacks):
            last_item = stack[-1]

            for new_idx, new_stack in enumerate(self.list_of_stacks):
                last_item_new_stack = new_stack[-1]
                if last_item_new_stack != last_item:
                    possible_moves.append(((idx, last_item), (new_idx,last_item_new_stack)))
            if len(stack)>1:
                possible_moves.append(((idx, last_item), (-1,"Table")))

        return deepcopy(possible_moves)

    def distance_old(self, goal_state):
        score_goal = len(goal_state.map_block)
        score_self = 0
        for key, value in goal_state.map_block.items():
            if self.map_block[key] == value:
                score_self += 1
        return score_goal - score_self

    def distance(self, goal_state):
        total_distance = 0
        self.create_item_axis()
        self._build_map_block()
        for stack in self.list_of_stacks:
            for idx, item in enumerate(stack):
                if self.map_block[item] != goal_state.map_block[item]:
                    if idx == 0:
                        total_distance +=  2 * len(stack) - 1
                    else:
                        total_distance += 2*(len(stack) - idx)
                    break
        return total_distance
        #for stack in goal_state.list_of_stacks:
        #    table_item_x = self.item_axis[stack[0]][0]
        #    for idx, item  in enumerate(stack):
        #        x, y = self.item_axis[item]
        #        if x!=table_item_x or y != idx:
        #            total_distance += 1
        return total_distance

    def move(self, possible_move):
        from_stack = possible_move[0]
        to_stack = possible_move[1]
        if to_stack[1] == "Table":
            self.list_of_stacks.append([self.list_of_stacks[from_stack[0]].pop()])

        else:
            self.list_of_stacks[to_stack[0]].append(self.list_of_stacks[from_stack[0]].pop())

    def reverse_move(self, possible_move):
        from_stack = possible_move[0]
        to_stack = possible_move[1]
        if to_stack[1] == "Table":
            self.list_of_stacks[from_stack[0]].append(self.list_of_stacks.pop()[-1])
        else:
            self.list_of_stacks[from_stack[0]].append(self.list_of_stacks[to_stack[0]].pop())

    def drop_empty_stacks(self):

        for idx, stack in enumerate(self.list_of_stacks):
            if stack == []:
                self.list_of_stacks.pop(idx)


#    def move(self, origin_index, destination_index):
#        list_of_stacks = self.list_of_stacks.copy()
#        if destination_index == "Table":
#            move_from_parent_record = (list_of_stacks[origin_index][-1], "Table")
#            list_of_stacks.append([list_of_stacks[origin_index].pop(0)])
#        else:
#            move_from_parent_record = (list_of_stacks[origin_index][-1], list_of_stacks[destination_index][-1])
#            list_of_stacks[destination_index].insert(-1, list_of_stacks[origin_index].pop(0))
#        new_state = State(list_of_stacks)
#        new_state.parent = self
#        new_state.move_from_parent_record = move_from_parent_record
#        return new_state

#    def find_children(self):
#        num_stacks = len(self.list_of_stacks)
#        for i in range(num_stacks):
#            new_state = self.move(i, "Table")
#            self.children.append(new_state)
#            for j in range(num_stacks):
#                if i != j:
#                    new_state = self.move(i, j)
#                    self.children.append(new_state)
#
class BlockWorldAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        self.goal_state = None
        self.initial_state = None
        self.current_state = None
        self.path = []
    def solve(self, initial_arrangement, goal_arrangement):
        #Add your code here! Your solve method should receive
		#as input two arrangements of blocks. The arrangements
		#will be given as lists of lists. The first item in each
		#list will be the bottom block on a stack, proceeding
		#upward. For example, this arrangement:
		#
		#[["A", "B", "C"], ["D", "E"]]
		#
		#...represents two stacks of blocks: one with B on top
		#of A and C on top of B, and one with E on top of D.
		#
		#Your goal is to return a list of moves that will convert
		#the initial arrangement into the goal arrangement.
		#Moves should be represented as 2-tuples where the first
		#item in the 2-tuple is what block to move, and the
		#second item is where to put it: either on top of another
		#block or on the table (represented by the string "Table").
		#
		#For example, these moves would represent moving block B
		#from the first stack to the second stack in the example
		#above:
		#
		#("C", "Table")
		#("B", "E")
		#("C", "A")
        self.path = []
        self.goal_state = State(goal_arrangement)
        self.initial_state = State(initial_arrangement)
        self.move_strategy()
        return self.path 
      #  final_state = self._bfs(initial_state, goal_state)
      #  return self._get_path_to_root(final_state).reverse()

    def move_strategy(self):

        #trying all moves and choosing the one that gets us closer to the goal

        current_distance = self.initial_state.distance(self.goal_state)
        
        while current_distance > 0:
            moves = self.initial_state.list_possible_moves()

            for possible_move in moves:
                self.initial_state.move(possible_move)
                new_distance  = self.initial_state.distance(self.goal_state)
                if new_distance < current_distance:
                    self.path.append((possible_move[0][1], possible_move[1][1]))
                    current_distance = new_distance
                    self.initial_state.drop_empty_stacks()
                    break
                else:
                    self.initial_state.reverse_move(possible_move)
#            print("current state", self.initial_state.list_of_stacks, 'goal state:', self.goal_state.list_of_stacks)


  #  def _bfs(self, root_state, goal_state):
  #      queue = []
  #      visited = []
  #      queue.append(root_state)
  #      visited.append(root_state)
  #      while queue:
  #          current = queue.pop(0)
  #          if current.distance(goal_state) == 0:
  #              return current
  #          current.find_children()
  #          for child in current.children:
  #              if child not in visited:
  #                  queue.append(child)
  #                  visited.append(child)
  #      return None

  #  def _get_path_to_root(state):
  #      path = []
  #      while state.parent:
  #          path.append(state.move_from_parent_record)
  #          state = state.parent
  #      return path




