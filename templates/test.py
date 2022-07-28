import arithmetic
from unittest import TestCase
from app import app

# TEST METHODS MUST START WITH text_ UNDERSCORE!!!
# TO RUN use python -m unittest NAME_OF_FILE
# assertEqual, assertTrue, assertFalse, assertRaises(exception,function, argument)

# class Test(TestCase):

#     def test_adder(self):
#         assert arithmetic.adder(2,3) == 5
#     def test_example(self):
#         self.assertEqual(arithmetic.adder(2,2),4)

class RenderBoard(TestCase):
    def test_render_board(self):
        #client refers to our server 
        with app.test_client() as client: 
            res = client.get('/')