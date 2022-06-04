import pytest
from yuki import Yuki

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