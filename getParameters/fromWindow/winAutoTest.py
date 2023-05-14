from pywinauto import findwindows
from pywinauto.application import Application
app = Application().connect(title_re='NLHP')
wnd = app.window(title_re='NLHP')
wnd.capture_as_image().save('scad2.png')