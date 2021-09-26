import os
from f_excel.c_excel import Excel
from topic import Topic
from f_data_structure.node_tree import Node
from f_data_structure.tree import Tree


class Topics:

    # First Relevant Row in Excel
    fr = 2
    # First Relevant Col in Excel
    fc = 2
    # Excel-Topics file is appropriate to Topics in the Folders
    is_valid = None
    # Delimiter in the Topic-Name represents the Topic-Hierarchy
    delimiter = ' -> '
    # Tree of all Topics
    tree = Tree()

    def __init__(self, path_myq):
        """
        ========================================================================
         Description: Constructor. Init the Class Attributes.
        ------------------------------------------------------------------------
            1. tree : Tree of Topic (All Topics in Tree-Hierarchy).
            2. is_valid : bool (Excel-Topics equals to Question-Files.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. path_myq : str (Path to Myq-Directory).
        ========================================================================
        """
        self.path_myq = path_myq
        names_topics = self.__from_excel()
        self.__fill_tree(names_topics)
        self.__check_topics()

    def __from_excel(self):
        """
        ========================================================================
         Description: Extract Topic-Names from Topics-Excel.
        ========================================================================
         Return: list of str (Topic-Names).
        ========================================================================
        """
        xlsx = os.path.join(self.path_myq, 'topics.xlsx')
        excel = Excel(xlsx)
        lr = excel.last_row(self.fr, self.fc)
        names_topics = list()
        for r in range(self.fr, lr+1):
            path_names = list()
            c = self.fc
            while not excel.is_blank(r, c):
                path_names.append(excel.get_value(r, c))
                c = c + 1
            names_topics.append(self.delimiter.join(path_names))
        return names_topics

    def __fill_tree(self, names_topics):
        """
        ========================================================================
         Description: Fill class attribute Tree_Topics with Topics (objects).
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. names_topics : list of str ('English -> Popular 1000 -> A')
        ========================================================================
        """
        for i, name_topic in enumerate(names_topics):
            values = name_topic.split(self.delimiter)
            name = self.delimiter.join(values[:-1])
            priority = values[-1]
            name_parent = 'root'
            if len(values) > 2:
                name_parent = self.delimiter.join(values[:-2])
            parent = self.tree.nodes[name_parent]
            if not parent.name == 'root':
                priority = parent.data.priority + priority
            topic = Topic(name=name, priority=priority, i_row=i+2)
            node = Node(name=name, data=topic)
            self.tree.add(node, parent)              
        
    def __check_topics(self):
        """
        ========================================================================
         Description: Set Private Attribute Is_Valid to True if Excel-Topics
                        file is appropriate to Topics in the Folders.
        ========================================================================
         Return: bool
        ========================================================================
        """
        dir_questions = f'{self.path_myq}\\Questions'
        set_topics = set()
        for root, dirs, files in os.walk(dir_questions):
            for d in dirs:
                set_topics.add(os.path.join(root, d))
            for f in files:
                if f.endswith('.xlsx'):
                    set_topics.add(os.path.join(root, f))
        set_topics = {t.replace(f'{dir_questions}\\', '') for t in set_topics}
        set_topics = {t.replace('.xlsx', '') for t in set_topics}
        set_topics = {t.replace('\\', ' -> ') for t in set_topics}
        set_topics_xlsx = set(self.tree.nodes.keys()) - {'root'}
        self.is_valid = set_topics == set_topics_xlsx
        if not self.is_valid:
            print('Topics is not valid!')
            print(f'Left Join Folders: {set_topics - set_topics_xlsx}')
            print(f'Left Join Excel: {set_topics_xlsx - set_topics}')
