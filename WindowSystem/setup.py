
import os
os.environ['TCL_LIBRARY'] = "C:/Users/JPTrzy/AppData/Local/Programs/Python/Python37/tcl/tcl8.6"
os.environ['TK_LIBRARY'] = "C:/Users/JPTrzy/AppData/Local/Programs/Python/Python37/tcl/tk8.6"

from cx_Freeze import *
e = [Executable("start.py")]
setup(
              name = "name",
              options={"build_exe":{"packages":["pygame"]}},
              description="opis",
              executables = e
              )
