'''
Yuki is a chess path visualtion program.
'''
from PIL import Image, ImageDraw, ImageFont, ImageColor
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
chessboard = dir_path + '\\Chess_Board.png'


class Yuki:

    def __pos_to_px(self, x: int, y: int) -> tuple:
        step = 140
        return step + (252 * x), step + (252 * y)

    def __vaild_pos(self, x: int, y: int) -> bool:
        return 0 <= x < 9 and 0 <= y < 9

    def __draw_step_at_pos(self, pos: tuple, step: int, image: Image) -> Image:
        draw = ImageDraw.Draw(image)
        x, y = self.__pos_to_px(*pos)
        draw.text((y-6, x-13), str(step), font=ImageFont.truetype('BauhausRegular.ttf', size=24), fill=200)
        return image

    def __draw_path(self, end: tuple, x: int, y: int) -> list:
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
        return path

    def __init__(self) -> None:
        self.image_path = chessboard
        self.paths = []
        self.shortest_path = float('inf')

    def draw_line_from_points(self, start: tuple, end: tuple, image: Image = None) -> Image:
        x1, y1 = self.__pos_to_px(*start)
        x2, y2 = self.__pos_to_px(*end)
        image = image or Image.open(self.image_path)

        draw = ImageDraw.Draw(image)
        draw.line((y1, x1, y2, x2), fill=100, width=10)
        draw.ellipse((y2-15, x2-15, y2+15, x2+15), fill=50, width=30)
        draw.ellipse((y1-15, x1-15, y1+15, x1+15), fill=50, width=30)

        return image

    def draw_knight_move(self, start: tuple, end: tuple, image: Image = None, step: int = 0) -> Image:
        '''
        Draws a line from start pos to the end pos, if used for muiltiple steps needs to build the image backwards
        '''
        x, y = start
        path = self.__draw_path(end, x, y)

        if path == []:
            raise ValueError(f'Path is empty! - Check if the start{start} and/or end{end} pos is vaild!') 

        image = image or Image.open(self.image_path)
        image = self.draw_line_from_points(start, path[0], image)
        image = self.draw_line_from_points(path[0], path[1], image)
        image = self.__draw_step_at_pos(end, step, image)
        return image

    def draw_knight_from_path(self, path: list[tuple]) -> None:
        image = Image.open(self.image_path)
        for step in range(1, len(path)-1, -1):
            start, end = path[step], path[step-1]
            image = self.draw_knight_move(start, end, image, step)
        # image.show()

    def build_knight_paths(self, start: tuple, end: tuple, path: list = []) -> None:
        path = path or [start]

        if len(path) > self.shortest_path:
            return None

        if start == end and path not in self.paths:
            self.shortest_path = min(self.shortest_path, len(path))
            self.paths.append(path)
            return

        for move in [(-2, -1), (-2, 1), (2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]:
            x, y = start[0] + move[0], start[1] + move[1]
            if self.__vaild_pos(x, y) and (x, y) not in path:
                path.append((x, y))
                self.build_knight_paths((x, y), end, path.copy())
        return



            


yuki = Yuki()

# image = yuki.draw_knight_move((2, 5), (0, 6), step=2)
# image = yuki.draw_knight_move((3, 3), (2, 5), image=image, step=1)
# image = yuki.draw_knight_move((1, 2), (3, 3), image=image, step=0)
# image.show()


# yuki.build_knight_paths((0, 0), (5, 5))
# print(len(yuki.paths))
# print(min(yuki.paths))
# yuki.draw_knight_from_path([(1, 2), (3, 3), (2, 5), (0, 6)])

