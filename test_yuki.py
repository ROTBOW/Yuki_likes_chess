from yuki import Yuki
from PIL import Image
import pytest
import os

dir_path = os.path.dirname(os.path.realpath(__file__)) + r'\test_images'
my_girl = Yuki()

def test_yuki_has_board_image_path():
    '''
    Ensures that yuki starts with the board image path
    '''
    path = r'C:\Users\Josiah\Desktop\random coding stuff\Yuki\Chess_Board.png'
    assert my_girl.image_path == path

def test_yuki_can_draw_line_between_points():
    '''
    Tests that Yuki can draw lines between points on an image
    '''
    get = my_girl.draw_line_from_points((3, 1), (3, 6))
    want = Image.open(dir_path+r'\test_1.png')
    assert list(get.getdata()) == list(want.getdata())

def test_yuki_can_draw_knights_L():
    '''
    Tests that Yuki can Draw the knight's L shape movement
    '''
    get = my_girl.draw_knight_move((1, 2), (3, 3))
    want = Image.open(dir_path+r'\test_2.png')
    assert list(get.getdata()) == list(want.getdata())


def test_yuki_gets_paths():
    my_girl.build_knight_paths((0,0), (5, 5))
    get = (len(my_girl.paths), min(my_girl.paths))
    want = (67, [(0, 0), (2, 1), (0, 2), (2, 3), (0, 4), (2, 5), (0, 6), (2, 7), (0, 8), (1, 6), (3, 7), (1, 8), (2, 6), (0, 5), (0, 7), (2, 8), (4, 7), (6, 8), (6, 6), (5, 5)])
    assert get == want