# _*_ coding:utf-8 _*_
import urwid
import globalInput
import ProductInfo

class CheckBox(object):

    def __init__(self, loop, go_product, go_login):
        self.loop = loop
        self.go_product = go_product
        self.go_login = go_login

    palette = [
    ('buttn','yellow','light gray'),
    ('buttnf','white','dark blue','bold'),
    ]

    button_back = urwid.Button(u'  返回')
    button_next = urwid.Button(u' 下一步')
    button_list = [button_back, button_next]
    button = urwid.GridFlow([urwid.AttrWrap(button, 'btn', 'btn') for button in button_list], 12, 5, 0, 'left')

    text_cb_list = [u"Wax", u"导入 ISO 域", u"智能调度", u"虚拟机备份", u"显卡穿透", u"报表"]

    div = urwid.Divider()

    checkbox = urwid.Pile([urwid.AttrWrap(urwid.CheckBox(txt), 'buttn', 'buttnf') for txt in text_cb_list])

    listbox_content = [urwid.Padding(checkbox, left = 0, right = 2, min_width = 7), div, urwid.Padding(button, left = 0, right = 2, min_width = 7)]

    listbox = urwid.ListBox(urwid.SimpleListWalker(listbox_content))
    frame = urwid.Frame(urwid.AttrWrap(listbox, 'body'))

    def go_back(self, button):
       loop.widget = self.go_product

    def go_next(self, button):
       loop.widget = go_login

    urwid.connect_signal(button_back, 'click', go_back)
    urwid.connect_signal(button_next, 'click', go_next)
    
    def get_frame(self):
       return frame
