from vector import Vector
from line import Line
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
    v1a = Vector([4.046,2.836])
    v1b = Vector([10.115,7.09])
    line1a = Line(v1a,1.21)
    line1b = Line(v1b,3.025)
    print ('Pair 1 Is Parallel '+str(line1a.is_parallel(line1b)))
    print ('Pair 1 Is Same Line ' + str(line1a==line1b))
    print(line1a.find_intersection(line1b))

    v2a = Vector([7.204,3.182])
    v2b = Vector([8.172,4.114])
    line2a = Line(v2a,8.68)
    line2b = Line(v2b,9.883)
    print ('Pair 2 Is Parallel '+str(line2a.is_parallel(line2b)))
    print ('Pair 2 Is Same Line ' + str(line2a==line2b))
    print(line2a.find_intersection(line2b))

    v3a = Vector([1.182,5.562])
    v3b = Vector([1.773,8.343])
    line3a = Line(v3a,6.744)
    line3b = Line(v3b,9.525)
    print ('Pair 3 Is Parallel '+str(line3a.is_parallel(line3b)))
    print ('Pair 3 Is Same Line ' + str(line3a==line3b))
    print(line3a.find_intersection(line3b))



if __name__ == "__main__":
   main()

