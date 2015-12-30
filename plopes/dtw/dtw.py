from dtw import dtw

class DTWDistance:
    
    x = []
    y = []
    dist = 0
    cost = 0
    path = []
    norm = None #note we are using L1 norm as cost function

    def __init__(self):
        pass

    def set_x(self, x)
        self.x = x
    
    def set_y(self, y)
        self.y = y

    def analyze(self):
        dist, cost, path = dtw(x, y, dist=norm)

    def get_distance(self):
        return self.dist
    
    def get_cost(self):
        return self.cost
    
    def get_path(self):
        return self.path

    def run(self):
        analyze(self)
        return get_distance(self)
    
    def set_norm(norm_name):
        #try
        norm = norm_name #which should be function pointer
        #catch
            #pdgui.post("problem with provided norm. please check python file.")
            #norm = None

    def my_custom_norm(x, y):
        return (x * x) + (y * y)

    
