is_on = True

while is_on:

    number_collector = input("What number do you wish to find the sum? ")
    if len(number_collector) >= 3:
        print(f"You are expected to input a two digit number and not a {len(number_collector)} digits number.")
        is_on = False
    else:
        number_collector_sum = int(number_collector[0]) + int(number_collector[1])
        print(number_collector_sum)

