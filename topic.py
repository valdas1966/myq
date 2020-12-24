class Topic:

    def __init__(self, name, level, priority):
        """
        ========================================================================
         Description: Constructor. Init the Arguments.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. name : str (Topic Name like Programming Language).
            2. level : int (Topic Level - 1 is the top).
            3. priority : str (A | B | C).
        ========================================================================
        """
        assert type(name) == str
        assert type(level) == int
        assert type(priority) == str
        self.name = name
        self.level = level
        self.priority = priority
        self.subtopics = list()

    def nest(self, subtopic):
        """
        ========================================================================
         Description: Nest SubTopic.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. subtopic : Topic
        ========================================================================
        """
        assert type(subtopic) == Topic
        self.subtopics.append(subtopic)
