import sys, os

sys.path.append("./EduTK.python.zip")
sys.path.append("../EduTK.python.zip")

if ('EPEIOS_SRC' in os.environ):
  sys.path.append("/cygdrive/h/hg/epeios/other/libs/edutk/PYH/edutk")

import edutk as _

from edutk import Atlas, Core, core, dom, readBody, recall, store

# Uncomment for exceptions behaving normally again
# instead of being displayed in a alert box.
# _.regularException = True

F_MY_FUNCTION = "MyFunction"
F_CONNECT = "Connect"
F_SUBMIT = "Submit"
F_RESTART = "Restart"
F_HANGMAN = "Hangman"

def _defineUserFunction(name):
  _.defineUserFunction(globals(), "uf", name)

_defineUserFunction(F_MY_FUNCTION)
_defineUserFunction(F_CONNECT)
_defineUserFunction(F_SUBMIT)
_defineUserFunction(F_RESTART)
_defineUserFunction(F_HANGMAN)


def mainBase(folder, callback, callbacks, ids, globals, userFunctionLabels, title):
  if ids:
    _.setUserFunctions(ids, globals, userFunctionLabels)
  _.main(folder, callback, callbacks, title)
