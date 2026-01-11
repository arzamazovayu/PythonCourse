import math
#from itertools import starmap
#----ввод данных----
def inputing():
    d1 = float ( input("Введите кратчайшее расстояние от спасателя до кромки воды (в ярдах): ") )
    d2 = float ( input("Введите кратчайшее расстояние от утопающего до берега (в футах): ") )
    h = float ( input("Введите боковое смещение между спасателем и утопающим (в ярдах): ") )
    v = float ( input("Введите скорость движения спасателя по песку (в милях в час): ") )
    n = float ( input("Введите коэффициент замедления спасателя при движении в воде (во сколько раз медленнее): ") )
    tang = float ( input("Введите направление движения спасателя по песку (в градусах). Введите 0 для просчёта оптимального угла: ") )
    return d1, d2, h, v, n, tang

# ----вычисления и конвертации----
# Преобразование в градусов радианы
convert_angle = lambda tang: math.radians(tang)

# Преобразование единиц измерения
def convert_units ( d2, v ):
    d2y = d2 / 3 #футы в ярды
    vys = (v * 1760 / 3600) #мили в час в ярды в секунду
    return d2y, vys

# Вычисления
def calculating ( d1, trad, h, d2y, vys, n ):
    x = d1 * math.tan(trad)
    l1 = math.sqrt(x**2 + d1**2)
    l2 = math.sqrt((h - x)**2 + d2y**2)
    time = (1/vys) * (l1 + n * l2)
    return time

#----вывод данных----
# Вывод
def outputing ( tang,  time ):
    print(f"Если спасатель начнёт движение под углом theta1, равным {tang}°, он достигнет утопащего через {time:.1f} секунды")
    
#----исполение----
def count(d1, d2, h, v, n, tang): 
    d2y, vys = convert_units( d2, v )
    trad = convert_angle (tang)
    time = calculating( d1, trad, h, d2y, vys, n )
    outputing( tang, time )

def optimal(d1, d2, h, v, n, angle):  
    d2y, vys = convert_units( d2, v )
    trad = convert_angle (angle)
    time = calculating( d1, trad, h, d2y, vys, n )
    return time 

def main():
    print("Привет!")
    d1, d2, h, v, n, tang = inputing()
    
    if tang == 0:
        angle = 0
        angle_results = []
        time_results = []
        while angle < 90:
            time = optimal(d1, d2, h, v, n, angle)
            angle_results.append(angle)
            time_results.append(time)
            angle += 1
        min_index = time_results.index(min(time_results))
        optimal_angle = angle_results[min_index]
        minimum_time = time_results[min_index]
        print(f"Оптимальный угол для указанных параметров равен {optimal_angle}° и минимальное время {minimum_time:.1f} секунд")
    else:
        count(d1, d2, h, v, n, tang)
        
    
#----тестирование----

def convert_angle_test ():
    values = [(57.3, 1),
                    (30, 0.5), 
                    (0, 0), 
                    (90, 1.57), 
                    (45, 0.7), 
                    (45, 0.79)] #2й и 5й тесты должны быть failed
    
    count = 0
    passed = 0
    total = len(values)
    
    for deg, rad in values:
        actual = round(convert_angle(deg), 2)
        try:
            count += 1
            assert (actual == rad), f"Получилось {actual}, а хотелось {rad}"
            passed += 1
        except AssertionError as e:
            print(f"Error: ошибка в тесте {count} {e}")
    print(f"Итого: {passed}/{total} тестов для convert_angle пройдено")
    return passed == total

def convert_units_test ():
    values = [(30, 10, (10.0, 4.89)),
                    (15, 1, (10.0, 0.49)),
                    (0, 0, (0.0, 0.0)), 
                    (15, 1, (5.0, 0.49))] #2й тест failed
    
    count = 0
    passed = 0
    total = len(values)
    
    for d2, v, (d2y, vys) in values:
        actual_d2y, actual_vys = convert_units (d2, v)
        try:
            count +=1
            assert (actual_d2y == d2y), f"Получилось {actual_d2y}, а хотелось {d2y}"
            assert (round(actual_vys, 2) == vys), f"Получилось {actual_vys}, а хотелось {vys}"
            passed += 1
        except AssertionError as e:
            print(f"Error: ошибка в тесте {count} {e}")
    print(f"Итого: {passed}/{total} тестов для convert_units пройдено")
    return passed == total
    
def calculating_test ():
    d1 = 8
    d2y, vys = convert_units( 10, 5 )
    h = 50
    n = 2
    trad = convert_angle (39)
    expected_time = 39.9
    
    count = 0
    passed = 0
    total = 1
    
    actual_time = round(calculating ( d1, trad, h, d2y, vys, n ), 1)
    try:
        count +=1
        assert (actual_time == expected_time), f"Получилось {actual_time}, а хотелось {expected_time}"
        passed += 1
    except AssertionError as e:
            print(f"Error: ошибка в тесте {count} {e}")
    print(f"Итого: {passed}/{total} тестов для calculating пройдено")
    return passed == total
    
#----вызов функции main----
if __name__ == "__main__":
    main()
    angle_ok = convert_angle_test ()
    units_ok = convert_units_test ()
    calc_ok = calculating_test ()
    if angle_ok and units_ok and calc_ok:
        print("Все тесты  пройдены успешно")
    else:
        print("Не все тесты пройдены успешно")