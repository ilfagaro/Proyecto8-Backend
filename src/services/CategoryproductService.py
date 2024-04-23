from src.database.dbmysql import get_connection
from src.models.categoryproductModel import Categoryproduct

class CategoryproductService():
    @classmethod
    def get_categoryproduct(cls):
        try:
            connection=get_connection()
            print(connection)

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM categoryproduct")
                result = cursor.fetchall()
                print(result)             

            connection.close()
            return 0    

        except Exception as ex:

            print(ex)
    @classmethod
    def post_categoryproduct(self, categoryproduct: Categoryproduct):
        try:
            connection=get_connection()
            print(connection)

            with connection.cursor() as cursor:
                ID_CategoryProduct = categoryproduct.ID_CategoryProduct
                Name_CategoryProduct = categoryproduct.Name_CategoryProduct

                cursor.execute("INSERT INTO categoryproduct (ID_CategoryProduct, Name_CategoryProduct)"+
                                "VALUES ('{0}', '{1}');"
                                .format(ID_CategoryProduct, Name_CategoryProduct))

                connection.commit()

            connection.close()

            return 0

        except Exception as ex:

            print(ex)        