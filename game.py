from scripts.window import Window
from scripts.input import Input
from scripts.assets import Assets
from scripts.state import State
from scripts.managers.manager import Manager
from scripts.renderer import Renderer
from scripts.camera import Camera

class Game:
    def __init__(self):
        self.window = Window(self)
        self.state = State(self)
        self.input = Input(self)
        self.assets = Assets()
        self.manager = Manager(self)
        self.renderer = Renderer(self)
        self.camera = Camera(self)
        
    def update(self):
        self.input.update()
        self.camera.update()
        self.renderer.render()
        self.state.update()
        
    def run(self):
        while True:
            self.update()     
                   
             
if __name__ == "__main__":
    Game().run()