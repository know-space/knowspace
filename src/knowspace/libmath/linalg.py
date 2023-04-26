class Vector:
    def __init__(self, *args) -> None:
        """object used to perform vector math
        """
        self.elements: tuple = args[:]
        self.dimension: float = len(self.elements)
        
    def plus(self, vec_to_add: "Vector") -> "Vector":
        """performs element-wise addition

        :param vec_to_add: vector to be added to the calling vector
        :type vec_to_add: Vector
        :return: vector representing sum of calling vector and argument vector
        :rtype: Vector
        """
        return Vector(*[a + b for a, b in zip(self.elements, vec_to_add.elements)])
    