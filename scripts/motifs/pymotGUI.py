#!/usr/bin/env python

import wx
import pymot
import fasta

class pymot(wx.App):

    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)

class pymotGUI(wx.Frame):
    
    def __init__(self, parent, id):
        
        wx.Frame.__init__(self, parent, id,  'Python Motif Finder', style=wx.DEFAULT_FRAME_STYLE)
        self.__do_layout()
#        self.__do_binding()

    def __do_layout(self):
        pass

#if __name__ == '__main__':
app = pymot()
frame = pymotGUI(parent=None, id = -1)
#frame.CentreOnScreen()
frame.Show()
app.MainLoop()