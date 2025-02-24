import json


class SquareNestNode(dict):
    def __init__(self, value):
        super().__init__()
        self['value'] = value
        self['up'] = None
        self['left'] = None
        self['right'] = None
        self['down'] = None

    def get_next_direction(self, value):
        if value < self['value']:
            return 'up' if not self['left'] else 'left'
        return 'down' if not self['right'] else 'right'

    def __str__(self):
        return json.dumps(self)

    def get_next(self, value):
        return self[self.get_next_direction(value)]

    def set_next(self, value):
        self[self.get_next_direction(value)] = SquareNestNode(value)


class SquareNest:
    def __init__(self):
        self.root: SquareNestNode | None = None

    def _appending(self, node: SquareNestNode, value):
        if not node.get_next(value):
            node.set_next(value)
        else:
            self._appending(node.get_next(value), value)

    def append(self, value):
        if not self.root:
            self.root = SquareNestNode(value)
        else:
            self._appending(self.root, value)

    def __str__(self):
        return str(self.root)

square_nest = SquareNest()
square_nest.append(3)
square_nest.append(2)
square_nest.append(1)
square_nest.append(4)
square_nest.append(5)

print(square_nest)

