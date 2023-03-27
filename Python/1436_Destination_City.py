class Solution:
    def destCity(self, paths) -> str:
        # Create a dictionary that would store the number of outgoing paths for each city 
        outgoing_count ={}
        # Need to iterate through paths array 
        for path in paths: 
            # There are two items in path
            city_a, city_b = path 
            # If the city is already not in the dictionary we return 0 othwerwise add an increment of 1
            outgoing_count[city_a] = outgoing_count.get(city_a, 0) + 1 
            outgoing_count[city_b] = outgoing_count.get(city_b, 0)

        for city in outgoing_count: 
            if outgoing_count[city] == 0:
                return city 

# Create an instance of the Solution class
solution = Solution()
# Define the input array
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# Call the destCity function and store the output in a variable
result = solution.destCity(paths)
# Print the output
print(result)
