import math
def surface_area_of_earth():
    radius_of_earth_km = 6371 
    surface_area = 4 * math.pi * radius_of_earth_km ** 2 
    print(f"Площадь поверхности Земли: {surface_area:.2f} км².")
surface_area_of_earth()