
def get_type(length, height, width):
    sides = length + 2*(height + width)

    if 3.5 <= length <= 4.25 and  3.5 <= height <= 6 and .007 <= width <= .016:
        return "regular post card"
    elif 4.35 <= length <= 6 and  6 <= height <= 11.5 and .007 <= width <= .015:
        return ("large post card")
    elif 3.5 <= length <= 6.125 and  5 <= height <= 11.5 and .016 <= width <= .025:
        return ("Envelope")
    elif 6.125 <= length <= 24 and  11 >= height <= 18 and .25 <= width <= .5:
        return ("LARGE ENVELOPE")
    elif length > 24 or height > 18 or width > .5 and sides <= 84:
        return ("PACKAGE")
    elif length > 24 or height > 18 or width > .5 and 84 < sides <= 130:
        return ("large package")
    
def get_zone(zipcode):
    if zipcode > 1 and zipcode < 6999:
        return 1
    elif zipcode > 7000 and zipcode < 19999:
        return 2
    elif zipcode > 20000 and zipcode < 35999:
        return 3 
    elif zipcode > 36000 and zipcode < 62999:
        return 4
    elif zipcode > 63000 and zipcode < 62999:
        return 5
    elif zipcode > 85000 and zipcode < 99999:
        return 6    
    else:
        return 'UNMAILABLE'
    
def find_distance(startzip, endzip):
    startzone = get_zone(startzip)
    endzone = get_zone(endzip)

    if startzone == 'UNMAILABLE' or endzone == 'UNMAILABLE':
        return 'UNMAILABLE'
    return abs(startzone - endzone)

def find_price(package_type, per_zone, package_price):
        

    if package_type == "regualar post card":
        return package_price = .20 + .03 *(per zone)
    elif package_type == "LARGE POST CARD":
        return package_price = .37 + .03 *(per zone)
    elif package_type == "ENVELOPE":
        return package_price = .37 + .04 *(per zone)
    elif package_type == "Large ENVELOPE":
        return package_price = .60 + .05 *(per zone)
    elif package_type == "PACKAGE":
        return package_price = 2.95 + .25 *(per zone)
    elif package_type == "LArge Package":
        return package_price = 3.95 + .35 *(per zone)

def data():
    data = input('').split(',')
    return float(data[0], float(data[1]), float(data[2]), int(data[3]), int(data[4]))

def main(package_type):
    input("what is legnth, height, and width of your package, and how far is your destination")
    data = input("what is legnth, height, and width of your package, and how far is your destination")
    data1 = data.split(", ")

    length  = float(data1[0])
    width = float(data1[1])
    height = float(data1[2])
    startzone = int(data1[3])
    endzone = int(data1[4])
    package_type = get_type(length, height, width)
    total_zones = find_distance(startzone, endzone)
    price = find_price(package_type, total_zones)
    print(price)
