#!/usr/bin/env python

import wx
import pymot
import pymotif
import fasta
import os

class pymot(wx.App):

    def __init__(self, redirect=False):
        wx.App.__init__(self, redirect)
        

class pymotGUI(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id,  'Python Motif Finder', style=wx.DEFAULT_FRAME_STYLE)
        self.__do_layout()
        self.fore_file = ''
        self.back_file = ''

    def __do_layout(self):
        
        #adding the panel
        panel = wx.Panel(self)
        
        #defines the menubar
        menubar = wx.MenuBar()
        
        #file menu
        filemenu = wx.Menu()
        foreground_menu = filemenu.Append(-1, 'Select foreground file')
        background_menu = filemenu.Append(-1, 'Select background file')
        sep = filemenu.AppendSeparator()
        quitmenu = filemenu.Append(-1, 'Quit')
        
        #appends the menu to the menubar and creates it
        menubar.Append(filemenu, 'File')
        self.SetMenuBar(menubar)

        #input box for motif width, and label
        self.one_label = wx.StaticText(panel, -1, 'Motif width', (10,50))
        self.motif_width = wx.TextCtrl(panel, -1, '10', (95, 50), (40,18))

        #run bbutton
        self.run_button = wx.Button(panel, -1, 'Run', (10, 80))

        #labels
        self.fore_label = wx.StaticText(panel, -1, 'Select the foreground file', (10, 10))
        self.back_label = wx.StaticText(panel, -1, 'Select the background file', (10, 30))

        #binding the menus to functions 
        self.Bind(wx.EVT_MENU, self.on_foreground, foreground_menu)
        self.Bind(wx.EVT_MENU, self.on_background, background_menu)
        self.Bind(wx.EVT_BUTTON, self.run_finder, self.run_button)
        
        
    def on_foreground(self, event):
        dialog = wx.FileDialog(self, style=wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            fore_file = dialog.GetPath()
            self.fore_label.SetLabel(fore_file)

    def on_background(self, event):
        dialog = wx.FileDialog(self, style=wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            back_file = dialog.GetPath()
            self.back_label.SetLabel(back_file)

    def run_finder(self, event):
        pymotif.calculate_motifs(self.fore_file, self.back_file)
        #wx.MessageBox('It should run, eh?')


#if __name__ == '__main__':
app = pymot()
frame = pymotGUI(parent=None, id = -1)
#frame.CentreOnScreen()
frame.Show()
app.MainLoop()