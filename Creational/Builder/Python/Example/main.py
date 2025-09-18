from meal_builder import VegMealBuilder, NonVegMealBuilder
from director import MealDirector

def main():
    veg_builder = VegMealBuilder()
    director = MealDirector(veg_builder)
    director.construct_meal()
    veg_meal = veg_builder.get_meal()
    veg_meal.show_meal()

    nonveg_builder = NonVegMealBuilder()
    director = MealDirector(nonveg_builder)
    director.construct_meal()
    nonveg_meal = nonveg_builder.get_meal()
    nonveg_meal.show_meal()


if __name__ == "__main__":
    main()
