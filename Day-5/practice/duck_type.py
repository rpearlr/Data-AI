class PyCharm :
    def execute(self) :
        print("This is a Pycharm")

class VsCode :
    def execute(self) :
        print("This is a Vscode")

def code(editor) :
    editor.execute()
    
code(PyCharm())
code(VsCode())