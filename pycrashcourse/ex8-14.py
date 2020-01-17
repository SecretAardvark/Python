def build_car(manufacturer, model, **car_info,):
    cars = {}
    cars['manufacturer'] = manufacturer
    cars['model'] = model
    for key, value in car_info.items():
        cars[key] = value 

    print(cars)


build_car('toyota', 'corolla', miles = '100,000,', color = 'green', year = '2006')