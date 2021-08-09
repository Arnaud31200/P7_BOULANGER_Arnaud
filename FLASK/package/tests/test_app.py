from package.app import *

# content of test_app.py
def test_home():
    assert home() == render_template('front.html')