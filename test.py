from vector import Vector

def main():
    '''
 	#  x = Vector([8.218,-9.341])
 	#  y = Vector([-1.129,2.111])
 	# x.add(y)

	#   x = Vector([7.119,8.215])
 	#  y = Vector([-8.223,.878])
 	#  x.subtract(y)

 	#  x = Vector([1.671,-1.012,-.318])
 	#  multiplier= 7.41
 	#  x.scalar_multiply(multiplier)
  	
    
   	x = Vector([-.221,7.437])
   	x.magnitude()
   	x = Vector([8.813,-1.331,-6.247])
   	x.magnitude()

   	x = Vector([5.581,-2.136])
   	x.normalized()

   	x = Vector([1.996,3.108,-4.554])
   	x.normalized()
    '''
    x = Vector([7.887,4.138])
    y = Vector([-8.802,6.776])
    x.dot_product(y)

    x = Vector([-5.955,-4.904,-1.874])
    y = Vector([-4.496,-8.755,7.103])
    x.dot_product(y)
    
    x = Vector([3.183,-7.627])
    y = Vector([-2.668,5.319])
    x.find_angle(y)
    
    x = Vector([7.35,.221,5.188])
    y = Vector([2.751,8.259,3.985])
    x.find_angle(y,True)

if __name__ == "__main__":
   main()

