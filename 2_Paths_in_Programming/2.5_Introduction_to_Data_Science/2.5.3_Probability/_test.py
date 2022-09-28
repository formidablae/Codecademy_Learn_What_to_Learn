load_file_in_context('script.py')

if num_people_in_room > 2:
    pass_tests()
else:
    fail_tests("Did you change `num_people_in_room` to a number greater than `2`?")
