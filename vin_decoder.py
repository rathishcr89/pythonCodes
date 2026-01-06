from sqlalchemy.sql._elements_constructors import null
class VINDecoder:
    def __init__(self, vin):
        self.vin = vin.upper()
        if len(self.vin) != 17:
            raise ValueError("VIN must be 17 characters long")
        self.decode_vin()

    def decode_vin(self):
        # WMI: first 3 characters
        self.wmi = self.vin[0:3]
        
        # Country: based on first 2 characters
        self.country = "India" if self.vin[:2] in ["MA", "ME"] else "Unknown"
        
        # Manufacturer mapping (some common Indian manufacturers)
        self.manufacturer_codes = {
            'MAT': 'Tata',
            'MA1': 'Mahindra',
            'MA3': 'Maruti Suzuki',
            'KMH': 'Hyundai',
            'MAL': 'Hyundai',
            'MLH': 'Honda',
            'JT': 'Toyota',
            'MAJ': 'Ford',
            'WVW': 'Volkswagen',
            'VF1': 'Renault',
            'JN': 'Nissan',
            'KNA': 'Kia',
            'TMB': 'Skoda',
            '1C4': 'Jeep',
            'WBA': 'BMW',
            'WDB': 'Mercedes-Benz',
            'WAU': 'Audi',
            #bikes
            'ME3': 'Royal Enfield',
            # Add more as needed
        }
        self.manufacturer = self.manufacturer_codes.get(self.wmi, 'Unknown')
        # Plant decoding for Royal Enfield 11th Character
   
        if self.manufacturer == 'Royal Enfield':
            plant_codes = {
                '1': 'Oragadam',
                '2': 'Vallam Vadagal'
            }
            self.plant = plant_codes.get(self.vin[10], 'Unknown')
        else:
            self.plant = self.vin[10]
         
        # VDS: characters 4-8 (Vehicle Descriptor Section, includes model info)
        self.vds = self.vin[3:9]
        self.model = self.vds  # Using VDS as model code; full decoding requires manufacturer-specific knowledge
  
        # Engine Series: 4th character
        engine_code = self.vin[3]
        self.engine_series_codes = {
            'J': 'J Series Engine',
            'U': 'U Series Engine'
        }
        self.engine_series = self.engine_series_codes.get(engine_code, 'Unknown')

        # Engine Size: 5th character
        engine_size_code = self.vin[4]
        self.engine_size_codes = {
            '3': '350cc Engine',
            '4': '400cc Engine',
            '6': '650cc Engine'
        }
        self.engine_size = self.engine_size_codes.get(engine_size_code, 'Unknown')
        
        # Cooling Type: 6th character
        cooling_code = self.vin[5]
        self.cooling_type_codes = {
            'A': 'Air Cooled',
            'O': 'Oil Cooled',
            'L': 'Liquid Cooled'
        }
        self.cooling_type = self.cooling_type_codes.get(cooling_code, 'Unknown')
        
        # Number of Gears: 7th character
        gears_code = self.vin[6]
        self.gears_codes = {
            '4': '4 Gears',
            '5': '5 Gears',
            '6': '6 Gears',
            '8': '8 Gears',
            'A': 'Automatic',
            'M': 'Manual'
        }
        self.gears = self.gears_codes.get(gears_code, 'Unknown')

        # Fuel Type: 8th character
        fuel_code = self.vin[7]
        self.fuel_type_codes = {
            'F': 'Petrol/Diesel',
            'G': 'Gas'
        }
        self.fuel_type = self.fuel_type_codes.get(fuel_code, 'Unknown')

         # Month: 9th character
        month_code = self.vin[8]
        self.month_codes = {
            'A': 'January', 'B': 'February', 'C': 'March', 'D': 'April', 'E': 'May', 'F': 'June',
            'G': 'July', 'H': 'August', 'J': 'September', 'K': 'October', 'N': 'November', 'P': 'December'
        }
        self.month = self.month_codes.get(month_code, 'Unknown')
        
        # Year: 10th character
        year_code = self.vin[9]
        self.year_codes = {
            'A': 1980, 'B': 1981, 'C': 1982, 'D': 1983, 'E': 1984, 'F': 1985, 'G': 1986, 'H': 1987, 'J': 1988, 'K': 1989,
            'L': 1990, 'M': 1991, 'N': 1992, 'P': 1993, 'R': 1994, 'S': 1995, 'T': 1996, 'V': 1997, 'W': 1998, 'X': 1999,
            'Y': 2000, '1': 2001, '2': 2002, '3': 2003, '4': 2004, '5': 2005, '6': 2006, '7': 2007, '8': 2008, '9': 2009,
            'A': 2010, 'B': 2011, 'C': 2012, 'D': 2013, 'E': 2014, 'F': 2015, 'G': 2016, 'H': 2017, 'J': 2018, 'K': 2019,
            'L': 2020, 'M': 2021, 'N': 2022, 'P': 2023, 'R': 2024, 'S': 2025, 'T': 2026, 'V': 2027, 'W': 2028, 'X': 2029,
            'Y': 2030, '1': 2031, '2': 2032, '3': 2033, '4': 2034, '5': 2035, '6': 2036, '7': 2037, '8': 2038, '9': 2039,
        }
        self.year = self.year_codes.get(year_code, 'Unknown')       

        
        # Serial: characters 12-17
        self.serial = self.vin[11:17]

    def display_info(self):
        
        print(f"Country:\t\t{self.country}")
        print(f"Manufacturer:\t\t{self.manufacturer}")
        print(f"Engine Series:\t\t{self.engine_series}")
        print(f"Engine Size:\t\t{self.engine_size}")
        print(f"Cooling Type:\t\t{self.cooling_type}")
        print(f"Number of Gears:\t{self.gears}")
        print(f"Fuel Type:\t\t{self.fuel_type}") 
        # print(f"Model:\t\t\t{self.model}")
        print(f"Year:\t\t\t{self.year}")
        print(f"Month:\t\t\t{self.month}")
        print(f"Plant:\t\t\t{self.plant}")        
        print(f"Serial:\t\t\t{self.serial}")

# Example usage
if __name__ == "__main__":
    vin = input("Enter VIN: ")
    try:
        decoder = VINDecoder(vin)
        decoder.display_info()
    except ValueError as e:
        print(e)