import pyodbc


class Connection:
    server = "DESKTOP-RVDEQLA"
    database = "Indian_Medicine"
    username = ""
    password = ""

    def windows_authentication(self):
        connection = pyodbc.connect('Trusted_Connection=yes', driver='{SQL Server}', server=self.server,
                                    database=self.database)
        cursor = connection.cursor()
        return cursor
