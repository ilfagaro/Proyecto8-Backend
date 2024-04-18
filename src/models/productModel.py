class ProductModel():
    def __init__(self, id_product, Name_Product, Description_Product, Price_Product, Dimension_Product, State_product, ID_User_FK, ID_Category_FK) -> None: 

        self.id_product = id_product
        self.Name_Product = Name_Product
        self.Description_Product = Description_Product
        self.Price_Product = Price_Product
        self.Dimension_Product = Dimension_Product
        self.State_Product = State_product
        self.ID_User_FK = ID_User_FK
        self.ID_Category_FK = ID_Category_FK