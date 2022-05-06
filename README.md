# Electric-Vehicle-Charging-Station-Map

The aim of this project is to build a mobile application similar to google maps. This application is connected to your electric vehicle and it can receive the information related to the SOC of its battery. When you open the APP you can search for the destination that you want to go and it will show the best route along with the best charging places throughout your journey. The app will consider factors such as the time that will take you to get to a charging station, grid balance (if there is more power consumption in one side of the grid, the grid is unbalanced), and the congestion in the charging station to predict what is the best location to charge your car. You will receive points for charging your car at the suggested location since that will help utilities to balance the grid and better forecast the EV electricity consumption throughout the grid operation. You need to confirm your charging location before you start your journey to be able to receive the points.

The APP will have following parts:
- An interface like google to find the best route to destination
- Locate all feasible locations to charge the car
- Perform optimization considering distance, grid balance and congestion to find the best location for charging (we can even have a grading system and say the first best, the second best, etc.)
- Maximum points are awarded if you choose to charge your car at the first best location, less points if you choose second best and so on. You can redeem your points for a free charging when you reach a limit.
## Test Front End
#### Install modules
```
pip3 install -r requirements.txt
```
Run all cells from the `ev_routing_based_on_start_end.ipynb` file. 

Specify the start city in `dijkstra_algorithm` function. Specify the start city again and end city in `print_function`. 

Running `print_result` function will display the best route between cities. The `path_with_charging` list contains the cities the car must pass through and where it needs to charge.
