from vpython import *
from math import *


class Ball:
    field_radius = .1
    current_energy = 10000000
    
    def __init__(self, vect, rad, col,dest_coordinates):
        self.vector = vect
        self.arrow_vect = vector(0,0,0)
        self.color = col
        self.radius = rad
        self.destination = dest_coordinates
        self.vpython_object = sphere(pos=self.vector, radius=self.radius, color=self.color)
        self.arrow = arrow(pos=self.vpython_object.pos, axis=self.arrow_vect, color=color.yellow)

    def update_objects(self, list_of_objects):
        self.other_objects = list_of_objects
        return 1
    
    def get_X(self):
        return self.vector.x
    
    def get_Y(self):
        return self.vector.y
        
    def move(self,d_X, d_Y):
        # Update X and Y
        self.vector.x += d_X
        self.vector.y += d_Y
        
        # Update Arrow X and Y
        self.arrow_vect.x = 5*d_X
        self.arrow_vect.y = 5*d_Y
        
        # Update vpython Objects
        self.vpython_object.pos = self.vector
        self.arrow.pos = self.vector
        self.arrow.axis = self.arrow_vect
        
    def descend_gradient(self):
        #set local_min to current energy, that way if no step is better 
        #then current location, no step is taken
        local_min = self.current_energy
        current_x = self.vector.x
        current_y = self.vector.y
        goal_x = self.destination[0]
        goal_y = self.destination[1]
        d_X = 0
        d_Y = 0
        #Distance of Each Step
        step_distance = 0.1
        #Precision of Gradient in Degrees (30 would be a 30 degree increment, so [0,30,60,90...360))
        precision = 10
        i = 0
        while i<360:
            # Get Point
            temp_d_X = round(step_distance*sin(radians(i)),6)
            temp_d_Y = round(step_distance*cos(radians(i)),6)
            check_x = current_x + temp_d_X
            check_y = current_y + temp_d_Y
            
            # Get Point Weight
            # Point Weight = dist_goal + COLLISION_FORCE
            # This means that the closest point will be the smallest weight, but if it collides, it will not be
            collision_cost = self.check_collision(check_x, check_y)
            distance_goal = sqrt((goal_x-check_x)**2 + (goal_y-check_y)**2)
            point_weight = collision_cost + distance_goal
            # if Point weight < local_min, set to local_min
            if point_weight < local_min:
                local_min = point_weight
                d_X = temp_d_X
                d_Y = temp_d_Y
            
            #increase iterator
            i+=precision
        #move to point
        self.move(d_X, d_Y)
        
        
    def check_collision(self,X,Y):
        ## Still working on collision detection
        for i in self.other_objects:
            # Get Distance Between Two Items
            dist =sqrt((i.get_X()-X)**2 + (i.get_Y()-Y)**2)
            
            #add forcefield radius
            field_radiuses = self.field_radius + i.field_radius
            
            if dist <= field_radiuses:
                #return arbitrarily large number
                return 900000000
            
        return 0
