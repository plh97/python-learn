from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
m = PyMouse()
k = PyKeyboard()

x_dim, y_dim = m.screen_size()



for i in range(1000):
    # time.sleep(0.05)
    m.click(x_dim*0.8, y_dim/2, 1)


# k.type_string('Hello, World!')