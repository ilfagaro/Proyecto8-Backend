from src.database.dbmysql import get_connection
from src.models.personModel import Person

class PersonService():
    @classmethod
    def get_person(cls):
        try:
            connection=get_connection()
            print(connection)

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM person")
                result = cursor.fetchone()
                print(result)
                           
            connection.close()
            return 0

        except Exception as ex:

            print(ex)

    @classmethod
    def post_person(cls, person: Person):
        try:
            connection=get_connection()
            print(connection)

            with connection.cursor() as cursor:
                DNI_Person = person.DNI_Person
                Name_Person = person.Name_Person
                Email_Person = person.Email_Person
                Adress_Person = person.Adress_Person
                Telephone_Person = person.Telephone_Person

                cursor.execute("INSERT INTO person (DNI_Person, Name_Person, Email_Person, Adress_Person, Telephone_Person)"+
                                "VALUES ('{0}', '{1}', '{2}', '{3}', '{4}');"
                                .format(DNI_Person, Name_Person, Email_Person, Adress_Person, Telephone_Person))

                connection.commit()
                                  
            connection.close()
            return " Persona añadida"    

        except Exception as ex:

            print(ex)

    @classmethod
    def update_person(cls, person: Person):
        try:
            connection=get_connection()
            print(connection)

            with connection.cursor() as cursor:
                DNI_Person = person.DNI_Person
                Name_Person = person.Name_Person
                Email_Person = person.Email_Person
                Adress_Person = person.Adress_Person
                Telephone_Person = person.Telephone_Person

                cursor.execute("UPDATE person SET Name_Person = '{0}', Email_Person = '{1}', Adress_Person = '{2}', Telephone_Person = '{3}' WHERE DNI_Person = '{4}';"
                                .format(Name_Person, Email_Person, Adress_Person, Telephone_Person, DNI_Person))

                connection.commit()
                                  
            connection.close()

            return " Persona modificada"    

        except Exception as ex:

            print(ex)

    @classmethod
    def delete_person(cls, person: Person):
        try:
            connection=get_connection()
            print(connection)

            with connection.cursor() as cursor:
                DNI_Person = person.DNI_Person

                cursor.execute("DELETE FROM person WHERE DNI_Person = '{0}';"
                                .format(DNI_Person))

                connection.commit()
                                  
            connection.close()

            return " Persona eliminada"    

        except Exception as ex:

            print(ex)