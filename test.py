from pywinauto import application
import time

app = application.Application()
app.start("putty.exe")
app.putty.edit.TypeKeys("enzenglobal.tk")

