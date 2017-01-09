from vector import Vector
from line import Line
from plane import Plane
#test modification
def main():
    '''    
    x = Vector([-7.579,-7.88])
    y = Vector([22.737,23.64])
    x.is_parallel(y)	
    x.is_orthogonal(y)    

    x = Vector([-2.029,9.97,4.172])
    y = Vector([-9.231,-6.639,-7.245])
    x.is_parallel(y)
    x.is_orthogonal(y)
    
    x = Vector([-2.328,-7.284,-1.214])
    y = Vector([-1.821,1.072,-2.94])
    x.is_parallel(y)
    x.is_orthogonal(y)
    
    x = Vector([2.118,4.827])
    y = Vector([0,0])
    x.is_parallel(y)
    x.is_orthogonal(y)
    
    x = Vector([3.039,1.879])
    y = Vector([.825,2.036])
    x.component_parallel_to(y)
        
    x = Vector([-9.88,-3.264,-8.159])
    y = Vector([-2.155,-9.353,-9.473])
    x.component_orthogonal_to(y)
    
    x = Vector([3.009,-6.172,3.692,-2.51])
    y = Vector([6.404,-9.144,2.759,8.718])
    x.component_parallel_to(y)
    x.component_orthogonal_to(y)
    
    x = Vector([8.462,7.893,-8.187])
    y = Vector([6.984,-5.975,4.778])
    x.cross_product(y)
    
    x = Vector([-8.987,-9.838,5.031])
    y = Vector([-4.268,-1.861,-8.866])
    x.area_parallelogram_with(y)
    x.area_triangle_with(y)

    x = Vector([1.5,9.547,3.691])
    y = Vector([-6.007,.124,5.772])
    x.area_parallelogram_with(y)
    x.area_triangle_with(y)
    '''
    v1a = Vector([-0.412,3.806,.728])
    v1b = Vector([1.03,-9.515,-1.82])
    plane1a = Plane(v1a,-3.46)
    plane1b = Plane(v1b,8.65)
    print ('Plane Pair 1 Is Parallel '+str(plane1a.is_parallel(plane1b)))
    print ('Plane Pair 1 Is Same Plane ' + str(plane1a==plane1b))
    #print(line1a.find_intersection(plane1b))

    v2a = Vector([2.611,5.528,.283])
    v2b = Vector([7.715,8.306,5.342])
    plane2a = Plane(v2a,4.6)
    plane2b = Plane(v2b,3.76)
    print ('Plane Pair 2 Is Parallel '+str(plane2a.is_parallel(plane2b)))
    print ('Plane Pair 2 Is Same Plane ' + str(plane2a==plane2b))
    #print(line1a.find_intersection(plane1b))

    v3a = Vector([-7.926,8.625,-7.217])
    v3b = Vector([-2.642,2.875,-2.404])
    plane3a = Plane(v3a,-7.952)
    plane3b = Plane(v3b,2.443)
    print ('Plane Pair 3 Is Parallel '+str(plane3a.is_parallel(plane3b)))
    print ('Plane Pair 3 Is Same Plane ' + str(plane3a==plane3b))
    #print(line1a.find_intersection(plane1b))

    v3a = Vector([1,1,1])
    v3b = Vector([1,1,1])
    plane3a = Plane(v3a,1)
    plane3b = Plane(v3b,1)
    print ('Plane Pair 3 Is Parallel '+str(plane3a.is_parallel(plane3b)))
    print ('Plane Pair 3 Is Same Plane ' + str(plane3a==plane3b))
    #print(line1a.find_intersection(plane1b))

    



if __name__ == "__main__":
   main()

