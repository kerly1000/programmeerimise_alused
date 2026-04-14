
import pytest

from hobbies import *

@pytest.fixture(autouse=True)

def init_tests():
    person1 = Person("Mari", "Kukk", ["dancing", "biking", "programming"])
    person2 = Person("Jeff", "Bezos", ["money", "hair", "late_capitalism", "space", "unions"])
    person3 = Person("Elon", "Musk", ["late_capitalism", "space", "cars"])
    print ("Test start")
    yield person1, person2, person3
    print("Test done")

def test_sort_by_most_hobbies():
    (person1, person2, person3) = init_tests()
    assert sort_by_most_hobbies(people) == [people[1], people[2], people[0]]

def test_sort_by_least_hobbies():
    assert sort_by_most_hobbies(people) == ["JeffBezos", "MariKukk", "ElonMusk"]

def test_filter_by_hobby():
    people = init_tests()
    assert filter_by_hobby(people, "space") == ["ElonMust", "JeffBezos"]

def test_sort_people_and_hobbies():
    people = init_tests()
    assert sort_people_and_hobbies() == ["ElonMusk", "JeffBezos", "MariKukk"]

def test_person_get_hobbies():
    person1 = Person("Mari", "Kukk", ["dancing", "biking", "programming"])
    assert person1.hobbies == ["biking", "dancing", "programming"]

def test_input_list_is_untouched():
    people_original = init_tests()
    people_param = people_original[::]
    sort_by_most_hobbies(people_param)
    assert people_param == people_original, "sort_by_most_hobbies modified input parameter"
    sort_by_most_hobbies(people_param)
    assert people_param == people_original, "sort_by_most_hobbies modified input parameter"
    sort_by_least_hobbies()
    assert people_param == people_original, "sort_by_most_hobbies modified input parameter"
    original_hobbies = people[0]hobbies[::]
    sort_people_and_hobbies(people_param)
    assert people_param == people_original, "sort_by_most_hobbies modified input parameter"
    filter_by_hobby()
    assert people_param == people_original, "sort_by_most_hobbies modified input parameter"
    person1.hobbies()
    assert people_param == people_original