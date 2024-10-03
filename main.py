#from TestClass import DataTest
from NewtonsMethodClass import NewtonsMethod
from FileManagerClass import FileManager

system, nodes, branches = FileManager.open_file()
print('Начало рассчета!')
print(NewtonsMethod.solver(system, nodes, branches))