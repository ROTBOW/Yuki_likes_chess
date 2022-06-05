'''
Yuki is a chess path visualtion program.
'''
from PIL import Image, ImageDraw, ImageFont, ImageColor
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
chessboard = dir_path + '\\Chess_Board.png'


class Yuki:

    def __build_board(self) -> list:
        return [[0]*8]*8

    def __pos_to_px(self, x: int, y: int) -> tuple:
        step = 140
        return step + (252 * x), step + (252 * y)

    def __vaild_pos(self, x: int, y: int) -> bool:
        return 0 < x < 9 and 0 < y < 9

    def __draw_step_at_pos(self, pos: tuple, step: int, image: Image) -> Image:
        draw = ImageDraw.Draw(image)
        x, y = self.__pos_to_px(*pos)
        draw.text((x-6, y-13), str(step), font=ImageFont.truetype('BauhausRegular.ttf', size=24), fill=200)
        return image

    def __init__(self) -> None:
        self.board = self.__build_board()
        self.image_path = chessboard

    def draw_line_from_points(self, start: tuple, end: tuple, image = None) -> Image:
        x1, y1 = self.__pos_to_px(*start)
        x2, y2 = self.__pos_to_px(*end)
        image = image or Image.open(self.image_path)

        draw = ImageDraw.Draw(image)
        draw.line((y1, x1, y2, x2), fill=100, width=10)
        for pos in [(y1-15, x1-15, y1+15, x1+15), (y2-15, x2-15, y2+15, x2+15)]:
            draw.ellipse(pos, fill=50, width=30)

        return image

    def draw_knight_move(self, start: tuple, end: tuple, image: Image = None, step: int = 0) -> Image:
        x, y = start
        path = list()
        for x2, y2, direction in [(2, 0, 'h'), (0, 2, 'v'), (-2, 0, 'h'), (0, -2, 'v')]:
            new_x, new_y = x + x2, y + y2
            if self.__vaild_pos(new_x, new_y):
                if direction == 'h':
                    if ((new_x, new_y+1) == end):
                        path = [(new_x, new_y), (new_x, new_y+1)]
                        break
                    elif ((new_x, new_y-1) == end):
                        path = [(new_x, new_y), (new_x, new_y-1)]
                        break
                else:
                    if ((new_x+1, new_y) == end):
                        path = [(new_x, new_y), (new_x+1, new_y)]
                        break
                    elif ((new_x-1, new_y) == end):
                        path = [(new_x, new_y), (new_x-1, new_y)]
                        break

        if path == []:
            raise ValueError(f'Path is empty! - Check if the start{start} and end{end} pos is vaild!') 

        image = image or Image.open(self.image_path)
        image = self.draw_line_from_points(start, path[0], image)
        image = self.draw_line_from_points(path[0], path[1], image)
        image = self.__draw_step_at_pos(end, step, image)
        return image
            


yuki = Yuki()

# image = yuki.draw_knight_move((1, 2), (3, 3))
# image = yuki.draw_knight_move((3, 3), (2, 5), image)
# image = yuki.draw_knight_move((4, 6), (2, 5), image)
# image.show()
