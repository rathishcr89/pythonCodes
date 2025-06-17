def person_lister(func):
    def inner(people):
        # Sort by age (index 2), convert to int for sorting
        sorted_people = sorted(people, key=lambda x: int(x[2]))
        # Apply the formatting function to each person
        return [func(person) for person in sorted_people]
    return inner

@person_lister
def name_format(person):
    title = "Mr." if person[3] == "M" else "Ms."
    return f"{title} {person[0]} {person[1]}"

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')