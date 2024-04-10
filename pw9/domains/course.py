class Course:
    def __init__(self, name, id, credit):
        self.__id = id
        self.__name = name
        self.__credits = credit
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
    
    def get_credits(self):
        return self.__credits