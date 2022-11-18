def product_menu():
    customer_order_list = []
    
    product_looping = True
    while product_looping:
    
        product_menu_option = int(input("1 -- Product Menu\n2 -- Create Order\n3 -- Update Product list\n4 -- Delete Product\n0 -- Exit Order Menu\n--------------\nPlease enter number :  "))
        # Type 0 for going back main menu
                
        if product_menu_option == 0:
                product_looping = False
                break
                
                    
        elif product_menu_option == 1:
            # Product list
                file = open("data/product_list.txt", 'r')
                row = file.read()
                print(row)
                    
        elif product_menu_option == 2:
                        
                for x in range(1):
                    order_list = input("What would you like to order?\n")
                    customer_order_list = order_list.split(", ")
                    print("Your order {} item(s): ".format(len(customer_order_list)), customer_order_list)
                            
                for i in range(len(customer_order_list)):
                    customer_order_list[i] = str(customer_order_list[i])
                            
                with open("data/order_list.txt", "a+") as fileHandler:
                    fileHandler.write("{}\n".format(order_list))
                        
                fileHandler.close()
                            
                        
        elif product_menu_option == 3:

                with open("data/order_list.txt", "r") as file:
                    customer_order_list = [x.strip() for x in file.readlines()]
                    
                for i, e in enumerate(customer_order_list):
                    print(f"[{i+1}]: {e}")
                    
                item_index_update = int(input("Please enter index of product: \n"))
                new_order_product = str(input("Please add product in order.\n"))
                customer_order_list.remove(item_index_update)
                # customer_order_list.append(new_order_product)
                        
                # with open("data/order_list.txt", "w+") as file:
                #     for e in customer_order_list:
                #         file.write(f"{e}\n")
                        
                        
                # print("{} has been added in your order now.".format(new_order_product))

                        
        elif product_menu_option == 4:
                with open("data/order_list.txt", "r") as file:
                    customer_order_list = [x.strip() for x in file.readlines()]
                    print(customer_order_list)
                item_index_delete = int(input("Please enter index of product: \n"))
                customer_order_list.remove(item_index_delete)