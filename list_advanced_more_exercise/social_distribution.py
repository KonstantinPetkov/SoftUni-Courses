population = list(map(int, input().split(", ")))
minimum_wealth = int(input())

distribution = True

for index in range(len(population)):
    value = population[index]
    if value < minimum_wealth:
        result = minimum_wealth - value
        max_value = max(population)
        index_max_value = population.index(max_value)
        current_value = max_value - result
        if current_value >= minimum_wealth:
            population[index] = minimum_wealth
            population[index_max_value] = max_value - result
        else:
            distribution = False
            print("No equal distribution possible")
            break
    else:
        population[index] = value

if distribution:
    print(population)




