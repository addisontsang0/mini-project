#add product
# customer_order_list = []

#Main Menu
main_menu = int(input("Please type 1 if you would like to order or 0 if you want to exit.\n"))

# order status
order_status = ["Preparing", "Awaiting Pickup", "Out-for-Delivery", "Delivered"]

# Product list
cafe = {"coffee": ["cappuccino", "latte", "flat_white"], 
        "sandwich": ["ham", "cheese", "egg", "chicken"], 
        "soft_drink": ["still_water", "sparking_water", "coke", "orange_juice"]
        }


# Customer can type the number of product type that they want to order

if main_menu == 0:
    exit("Thank you so much and welcome to see you soon.")
    
elif main_menu == 1:
    product_menu_option = int(input("1 for seeing product menu, 2 for asking new product, 3 for updating the product list, 4 for deleting product, 0 for going back main menu."))
    
    # Type 0 for going back main menu
    if product_menu_option == 0:
        print(main_menu)
    
    elif product_menu_option == 1:
        print(cafe)
    
    elif product_menu_option == 2:
       order_list = input("What would you like to order?\n")
       customer_order_list = order_list.split()
       print(customer_order_list)
       
       for i in range(len(customer_order_list)):
           customer_order_list[i] = str(customer_order_list[i])
               
    elif product_menu_option == 3:
        for x in customer_order_list[x]:
            
        
        print("...")
        
    # elif product_menu_option == 4:
    #     print("!!!")
            