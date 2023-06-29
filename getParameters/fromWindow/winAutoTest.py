from pywinauto import findwindows
from pywinauto.application import Application

def screen(n):
    app = Application().connect(title_re='Покер')
    wnd = app.window(title_re='NLHP')
    wnd.capture_as_image().save('spoq' + str(n) + '.png')

#for i in range (24, 35):
 #   print('spoq' + str(i))
  #  input()
   # screen(i)