NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    names = []
    for name in NAMES:
        name = name.title()
        if name not in names:
            names.append(name)
    return names


def sort_by_surname_desc(names):
    names = dedup_and_title_case_names(names)
    #names.sort(key=lambda x: x.split(" ")[1], reverse=True)
    return sorted(names, key=lambda x: x.split(" ")[1], reverse=True)


def shortest_first_name(names):
    names = dedup_and_title_case_names(names)
    shortest_name = min(names, key=lambda x: len(x))
    return shortest_name.split(" ")[0]


if __name__ == "__main__":
    def test_dedup_and_title_case_names():
        names = dedup_and_title_case_names(NAMES)
        assert names.count('Bob Belderbos') == 1
        assert names.count('julian sequeira') == 0
        assert names.count('Brad Pitt') == 1
        assert len(names) == 10
        assert all(n.title() in names for n in NAMES)


    def test_sort_by_surname_desc():
        names = sort_by_surname_desc(NAMES)
        assert names[0] == 'Julian Sequeira'
        assert names[-1] == 'Alec Baldwin'


    def test_shortest_first_name():
        assert shortest_first_name(NAMES) == 'Al'

    print(test_dedup_and_title_case_names())
    print(test_sort_by_surname_desc())
    print(test_shortest_first_name())