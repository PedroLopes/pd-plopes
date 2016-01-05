import dtw_distance
import pdgui
class Reloader:
    #DEBUG = False
    def __init__(self):
        #if self.DEBUG pdgui.post("Started reloader for:" + dtw_distance)
        pdgui.post("Started reloader for:" + dtw_distance)
        return
    def reload_demo_module(self):
        reload(dtw_distance)
        #if self.DEBUG: pdgui.post("Done reloading:" + dtw_distance)
        pdgui.post("Done reloading:" + dtw_distance)
        return
    #def set_debug(self,flag):
    #    self.DEBUG = flag
    #    return
