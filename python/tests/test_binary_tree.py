import pytest
import random

from python.binary_tree import Node


@pytest.fixture
def node():
    return Node(random.randrange(100, 1000))


@pytest.fixture
def generate_random_numbers_list_big(is_iterations=1000, min_number=-500, max_number=1000):
    random_list = []

    for _ in range(is_iterations):
        a = random.randrange(min_number, max_number)
        random_list.append(a)

    return random_list


@pytest.fixture
def generate_random_numbers_list_small(is_iterations=30, min_number=-500, max_number=1000):
    random_list = []

    for _ in range(is_iterations):
        a = random.randrange(min_number, max_number)
        random_list.append(a)

    return random_list


def test_finding(node, generate_random_numbers_list_big):

    [node.append(el) for el in generate_random_numbers_list_big]
    assert node.check_having_element(generate_random_numbers_list_big[random.randrange(0, len(generate_random_numbers_list_big) - 1)])
    assert node.check_having_element(generate_random_numbers_list_big[random.randrange(0, len(generate_random_numbers_list_big) - 1)])
    assert node.check_having_element(generate_random_numbers_list_big[random.randrange(0, len(generate_random_numbers_list_big) - 1)])


def test_appending(node, generate_random_numbers_list_small):

    [node.append(el) for el in generate_random_numbers_list_small]
    generate_random_numbers_list_small.insert(0, node.data)

    assert node.list_of_all_elements().sort() == generate_random_numbers_list_small.sort()

