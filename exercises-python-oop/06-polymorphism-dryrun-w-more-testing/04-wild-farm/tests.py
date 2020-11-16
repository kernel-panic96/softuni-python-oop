from collections import namedtuple

from project import Animal, Bird, Mammal
from project.animals.birds import Hen, Owl
from project.animals.mammals import Cat, Dog, Mouse, Tiger
from project.food import Fruit, Meat, Seed, Vegetable


def run_tests(locals):
    for name, test_func in locals.items():
        if not name.startswith('test'):
            continue
        test_func()
        print(f'{name} PASSED')


def assert_raises(exception, fn):
    try:
        fn()
    except exception:
        pass
    except Exception as e:
        assert False, f'expected {exception.__name__}, got {e.__class__.__name__}'
    else:
        assert False, f'expected {exception.__name__}, did not happen'


def test_cannot_instantiate_animal_by_itself():
    assert_raises(TypeError, lambda: Animal('name', weight=30))


def test_cannot_instantiate_bird_by_itself():
    assert_raises(TypeError, lambda: Bird('name', weight=30, wing_size=30))


def test_cannot_instantiate_mammal_by_itself():
    assert_raises(TypeError, lambda: Mammal('name', weight=30, wing_size=30))


def test_bird_sounds():
    tests = [
        (Owl('buho', weight=3, wing_size=30), 'Hoot Hoot'),
        (Hen('hencho', weight=2, wing_size=10), 'Cluck')
    ]
    for bird, expected_sound in tests:
        assert bird.make_sound() == expected_sound, \
            f'({bird.__class__.__name__}) should "{expected_sound}" was "{bird.make_sound()}"'


def test_mammal_sounds():
    tests = [
        (Mouse('mickey', weight=3, living_region=30), 'Squeak'),
        (Dog('barni', weight=2, living_region=10), 'Woof!'),
        (Cat('malkokote', weight=2, living_region=10), 'Meow'),
        (Tiger('tincho', weight=2, living_region=10), 'ROAR!!!'),
    ]
    for mammal, expected_sound in tests:
        assert mammal.make_sound() == expected_sound, \
            f'({mammal.__class__.__name__}) should "{expected_sound}" was "{mammal.make_sound()}"'


def test_feeding_birds_should_increase_weight():
    test = namedtuple('test', 'bird food expected_increase')
    tests = [
        test(Owl('buho', weight=3, wing_size=30), food=Meat(3), expected_increase=3 * 0.25),
        test(Hen('hencho', weight=2, wing_size=10), food=Seed(3), expected_increase=3 * 0.35)
    ]

    for bird, food, expected_increase in tests:
        before = bird.weight
        bird.feed(food)
        after = bird.weight

        assert after - before == expected_increase, \
            f'{bird.__class__.__name__} with w:{before} ate {food.quantity} {food.__class__.__name__}'\
            f' should have gained {expected_increase}, but it gained {after - before}'


def test_feeding_mammals_should_increase_weight():
    test = namedtuple('test', 'given eats expected_weight_increase')
    tests = [
        test(
            given=Tiger('tincho', weight=3, living_region=''),
            eats=Meat(4),
            expected_weight_increase=4 * 1
        ),
        test(
            given=Dog('kucho', weight=2, living_region=''),
            eats=Meat(4),
            expected_weight_increase=4 * 0.40
        ),
        test(
            given=Cat('kotio', weight=2, living_region=''),
            eats=Vegetable(5),
            expected_weight_increase=5 * 0.30
        ),
        test(
            given=Mouse('misho', weight=2, living_region=''),
            eats=Fruit(5),
            expected_weight_increase=5 * 0.10
        ),
    ]

    for mammal, food, expected_increase in tests:
        before = mammal.weight
        mammal.feed(food)
        after = mammal.weight

        assert after - before == expected_increase, \
            f'{mammal.__class__.__name__} with weight:{before} ate {food.quantity} {food.__class__.__name__}'\
            f' should have gained {expected_increase}, but it gained {after - before}'


def test_feeding_animals_food_that_they_dont_like():
    test = namedtuple('test', 'given tries_to_eat expected_complaint')
    tests = [
        test(
            given=Owl('buho', weight=2, wing_size=1),
            tries_to_eat=Seed(3),
            expected_complaint='Owl does not eat Seed!'
        ),
        # no test for hens, they eat everything. Glutonous bunch ¯\_(ツ)_/¯
        test(
            given=Tiger('tincho', weight=1, living_region=''),
            tries_to_eat=Seed(3),
            expected_complaint='Tiger does not eat Seed!',
        ),
        test(
            given=Tiger('tincho', weight=1, living_region=''),
            tries_to_eat=Vegetable(3),
            expected_complaint='Tiger does not eat Vegetable!',
        ),
        test(
            given=Tiger('tincho', weight=1, living_region=''),
            tries_to_eat=Fruit(3),
            expected_complaint='Tiger does not eat Fruit!',
        ),
        test(
            given=Dog('kucho', weight=1, living_region=''),
            tries_to_eat=Seed(3),
            expected_complaint='Dog does not eat Seed!',
        ),
        test(
            given=Dog('kucho', weight=1, living_region=''),
            tries_to_eat=Vegetable(3),
            expected_complaint='Dog does not eat Vegetable!',
        ),
        test(
            given=Dog('kucho', weight=1, living_region=''),
            tries_to_eat=Fruit(3),
            expected_complaint='Dog does not eat Fruit!',
        ),
        test(
            given=Cat('malkokote', weight=1, living_region=''),
            tries_to_eat=Seed(3),
            expected_complaint='Cat does not eat Seed!',
        ),
        test(
            given=Cat('malkokote', weight=1, living_region=''),
            tries_to_eat=Fruit(3),
            expected_complaint='Cat does not eat Fruit!',
        ),
    ]

    for bird, food_that_it_doesnt_like, expected_complaint in tests:
        before = bird.weight
        response = bird.feed(food_that_it_doesnt_like)

        assert response == expected_complaint,\
            str(response) + f' for {bird.__class__.__name__} & {food_that_it_doesnt_like.__class__.__name__}'
        assert before == bird.weight


def test_animals_repr():
    test = namedtuple('test', 'given that_eats expected_repr')
    tests = [
        test(
            given=Tiger('tincho', weight=1, living_region='Sudan'),
            that_eats=[Meat(1), Meat(2)],
            expected_repr='Tiger [tincho, 4, Sudan, 3]',
        ),
        test(
            given=Owl('buho', weight=1, wing_size=20),
            that_eats=[Meat(1), Meat(2)],
            expected_repr='Owl [buho, 20, 1.75, 3]',
        ),
    ]

    for animal, food_to_be_eaten, expected in tests:
        for f in food_to_be_eaten:
            animal.feed(f)
        assert repr(animal) == expected, \
            f'wanted "{expected}", got {repr(animal)}'


run_tests(locals())
