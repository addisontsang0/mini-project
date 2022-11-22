import csv
import readCSVtoDict

def order_menu():
    
    order_looping = True
    while order_looping:
        
        order_menu_option = int(input("1 -- Order List\n2 -- Enter Customer Information\n3 -- Order Status\n4 -- Update Order\n5 -- Delete Order\n0 -- Exit Order Menu\n--------------------\nPlease enter number :  "))
    
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
                
                product_local_list = []
                product_local_list = readCSVtoDict.readCSVtoDict()
                    
                for i, item in enumerate(product_local_list):
                        print(f"({i+1}) --  {item}")
                        
                product_index = str(input("Please enter Product's index: \n"))
                
                courier_local_list = []
                with open("data/courier_list.csv", mode = "r") as csvFile:
                    for line in csv.DictReader(csvFile):
                        courier_local_list.append(line)

                for i, item in enumerate(courier_local_list):
                        print(f"({i+1}) --  {item}")
                    
                courier_index = int(input("Please enter Courier's index: \n"))
                
                order_status = "PREPARING"

                with open("data/order_dictionary.csv", mode = "a+") as file:
                        fieldnames = ["Customer Name", "Customer Address", "Customer Phone","Courier", "Status","Items"]
                        writer = csv.DictWriter(file, fieldnames = fieldnames)
                        
                        
                        writer.writerow({
                                "Customer Name": customer_name, 
                                "Customer Address": customer_address,
                                "Customer Phone": customer_phone_number,
                                "Courier": courier_index,
                                "Status": order_status,
                                "Items": product_index
                                })
                print("Order Completed, Thanks a lot.")
                        
        elif order_menu_option == 3:
                order_local_list = []
                order_local_list = readCSVtoDict.readorderCSVtoDict()
                    
                for i, item in enumerate(order_local_list):
                        print(f"({i+1}) --  {item}")
                    
                order_index_update = int(input("Please enter order's index for update: \n"))
                order_index_update -= 1

                print(f'Selected {order_local_list[order_index_update]} to update')
                
                order_status = ["Preparing", "Out-For-Delivery", "Delivered"]
                for x, item in enumerate(order_status):
                        print(f'{x} -- {item}')
                
                order_status_index = int(input("Please enter index of order status for update: \n"))
                order_local_list[order_index_update]['Status'] = order_status[order_status_index]
                
                with open("data/order_dictionary.csv", mode = "w") as file:
                        fieldnames = ['Customer Name', 'Customer Address', 'Customer Phone', 'Courier', 'Status', 'Items']
                        writer = csv.DictWriter(file, fieldnames= fieldnames)
                        writer.writeheader()
                        writer.writerows(order_local_list)
                
                print(f"{order_local_list[order_index_update]} has been updated")
                
        elif order_menu_option == 4:
                order_local_list = []
                order_local_list = readCSVtoDict.readorderCSVtoDict()
                    
                for i, item in enumerate(order_local_list):
                        print(f"({i+1}) --  {item}")
                    
                order_index_update = int(input("Please enter order's index for update: \n"))
                order_index_update -= 1
     
                print(f'Selected {order_local_list[order_index_update]} to update')
                for updateProperty in order_local_list[order_index_update]:
                        selectProperty = input(f'Enter update for {updateProperty}: ')
                        if (len(selectProperty) != 0):
                                order_local_list[order_index_update][updateProperty] = selectProperty
                                print(f'{updateProperty} has been update to {selectProperty}')
                        
                        else:
                                print(f'Skip update for {updateProperty}')
            
                print(order_local_list)        
                
                with open("data/order_dictionary.csv", mode = "w") as file:
                        fieldnames = ['Customer Name', 'Customer Address', 'Customer Phone', 'Courier', 'Status', 'Items']
                        writer = csv.DictWriter(file, fieldnames= fieldnames)
                        writer.writeheader()
                        writer.writerows(order_local_list)
        
        elif order_menu_option == 5:
                order_local_list = []
                order_local_list = readCSVtoDict.readorderCSVtoDict()
                    
                for i, item in enumerate(order_local_list):
                        print(f"({i+1}) --  {item}")
                    
                order_index_delete = int(input("Please enter product's index for delete: \n"))
                order_index_delete -= 1
                print(f'Selected {order_local_list[order_index_delete]} to delete')
                order_local_list.remove(order_local_list[order_index_delete])
            
                with open("data/order_dictionary.csv", mode = "w") as file:
                        fieldnames = ['Customer Name', 'Customer Address', 'Customer Phone', 'Courier', 'Status', 'Items']
                        writer = csv.DictWriter(file, fieldnames= fieldnames)
                        writer.writeheader()
                        writer.writerows(order_local_list)
                        
                print("The order has been deleted.")