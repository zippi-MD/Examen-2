from tkinter import Tk, Label, Canvas, N, S, E, W, LabelFrame, PhotoImage
from Views.ButtonsArea import ButtonsArea


class MainView(Tk):
    class Constants:
        title = "Pizarra Mágica"
        buttons_title = "Selecciona el color de la linea"
        font = ("Phosphate", 48, "bold")
        height = 900
        width = 1000
        center = N + S + E + W
        border_color = '#F44336'
        magic_board_color = '#FAFAFA'

        @classmethod
        def size(cls):
            return '{}x{}'.format(cls.width, cls.height)

    def __init__(self, color_handler=None):
        super().__init__()

        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.minsize(width=self.Constants.width, height=self.Constants.height)
        self.configure(bg=self.Constants.border_color)
        self.grid_columnconfigure(0, weight=1)

        self.drawing_canvas_setup()

        self.title = Label(self, text=self.Constants.title, bg=self.Constants.border_color, font=self.Constants.font, pady=20)
        self.title.grid(row=0, column=0)

        ButtonsArea(self, self.Constants.buttons_title, color_handler)



    def update_drawing(self, coordinates, color):
        print(coordinates.actual_x_coordinate, coordinates.actual_y_coordinate,
              coordinates.modify_x_coordinate, coordinates.modify_y_coordinate)

        self.__magic_board.create_line(coordinates.actual_x_coordinate, 500-coordinates.actual_y_coordinate,
                                       coordinates.modify_x_coordinate, 500-coordinates.modify_y_coordinate,
                                       fill=color, width=2)

    def reset_drawing(self):
        print('Reseting drawing canvas')
        self.__magic_board.destroy()
        self.drawing_canvas_setup()

    def drawing_canvas_setup(self):
        self.__magic_board = Canvas(self, width=600, height=500, bg=self.Constants.magic_board_color)
        self.__magic_board.grid(row=1, column=0)


