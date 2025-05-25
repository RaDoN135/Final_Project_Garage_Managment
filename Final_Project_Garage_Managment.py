# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 16:37:44 2024

@author: RaDoN
"""
import datetime # Importing the datetime module to work with dates
import matplotlib.pyplot as plt  # Importing matplotlib for plotting

#First Inheritance Tree(Motorcycle):
class Motorcycle:
    """
    A class representing a Motorcycle.
    """
    def __init__(self, brand, model, year):
        """
        Initializes a new instance of the Motorcycle class.
        """
        self.brand = brand  # Assigning the brand of the motorcycle
        self.model = model  # Assigning the model of the motorcycle
        self.year = year  # Assigning the manufacturing year of the motorcycle

    def __str__(self):
        """
        Returns a string representation of the motorcycle.
        """
        return f"{self.brand} {self.model} ({self.year})\n"

    def __repr__(self):
        """
        Returns a string representation of the motorcycle for debugging.
        """
        return f"Motorcycle(brand={self.brand}, model={self.model}, year={self.year})\n"

    def is_modern(self):
        """
        Checks if the motorcycle is modern (manufactured within the last 2 years).
        """
        current_year = datetime.datetime.now().year  # Getting the current year
        return current_year - self.year <= 2  # Checking if the motorcycle is modern

    def print_details(self):
        """
        Prints details of the motorcycle (brand, model, year).
        """
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}\n")  # Printing the details

    def upgrade_model(self, new_model):
        """
        Attempts to upgrade the model of the motorcycle to a new model.
        """
        try:
            if not isinstance(new_model, str):  # Checking if the new model is a string
                raise TypeError("New model must be a string")  # Raising a TypeError if not
            self.model = new_model  # Updating the model
            print(f"{self.brand} {self.model} upgraded successfully to {new_model}\n")  # Printing success message
        except TypeError as e:
            print(f"Error: {e}")  # Printing error message

class SportsBike(Motorcycle):
    """
    A class representing a SportsBike, which is a type of Motorcycle.
    """
    def __init__(self, brand, model, year, max_speed):
        """
        Initializes a new instance of the SportsBike class.
        """
        try:
            super().__init__(brand, model, year)  # Initializing the parent Motorcycle class
            self.max_speed = max_speed  # Assigning the maximum speed of the sports bike
            self.type = "Sport"  # Assigning the type of the bike as "Sport"
        except TypeError as e:
            print(f"Error initializing SportsBike: {e}")  # Printing error message if initialization fails

    def __str__(self):
        """
        Returns a string representation of the sports bike.
        """
        return f"{super().__str__()}Max Speed: {self.max_speed} km/h\n"  # Including max speed in the string representation

    def __repr__(self):
        """
        Returns a string representation of the sports bike for debugging.
        """
        return f"SportsBike(brand='{self.brand}', model='{self.model}', year={self.year}, max_speed={self.max_speed})"

    def display_info(self):
        """
        Prints detailed information about the sports bike.
        """
        try:
            print(f"{self.brand} {self.model} - Type: {self.type}, Max Speed: {self.max_speed} km/h\n")
        except AttributeError as e:
            print(f"Error displaying SportsBike info: {e}")

class Cruiser(Motorcycle):
    """
    A class representing a Cruiser motorcycle, inheriting from Motorcycle.
    """
    def __init__(self, brand, model, year, engine_capacity):
        """
        Initializes a new instance of the Cruiser class.
        """
        try:
            super().__init__(brand, model, year)  # Initializing the parent Motorcycle class
            self.engine_capacity = engine_capacity  # Assigning the engine capacity of the cruiser motorcycle
            self.type = "Cruiser"  # Assigning the type of the bike as "Cruiser"
        except TypeError as e:
            print(f"Error initializing Cruiser: {e}")

    def __str__(self):
        """
        Returns a string representation of the cruiser motorcycle.
        """
        return f"{super().__str__()}Engine Capacity: {self.engine_capacity} cc\n"

    def __repr__(self):
        """
        Returns a string representation of the cruiser motorcycle for debugging.
        """
        return f"Cruiser(brand='{self.brand}', model='{self.model}', year={self.year}, engine_capacity={self.engine_capacity})"

    def display_info(self):
        """
        Prints detailed information about the cruiser motorcycle.
        """
        try:
            print(f"{self.brand} {self.model} - Type: {self.type}, Engine Capacity: {self.engine_capacity} cc\n")
        except AttributeError as e:
            print(f"Error displaying Cruiser info: {e}")

class DirtBike(Motorcycle):
    """
    A class representing a Dirt motorcycle, inheriting from Motorcycle.
    """
    def __init__(self, brand, model, year, offroad_capability):
        """
        Initializes a new instance of the DirtBike class.
        """
        try:
            super().__init__(brand, model, year)  # Initializing the parent Motorcycle class
            self.offroad_capability = offroad_capability  # Assigning the offroad capability of the dirt bike
            self.type = "Dirt"  # Assigning the type of the bike as "Dirt"
        except TypeError as e:
            print(f"Error initializing DirtBike: {e}")

    def __str__(self):
        """
        Returns a string representation of the Dirt motorcycle.
        """
        return f"{super().__str__()}Offroad Capability: {self.offroad_capability}\n"

    def __repr__(self):
        """
        Returns a string representation of the dirt motorcycle for debugging.
        """
        return f"DirtBike(brand='{self.brand}', model='{self.model}', year={self.year}, offroad_capability='{self.offroad_capability}')"

    def display_info(self):
        """
        Prints detailed information about the dirt motorcycle.
        """
        try:
            print(f"{self.brand} {self.model} - Type: {self.type}, Offroad Capability: {self.offroad_capability}\n")
        except AttributeError as e:
            print(f"Error displaying DirtBike info: {e}")

class ElectricBike(Motorcycle):
    """
    A class representing an Electric motorcycle, inheriting from Motorcycle.
    """
    def __init__(self, brand, model, year, battery_range):
        """
        Initializes a new instance of the ElectricBike class.
        """
        try:
            super().__init__(brand, model, year)  # Initializing the parent Motorcycle class
            self.battery_range = battery_range  # Assigning the battery range of the electric bike
            self.type = "Electric"  # Assigning the type of the bike as "Electric"
        except TypeError as e:
            print(f"Error initializing ElectricBike: {e}")

    def __str__(self):
        """
        Returns a string representation of the Electric motorcycle.
        """
        return f"{super().__str__()}Battery Range: {self.battery_range} km\n"

    def __repr__(self):
        """
        Returns a string representation of the Electric motorcycle for debugging.
        """
        return f"ElectricBike(brand='{self.brand}', model='{self.model}', year={self.year}, battery_range={self.battery_range})"

    def display_info(self):
        """
        Prints detailed information about the Electric motorcycle.
        """
        try:
            print(f"{self.brand} {self.model} - Type: {self.type}, Battery Range: {self.battery_range} km\n")
        except AttributeError as e:
            print(f"Error displaying ElectricBike info: {e}")

class TouringBike(Motorcycle):
    """
    A class representing a Touring motorcycle, inheriting from Motorcycle.
    """
    def __init__(self, brand, model, year, luggage_capacity):
        """
        Initializes a new instance of the TouringBike class.
        """
        try:
            super().__init__(brand, model, year)  # Initializing the parent Motorcycle class
            self.luggage_capacity = luggage_capacity  # Assigning the luggage capacity of the touring bike
            self.type = "Touring"  # Assigning the type of the bike as "Touring"
        except TypeError as e:
            print(f"Error initializing TouringBike: {e}")

    def __str__(self):
        """
        Returns a string representation of the Touring motorcycle.
        """
        return f"{super().__str__()}Luggage Capacity: {self.luggage_capacity} liters\n"

    def __repr__(self):
        """
        Returns a string representation of the Touring motorcycle for debugging.
        """
        return f"TouringBike(brand='{self.brand}', model='{self.model}', year={self.year}, luggage_capacity={self.luggage_capacity})"

    def display_info(self):
        """
        Prints detailed information about the Touring motorcycle.
        """
        try:
            print(f"{self.brand} {self.model} - Type: {self.type}, Luggage Capacity: {self.luggage_capacity} liters\n")
        except AttributeError as e:
            print(f"Error displaying TouringBike info: {e}")

#Second Inheritance Tree(Service):
class Service:
    """
    A class representing a service.
    """
    def __init__(self, service_id, description):
        """
        Initializes a new instance of the Service class.
        """
        try:
            self.service_id = int(service_id)  # Ensure service_id is converted to an integer
            self.description = str(description)  # Ensure description is converted to a string
        except (TypeError, ValueError) as e:
            print(f"Error initializing Service: {e}")
            # Handle additional actions upon error if needed

    def __str__(self):
        """
        Returns a string representation of the service.
        """
        try:
            return f"Service ID: {self.service_id}, Description: {self.description}\n"
        except AttributeError as e:
            return f"Error generating string representation for Service: {e}"
            # Handle additional actions upon error if needed

    def __repr__(self):
        """
        Returns a string representation of the service for debugging.
        """
        try:
            return f"Service(service_id={self.service_id}, description='{self.description}')\n"
        except AttributeError as e:
            return f"Error generating repr for Service: {e}"
            # Handle additional actions upon error if needed

    def display_info(self):
        """
        Prints detailed information about the service.
        """
        try:
            print(f"Service ID: {self.service_id}, Description: {self.description}\n")
        except AttributeError as e:
            print(f"Error displaying Service info: {e}")
            # Handle additional actions upon error if needed

class Maintenance(Service):
    """
    A class representing a maintenance service, inheriting from Service.
    """
    def __init__(self, service_id, description, frequency):
        """
        Initializes a new instance of the Maintenance class.
        """
        try:
            super().__init__(service_id, description)  # Ensure service_id and description are passed to the parent initializer
            self.frequency = frequency  # Ensure frequency is converted to an integer or handled appropriately
            self.type = "Maintenance" 
        except (TypeError, ValueError) as e:
            print(f"Error initializing Maintenance service: {e}")
            # Handle additional actions upon error if needed

    def __str__(self):
        """
        Returns a string representation of the maintenance service.
        """
        try:
            return f"{super().__str__()}, Frequency: {self.frequency}\n"
        except AttributeError as e:
            return f"Error generating string representation for Maintenance service: {e}"
            # Handle additional actions upon error if needed

    def __repr__(self):
        """
        Returns a string representation of the maintenance service for debugging.
        """
        try:
            return f"Maintenance(service_id={self.service_id}, description='{self.description}', frequency={self.frequency})\n"
        except AttributeError as e:
            return f"Error generating repr for Maintenance service: {e}"
            # Handle additional actions upon error if needed

    def display_info(self):
        """
        Prints detailed information about the maintenance service.
        """
        try:
            print(f"Maintenance Service - ID: {self.service_id}, Description: {self.description}, Frequency: {self.frequency}\n")
        except AttributeError as e:
            print(f"Error displaying Maintenance service info: {e}")
            # Handle additional actions upon error if needed


class Repair(Service):
    """
    A class representing a repair service, inheriting from Service.
    """
    def __init__(self, service_id, description, parts_needed):
        """
        Initializes a new instance of the Repair class.
        """
        try:
            super().__init__(service_id, description)  # Ensure service_id and description are passed to the parent initializer
            self.parts_needed = list(parts_needed)  # Ensure parts_needed is converted to a list
            self.type = "Repair"
        except (TypeError, ValueError) as e:
            print(f"Error initializing Repair service: {e}")
            # Handle additional actions upon error if needed

    def __str__(self):
        """
        Returns a string representation of the repair service.
        """
        try:
            return f"{super().__str__()}, Parts Needed: {', '.join(self.parts_needed)}\n"
        except AttributeError as e:
            return f"Error generating string representation for Repair service: {e}"
            # Handle additional actions upon error if needed

    def __repr__(self):
        """
        Returns a string representation of the repair service for debugging.
        """
        try:
            return f"Repair(service_id={self.service_id}, description='{self.description}', parts_needed={self.parts_needed})\n"
        except AttributeError as e:
            return f"Error generating repr for Repair service: {e}"
            # Handle additional actions upon error if needed

    def display_info(self):
        """
        Prints detailed information about the repair service.
        """
        try:
            print(f"Repair Service - ID: {self.service_id}, Description: {self.description}, Parts Needed: {', '.join(self.parts_needed)}\n")
        except AttributeError as e:
            print(f"Error displaying Repair service info: {e}")
            # Handle additional actions upon error if needed

class Customization(Service):
    """
    A class representing a customization service, inheriting from Service.
    """
    def __init__(self, service_id, description, customization_type):
        """
        Initializes a new instance of the Customization class.
        """
        try:
            super().__init__(service_id, description)  # Ensure service_id and description are passed to the parent initializer
            self.customization_type = str(customization_type)  # Ensure customization_type is converted to a string
            self.type = "Customization"
        except (TypeError, ValueError) as e:
            print(f"Error initializing Customization service: {e}")
            # Handle additional actions upon error if needed

    def __str__(self):
        """
        Returns a string representation of the customization service.
        """
        try:
            return f"{super().__str__()}, Customization Type: {self.customization_type}\n"
        except AttributeError as e:
            return f"Error generating string representation for Customization service: {e}"
            # Handle additional actions upon error if needed

    def __repr__(self):
        """
        Returns a string representation of the customization service for debugging.
        """
        try:
            return f"Customization(service_id={self.service_id}, description='{self.description}', customization_type='{self.customization_type}')\n"
        except AttributeError as e:
            return f"Error generating repr for Customization service: {e}"
            # Handle additional actions upon error if needed

    def display_info(self):
        """
        Prints detailed information about the customization service.
        """
        try:
            print(f"Customization Service - ID: {self.service_id}, Description: {self.description}, Type: {self.customization_type}\n")
        except AttributeError as e:
            print(f"Error displaying Customization service info: {e}")
            # Handle additional actions upon error if needed

class Garage:
    """
    A class representing a garage that stores motorcycles and services.
    """

    def __init__(self):
        """
        Initializes a new instance of the Garage class.
        """
        self.motorcycles = []  # List to store motorcycles
        self.services = []     # List to store services

    def __getitem__(self, index):
        """
        Retrieves motorcycles or services based on the index.
        """
        if index == 0:
            return self.motorcycles
        elif index == 1:
            return self.services
        else:
            raise IndexError("Index out of range")  # Raise IndexError for invalid index

    def __setitem__(self, index, value):
        """
        Sets motorcycles or services lists using indexing.
        """
        if index == 0:
            self.motorcycles = value
        elif index == 1:
            self.services = value
        else:
            raise IndexError("Index out of range")  # Raise IndexError for invalid index

    def __delitem__(self, index):
        """
        Clears motorcycles or services lists using indexing.
        """
        if index == 0:
            self.motorcycles = []
        elif index == 1:
            self.services = []
        else:
            raise IndexError("Index out of range")  # Raise IndexError for invalid index

    def print_all_objects(self):
        """
        Prints all motorcycles and services currently stored in the garage.
        """
        print("All objects in the Garage:")
        for obj in self.motorcycles + self.services:
            print(repr(obj))
    
    def remove_duplicate_services(self):
        """
        Removes duplicate services based on service ID.
        """
        seen_ids = set()
        unique_services = []
        deleted_services = []

        for service in self.services:
            if service.service_id not in seen_ids:
                seen_ids.add(service.service_id)
                unique_services.append(service)
            else:
                deleted_services.append(service)

        if len(unique_services) < len(self.services):
            self.services = unique_services
            print("Duplicate services removed successfully.")
            if deleted_services:
                print("Deleted services:")
                for service in deleted_services:
                    print(f"  - {service}")
        else:
            print("No duplicate services found.")

    def add_object(self):
        """
        Adds a new motorcycle or service to the garage based on user input.
        """
        print("1. Add a motorcycle")
        print("2. Add a service")
        print("3. Go back to the main menu")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                bike_type = input("Enter the type of motorcycle (Sport/Cruiser/Dirt/Electric/Touring): ").lower()
                brand = input("Enter the brand of the motorcycle: ")
                model = input("Enter the model of the motorcycle: ")
                year = int(input("Enter the year of the motorcycle: "))

                if bike_type == "sport":
                    max_speed = int(input("Enter the motorcycle Max speed:"))
                    motorcycle = SportsBike(brand, model, year, max_speed)
                elif bike_type == "cruiser":
                    engine_capacity = int(input("Enter the engine capacity:"))
                    motorcycle = Cruiser(brand, model, year, engine_capacity)
                elif bike_type == "dirt":
                    offroad_capability = input("Enter the offroad capability (High/Medium/Low): ").capitalize()
                    motorcycle = DirtBike(brand, model, year, offroad_capability)
                elif bike_type == "electric":
                    battery_range = int(input("Enter the battery range of the electric bike (in km): "))
                    motorcycle = ElectricBike(brand, model, year, battery_range)
                elif bike_type == "touring":
                    luggage_capacity = int(input("Enter the luggage capacity of the touring bike (in liters): "))
                    motorcycle = TouringBike(brand, model, year, luggage_capacity)
                else:
                    print("Invalid motorcycle type. Motorcycle not added.")
                    return

                self.add_motorcycle(motorcycle)
                print(f"Added {bike_type} bike {brand} {model} to the garage.")
            elif choice == "2":
                 service_id = int(input("Enter the service ID: "))
                 service_type = input("Enter the type of service (Maintenance/Repair/Customization): ").lower()
                 if service_type == "maintenance":
                     frequency = input("Enter the maintenance frequency (in years): ")
                     service = Maintenance(service_id, "", frequency)
                 elif service_type == "repair":
                     parts_needed = input("Enter the parts needed (comma-separated): ").split(',')
                     service = Repair(service_id, "", parts_needed)
                 elif service_type == "customization":
                     customization_type = input("Enter the customization type: ")
                     service = Customization(service_id, "", customization_type)
                 else:
                     print("Invalid service type. Service not added.")
                     return  # <-- This return statement was incorrectly placed
                     
                 self.add_service(service)
                 print(f"Added service of type '{service_type}' to the garage.")
            elif choice == "3":
                return  # Return from the method to go back to the main menu
            else:
                print("Invalid choice.")
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid value.")
        except Exception as e:
            print(f"An error occurred: {e}. Operation failed.")
    


    def delete_object(self):
        """
        Deletes a motorcycle or service from the garage based on user input.
        """
        print("Choose the type of object to delete:")
        print("1. Delete a motorcycle")
        print("2. Delete a service")
        print("3. Go back to the main menu")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                brand = input("Enter the brand of the motorcycle to delete: ")
                motorcycles = self.find_motorcycle_by_brand(brand)
                if motorcycles:
                    for motorcycle in motorcycles:
                        self.remove_motorcycle(motorcycle)
                        print(f"Deleted {motorcycle.brand} {motorcycle.model} from the garage.")
                else:
                    print(f"No motorcycles found for brand '{brand}'.")
            elif choice == "2":
                service_id = int(input("Enter the service ID to delete: "))
                service = self.find_service_by_id(service_id)
                if service:
                    self.remove_service(service)
                    print(f"Deleted service '{service.description}' from the garage.")
                else:
                    print(f"Service with ID {service_id} not found.")
            elif choice == "3":
                return  # Return from the method to go back to the main menu
            else:
                print("Invalid choice.")
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid value.")
        except Exception as e:
            print(f"An error occurred: {e}. Operation failed.")
            
    def update_object(self):
        """
        Updates information of a motorcycle or service in the garage based on user input.
        """
        print("Choose the type of object to update:")
        print("1. Update a motorcycle")
        print("2. Update a service")
        print("3. Go back to the main menu")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                brand = input("Enter the brand of the motorcycle to update: ")
                motorcycles = self.find_motorcycle_by_brand(brand)
                if motorcycles:
                    for motorcycle in motorcycles:
                        new_model = input(f"Enter the new model for {motorcycle.brand} {motorcycle.model}: ")
                        motorcycle.upgrade_model(new_model)
                else:
                    print(f"No motorcycles found for brand '{brand}'.")
            elif choice == "2":
                service_id = int(input("Enter the service ID to update: "))
                service = self.find_service_by_id(service_id)
                if service:
                    new_description = input(f"Enter the new description for service '{service.description}': ")
                    service.update_description(new_description)
                else:
                    print(f"Service with ID {service_id} not found.")
            elif choice == "3":
                return  # Return from the method to go back to the main menu
            else:
                print("Invalid choice.")
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid value.")
        except Exception as e:
            print(f"An error occurred: {e}. Operation failed.")

    def add_motorcycle(self, motorcycle):
        """
        Adds a motorcycle to the garage.
        """
        self.motorcycles.append(motorcycle)

    def add_service(self, service):
        """
        Adds a service to the garage.
        """
        self.services.append(service)

    def remove_motorcycle(self, motorcycle):
        """
        Removes a motorcycle from the garage.
        """
        self.motorcycles.remove(motorcycle)

    def remove_service(self, service):
        """
        Removes a service from the garage.
        """
        self.services.remove(service)

    def find_motorcycle_by_brand(self, brand):
        """
        Finds motorcycles in the garage by brand.
        """
        return [motorcycle for motorcycle in self.motorcycles if motorcycle.brand.lower() == brand.lower()]

    def find_service_by_id(self, service_id):
        """
        Finds a service in the garage by service ID.
        """
        for service in self.services:
            if service.service_id == service_id:
                return service
        return None
    
    def sort_motorcycles(self):
        """
        Sorts the motorcycles in the garage alphabetically by brand and model.
        User can choose to sort from A-Z or Z-A and print the sorted motorcycles.
        """
        print("Choose the sorting order:")
        print("1. Sort from A-Z")
        print("2. Sort from Z-A")
        choice = input("Enter your choice: ")

        if choice == "1":
            self.motorcycles.sort(key=lambda bike: (bike.brand.lower(), bike.model.lower()))
            print("Motorcycles sorted from A-Z by brand and model.")
        elif choice == "2":
            self.motorcycles.sort(key=lambda bike: (bike.brand.lower(), bike.model.lower()), reverse=True)
            print("Motorcycles sorted from Z-A by brand and model.")
        else:
            print("Invalid choice. Motorcycles not sorted.")
            return

        print("\nSorted Motorcycles:")
        for motorcycle in self.motorcycles:
            print(f"Brand: {motorcycle.brand}, Model: {motorcycle.model}, Year: {motorcycle.year}")

    def sort_motorcycles_by_year(self):
        """
        Sorts the motorcycles in the garage by their year.
        User can choose to sort in ascending or descending order and print the sorted motorcycles.
        """
        print("Choose the sorting order by year:")
        print("1. Sort from oldest to newest")
        print("2. Sort from newest to oldest")
        choice = input("Enter your choice: ")

        if choice == "1":
            self.motorcycles.sort(key=lambda bike: bike.year)
            print("Motorcycles sorted from oldest to newest by year.")
        elif choice == "2":
            self.motorcycles.sort(key=lambda bike: bike.year, reverse=True)
            print("Motorcycles sorted from newest to oldest by year.")
        else:
            print("Invalid choice. Motorcycles not sorted by year.")
            return

        print("\nSorted Motorcycles by Year:")
        for motorcycle in self.motorcycles:
            print(f"Brand: {motorcycle.brand}, Model: {motorcycle.model}, Year: {motorcycle.year}")
            
    def save_garage_to_file(self, filename):
        """
        Saves the garage (motorcycles and services) to a text file in a format that can be loaded using eval().
        """
        with open(filename, 'w') as f:
            f.write("Motorcycles:\n")
            for motorcycle in self.motorcycles:
                f.write(repr(motorcycle) + "\n")

            f.write("\nServices:\n")
            for service in self.services:
                f.write(repr(service) + "\n")

        print(f"Garage data saved to {filename}")

    def load_garage_from_file(self, filename):
        """
        Loads the garage data (motorcycles and services) from a text file.
        """
        try:
            with open(filename, 'r') as f:
                motorcycles = []
                services = []
                current_section = None

                for line in f:
                    line = line.strip()

                    if line == "Motorcycles:":
                        current_section = "motorcycles"
                    elif line == "Services:":
                        current_section = "services"
                    elif line:
                        try:
                            if current_section == "motorcycles":
                                motorcycles.append(eval(line))  # Convert string representation back to object
                            elif current_section == "services":
                                services.append(eval(line))     # Convert string representation back to object
                        except Exception as e:
                            print(f"Error loading line '{line}': {e}")

                self.motorcycles = motorcycles
                self.services = services

            print(f"Garage data loaded from {filename}")
        except IOError as e:
            print(f"Error loading garage data: {e}")

    def plot_motorcycle_types(self):
        """
        Plots the number of motorcycles of each type in the garage.
        """
        try:
            motorcycle_types = {'Sport': 0, 'Cruiser': 0, 'Dirt': 0, 'Electric': 0, 'Touring': 0}

            for motorcycle in self.motorcycles:
                if isinstance(motorcycle, SportsBike):
                    motorcycle_types['Sport'] += 1
                elif isinstance(motorcycle, Cruiser):
                    motorcycle_types['Cruiser'] += 1
                elif isinstance(motorcycle, DirtBike):
                    motorcycle_types['Dirt'] += 1
                elif isinstance(motorcycle, ElectricBike):
                    motorcycle_types['Electric'] += 1
                elif isinstance(motorcycle, TouringBike):
                    motorcycle_types['Touring'] += 1
                else:
                    print(f"Unknown motorcycle type: {type(motorcycle)}")

            print("Motorcycle types in the garage:", motorcycle_types)  # Debugging print

            labels = list(motorcycle_types.keys())
            values = list(motorcycle_types.values())

            plt.figure(figsize=(10, 6))
            plt.bar(labels, values, color=['red', 'blue', 'green', 'purple', 'orange'])
            plt.title('Motorcycle Types in the Garage')
            plt.xlabel('Motorcycle Type')
            plt.ylabel('Number of Motorcycles')
            plt.show()

        except AttributeError as e:
            print(f"Error plotting motorcycle types: {e}")
    
    def plot_service_types(self):
        """
        Plots the number of each type of service in the garage.
        """
        try:
            print("Number of services:", len(self.services))  # Check the number of services
            print("Services:", self.services)  # Print the list of services
            
            service_types = {'Maintenance': 0, 'Repair': 0, 'Customization': 0}

            for service in self.services:
                if isinstance(service, Maintenance):
                    service_types['Maintenance'] += 1
                elif isinstance(service, Repair):
                    service_types['Repair'] += 1
                elif isinstance(service, Customization):
                    service_types['Customization'] += 1
                else:
                    print(f"Unknown service type: {type(service)}")

            print("Service types in the garage:", service_types)  # Debugging print

            labels = list(service_types.keys())
            values = list(service_types.values())

            plt.figure(figsize=(10, 6))
            plt.bar(labels, values, color=['red', 'blue', 'green'])
            plt.title('Service Types in the Garage')
            plt.xlabel('Service Types')
            plt.ylabel('Number of Services')
            plt.show()

        except AttributeError as e:
            print(f"Error plotting service types: {e}")
            

def main():
    garage = Garage()

    while True:
        print("\n==== Garage Management System ====")
        print("1. Add a motorcycle or a service")
        print("2. Delete a motorcycle or a service")
        print("3. Update a motorcycle or a service")
        print("4. Print all bikes and services")
        print("5. Save garage info to file")
        print("6. Load garage info from file")
        print("7. Remove duplicate services based on ID")
        print("8. Load Motorcycle type plot")
        print("9. Load Service type plot")
        print("10. Sort motorcycles by Name")
        print("11. Sort motorcycles by Year")
        print("12. Exit")

        choice = input("Enter your choice: ").strip()  # Remove leading and trailing whitespace

        try:
            if choice == "1":
                garage.add_object()
            elif choice == "2":
                garage.delete_object()
            elif choice == "3":
                garage.update_object()
            elif choice == "4":
                garage.print_all_objects()
            elif choice == "5":
                filename = input("Enter the filename to save the garage data: ").strip()
                garage.save_garage_to_file(filename)
            elif choice == "6":
                filename = input("Enter the filename to load the garage data from: ").strip()
                garage.load_garage_from_file(filename)
            elif choice == "7":
                garage.remove_duplicate_services()
            elif choice == "8":
                garage.plot_motorcycle_types()  # Call the correct method
            elif choice == "9":
                garage.plot_service_types()  # Call the correct method
            elif choice == "10":
                garage.sort_motorcycles()  # Sort motorcycles by name
            elif choice == "11":
                garage.sort_motorcycles_by_year()  # Sort motorcycles by year
            elif choice == "12":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 9.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    main()

