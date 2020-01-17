def build_car(manufacturer, model, **car_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_info:
        car[key] = value 

    print(car)


build_car('toyota', 'corolla', miles = 100,000, color = 'green', year = '2006')