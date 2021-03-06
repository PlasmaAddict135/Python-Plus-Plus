class __prece__:
    def __init__(self, types, origin, prece: int, *ap):
        self.types = types
        self.origin = origin
        self.prece = prece
        self.ap = ap
        g = globals()
        org = g.get(self.origin)
        if '' == self.ap:
            return None
        if self.prece == 1 and self.types == 'fn':
            self.origin()
        elif self.types == 'var':
            if self.origin:
                if self.prece > 1:
                    print(g[org])

class __with__:
    def __init__(self, types, origin, target):
        self.types = types
        self.origin = origin
        self.target = target

        if 'var' == self.types:
            if self.origin:
                g = globals()
                a = g.get(self.origin)
                b = g.get(self.target)
                un = g.get(self.origin)
                g[self.origin] = a + b
        elif 'fn' == self.types:
            if self.origin:
                try: self.target()
                except: print(f'TypeError: type "{self.types}" not found for origin, instead found "{self.origin}"')
    def __repr__(self):
        return self.origin
    def uncouple(self):
        g = globals()
        a = g.get(self.origin)
        b = g.get(self.target)
        g[self.origin] = un

class __count__:
    def __init__(self,x):
        self.__x = x
        self.counter = 0
    def __str__(self):
        self.counter += 1
        return str(self.__x)
    @property
    def x(self):
        self.counter_ += 1
        return self.__x
    @x.setter
    def x(self, x):
        self.__x = x
        self.counter = 0
