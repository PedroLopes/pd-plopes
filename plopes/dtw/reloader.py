# reloader.py : Python class to manage reloading other modules during a single Pd session

import dtw_distance
import pdgui

class Reloader:

    DEBUG = False

    def __init__(self):
        if (self.DEBUG) pdgui.post("hello from reloader")
        pass

    def reload_demo_module(self):
        reload(dtw_distance)
        if (self.DEBUG) pdgui.post("done reloading")
        return
