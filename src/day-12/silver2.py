# DID NOT WORK

CUR_NAME_GROUP = 0
def get_name_group():
    global CUR_NAME_GROUP
    name = f"s{CUR_NAME_GROUP}"
    CUR_NAME_GROUP += 1
    return name

CUR_NAME_MIDDLE = 0
def get_name_middle():
    global CUR_NAME_MIDDLE
    name = f"t{CUR_NAME_MIDDLE}"
    CUR_NAME_MIDDLE += 1
    return name


class State:
    def __init__(self, name):
        self.name = name
        self.transitions = {}
        self.is_final = False
        self.remaining_input = None

    def add_transition(self, symbol, state):
        self.transitions[symbol] = state

    def transit(self, symbol):
        return self.transitions[symbol]
    
    def get_next(self):
        for state in self.transitions.values():
            if self != state:
                return state

    def print_dfa(self):
        if not self.is_final:
            return str(self) + "\n" + str(self.get_next().traverse())
        else:
            return "FINAL -> ['.']"


    def __str__(self):
        return f"{self.name} -> {[key for key in self.transitions.keys()]}"
    
    def __eq__(self, other):
        return self.name == other.name


def create_DFA(groups):
    initial_state = State(get_name_middle())
    state_groups = []
    for group in groups:
        state_group = [State(get_name_group()) for _ in range(group)]
        for i, state in enumerate(state_group):
            if i+1 < len(state_group):
                state.add_transition("#", state_group[i+1])
        state_groups.append(state_group)
    initial_state.add_transition(".", initial_state)
    initial_state.add_transition("#", state_groups[0][0])
    for i, state_group in enumerate(state_groups):
        middle = State(get_name_middle())
        state_group[-1].add_transition(".", middle)
        middle.add_transition(".", middle)
        if i+1 < len(state_groups):
            middle.add_transition("#", state_groups[i+1][0])
        else:
            middle.is_final = True
    return initial_state

        


### SCRIPT ###

file = open("src/day-12/example.txt")
lines = file.readlines()
lines = [line.replace('\n', '') for line in lines]
lines = [line.split(' ') for line in lines]
fields = [line[0] for line in lines]
groups = [[int(val) for val in list(line[1].split(','))] for line in lines]
dfas = [create_DFA(group) for group in groups]

dfa = dfas[0]
# for dfa in dfas:
print(dfa.print_dfa())

print("Hello")