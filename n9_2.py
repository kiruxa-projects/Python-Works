class States:
    A = list()
    B = list()
    C = list()
    D = list()
    E = list()
    F = list()


class StateMachine:
    state = States.A

    def __init__(self):
        # Making a map

        States.A.append(('crawl', 0, States.B))
        States.A.append(('add', 1, States.E))
        States.B.append(('crawl', 2, States.C))
        States.C.append(('add', 3, States.D))
        States.D.append(('crawl', 4, States.E))
        States.D.append(('add', 5, States.A))
        States.E.append(('crawl', 6, States.F))
        States.E.append(('add', 8, States.B))
        States.E.append(('bend', 7, States.C))

    def __get_next_node(self, method_name):
        found = None
        for node in self.state:
            if node[0] == method_name:
                found = node
                break
        return found

    def base_method(self, next_state):
        if next_state is not None:
            self.state = next_state[2]
            return next_state[1]
        else:
            raise KeyError("No such edge!")

    def add(self):
        next_state = self.__get_next_node('add')
        return self.base_method(next_state)

    def crawl(self):
        next_state = self.__get_next_node('crawl')
        return self.base_method(next_state)

    def bend(self):
        next_state = self.__get_next_node('bend')
        return self.base_method(next_state)


def main():
    return StateMachine()
