from src.database.dbmysql import get_connection
from src.models.productModel import Product

class ProductService(): 

    @classmethod
    def get_product(cls):
        try:
            connection=get_connection()
            print(connection)

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM product")
                result = cursor.fetchone()
                print(result)
                           
            connection.close()
            return 0

        except Exception as ex:

            print(ex)
    @classmethod
    def post_product(cls,product: Product):   
        try:
            connection=get_connection()
            print(connection)

            with connection.cursor() as cursor:
                ID_Product = product.id_product
                Name_Product = product.Name_Product
                Description_Product = product.Description_Product
                Price_Product = product.Price_Product
                Dimension_Product = product.Dimension_Product
                State_Product = product.State_Product
                ID_User_FK = product.ID_User_FK
                ID_Category_FK = product.ID_Category_FK

                cursor.execute("INSERT INTO product (ID_Product, Name_Product, Description_Product, Price_Product, Dimension_Product, State_Product, ID_User_FK, ID_Category_FK)"+
                                "VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}');"
                                .format(ID_Product, Name_Product, Description_Product, Price_Product, Dimension_Product, State_Product, ID_User_FK, ID_Category_FK))

                connection.commit()
                                  
            connection.close()

            return 0

        except Exception as ex:

            print(ex)

    @classmethod
    def update_product(cls, product: Product):
        try:

            connection=get_connection()
            print(connection)

            with connection.cursor() as cursor:
                id_product = product.id_product
                Name_Product = product.Name_Product
                Description_Product = product.Description_Product
                Price_Product = product.Price_Product
                Dimension_Product = product.Dimension_Product
                State_product = product.State_Product
                Id_user_fk = product.ID_User_FK
                ID_catedory_fk = product.ID_Catedory_FK

                cursor.execute("UPDATE product SET Name_Product = '{0}', Description_Product = '{1}', Price_Product = '{2}', Dimension_Product = '{3}', State_Product = '{4}', ID_User_FK = '{5}', ID_Catedory_FK = '{6}' WHERE ID_Product = '{7}';"
                                .format(Name_Product, Description_Product, Price_Product, Dimension_Product, State_product, Id_user_fk, ID_catedory_fk, id_product))

                connection.commit()

            connection.close()

            return "Producto modificado"

        except Exception as ex:

            print(ex)

    @classmethod
    def delete_product(cls, product: Product):   
        try:
            connection=get_connection()
            print(connection)

            with connection.cursor() as cursor:
                id_product = product.id_product

                cursor.execute("DELETE FROM product WHERE ID_Product = '{0}';" 
                               .format(id_product)) 

                connection.commit()

            connection.close()

            return "Producto eliminado"   

        except Exception as ex:
            print(ex) 

