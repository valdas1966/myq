class Topic:

    def __init__(self, name, priority):
        """
        ========================================================================
         Description: Constructor. Init the Arguments.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. name : str (Topic Name like: Programming Language -> Html).
            2. priority : str (A | B | C).
        ========================================================================
        """
        assert type(name) == str
        assert type(priority) == str
        self.name = name
        self.priority = priority
        self.level = self.name.count('->')

    def __str__(self):
        """
        ========================================================================
         Description: Return Str-Representation of the Topic.
        ========================================================================
         Return: str ('Programming Language -> Html -> Basic: B')
        ========================================================================
        """
        return f'{self.name}: {self.priority}'

    def __repr__(self):
        """
        ========================================================================
         Description: Return Str-Representation of the Topic.
        ========================================================================
         Return: str ('Programming Language -> Html -> Basic: B')
        ========================================================================
        """
        return self.__str__()
