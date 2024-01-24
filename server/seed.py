from app import app
from models import db, Restaurant,Pizza,RestaurantPizza
from random import randint, choice as rc
from faker import Faker

fake = Faker()
with app.app_context():
    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    restaurants = []
    for _ in range(15):
        restaurant = Restaurant(
            name=fake.company(),
            address= fake.address()
        )
        restaurants.append(restaurant)

    db.session.add_all(restaurants)
    db.session.commit()

    pizzas =[
        Pizza(name="BBQ chicken", ingredients="tomato, onions"),
        Pizza(name="Hawaiian", ingredients="parsley, scallops"),
        Pizza(name="Sicilian pizza", ingredients="Mozzarella"),
        Pizza(name="Margherita", ingredients="yeast, shrimp"),
        Pizza(name="Veggie pizza", ingredients="garlic, flour, shrimp"),
        Pizza(name="Pepperoni", ingredients="parsley, mozzarella"),
        Pizza(name="Cuban pizza", ingredients="bacon, pineapple, pepper"),
        Pizza(name="Bagel pizza", ingredients="corn, olive oil"),

        Pizza(name="Panizza", ingredients="tomatoes, gruyere,itallian sausage"),
        Pizza(name="Italian pizzza", ingredients="pepperoni, oregano"),
        Pizza(name="New haven", ingredients="baco, pepperoni,mozzarella"),
        Pizza(name="Capricciossa", ingredients="red pepper flakes, oregano"),
        Pizza(name="Calzone", ingredients="shrimp, cheese, flour"),
        Pizza(name="Buffalo Chicken", ingredients="yeast, honey, water"),
        Pizza(name="Caprese", ingredients="tomatoes, yeast scallops")
    ]

    for pizza in pizzas:
        db.session.add(pizza)
    db.session.commit()

    restaurantpizzas =[
        RestaurantPizza(
            price = randint(1,30),
            restaurant_id= randint(1, len(restaurants)),
            pizza_id = randint(1, len(pizzas))
        )
        for _ in range(15)
    ]

    for restautantpizza in restaurantpizzas:
        db.session.add(restautantpizza)
    db.session.commit()