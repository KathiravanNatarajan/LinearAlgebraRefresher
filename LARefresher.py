# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 10:39:02 2018

@author: sunka
"""
import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        print v.coordinates
        return self.coordinates == v.coordinates
        
    def __add__(self, v):
        added = [x + y for x, y in zip(self.coordinates,v.coordinates)]
        return Vector(added)
    
    # You can call a funtion like above as well as below
    def subtract(v1,v2):
        subtracted = []
        for i in range(len(v1.coordinates)):
            subtracted.append(v1.coordinates[i] - v2.coordinates[i])
        return Vector(subtracted)
        
    def scalar_multiply(self,s):
        multiplied = [s*x for x in self.coordinates]
        return Vector(multiplied)
        
    def magnitude(self):
        mag = [i*i for i in self.coordinates]
        mag = math.sqrt(sum(mag))
        return mag
        
    def normalize(self):
        try:
            mag = self.magnitude()
            unit_vector = self.scalar_multiply(1/mag)
            return unit_vector
        except ZeroDivisionError:
            raise Exception("Cannot normalize the zero vector")
    def dot_product(v1,v2):
        dot = sum([x*y for x, y in zip(v1.coordinates,v2.coordinates)])
        return dot     
        
    def angle_of_vectors(v1,v2,second = False):
        if second == True:
            x = Vector.dot_product(Vector.normalize(v1),Vector.normalize(v2))
        else:
            x = (Vector.dot_product(v1,v2))/(v1.magnitude() * v2.magnitude())       
        angle_in_rad = math.acos(x)
        angle_in_deg = math.degrees(angle_in_rad)
        return angle_in_rad, angle_in_deg

        
my_vector = Vector([3,4,1])
my_vector2 = Vector([2,5,1])
print my_vector == my_vector2
print my_vector + my_vector2
print Vector.subtract(my_vector,my_vector2)
print Vector.scalar_multiply(my_vector,2)
print my_vector.magnitude()
print my_vector.normalize()
print Vector.dot_product(my_vector,my_vector2)
m1=Vector([7.35,0.221,5.188])
m2=Vector([2.751,8.259,3.985])
print Vector.angle_of_vectors(m1,m2,True)