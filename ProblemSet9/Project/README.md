  # TRAVELING SALESMAN
    #### Video Demo: https://www.youtube.com/watch?v=iRDCU9yXHAs
    #### Description:

        This Python script performs an optimization of the traveling salesmen problem by finding the shortest path that visits all cities. It uses a nearest neighbor algorithm to determine the optimal route.
        This was an old project from school that I decided to remake with the knowledge I acquired during the CS50 course

        ## Overview

        The code consists of two classes: `CityTour` and `CityTourUseCase`, along with a `main` function to execute the optimization.

        ### CityTour Class

        This class handles the reading of city coordinates from a file, precalculates the distance matrix between cities, and implements the nearest neighbor algorithm to find the optimal tour.

        - **Methods:**
        - `__init__(self, file_path)`: Initializes the CityTour object with a file path.
        - `read_coordinates_from_file(self)`: Reads city coordinates from the specified file.
        - `precalculate_distances(self)`: Precalculates the distance matrix between cities based on their coordinates.
        - `find_nearest_neighbor(self, current_city, cities_to_check)`: Finds the nearest neighbor for a given city.
        - `reset_cities(self)`: Resets the list of cities to their original coordinates.
        - `tour(self, starting_point)`: Performs the city tour optimization using the nearest neighbor algorithm.
        - `calculate_total_distance(self, tour)`: Calculates the total distance of the tour.

        ### CityTourUseCase Class

        This class encapsulates the use case of finding the best starting point for the tour.

        - **Methods:**
        - `__init__(self, city_tour)`: Initializes the CityTourUseCase object with a CityTour instance.
        - `find_best_starting_point(self)`: Finds the best starting point for the city tour based on the shortest total distance.

        ### main Function

        The `main` function is the entry point of the script. It takes user input for the file path containing city coordinates, creates instances of the `CityTour` and `CityTourUseCase` classes, executes the optimization, and prints the results.

        ## Usage

        1. Run the script.
        2. Provide the file path containing city coordinates when prompted.
        3. The script will output the total distance of the optimized tour and the path of the tour.

        **Note:** The distance is given in kilometers, and the coordinates are read from a CSV file with each line representing a city with its corresponding X and Y coordinates.

        **Note2:** The submitted file should follow this pattern for the script to read it properly:
        id(ex. 1,2,3...),x_cordinate(ex. 565.0),y_condinate(ex. 575.0)
        (DIVIDED BY COMAS AND ONE PER LINE)

        ## Example

        ```
        Provide the file path: city_coordinates.csv
        The traveled distance  was: 123.45 km
        The fastest path is: [0, 2, 1, 3, 0]
        ```

        In this example, the optimized tour starts at city 0, visits cities 2, 1, and 3 in that order, and returns to city 0. The total distance of the tour is 123.45 kilometers.
