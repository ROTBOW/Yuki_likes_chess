'''
Yuki is a chess path visualtion program.
'''
from PIL import Image, ImageDraw
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
chessboard = dir_path + '\\Chess_Board.png'


class Yuki:

    def __build_board(self):
        return [[0]*8]*8

    def __board_loca_to_px(self, x, y):
        step = 140
        return step + (252 * x), step + (252 * y)


    def __init__(self) -> None:
        self.board = self.__build_board()
        self.image_path = chessboard

    def draw_line_from_points(self, x1, y1, x2, y2):
        with Image.open(self.image_path) as im:
            draw = ImageDraw.Draw(im)
            draw.line(self.__board_loca_to_px(x1, y1), fill=128*3)
            draw.line(self.__board_loca_to_px(x2, y2), fill=128*3)

            im.show()
            


yuki = Yuki()
yuki.draw_line_from_points(0, 0, 2, 2)
# print(yuki.board_loca_to_px(2,3))