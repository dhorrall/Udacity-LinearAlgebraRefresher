#note that this works in python 2.7, not 2.6 or 3
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
        return self.coordinates == v.coordinates

    def add(self,newVector):
	
	#using a list comprehension and zip to sum up two list objects which are the coordinates of the orginal and new vector
	#to do should check to see if lengths are the same first
	newSum = [(x+y) for x,y in zip(self.coordinates,newVector.coordinates)]
	#Convert list to a Vector object	
	newVector = Vector(newSum)
	#print (newVector)
	#newVector = float("{0:.3f}".format(newVector))
	return newVector

    def subtract(self,newVector):
	
	#using a list comprehension and zip to subract two list objects which are the coordinates of the orginal and new vector
	#to do should check to see if lengths are the same first
	newSum = [(x-y) for x,y in zip(self.coordinates,newVector.coordinates)]
	#Convert list to a Vector object	
	newVector = Vector(newSum)
	#print (newVector)
	return newVector

    def magnitude(self):
	
	#using a list comprehension to multiply a list by a scalar value and returns new vector
	#to do should check to see if lengths are the same first
	#newSum = [round(x**2,3) for x in self.coordinates]
	#This squares each coordinate via lambda function
	sqrList=list(map((lambda x: x **2), self.coordinates))
	#This reduces via suming each item of the list
	magnitude= reduce(lambda x,y: x + y, sqrList)
	magnitude = math.sqrt(magnitude)
	#Convert list to a Vector object	
	#newVector = Vector(newSum)
	#print (round(magnitude,3))
	return (round(magnitude,3))

    def normalized(self):
	
	#This squares each coordinate via lambda function
	#needs to use a try catch to avoid possibly dividing by zero
	sqrList=list(map((lambda x: x **2), self.coordinates))
	#This reduces via suming each item of the list
	theMagnitude = self.magnitude()
	invMagnitude = 1./self.magnitude()
	normalized = self.scalar_multiply(invMagnitude)
	#print ((normalized))
	return normalized

    def scalar_multiply(self,multiplier):
	
	
	#using a list comprehension to multiply a list by a scalar value and returns new vector
	#to do should check to see if lengths are the same first
	#
	newSum = [(x * multiplier) for x in self.coordinates]
	#Convert list to a Vector object	
	newVector = Vector(newSum)
	#print (newVector)
	return newVector

    def dot_product(self,newVector):
	
	#using a list comprehension and zip to multiply two list objects which are the coordinates of the orginal and new vector
	#to do should check to see if lengths are the same first
	listProduct = [(x*y) for x,y in zip(self.coordinates,newVector.coordinates)]
	#This reduces via suming each item of the list
	dot_product= reduce(lambda x,y: x + y, listProduct)
	dot_product = float("{0:.3f}".format(dot_product))
	print (dot_product)
	return dot_product

    def find_angle(self,newVector,degrees=False):
	n1 = self.normalized()
	n2 = newVector.normalized()
	#compute angle between two vectors is a formula: Angle of vectors = arcos(v dot w/||V|| x ||W||) in radians
	angle_in_radians = math.acos(n1.dot_product(n2))
	if degrees == True:
	    degrees_per_radian = 180./math.pi
	    angle = angle_in_radians * degrees_per_radian
	else:
	    angle=angle_in_radians

	#angle = round(math.acos(dotProd/(magOne *magTwo)),3)

	#using a list comprehension and zip to multiply two list objects which are the coordinates of the orginal and new vector
	#to do should check to see if lengths are the same first
	#listProduct = [round(x*y,3) for x,y in zip(self.coordinates,newVector.coordinates)]
	#This reduces via suming each item of the list
	#dot_product= reduce(lambda x,y: x + y, listProduct)
	print (angle)
	angle = float("{0:.3f}".format(angle))
	print ((angle))
	#return dot_product	
	return angle
    
    def is_parallel(self,newVector):
	#using a list comprehension and zip to find modulo two list objects which are the coordinates of the orginal and new vector
	#to do should check to see if lengths are the same first
        #If modulo is zero, then they are multiples of one other which means they are parallel
	listModulo = [(x % y) for x,y in zip(self.coordinates,newVector.coordinates)]
	#This reduces via suming each item of the list
	moduloSum= reduce(lambda x,y: x + y, listModulo)
	moduloSum = float("{0:.3f}".format(moduloSum))
	print (moduloSum)
	return moduloSum
        
    
    def is_orthogonal(self,newVector):
        print(True)
 	
