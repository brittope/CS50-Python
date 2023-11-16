from math import sqrt

class CityTour:
    def __init__(self, file_path):
        self.file_path = file_path
        self.city_num = []
        self.coord_x = []
        self.coord_y = []
        self.cities = []
        self.distance_matrix = []

    def read_coordinates_from_file(self):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()

        for line in lines:
            columns = line.split(',')
            city_num = int(columns[0])
            x, y = float(columns[1]), float(columns[2])
            self.city_num.append(city_num)
            self.coord_x.append(x)
            self.coord_y.append(y)
            self.cities.append([x, y])

    def precalculate_distances(self):
        n = len(self.coord_x)
        self.distance_matrix = [
            [
                sqrt((self.coord_x[i] - self.coord_x[j]) ** 2 + (self.coord_y[i] - self.coord_y[j]) ** 2)
                for j in range(n)
            ]
            for i in range(n)
        ]

    def find_nearest_neighbor(self, current_city, cities_to_check):
        min_distance = float('inf')
        nearest_neighbor = -1

        for city_index in cities_to_check:
            distance = self.distance_matrix[current_city][city_index]

            if 0 < distance < min_distance:
                min_distance = distance
                nearest_neighbor = city_index

        return nearest_neighbor, min_distance

    def reset_cities(self):
        self.cities = [[x, y] for x, y in zip(self.coord_x, self.coord_y)]

    def tour(self, starting_point):
        self.reset_cities()
        tour_cities = []
        current_city = starting_point

        for _ in range(len(self.cities) - 1):
            cities_to_check = [city for city in range(len(self.cities)) if self.cities[city]]
            next_city, distance = self.find_nearest_neighbor(current_city, cities_to_check)

            if next_city != -1:
                tour_cities.append(current_city)
                self.cities[current_city] = []
                current_city = next_city

        last_unvisited_city = next(city for city in range(len(self.cities)) if self.cities[city])
        tour_cities.append(last_unvisited_city)
        tour_cities.append(starting_point)

        return tour_cities

    def calculate_total_distance(self, tour):
        total_distance = sum(
            self.distance_matrix[tour[i]][tour[i + 1]]
            for i in range(len(tour) - 1)
        )

        return total_distance / 1000

class CityTourUseCase:
    def __init__(self, city_tour):
        self.city_tour = city_tour

    def find_best_starting_point(self):
        smallest_distance = float('inf')
        best_start_point = 0

        for starting_point in range(len(self.city_tour.city_num)):
            tour_result = self.city_tour.tour(starting_point)
            total_distance = self.city_tour.calculate_total_distance(tour_result)

            if total_distance < smallest_distance and total_distance != 0:
                smallest_distance = total_distance
                best_start_point = starting_point

        return best_start_point

def main():
    file_path = input('Provide the file path: ')

    city_tour = CityTour(file_path)
    city_tour.read_coordinates_from_file()
    city_tour.precalculate_distances()

    city_tour_use_case = CityTourUseCase(city_tour)
    starting_point = city_tour_use_case.find_best_starting_point()

    tour_result = city_tour.tour(starting_point)
    total_distance = city_tour.calculate_total_distance(tour_result)

    print(f"The traveled distance  was: {round(total_distance, 2)} km")
    print("The fastest path is:", tour_result)

if __name__ == "__main__":
    main()

