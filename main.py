#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.1.0b1 on Sat Aug  3 20:26:58 2024
#

import wx
from record import RecordMouseMovement
from repro import ReproductionMouse
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.SetTitle("frame")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, u"ファイル名")
        sizer_1.Add(label_1, 0, 0, 0)

        self.text_ctrl_1 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        sizer_1.Add(self.text_ctrl_1, 0, 0, 0)

        # 繰り返し
        label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, u"繰り返し回数")
        sizer_1.Add(label_2, 0, 0, 0)

        self.text_ctrl_2 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        sizer_1.Add(self.text_ctrl_2, 0, 0, 0)

        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)

        self.button_1 = wx.Button(self.panel_1, wx.ID_ANY, u"記録")
        sizer_2.Add(self.button_1, 0, 0, 0)

        self.button_2 = wx.Button(self.panel_1, wx.ID_ANY, u"再現")
        sizer_2.Add(self.button_2, 0, 0, 0)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()

        self.button_1.Bind(wx.EVT_BUTTON, self.btn_record)
        self.button_2.Bind(wx.EVT_BUTTON, self.btn_repro)
        # end wxGlade

    def btn_record(self, event):  # wxGlade: MyFrame.<event_handler>
        '''記録ボタンを押された'''
        record = RecordMouseMovement()
        text=self.text_ctrl_1.GetValue()
        record.start(filename=text)
        event.Skip()

    def btn_repro(self, event):  # wxGlade: MyFrame.<event_handler>
        '''再現ボタンが押された'''
        name=self.text_ctrl_1.GetValue()
        num=self.text_ctrl_2.GetValue()
        repro = ReproductionMouse(int(num))
        repro.get_content(filename=name)
        event.Skip()

# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
