import pygame
from pygame.locals import QUIT
from render import render_barchart


class App:
    def __init__(self):
        '''(App) -> NoneType'''
        self.width = None # width of the display window
        self.height = None # height of the display window
        self.running = None # running status of program
        self.fps = None
        self.fps_clock = None # control FPS of program
        self.window = None

    def init(self):
        '''(App) -> int
        Loads initialization data for this program and pygame initialization,
        and loads the barchart for display. If data initialization fails,
        returns with -1. If the barchart fails to load correctly, returns -2,
        Otherwise, returns 0.'''
        init_data = self.load_init_data()
        if init_data == {}:
            return -1

        self.width = int(init_data["width"])
        self.height = int(init_data["height"])
        self.running = True
        self.fps = int(init_data["fps"])
        self.fps_clock = pygame.time.Clock()

        pygame.init()

        self.window = pygame.display.set_mode((self.width, self.height))

        WHITE = (255, 255, 255)
        self.window.fill(WHITE)
        pygame.display.flip()

        FILE_NAME = "input.txt"

        pygame.display.set_caption("barchart - %s" % FILE_NAME)

        if self.load_barchart(FILE_NAME) == False:
            return -2

        return 0

    def load_init_data(self):
        '''(App) -> dict
        Loads initialization data for this program into a dict and returns it.
        If loading fails, returns empty dict.'''
        REQ_INIT_DATA = ["width", "height", "fps"]
        data = dict((property, None) for property in REQ_INIT_DATA)
        FILE_NAME = "init.txt"
        with open(FILE_NAME, "r") as FILE:
            for line in FILE:
                property, value = line.split()
                if property in data:
                    data.update({property: value})

        if None in data.values():
            return {}

        return data

    def load_barchart(self, FILE_NAME):
        '''(App, str) -> bool
        Loads the barchart given in FILE_NAME and displays it. If the data
        initialization fails, returns False and does not display the barchart.
        Otherwise, returns True.'''
        DATA = _load_barchart_data(FILE_NAME)
        if DATA == {}:
            return False

        PLOT_DATA = [tuple(plot) for plot in DATA["bar"]]
        render_barchart(self, DATA["title"], PLOT_DATA)

        pygame.display.flip()

        return True

    def exit(self):
        '''(App) -> NoneType'''
        self.running = False

    def main(self):
        '''(App) -> int
        Initializes the program and loads and displays barchart. If such
        initialization fails, the return of init is returned. Otherwise,
        the program runs until the user quits.'''
        init_status = self.init()
        if init_status != 0:
            return init_status

        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.exit()
            self.fps_clock.tick(self.fps)

        return 0


def _load_barchart_data(FILE_NAME):
    '''(str) -> dict
    Loads the barchart data given in FILE_NAME into a dict and returns it.
    If loading fails, an empty dict is returned.'''
    data = {"title": None, "bar": []}
    with open(FILE_NAME, "r") as FILE:
        for line in FILE:
            line_data = line.split()
            if line[0] == "#":
                # comment
                continue
            elif line_data[0] == "title":
                title = line_data[1]
                data.update({"title": title})
            elif line_data[0] == "bar":
                title, val = line_data[1:]
                data["bar"].append([title, float(val)])

    if data["title"] == None:
        return {}

    return data

