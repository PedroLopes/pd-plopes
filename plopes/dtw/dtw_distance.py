from dtw import dtw

class DtwDistance:
    
    x = []
    y = []
    dist = 0
    cost = 0
    path = []
    norm = None #note we are using L1 norm as cost function

    def __init__(self):
        pass

    def set_x(self, *args):
        self.x = []
        for arg in args:
            self.x.append(arg)
    
    def add_x(self, *args):
        for arg in args:
            self.x.append(arg)
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def set_y(self, *args):
        self.y = []
        for arg in args:
            self.y.append(arg)
    
    def add_y(self, *args):
        for arg in args:
            self.y.append(arg)

    def analyze(self):
        d, c, p = dtw(self.x, self.y)
        #self.dist, self.cost, self.path = dtw(self.x, self.y, dist=self.norm)
        self.dist = d
        self.cost = c
        self.path = p
        #get_distance(self)
        return d

    def get_distance(self):
        return self.dist
    
    def get_cost(self):
        return self.cost
    
    def get_path(self):
        return self.path
    
    def set_norm(norm_name):
        #try
        norm = norm_name #which should be function pointer
        #catch
            #pdgui.post("problem with provided norm. please check python file.")
            #norm = None

    def my_custom_norm(x, y):
        return (x * x) + (y * y)

    def get_alive(self):
        return "dea22erterdalive"
    
