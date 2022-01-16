class StringHelper:

    def __init__(self, string):
        self.__string = string

    def upper_case(self):
        return self.__string.upper()


class TextHelper:

    @staticmethod
    def upper_case(list):
        for i in range(len(list)):
            obj = StringHelper(list[i])
            new_str = obj.upper_case()
            list[i] = new_str
