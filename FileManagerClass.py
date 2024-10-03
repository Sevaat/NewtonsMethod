from tkinter import filedialog
from NodeClass import Node
from SystemClass import System
from BranchClass import Branch


class FileManager():
    
    @staticmethod
    def save_file():
        filepath = filedialog.asksaveasfilename(
            title = 'Сохранение файла',
            defaultextension = 'txt',
            initialfile = 'Input.txt'
            )
        if filepath != "":
            with open(filepath, "w") as file:
                pass
    
    @staticmethod
    def open_file():
        filepath = filedialog.askopenfilename(
            title = 'Загрузка файла',
            defaultextension = 'txt',
            initialfile = 'Output.txt'
            )
        if filepath != "":
            system = FileManager.get_system(filepath)
            nodes = FileManager.get_nodes(filepath, system)
            branches = FileManager.get_branches(filepath)
                    
            return system, nodes, branches

    @staticmethod
    def get_system(filepath):
        with open(filepath, "r") as file:
            while True:
                line = file.readline().strip()
                if line == 'НАСТРОЙКИ ПРОГРАММЫ РАСЧЕТА':
                    line = file.readline().strip().split('/')
                    
                    return System(float(line[0]), float(line[1]))
    
    @staticmethod
    def get_nodes(filepath, system):
        with open(filepath, "r") as file:
            while True:
                line = file.readline().strip()
                if line == 'ДАННЫЕ УЗЛОВ':
                    nodes = []
                    while True:
                        line = file.readline().strip()
                        if line == 'ДАННЫЕ ВЕТВЕЙ':
                            return nodes
                        else:
                            line = line.split('/')
                            for i in range(1, len(line)):
                                if line[i] == 'inf':
                                   line[i] = float('inf')
                                else:
                                    line[i] = float(line[i])
                            node = Node(line[0], line[1], line[2], line[3])
                            node.initial_voltage(system)
                            nodes.append(node)
    
    @staticmethod
    def get_branches(filepath):
        with open(filepath, "r") as file:
            while True:
                line = file.readline().strip()
                if line == 'ДАННЫЕ ВЕТВЕЙ':
                    branches = []
                    while True:
                        line = file.readline().strip()
                        if line == 'КОНЕЦ':
                            return branches
                        else:
                            line = line.split('/')
                            for i in range(2, len(line)):
                                line[i] = float(line[i])
                            if len(line) == 6:
                                branches.append(Branch(line[0], line[1], line[2], line[3], line[4], line[5]))
                            else:
                                branches.append(Branch(line[0], line[1], line[2], line[3], line[4]))