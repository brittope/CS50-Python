import pytest
from math import isclose
from project import CityTour, CityTourUseCase

@pytest.fixture
def city_tour_instance():
    file_path = '/workspaces/131783699/ProblemSet9/Project/berlin52.csv' # Replace with a file path for testing
    city_tour = CityTour(file_path)
    city_tour.read_coordinates_from_file()
    city_tour.precalculate_distances()
    return city_tour

def test_read_coordinates_from_file(city_tour_instance):
    assert len(city_tour_instance.coord_x) == len(city_tour_instance.coord_y)
    assert len(city_tour_instance.coord_x) == len(city_tour_instance.city_num)

def test_precalculate_distances(city_tour_instance):
    assert len(city_tour_instance.distance_matrix) == len(city_tour_instance.coord_x)
    assert all(len(row) == len(city_tour_instance.coord_x) for row in city_tour_instance.distance_matrix)

def test_find_nearest_neighbor(city_tour_instance):
    starting_city = 0
    cities_to_check = [1, 2, 3]
    nearest_neighbor, distance = city_tour_instance.find_nearest_neighbor(starting_city, cities_to_check)

    assert nearest_neighbor in cities_to_check
    assert distance >= 0

def test_tour(city_tour_instance):
    starting_point = 0
    tour_result = city_tour_instance.tour(starting_point)
    assert len(tour_result) == len(set(tour_result)) + 1

def test_calculate_total_distance(city_tour_instance):
    tour_result = [39, 37, 36, 38, 35, 34, 33, 43, 45, 47, 23, 4, 14, 5, 3, 24, 11, 27, 26, 25, 46, 12, 13, 51, 10, 50, 32, 42, 9, 8, 7, 40, 18, 44, 31, 48, 0, 21, 30, 17, 2, 16, 20, 22, 19, 49, 15, 28, 29, 41, 6, 1, 39]
    total_distance = city_tour_instance.calculate_total_distance(tour_result)
    assert total_distance >= 0

def test_find_best_starting_point(city_tour_instance):
    city_tour_use_case = CityTourUseCase(city_tour_instance)
    best_starting_point = city_tour_use_case.find_best_starting_point()
    assert best_starting_point >= 0

if __name__ == '__main__':
    pytest.main()

