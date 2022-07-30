from unittest import TestCase
from app import app # means from app.py import app
from boggle import Boggle
from flask import session


# TEST METHODS MUST START WITH test_ UNDERSCORE!!!
# TO RUN use python -m unittest NAME_OF_FILEs

class BoggleTests(TestCase):

    def setUp(self):
        """Runs before any other test"""
        # code below - if we get errors we get it in python format rather than default flask error messages 
        app.config['TESTING'] = True


    def test_render_board(self):
        #client refers to our server 
        with app.test_client() as client: 
            res = client.get('/')
            # html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)

    def test_check_word(self):
        with app.test_client() as client:
            client.get('/')
            res = client.get('/check-word?word=spaghetti')
            # html = res.get_data(as_text=True)
            self.assertEqual(res.json['result'],'not-on-board')

      

    def test_num_plays(self):
        """check if num plays is 1 on first play"""
        with app.test_client() as client: 
            res = client.post('/nplays')
            self.assertEqual(session['nplays'],1)


