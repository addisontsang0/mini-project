import csv
import readCSVtoDict

def couriers_menu():
    
    couriers_looping = True
    while couriers_looping:
        
        couriers_menu_option = int(input("1 -- Couriers List\n2 -- Create New Courier\n3 -- Update Courier\n4 -- Delete Courier\n0 -- Exit Couriers Menu\n--------------\nPlease enter number :  "))
        
        if couriers_menu_option == 0:
            couriers_looping = False
            break
        
        elif couriers_menu_option == 1:
            with open("data/courier_list.csv", "r") as file:
                    csv_file = csv.DictReader(file)
                    for row in csv_file:
                        print(row)
        
        elif couriers_menu_option == 2:
            
            courier_name = str(input("Please enter courier name: \n"))
            courier_phone = str(input("Please enter courier phone number: \n"))
            
            with open("data/courier_list.csv", mode = "a+") as file:
                    fieldnames = ["Name", "Phone"]
                    writer = csv.DictWriter(file, fieldnames = fieldnames) 
                    writer.writerow({
                                "Name": courier_name,
                                "Phone": courier_phone
                                })
        
        elif couriers_menu_option == 3:
            local_list = []
            local_list = readCSVtoDict.readcourierCSVtoDict()
                    
            for i, item in enumerate(local_list):
                print(f"({i+1}) --  {item}")
                    
            courier_index_update = int(input("Please enter Courier's index for update: \n"))
            courier_index_update -= 1
     
            print(f'Selected {local_list[courier_index_update]} to update')
            for updateProperty in local_list[courier_index_update]:
                selectProperty = input(f'Enter update for {updateProperty}: ')
                if (len(selectProperty) != 0):
                    local_list[courier_index_update][updateProperty] = selectProperty
                    print(f'{updateProperty} has been update to {selectProperty}')
                        
                else:
                    print(f'Skip update for {updateProperty}')
            
            print(local_list)        
                
            with open("data/courier_list.csv", mode = "w") as file:
                fieldnames = ['Name', 'Phone']
                writer = csv.DictWriter(file, fieldnames= fieldnames)
                writer.writeheader()
                writer.writerows(local_list)
        
        elif couriers_menu_option == 4:
            local_list = []
            local_list = readCSVtoDict.readcourierCSVtoDict()
                    
            for i, item in enumerate(local_list):
                print(f"({i+1}) --  {item}")
                    
            courier_index_delete = int(input("Please enter Courier's index for delete: \n"))
            courier_index_delete -= 1
            print(f'Selected {local_list[courier_index_delete]} to delete')
            local_list.remove(local_list[courier_index_delete])
            
            with open("data/courier_list.csv", mode = "w") as file:
                fieldnames = ['Name', 'Phone']
                writer = csv.DictWriter(file, fieldnames= fieldnames)
                writer.writeheader()
                writer.writerows(local_list)