#note that this works in python 2.7, not 2.6 or 3
#DGH need to add the error handling code
import math
import numpy
from decimal import Decimal
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
        return 'Vector: {0}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __getitem__(self, i):
        return self.coordinates[i]

    def __iter__(self):
        return self.coordinates.__iter__()

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

    def unit_vector(self):
        try:	
            sqrList = list(map((lambda x: x **2), self.coordinates))
            theMagnitude = self.magnitude()
            invMagnitude = 1./self.magnitude()
            normalized = self.scalar_multiply(invMagnitude)
            return normalized
        
        except ZeroDivisionError:
           raise Exception('Cannot normalize the zero vector!')
            

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
	    #print (dot_product)
	    return dot_product

    def find_angle(self,newVector,degrees=False):
        n1 = self.unit_vector()
        n2 = newVector.unit_vector()
	    #compute angle between two vectors is a formula: Angle of vectors = arcos(v dot w/||V|| x ||W||) in radians
        angle_in_radians = math.acos(n1.dot_product(n2))
        if degrees == True:
            degrees_per_radian = 180./math.pi
            angle = angle_in_radians * degrees_per_radian
	    
        else:
            angle = angle_in_radians
        
        print angle
        return angle

    def is_parallel(self,newVector):
    #need to first check if either if magnitude is zero, if so, then by default they are parallel
        result= (self.is_mag_zero() or newVector.is_mag_zero() or self.find_angle(newVector) == 0 or self.find_angle(newVector) == math.pi)
        print ('Parallel:'+str(result))
        return result
	

    def is_mag_zero(self,tolerance=1e-10):
        #print (self.magnitude() < tolerance)
        return (self.magnitude() < tolerance)
        
        
    def is_orthogonal(self,newVector):
        result = (self.dot_product(newVector)==0)
        print('Orthogonal:'+str(result))
        return (result)

    def component_parallel_to(self,baseVector):
        #the projection of a vector onto another vector 
        try:        
            norm = baseVector.unit_vector()
            scalarWeight = self.dot_product(norm)
            result_parallel = norm.scalar_multiply(scalarWeight)
            print((result_parallel.coordinates))
            return result_parallel
        except Exception as e:
            if str(e)==self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e

    def component_orthogonal_to(self,baseVector):
        try:
            #This works because v = v_parallel + v_perp
            projection = self.component_parallel_to(baseVector)
            result = self.subtract(projection)
            print((result.coordinates))
            return result
        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG)
            else:
                raise e

    def cross_product(self,aVector):
        #using numpy library instead of implementing cross product myself
        x=Vector(numpy.cross(self.coordinates,aVector.coordinates).tolist())
        print (type(x))
        return x

    def area_parallelogram_with(self,aVector):
        #Area of the parallelogram equals the magnitude of the resulting vector generated by taking the cross product
        cross_prod = self.cross_product(aVector)
        area = cross_prod.magnitude()
        print (area)
        return area

    def area_triangle_with(self,aVector):
        #Area of the triangle equals 1/2 the value of the parallelogram
        area = self.area_parallelogram_with(aVector)/2        
        print (area)
        return area     



        
 	
