def sorting_cheeses(**cheeses):
    sorted_cheeses = sorted(cheeses.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ""
    for name, quantities in sorted_cheeses:
        result += name + "\n"
        sorted_quantities = sorted(quantities, reverse=True)
        result += "\n".join(str(x) for x in sorted_quantities)
        result += "\n"
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
