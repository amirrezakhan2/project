class User:
    def __init__(self):
        self.UPA = []
        self.is_login = False

    def register_user(self,Username,Password,address):

        for i in self.UPA:
            if i.split('-')[0] == Username:
                print('Username is alreay Taken')
                return
        info = f'{Username}-{Password}-{address}'
        self.UPA.append(info)
        print('thanks for sign up ')
    
    def login(self,Username,Password):

        for i in self.UPA:

            if i.split('-')[0] == Username and i.split('-')[1] == Password:
                print(f'{Username} welcome')
                self.is_login = True
                return self.is_login
        else:
            print('your Username or Password dose not match')
            return self.is_login

    def show_users(self):  
     
            if not self.UPA:  
                print('No users registered.')  
            else:  
                print('Registered Users:')  
                for user_info in self.UPA:  
                    print(user_info) 


class Product:
    def __init__(self):
        self.shop_item = []

    def add_item(self,Name,price,inventory,detal):

        in_shope = f'{Name}-{price}-{inventory}-{detal}'
        self.shop_item.append(in_shope)

    def Edit_item(self,l_name,Name,price,inventory,detal):

        for i in self.shop_item:
            if i.split('-')[0] == l_name:
                self.shop_item.remove(i)
                in_shop =  f'{Name}-{price}-{inventory}-{detal}'
                self.shop_item.append(in_shop)
    def delete_item(self,name):
        
        for i in self.shop_item:
            if i.split('-')[0] == name:
                self.shop_item.remove(i)
        
    def show_item(self):
        print(self.shop_item)
        for i in self.shop_item:
            print(i)

    def get_items(self):  
        return self.shop_item


class Admin:  
    def __init__(self, product_manager: Product):  
        self.product_manager = product_manager  

    def add_product(self, name, price, inventory, details):  
        return self.product_manager.add_item(name, price, inventory, details)  

    def edit_product(self, old_name, name, price, inventory, details):  
        return self.product_manager.edit_item(old_name, name, price, inventory, details)  

    def delete_product(self, name):  
        return self.product_manager.delete_item(name)  

    def view_products(self):  
        return self.product_manager.show_items()

                
class Shopping_cart:
    def __init__(self):
        self.list_card = []
        self.ordder = []

   
    def add_item_card(self,name,number,item_list):

        while True:
            for i in item_list:
                cs = i.split('-')
                if cs[0] == name:
                    if int(number) <= int(cs[2]):
                        price = int(cs[1])
                        self.list_card.append((name,price,number))

                        return self.get_cart_summary()  
                    
                           
                    else:
                        print('we have not number item you want')

            print('Item not found')
            break        
    
    def get_cart_summary(self):  

        if not self.list_card:  
            return 'Your cart is empty.'  

        total_cost = 0  
        summary = "Your cart contains:\n"  
        for item_name, price, number in self.list_card:  
            item_cost = int(price) * int(number)  
            total_cost += item_cost  
            summary += f"{item_name}: {number} x {price} = {item_cost}\n"  
        summary += f"Total Cost: {total_cost}"
        self.ordder.append(summary)
        return print(summary)

    
   
    def order(self, confirm):  
        if confirm.lower() == 'yes':  
            return '\n'.join(self.orders)  
        return 'Order not confirmed.'
        


    
    def sort_by(self,Criterion,lst):
        
        if Criterion == 'price':
            sort_list = []
            for i in lst :
                cs = i.split('-')
                sort_list.append(f'{cs[0]}:price:{int(cs[1])}')
            sort_list.sort(key=lambda x: int(x.split("price:")[1])) 
            return print(sort_list)
        
        if Criterion == 'inventory':
            sorts_list = []
            for i in lst :
                cs = i.split('-')
                sorts_list.append(f'{cs[0]}:inevntory:{int(cs[2])}')
            sorts_list.sort(key=lambda x: int(x.split("inventory:")[1])) 
            return print(sorts_list)
        
    def serch(self,name,lst):
        for i in lst:
            cs = i.split('-')
            if cs[0] == name :
                return print(f'name:{cs[0]} price:{cs[1]} inventory:{cs[2]}detal:{cs[3]}')
        else:
             return print('item dos not found')





def main():  
    user_manager = User()  
    product_manager = Product()  
    admin = Admin(product_manager)  
    shopping_cart = Shopping_cart()  

    while True:  
        print("\nWelcome to the Shopping System!")  
        print("1. Register")  
        print("2. Login")  
        print("3. Admin Actions")  
        print("4. Add to Cart")  
        print("5. View Cart")  
        print("6. Checkout")  
        print("0. Exit")  
        choice = input("Choose an option: ")  

        if choice == '1':  
            username = input("Enter username: ")  
            password = input("Enter password: ")  
            address = input("Enter address: ")  
            print(user_manager.register_user(username, password, address))  

        elif choice == '2':  
            username = input("Enter username: ")  
            password = input("Enter password: ")  
            print(user_manager.login(username, password))  

        elif choice == '3':  
            print("\nAdmin Actions:")  
            while True:  
                print("1. Add Product")  
                print("2. Edit Product")  
                print("3. Delete Product")  
                print("4. View Products")  
                print("0. Back to first window")  
                admin_choice = input("Choose an option: ")  

                if admin_choice == '1':  
                    name = input("Enter product name: ")  
                    price = input("Enter product price: ")  
                    inventory = input("Enter inventory count: ")  
                    details = input("Enter product details: ")  
                    print(admin.add_product(name, price, inventory, details))  

                elif admin_choice == '2':  
                    old_name = input("Enter the old product name to edit: ")  
                    name = input("Enter new product name: ")  
                    price = input("Enter new product price: ")  
                    inventory = input("Enter new inventory count: ")  
                    details = input("Enter new product details: ")  
                    print(admin.edit_product(old_name, name, price, inventory, details))  

                elif admin_choice == '3':  
                    name = input("Enter product name to delete: ")  
                    print(admin.delete_product(name))  

                elif admin_choice == '4':  
                    print(admin.view_products())  
                
                elif admin_choice == '0':  
                    break  

        elif choice == '4':  
            if user_manager.is_login:  
                item_name = input("Enter the product name to add to cart: ")  
                number = input("Enter number: ")  
                # print(product_manager.get_items())
                print(Shopping_cart.add_item_card(item_name,number,product_manager.get_items()))   #inja bug dareh 
            else:  
                print("You need to log in to add items to your cart.")  
        
        elif choice == '5':  
            print(shopping_cart.get_cart_summary())  

        elif choice == '6':  
            confirm = input("Do you want to checkout? (yes/no): ")  
            print(shopping_cart.order(confirm))  

        elif choice == '0':  
            print("bye")  
            break  

        else:  
            print("Invalid choice, please try again.")  

if __name__ == "__main__":  
    main()  