class Donante(object):
    """
    Class used to represent a donanate
    """

    def __init__(self, numtel: int = 1, name: str = 'Name', surname: str = "surname", email: str = "ejem@gmail.com", direccion: str = 'pozonM166',) -> object:
        """ Person constructor object.

        :param numtel: numero de telefono del donante
        :type numtel: int
        :param name: nombre del donante
        :type name: str
        :param surname: apellido del donante
        :type surname: str
        :returns: Donante object
        :rtype: object
        :param email: email of voluntario
        :type email: str

        """
        self.__numtel = numtel
        self.__name = name
        self.__surname = surname
        self.__email = email
        self.__direccion = direccion

    @property
    def numtel(self) -> int:
        """ Returns idn of the student.
          :returns: idn of student.
          :rtype: int
        """
        return str(self.__numtel)

    @numtel.setter
    def numtel(self, val: int):
        """ The id of the student.
        :param id: id of student.
        :type: int
        """
        self.__numtel = val

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
    def direccion(self) -> str:
        """ Returns the last name of the student.
          :returns: last name of student.
          :rtype: str
        """
        return self.__direccion

    @direccion.setter
    def intereses(self, direccion: str):
        """ The last name of the student.
        :param surname: last name of student.
        :type: str
        """
        self.__intereses = direccion

    def __str__(self):
        return dict(numtel=self.numtel, name=self.name, surname=self.surname, email=self.email, direccion=self.direccion).__str__()


if __name__ == '__main__':

    david = Donante(numtel=23456, name="harlem", surname="hernandez", email="adreess@.com", direccion="pozon" )
    print(david)
    juan = Donante()
    print(juan)
