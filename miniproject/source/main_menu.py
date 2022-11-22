def main_menu():
    
    looping = True
    
    while looping:
    
        main_menu = int(input("Welcome, please select\n1 -- Product Menu\n2 -- Couries Menu\n3 -- Order Menu\n0 -- Exit\n-------------\nPlease enter:  "))
    # Customer can type the number of product type that they want to order
   
        if main_menu == 0:
            exit("Thank you, see you soon.")
        
        elif main_menu == 1:
            from product_menu import product_menu
            product_menu()
        
        elif main_menu == 2:
            from couriers_menu import couriers_menu
            couriers_menu()
           
        elif main_menu == 3:
            from order_menu import order_menu
            order_menu()
           