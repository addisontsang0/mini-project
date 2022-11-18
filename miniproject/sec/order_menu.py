import csv
def order_menu():
    
    # order_list  = [{'customer_name':'Success','customer_address':'address in Manchester','customer_phone':'07701','status':'processing'},
    #             {'customer_name':'Dylan','customer_address':'address 1 for Dylan','customer_phone':'07702','status':'processing'},
    #             {'customer_name':'Edward', 'customer_address':'.address near the city center','customer_phone':'07703','status':'processing'},
    #             {'customer_name':'Ghazala','customer_address':'Bolton of UK','customer_phone':'07704','status':'processing'},
    #             {'customer_name':'May','customer_address':'The main office of Generation','customer_phone':'07705','status':'processing'},
    #             {'customer_name':'Hafsa','customer_address':'Anywhere but Manchester','customer_phone':'07706','status':'processing'}]
    
    order_looping = True
    while order_looping:
        
        order_menu_option = int(input("1 -- Order Dictionary\n2 -- Enter Customer Information\n3 -- Order Status\n4 -- Update Order\n5 -- Delete Order\n0 -- Exit Order Menu\n--------------------\nPlease enter number :  "))
    
        if order_menu_option == 0:
                order_looping = False
                break
        
        
        elif order_menu_option == 1:
                with open("data/order_dictionary.csv", "r") as file:
                    csv_file = csv.DictReader(file)
                    for row in csv_file:
                        print(row)
                    
        elif order_menu_option == 2:
            
                customer_name = str(input("Enter customer name: \n"))
                customer_address = str(input("Enter customer address: \n"))
                customer_phone_number = int(input("Enter customer phone number: \n"))
                
            
                order_status = "PREPARING"

                with open("data/order_dictionary.csv", mode = "a+") as file:
                        fieldnames = ["customer_name", "customer_address", "customer_phone", "Status"]
                        writer = csv.DictWriter(file, fieldnames = fieldnames)
                        
                        
                        writer.writerow({
                                "customer_name": customer_name, 
                                "customer_address": customer_address,
                                "customer_phone": customer_phone_number,
                                "Status": order_status
                                })
                print("Order Completed, Thanks a lot.")
                        
        elif order_menu_option == 3:
                
                with open("data/order_dictionary.csv", "r") as file:
                        csv_file = csv.DictReader(file)
                        for row in csv_file:
                                print(row)
                                
                # for i, e in enumerate():
                #     print(f"[{i+1}]: {e}")
                    
                order_list_index = int(input("Please enter the order list index: \n"))
                
                order_status_index = int(input("Please enter the order status index: \n"))
                
        elif order_menu_option == 4:
                with open("data/order_dictionary.csv", "r") as file:
                        csv_file = csv.DictReader(file)
                        for row in csv_file:
                                print(row)
        
        
        
        elif order_menu_option == 5:
                with open("data/order_dictionary.csv", "r") as file:
                        csv_file = csv.DictReader(file)
                        for row in csv_file:
                                print(row)