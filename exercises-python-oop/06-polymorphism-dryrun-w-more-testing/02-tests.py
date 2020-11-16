solution = __import__('02-groups')

Person = solution.Person
Group = solution.Group
P, G = Person, Group


def test_person_addition_should_combine_names():
    assert (
        Person('Elon', 'Musk') + Person('Warren', 'Buffet')
    ).full_name == 'Elon Buffet'

    assert (
        Person('Warren', 'Buffet') + Person('Elon', 'Musk')
    ).full_name == 'Warren Musk'
    try:
        Person('Warren', 'Buffet') + 3
    except TypeError:
        pass
    except Exception as e:
        assert False, f'expected TypeError, got {e.__class__.__name__}'

    print('test passed')


def test_group_addition_should_combine_all_people():
    p1 = Person('t', 't')
    p2 = Person('T', 'T')

    one = Group('one', [p1, p1, p1])
    two = Group('two', [p2, p2, p2])

    group = str((one + two))
    # all_names = ','.join([p.full_name for p in (one + two)])
    # assert all_names == 't t,t t,t t,T T,T T,T T', all_names
    assert 'with members t t, t t, t t, T T, T T, T T' in group

    try:
        Group('one', []) + Person('t', 'T')
    except TypeError:
        pass
    except Exception as e:
        assert False, f"expected TypeError, got {e.__class__}"
    else:
        assert False, "Should have raised a TypeError, it didn't"

    print('test passed')


def test_group_to_string():
    group = str(G('b', [P('t', 't'), P('T', 'T')]))
    assert group == 'Group b with members t t, T T'
    print('test passed')


test_person_addition_should_combine_names()
test_group_addition_should_combine_all_people()
test_group_to_string()
