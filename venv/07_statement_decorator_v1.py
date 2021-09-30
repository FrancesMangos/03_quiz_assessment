def statement_generator(statement, decoration):

    sides = decoration * 3

    greeting = "{} {} {}".format(sides, statement, sides)

    top_bottom = decoration * len(greeting)

    print(top_bottom)
    print(greeting)
    print(top_bottom)

    return ""

statement_generator("Hello!", "*")
