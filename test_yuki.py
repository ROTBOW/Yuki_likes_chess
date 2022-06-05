from yuki import Yuki
from PIL import Image
import pytest
import os

dir_path = os.path.dirname(os.path.realpath(__file__)) + r'\test_images'
my_girl = Yuki()

def test_yuki_board():
    '''
    Test that yuki starts with a vaild internal board.
    '''
    assert my_girl.board == [[0]*8] * 8

def test_yuki_board_image_path():
    '''
    Ensures that yuki starts with the board image
    '''
    assert my_girl.image_path == r'C:\Users\Josiah\Desktop\random coding stuff\Yuki\Chess_Board.png'

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