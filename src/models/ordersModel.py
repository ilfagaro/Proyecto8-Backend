class OrdersModel():
    def __init__(self, ID_Order, Date_Order, State_Order, ID_User_FK, ID_Product_FK) -> None:
                 
        self.ID_Order = ID_Order
        self.Date_Order = Date_Order
        self.State_Order = State_Order
        self.ID_User_FK = ID_User_FK
        self.ID_Product_FK = ID_Product_FK
        