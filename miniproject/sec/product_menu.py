import csv
import readCSVtoDict

def product_menu():
    
    
    product_looping = True
    while product_looping:
    
        product_menu_option = int(input("1 -- Product Menu\n2 -- Create Product\n3 -- Update Product\n4 -- Delete Product\n0 -- Exit Order Menu\n--------------\nPlease enter number :  "))
        # Type 0 for going back main menu
                
        if product_menu_option == 0:
                product_looping = False
                break
                
                    
        elif product_menu_option == 1:
            # Product list
                with open("data/product_list.csv", 'r') as file:
                    csv_file = csv.DictReader(file)
                    for row in csv_file:
                        print(row)
                    
        elif product_menu_option == 2:
                        
                for x in range(1):
                    order_product_name = str(input("What product would you like to add?\n"))
                    order_product_price = float(input("Please enter product price.\n"))
                            
                with open("data/product_list.csv", "a+") as file:
                    fieldnames = ["Name", "Price"]
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writerow({
                        "Name": order_product_name,
                        "Price": order_product_price
                    })
                        
                             
        elif product_menu_option == 3:
            local_list = []
            local_list = readCSVtoDict.readCSVtoDict()
                    
            for i, item in enumerate(local_list):
                print(f"({i+1}) --  {item}")
                    
            item_index_update = int(input("Please enter product's index for update: \n"))
            item_index_update -= 1
     
            print(f'Selected {local_list[item_index_update]} to update')
            for updateProperty in local_list[item_index_update]:
                selectProperty = input(f'Enter update for {updateProperty}: ')
                if (len(selectProperty) != 0):
                    local_list[item_index_update][updateProperty] = selectProperty
                    print(f'{updateProperty} has been update to {selectProperty}')
                        
                else:
                    print(f'Skip update for {updateProperty}')
            
            print(local_list)        
                
            with open("data/product_list.csv", mode = "w") as file:
                fieldnames = ['Name', 'Price']
                writer = csv.DictWriter(file, fieldnames= fieldnames)
                writer.writeheader()
                writer.writerows(local_list)
                    

                        
        elif product_menu_option == 4:
            local_list = []
            local_list = readCSVtoDict.readCSVtoDict()
                    
            for i, item in enumerate(local_list):
                print(f"({i+1}) --  {item}")
                    
            item_index_delete = int(input("Please enter product's index for delete: \n"))
            item_index_delete -= 1
            print(f'Selected {local_list[item_index_delete]} to delete')
            local_list.remove(local_list[item_index_delete])
            
            with open("data/product_list.csv", mode = "w") as file:
                fieldnames = ['Name', 'Price']
                writer = csv.DictWriter(file, fieldnames= fieldnames)
                writer.writeheader()
                writer.writerows(local_list)
                
            print("The product has been deleted")