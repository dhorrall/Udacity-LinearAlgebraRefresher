from decimal import Decimal, getcontext
from copy import deepcopy

from vector import Vector
from plane import Plane

getcontext().prec = 30


class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def swap_rows(self, row1, row2):
        r1=self[row1]
        r2=self[row2]
        self[row1] =r2
        self[row2] =r1
        return self


    def multiply_coefficient_and_row(self, coefficient, row):
        x = self[row]
        newVector = x.normal_vector.scalar_multiply(coefficient)
        newPlane = Plane(normal_vector=newVector, constant_term=x.constant_term*coefficient)
        self[row]=newPlane
        #print(type(x),(x.normal_vector.coordinates),(x.constant_term),coefficient,newVector.coordinates,type(newPlane))
        print (self)        
        return (self)
        


    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        rowToAddVectorMultiple = self[row_to_add].normal_vector.scalar_multiply(coefficient)
        rowToAddToVector = self[row_to_be_added_to].normal_vector
        rowToAddToVectorFinal = rowToAddToVector.add(rowToAddVectorMultiple)
        k1= self[row_to_add].constant_term * coefficient
        k2 = self[row_to_be_added_to].constant_term
        kFinal = k1+k2        
        newPlane = Plane(normal_vector=rowToAddToVectorFinal, constant_term=kFinal)
        self[row_to_be_added_to]=newPlane
        print((self))
        return (self)


    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i,p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices
    
    def compute_triangular_form(self):
        system = deepcopy(self)
        #get number of equations in the system
        numEquations=len(self)
        #get number of variables in each plane
        numVariables= system.dimension
        #set counter for variable coefficents in each equation
        j=0
        #c= coefficnet of the var j in the row it
        #proceed downward from each equation in system one at a time
        #in most cases we will want to 'clear' var j below row i and then increment j to move on to next variable
        #however if c = zero, we need to swap with an appropriate row
        #if theres a row under row i with a nonzero coeff for var j, then swap that row with row i
        #clear all terms with var j below row i
        for i in range(numEquations):
            while j <numVariables:
                c= MyDecimal(system[i].normal_vector[j])
                if c.is_near_zero():
                    swap_succeeded = system.swap_with_row_below_for_nonzero_coefficient_if_able(i,j)
                    if not swap_succeeded:
                        j+=1
                        continue
                system.clear_coefficients_below(i,j)
                j+=1
                break
        
        return system

    def swap_with_row_below_for_nonzero_coefficient_if_able(self,row,col):
        num_equations = len(self)
        for k in range(row+1,num_equations):
            coefficient = MyDecimal(self[k].normal_vector[col])
            #print('if_able',coefficient)
            if not coefficient.is_near_zero():
                self.swap_rows(row,k)
                #print ('test linsys =',(row),(k))
                return True
        
        return False

    def clear_coefficients_below(self,row,col):
        #Get number of equations in system
        num_equations = len(self)
        #get the coefficient at the row location and column location
        beta = MyDecimal(self[row].normal_vector[col])
        #Loop through each row in the system starting with the row following the current row        
        for k in range(row+1,num_equations):
            #get the coefficients of the next row
            n=self[k].normal_vector
            #get a particular column for the next row
            gamma = n[col]
            #calculate alpha which is the inverse needed to multiply by the coefficient to clear it    
            alpha = -gamma/beta
            #print('clear',beta,gamma,alpha)
            self.add_multiple_times_row_to_row(alpha,row,k)

    def __len__(self):
        return len(self.planes)


    def __getitem__(self, i):
        return self.planes[i]


    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def __repr__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps

'''
p0 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
p1 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
p2 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
p3 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')

s = LinearSystem([p0,p1,p2,p3])

print s.indices_of_first_nonzero_terms_in_each_row()
print '{},{},{},{}'.format(s[0],s[1],s[2],s[3])
print len(s)
print s

s[0] = p1
print s

print MyDecimal('1e-9').is_near_zero()
print MyDecimal('1e-11').is_near_zero()
'''
