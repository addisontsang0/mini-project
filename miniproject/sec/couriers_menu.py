def couriers_menu():
    
    couriers_looping = True
    while couriers_looping:
        
        couriers_menu_option = int(input("1 -- Couriers List\n2 -- Create New Courier\n3 -- Update Courier\n4 -- Delete Courier\n0 -- Exit Couriers Menu\n--------------\nPlease enter number :  "))
        
        if couriers_menu_option == 0:
            couriers_looping = False
            break
        
        elif couriers_menu_option == 1:
            with open("data/courier_list.txt", 'r') as file:
                row = file.read()
                print(row)
        
        elif couriers_menu_option == 2:
            
            courier_name = str(input("Please enter the courier name: \n"))
            
            with open("data/courier_list.txt", "a+") as fileHandler:
                    fileHandler.write("{}\n".format(courier_name))
                        
            fileHandler.close()
        
        elif couriers_menu_option == 3:
            with open("data/courier_list.txt", "r") as file:
                    courier_list = [x.strip() for x in file.readlines()]
                    
            for i, e in enumerate(courier_list):
                    print(f"[{i+1}]: {e}")
                    
            courier_index_update = int(input("Please enter index of product: \n"))
            new_courier_name = str(input("Please add product in order.\n"))
            courier_list.remove(courier_index_update)
        
        elif couriers_menu_option == 4:
                with open("data/courier_list.txt", "r") as file:
                    courier_list = [x.strip() for x in file.readlines()]
                    print(courier_list)
                courier_index_delete = int(input("Please enter index of product: \n"))
                courier_list.remove(courier_index_delete)