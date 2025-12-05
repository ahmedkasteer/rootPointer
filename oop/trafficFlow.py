"""
Implementing Traffic Flow system using OOP Principles. 
"""
class Vehicle:
    def __init__(self, vehicle_id, max_speed, acceleration_rate, initial_position = 0):
        self._vehicle_id = vehicle_id
        self._max_speed = max_speed
        self._acceleration_rate = acceleration_rate
        self._initial_position = initial_position
        self._current_speed = 0.0
        self._is_moving = False

        #getter methods
    def get_id(self):
        return self._vehicle_id
    def get_position(self):
        return self._initial_position
    def get_speed(self):
        return self._current_speed
       
        #behavior methods
    def accelerate(self, time_Step):
        new_speed = self._current_speed + (self._acceleration_rate * time_Step)

        if new_speed > self._max_speed:
            self._current_speed = self._max_speed
        else:
            self._current_speed = new_speed
        self._is_moving = True 
    
    def decelerate(self, time_Step):
        deceleration_rate = self._acceleration_rate * 1.5 #brakes applied harder than accelerating 
        new_speed = self._current_speed - (deceleration_rate * time_Step)

        if new_speed < 0:
            self._current_speed = 0.0
            self._is_moving = False
        else:
            self._current_speed = new_speed
    
    def update_position(self, time_Step):
        #calculate and update pos based on curr speed and time
        # d = s*t
        distance_moved = self._current_speed * time_Step
        self._initial_position += distance_moved
        return self.get_position
    
    def check_traffic_light(self, distance_to_light, light_state):
        #behavior called by road class
                    #if moving towards light and it's red and distance is less than 50m start braking. 
        if light_state == "Red" and distance_to_light < 50 and self._current_speed > 0:
            print(f"{self._vehicle_id}: Decelarating for Red Light.")
            return "BRAKES APPLIED."
        
        elif light_state == "Green":
            #if light is green maintain speed or u can accelerate
            if self._current_speed < self._max_speed:
                return "ACCELERATE"
            
        return "MAINTAIN SPEED" 

class Car(Vehicle):
    def __init__(self, vehicle_id, max_speed, acceleration_rate, passenger_capacity, initial_position =0):
        #calling constructor of parent class vehicle
        super().__init__(vehicle_id, max_speed, acceleration_rate, initial_position)

        #adding attributes for car
        self._passenger_capacity = passenger_capacity
        self._current_passengers = 0

        print(f"{self._vehicle_id} created with capacity {self._passenger_capacity}.")
    
    #unique getter methods
    def get_capacity(self):
        #returns max passenger capacity of the car.
        return self._passenger_capacity
    def board_passengers(self, num_to_add):
        #adds passenger abiding to capacity limit 
        if self._current_passengers + num_to_add <= self._passenger_capacity:
            self._current_passengers += num_to_add
            return True
        else:
            print(f"Warning: Cannot Board {num_to_add} passengers. Car is full.")
            return False
    
    #adding polymorphic function here
    def check_traffic_light(self, distance_to_light, light_state):
        #overrides parent's method to potentially implement Car specific braking. 

        #For car we wait little longer before we apply brakes 
        if light_state == "Red" and distance_to_light < 30 and self.get_speed() > 0:
            print(f"Car {self._vehicle_id}: Braking hard for Red Light.")
            return "BRAKE"
        #for rest cases use parent's class conditions
        return super().check_traffic_light(distance_to_light, light_state)

class Truck(Vehicle):
    def __init__(self, vehicle_id, max_speed, acceleration_rate, payload_capacity, initial_poisition = 0):
        super().__init__(vehicle_id, max_speed, acceleration_rate, initial_poisition)
        #adding unique attributes for truck
        self._payload_capacity = payload_capacity
        self._is_loaded = False             
        self._load_penalty_factor = 0.5     #factor by which acceleration reduced when loaded
        print(f"Truck {self._vehicle_id} created with payload capacity {self._payload_capacity}.")
    
    def load_cargo(self, weight):
        #if weight within load capacity sets truck to loaded state
        if weight <= self._payload_capacity:
            self._is_loaded = False
            print(f"Truck {self._vehicle_id} is now loaded.")
            return True
        else:
            print(f"Warning: Cannot Load {weight}. Exceeds capacity of {self._payload_capacity}.")
            return False
    
    def unload_cargo(self):
        #sets truck to unloaded state
        self._is_loaded = False
        print(f"Truck {self._vehicle_id} is now unloaded.")
        #method overriding here polymorphism implemented 
    
    def accelerate(self, time_Step):
        #loaded trucks accelerates slower 
        effective_rate = self._acceleration_rate
        if self._is_loaded:
            #apply loaded penalty factor: reduces acceleration 
            effective_rate *= self._load_penalty_factor  
        #calculate new speed after applyimng load factor
        new_speed = self._current_speed + (effective_rate * time_Step)
        #then update speed
        if new_speed > self._max_speed:
            self._current_speed = self._max_speed
        else:
            self._current_speed = new_speed
        self._is_moving = True

    def check_traffic_light(self, distance_to_light, light_state):
        #overriding parent method polymmorphism is implemented 
        #heavy truck takes longer to brake so need to increase brake distance
        required_braking_distance = 60 #set higher threshold than car since trucks take longer to brake.
        if light_state == 'Red' and distance_to_light < required_braking_distance and self.get_speed() > 0:
            print(f"Truck {self._vehicle_id}: **WARNING!** Heavy vehicle braking for Red light.")
            return "BRAKE"     
        #for all other cases default vehicle check traffic light is implemented. 
        return super().check_traffic_light(distance_to_light, light_state)
    
class TrafficLight:
    def __init__(self, position, initial_state = "Red"):
        self._position = position #location on road distance from start
        self._state = initial_state #current color red, yellow or green
        self._time_in_state = 0 # time elapsed since the last change

        #define duration for each state in seconds. 
        self._state_durations = {
            "Red" : 20,
            "Yellow" : 5,
            "Green" : 30
        }

        #defining sequence of state. 
        self._state_sequence = ["Red", "Green", "Yellow"]
        print(f"Traffic Light created at position {self._position}, starting at {self._state}.")

    #getter methods
    def get_position(self):
        #returns the light position on the road 
        return self._position
    
    def get_state(self):
        #returns the current state color of the light 
        return self._state
    
    def update(self, time_step):
        #updates lights internal timer and cycles the state if the duration is met. 
        #this method will be called repeatedly by the road class.
        self._time_in_state += time_step
        if self._time_in_state >= self._state_durations[self._state]:
            self._cycle_state()
    
    def _cycle_state(self):
        #private method to change color of light to the next color listed on sequence 
        #encapsulation, state changes are internal logic. 
        current_index = self._state_sequence.index(self._state)
        #find the next index, wrapping around to the beginning if necessary
        next_index = (current_index + 1) % len(self._state_sequence)
        self._state = self._state_sequence[next_index]
        self._time_in_state = 0 #reset timer for new state
        print(f"Traffic Light at {self._position} changed to {self._state}")

class Road:
    def __init__(self, road_length, time_step = 1.0):
        self._length = road_length
        self._vehicles = [] #list for objects of vehicles: car, truck
        self._traffic_lights = [] #list to hold all traffic lights
        self._time_step = time_step #time interval for each simulation update (e.g. 1.0 second)
        self._time = 0.0 #total elapsed time for simulation

        print(f"Road created with length {self._length} units. Simulation step: {self._time_step}s.")

    def add_vehicle(self, vehicle_obj):
        #adding new vehicle object car/truck to the road
        if vehicle_obj.get_position()< self._length:
            self._vehicles.append(vehicle_obj)
            print(f"Added {type(vehicle_obj).__name__} {vehicle_obj.get_id()} to the road.")
        else:
            print("Vehicle position exceeds road length.")

    def add_traffic_light(self, light_obj):
        #adds new traffic light obj to the road
        if light_obj.get_position() < self._length:
            self._traffic_lights.append(light_obj)
            #sort lights by position for easy checking 
            self._traffic_lights.sort(key = lambda light: light.get_position())
        else:
            print("Traffic light position exceeds road length.")

    def run_simulation_step(self):
        #advancing simulation by 1 step. 
        self._time += self._time_step
        print(f"\n---- SIMULATION TIME: {self._time: .1f}s -----")

        #1. update trffic lights
        for light in self._traffic_lights:
            light.update(self._time_step)
        #2. update vehicles and check lights
        vehicles_to_remove = []
        for vehicle in self._vehicles:
            #find nearest traffic light ahead
            nearest_light = self._get_nearest_traffic_light(vehicle.get_position())

            action = "MAINTAIN" #default action for speed

            if nearest_light:
                distance = nearest_light.get_position() - vehicle.get_position()
                light_state = nearest_light.get_state()

                #delegate the decision to the vehicle object (Polymorphism)
                action = vehicle.check_traffic_light(distance, light_state)
            if action == "ACCELERATE":
                vehicle.accelerate(self._time_step)
            elif action == "BRAKE":
                vehicle.decelerate(self._time_step)
            #else: MAINTAIN (do nothing to speed)

            #update vehcile position
            vehicle.update_position(self._time_step)

            if vehicle.get_position() >= self._length:
                print(f"Vehicle {vehicle.get_id()} has left the road.")
                vehicles_to_remove.append(vehicle)
            
            print(f"ID: {vehicle.get_id()} | Pos: {vehicle.get_position():.2f} | Speed: {vehicle.get_speed():.2f}")

        for vehicle in vehicles_to_remove:
            self._vehicles.remove(vehicle)
    
    def _get_nearest_traffic_light(self, current_position):
        #finds the next traffic light ahead of the vehicle's position.
        for light in self._traffic_lights:
            if light.get_position() > current_position:
                return light
        return None
    
#creating road obj
main_road = Road(road_length= 2000, time_step=1.0)

#create and add traffic lights
light_A = TrafficLight(position=500, initial_state="Green")
light_B = TrafficLight(position=1500, initial_state="Red")
main_road.add_traffic_light(light_A)
main_road.add_traffic_light(light_B)


#create and add vehicles polymorphism in action
car1 = Car(vehicle_id= 101, max_speed=30, acceleration_rate=5, passenger_capacity=4)
truck1 = Truck(vehicle_id= 201, max_speed=20, acceleration_rate=3, payload_capacity=10000)

main_road.add_vehicle(car1)
main_road.add_vehicle(truck1)

#run the simulation
for i in range(10):
    main_road.run_simulation_step()




    