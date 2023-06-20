from pywinauto import findwindows
from pywinauto.application import Application
def screen():
    app = Application().connect(title_re='Покер')
    wnd = app.window(title_re='NLHP')
    wnd.capture_as_image().save('preFlopDesk.png')