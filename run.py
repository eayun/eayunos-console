from login import *
from productInfo import *
from checkbox import *
import globalInput

palette = [
       ('I say', 'yellow', 'light gray', 'bold'),
       ('btn', 'yellow', 'light gray', 'bold'),
       ('banner', 'yellow', 'light gray'),
       ('streak', 'yellow', 'light gray'),
       ('buttnf','white','dark blue','bold'),
       ]

loop = urwid.MainLoop(None, palette)

l = LogIn(loop)
p = Product(loop)
c = CheckBox(loop)

go_trial = [None, None]
go_login = l.get_widget()
go_product = p.get_widget()
go_checkbox = c.get_widget()

l.set_widgetList_other(go_trial, go_product)
p.set_widgetList_other(go_login, go_checkbox)
c.set_widgetList_other(go_product, go_login)

loop.widget = go_login[0]
loop.palette = go_login[1]

if __name__ == '__main__':
   loop.run() 
   #urwid.MainLoop(loop.widget, loop.palette).run()
