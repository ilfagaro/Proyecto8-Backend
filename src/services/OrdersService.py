from src.database.dbmysql import get_connection
from src.models.ordersModel import Orders

class OrdersService():
    @classmethod
    def get_orders(cls):
        try:
            connection=get_connection()
            print(connection)

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM orders")
                result = cursor.fetchall()
                print(result)

            connection.close()
            return 0

        except Exception as ex:

            print(ex)
    @classmethod
    def post_orders(self, orders: Orders):
        try:
            connection=get_connection() 
            print(connection)   

            with connection.cursor() as cursor:
                ID_Order = orders.ID_Order
                Date_Order = orders.Date_Order
                State_Order = orders.State_Order
                ID_User_FK = orders.ID_User_FK
                ID_Product_FK = orders.ID_Product_FK

                cursor.execute("INSERT INTO orders (ID_Order, Date_Order, State_Order, ID_User_FK, ID_Product_FK)"+
                                "VALUES ('{0}', '{1}', '{2}', '{3}', '{4}');"
                                .format(ID_Order, Date_Order, State_Order, ID_User_FK, ID_Product_FK))

                connection.commit()
                                  
            connection.close()

            return 0

        except Exception as ex:

            print(ex)
@classmethod
def update_orders(self, orders: Orders):
        try:
            connection=get_connection()
            print(connection)

            with connection.cursor() as cursor:
                ID_Order = orders.ID_Order
                Date_Order = orders.Date_Order
                State_Order = orders.State_Order
                ID_User_FK = orders.ID_User_FK
                ID_Product_FK = orders.ID_Product_FK

                cursor.execute("UPDATE orders SET Date_Order = '{0}', State_Order = '{1}', ID_User_FK = '{2}', ID_Product_FK = '{3}' WHERE ID_Order = '{4}';"
                                .format(Date_Order, State_Order, ID_User_FK, ID_Product_FK, ID_Order))

                connection.commit()
                                  
            connection.close()

            return "Pedidos actualizado"

        except Exception as ex:

            print(ex)

@classmethod
def delete_orders(self, orders: Orders):  
        try:
            connection=get_connection()
            print(connection)

            with connection.cursor() as cursor:
                ID_Order = orders.ID_Order

                cursor.execute("DELETE FROM orders WHERE ID_Order = '{0}';"    
                                .format(ID_Order))

                connection.commit()

            connection.close()

            return "Pedido eliminado"

        except Exception as ex:
                
                print(ex)     