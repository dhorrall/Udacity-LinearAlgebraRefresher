#note that this works in python 2.7, not 2.6 or 3
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

    def add(self,newIterable):
	
	#using a list comprehension and zip to sum up two list objects which are the coordinates of the orginal and new vector
	#to do should check to see if lengths are the same first
	newSum = [round(x+y,3) for x,y in zip(self.coordinates,newIterable.coordinates)]
	#Convert list to a Vector object	
	newVector = Vector(newSum)
	print (newVector)

    def subtract(self,newIterable):
	
	#using a list comprehension and zip to subract two list objects which are the coordinates of the orginal and new vector
	#to do should check to see if lengths are the same first
	newSum = [round(x-y,3) for x,y in zip(self.coordinates,newIterable.coordinates)]
	#Convert list to a Vector object	
	newVector = Vector(newSum)
	print (newVector)

    def scalar_multiply(self,multiplier):
	
	#using a list comprehension to multiply a list by a scalar value and returns new vector
	#to do should check to see if lengths are the same first
	newSum = [round(x * multiplier,3) for x in self.coordinates]
	#Convert list to a Vector object	
	newVector = Vector(newSum)
	print (newVector)
	

