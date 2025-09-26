class Product:
    product_counter = 0   # Class variable to keep track of product IDs
    inventory = [] # Class variable to store all product objects in a list
    
    def __init__(self, name, product_id,category,quantity,price,supplier):
        self.name = name
        self.product_id = product_id
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier
    
    #class method to add a new product to the inventory
    @classmethod
    def add_product(cls, name, category, quantity, price, supplier):
        cls.product_counter += 1  
        new_product = cls(name, cls.product_counter, category, quantity, price, supplier)
        cls.inventory.append(new_product)
        return "Product added successfully"
    
    #class method to update an existing product's quantity, price, and supplier
    @classmethod
    def update_product(cls, product_id, quantity, price, supplier):
        for product in cls.inventory:
            if product.product_id == product_id:
                product.quantity = quantity
                product.price = price
                product.supplier = supplier
                return "Product information updated successfully"
        return "Product not found"

    #class method to delete a product from the inventory by ID
    @classmethod
    def delete_product(cls, product_id):
        for product in cls.inventory:
            if product.product_id == product_id:
                cls.inventory.remove(product)
                return "Product deleted successfully"
        return "Product not found"
    
    # Class method to display the current inventory
    @classmethod
    def view_inventory(cls):
        if not cls.inventory:
            print("Inventory is empty.")
            return
        print("Current Inventory:")
        for product in cls.inventory:
            print(f"ID: {product.product_id}, Name: {product.name}, Category: {product.category}, "
                  f"Quantity: {product.quantity}, Price: {product.price}, Supplier: {product.supplier}")
        return ""
    
    class Order:
        def __init__(self, order_id, product_id, quantity):
            self.order_id = order_id
            self.product_id = product_id
            self.quantity = quantity
   

# Usage         
p1 = Product.add_product("TV", "Electronics", 10, 10000, "TechSupplier")
p2 = Product.add_product("Laptop", "Electronics", 5, 32000, "MobileStore")
p3 = Product.add_product("Smartphone", "Electronics", 15, 20000, "MobileStore")
p4 = Product.add_product("Camera", "Photography", 7, 35000, "PhotoStore")

#display inventory
view = Product.view_inventory()
print(view)

#delete product with ID 3 (Smartphone)
delete = Product.delete_product(3)
print(delete)

#add a new product: Tablet
add = Product.add_product("Tablet", "Electronics", 8, 15000, "GadgetWorld")
print(add)

#update product with ID 2 (Laptop): change quantity, price, and supplier
update = Product.update_product(2, 8, 30000, "TechSupplier")
print(update)

#view inventory again
view = Product.view_inventory()
print(view)
