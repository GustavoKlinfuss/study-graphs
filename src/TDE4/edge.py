from functools import total_ordering

@total_ordering
class Edge:
    def __init__(self, origin, dest, weight):
        self.origin = origin
        self.dest = dest
        self.weight = weight

    def add_weight(self, weight):
        self.weight += weight

    def get_weight(self):
        return self.weight

    def __eq__(self, other):
        return (self.origin, self.dest) == (other.origin, other.dest)
    
    def __lt__(self, other):
        return (self.origin, self.dest) < (other.origin, other.dest)
    
    def __le__(self, other):
        return (self.origin, self.dest) <= (other.origin, other.dest)
    
    def __gt__(self, other):
        return (self.origin, self.dest) > (other.origin, other.dest)

    def __ge__(self, other):
        return (self.origin, self.dest) >= (other.origin, other.dest)