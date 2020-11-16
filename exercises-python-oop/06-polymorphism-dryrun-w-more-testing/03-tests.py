A = Account = __import__('03-account').Account


def run_tests(locals):
    for name, test_func in locals.items():
        if not name.startswith('test'):
            continue
        test_func()
        print(name, 'PASSED')


def test_add_transaction():
    def test_constructor_affect_balance():
        acc = A('bob', 30)
        assert acc.balance == 30

    def test_add_transaction_affects_balance():
        acc = A('bob', 30)

        acc.add_transaction(20)
        assert acc.balance == 50

        acc.add_transaction(-20)
        assert acc.balance == 30

    def test_add_transaction_with_wrong_type_raises_ValueError():
        acc = A('bob', 30)
        try:
            acc.add_transaction(30.3)
        except ValueError:
            pass
        except Exception as e:
            assert False, f'expected ValueError, got {e.__class__.__name__}'
        else:
            assert False, 'should have raised ValueError'

    run_tests(locals())


def test_account_to_string():
    def test_default_account():
        acc = A('bob')
        assert str(acc) == 'Account of bob with starting amount: 0'

    def test_transactions_dont_affect_to_str():
        acc = A('bob', 40)
        acc.add_transaction(30)
        assert str(acc) == 'Account of bob with starting amount: 40'

    run_tests(locals())


def test_account_repr():
    def test_repr_default_account():
        acc = A('bob')
        assert repr(acc) == 'Account(bob, 0)'

    def test_repr_with_initial_amount():
        acc = A('bob', 40)
        assert repr(acc) == 'Account(bob, 40)'

    def test_add_transaction_does_not_affect_repr():
        acc = A('bob')
        acc.add_transaction(20)
        acc.add_transaction(20)
        assert repr(acc) == 'Account(bob, 0)'

    run_tests(locals())


def test_len_account_is_transaction_count():
    acc = A('bob')
    assert len(acc) == 0

    acc.add_transaction(10)
    acc.add_transaction(10)
    acc.add_transaction(10)

    assert len(acc) == 3


def test_iterator_should_give_transactions():
    acc = A('bob')
    acc.add_transaction(10)
    acc.add_transaction(-10)
    acc.add_transaction(10)

    assert list(acc) == [10, -10, 10]


def test_validate_transaction():
    try:
        zero_acc = A('bob', 0)
        Account.validate_transaction(zero_acc, -10)
    except ValueError as e:
        assert str(e) == 'sorry cannot go in debt!'
    except Exception as e:
        assert False, f'expected ValueError, got {e.__class__.__name__}'
    else:
        assert False, 'expected ValueError, no exception happened'


def test_reversed_with_transactions():
    acc = A('bob', 0)
    acc.add_transaction(1)
    acc.add_transaction(2)
    acc.add_transaction(3)

    assert list(reversed(acc)) == [3, 2, 1]


def test_compare_func():
    a1 = A('bob')
    a2 = A('alice')

    a1.add_transaction(1)
    a2.add_transaction(2)

    assert a1 < a2
    assert a2 > a1
    assert a1 != a2
    assert (a1 == a2) is False
    assert a2 >= a1
    assert a1 <= a2
    assert a1 <= a1
    assert a1 == a1
    assert a2 == a2


def test_add_accounts():
    a1 = A('bob', 20)
    a2 = A('alice')

    a1.add_transaction(10)
    a1.add_transaction(10)
    a2.add_transaction(20)
    a2.add_transaction(20)

    assert list(a1 + a2) == [10, 10, 20, 20]


run_tests(locals())
