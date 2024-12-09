PI = 3.141592653589793  # Определяем константу для числа Пи в ручную

def surface_area_of_earth():
    radius_of_earth_km = 6371  
    surface_area = 4 * PI * radius_of_earth_km ** 2  
    print(f"Площадь поверхности Земли: {surface_area:.2f} км².")
surface_area_of_earth()