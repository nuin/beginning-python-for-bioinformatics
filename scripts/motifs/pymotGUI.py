#!/usr/bin/env python

import wx
import pymot
import fasta

class pymot(wx.App):

    def __init__(self, redirect=False):
        wx.App.__init__(self, redirect)

class pymotGUI(wx.Frame):
    
    def __init__(self, parent, id):
        
        wx.Frame.__init__(self, parent, id,  'Python Motif Finder', style=wx.DEFAULT_FRAME_STYLE)
        self.__do_layout()
#        self.__do_binding()

    def __do_layout(self):
        #defines the menubar
        menubar = wx.MenuBar()
        
        #file menu
        filemenu = wx.Menu()
        self.convertmenu = filemenu.Append(-1, 'Select foreground file')
        self.seqmenu = filemenu.Append(-1, 'Select background file')
        self.treemenu = filemenu.AppendSeparator()
        self.treenooutmenu = filemenu.Append(-1, 'Quit')
        
        #appends the menu to the menubar and creates it
        menubar.Append(filemenu, 'File')
        self.SetMenuBar(menubar)


#if __name__ == '__main__':
app = pymot()
frame = pymotGUI(parent=None, id = -1)
#frame.CentreOnScreen()
frame.Show()
app.MainLoop()