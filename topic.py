class Topic:

    def __init__(self, name, priority, i_row):
        """
        ========================================================================
         Description: Constructor. Init the Arguments.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. name : str (Topic Name like: Programming Language -> Html).
            2. priority : str of Priority (A | B | C | AAB | ABBA).
            3. i_row : int (Number of Row in Excel-Topics).
        ========================================================================
        """
        assert type(name) == str
        assert type(priority) == str
        assert type(i_row) == int
        self.name = name
        self.priority = priority
        self.i_row = i_row
        self.level = self.name.count('->')

    def __str__(self):
        """
        ========================================================================
         Description: Return Str-Representation of the Topic.
        ========================================================================
         Return: str ('Programming Language -> Html -> Basic: B')
        ========================================================================
        """
        return self.name

    def __repr__(self):
        """
        ========================================================================
         Description: Return Str-Representation of the Topic.
        ========================================================================
         Return: str ('Programming Language -> Html -> Basic: B')
        ========================================================================
        """
        return self.__str__()

    def __eq__(self, other):
        """
        ========================================================================
         Description: Return True if Self is equals to Other.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. other : Topic
        ========================================================================
         Return: bool
        ========================================================================
        """
        assert type(other) == Topic
        return self.name == other.name

    def __hash__(self):
        """
        ========================================================================
         Description: Return Hash  of the Topic (Row Number in Excel-Topics).
        ========================================================================
         Return: int
        ========================================================================
        """
        return self.i_row

    def __lt__(self, other):
        return self.i_row < other.i_row

    def __le__(self, other):
        return self.i_row <= other.i_row

    def __gt__(self, other):
        return self.i_row > other.i_row

    def __ge__(self, other):
        return self.i_row >= other.i_row
