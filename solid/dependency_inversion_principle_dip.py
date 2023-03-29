""" This module has an example of the Dependency Inversion Principle(DIP) in
    Python.
"""


from abc import ABC, abstractmethod


# This is a tightly coupled example that violates the Dependency Inversion
# Principle (DIP) as the class MySQLStorageBadExample is called directly
# without using an abstraction.
class MySQLStorageBadExample():
    """ This is the implementation of MySQL storage.
    """

    def get(self):
        """ Get data
        """
        print("Get data from MySQL database")

    def set(self, data):
        """ Set data
        """
        print(f"Set {data} into MySQL database")


class UseCaseBadExample():
    """ This is the main class of the application.
    """
    def run(self):
        """ This is the main method of the use case.
        """
        bad_storage = MySQLStorageBadExample()
        bad_storage.get()
        bad_storage.set({"data": "Hello World"})


if __name__ == "__main__":
    use_case_bad_example = UseCaseBadExample()
    use_case_bad_example.run()


# This is a loosely coupled example that follows the Dependency Inversion
# Principle (DIP) as the class MySQLStorage is called using the
# abstract class Storage.
class Storage (ABC):
    """ This is the abstract class for the storage.
    """

    @abstractmethod
    def get(self):
        """ Get data
        """

    @abstractmethod
    def set(self, data):
        """ Set data
        """


class MySQLStorage(Storage):
    """ This is the implementation of MySQL storage.
    """

    def get(self):
        print("Get data from MySQL database")

    def set(self, data):
        print(f"Set {data} into MySQL database")


class CSVFileStorage(Storage):
    """ This is the implementation of CSV storage.
    """

    def get(self):
        print("Get data from CSV storage")

    def set(self, data):
        print(f"Set {data} into CSV storage")


class UseCase():
    """ This is the main class of the application.
    """
    def run(self, storage: Storage):
        """ This is the main method of the use case.
        """
        storage.get()
        storage.set({"data": "Hello World"})


if __name__ == "__main__":
    use_case = UseCase()
    use_case.run(MySQLStorage())
    use_case.run(CSVFileStorage())

# Consequently, following the Dependency Inversion Principle we can improve our
# code maintainability and flexibility because it will depend less on lower
# classes (like MySQLStorage in our example) and we can even use more than one
# lower class without changing the higher class (eg UseCase).
