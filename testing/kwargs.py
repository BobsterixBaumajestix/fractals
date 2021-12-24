def test_func(value_1=0, value_2=0):
    print('value_1 is {} and value_2 is {}.'.format(value_1, value_2))


kwargs = {'value_1': 5, 'value_2': 3}
test_func(value_1=5, value_2=3)
