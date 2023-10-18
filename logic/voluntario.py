class Voluntario(object):
    """
    Class used to represent a voluntario
    """

    def __init__(self, number: int = 1, name: str = 'Name', surname: str = "surname", email: str = "email", intereses: str = 'intereses') -> object:
        """ Person constructor object.

        :param idn: A unique number that uniquely identifies the voluntario in the system.
        :type idn: int
        :param name: name of student.
        :type name: str
        :param surname: last name of voluntario.
        :type surname: str
        :param email: email of voluntario
        :type email: str
        :returns: Voluntario object
        :rtype: object
        """
        self.__number = number
        self.__name = name
        self.__surname = surname
        self.__email = email
        self.__intereses = intereses

    @property
    def number(self) -> int:
        """ Returns idn of the student.
          :returns: idn of student.
          :rtype: int
        """
        return str(self.__number)

    @number.setter
    def idn(self, val: int):
        """ The id of the student.
        :param id: id of student.
        :type: int
        """
        self.__number = val

    @property
    def name(self) -> str:
        """ Returns the name of the student.
          :returns: name of student.
          :rtype: str
        """
        return self.__name

    @name.setter
    def name(self, name: str):
        """ The name of the student.
        :param name: name of student.
        :type: str
        """
        self.__name = name

    @property
    def surname(self) -> str:
        """ Returns the last name of the student.
          :returns: last name of student.
          :rtype: str
        """
        return self.__surname

    @surname.setter
    def surname(self, surname: str):
        """ The last name of the student.
        :param surname: last name of student.
        :type: str
        """
        self.__surname = surname
    
    @property
    def email(self) -> str:
        """ Returns the last name of the student.
        :returns: last name of student.
        :rtype: str
        """
        return self.__email

    @email.setter
    def surname(self, email: str):
        """ The last name of the student.
        :param surname: last name of student.
        :type: str
        """
        self.__email = email

    @property
    def intereses(self) -> str:
        """ Returns the last name of the student.
          :returns: last name of student.
          :rtype: str
        """
        return self.__intereses

    @intereses.setter
    def intereses(self, intereses: str):
        """ The last name of the student.
        :param surname: last name of student.
        :type: str
        """
        self.__intereses = intereses

    def __str__(self):
        return dict(idn=self.idn, name=self.name, surname=self.surname).__str__()


if __name__ == '__main__':

    edwin = Voluntario(number=23456, name="Edwin", surname="Puertas", email="adreess@.com", intereses="el campo" )
    print(edwin)
    juan = Voluntario()
    print(juan)
