from decimal import Decimal, getcontext

from vector import Vector

getcontext().prec = 30


class Line(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

        if not normal_vector:
            all_zeros = ['0']*self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector
        #print(self.normal_vector)

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()


    def set_basepoint(self):
        try:
            n = self.normal_vector
            c = self.constant_term
            basepoint_coords = ['0']*self.dimension

            initial_index = Line.first_nonzero_index(n)
            initial_coefficient = n[initial_index]
            #print(type(c),type(initial_coefficient))
            basepoint_coords[initial_index] = c/Decimal(initial_coefficient)
            self.basepoint = Vector(basepoint_coords)
            #print(n)
            #print(c)
            #print(self.dimension)
            #print (type(basepoint_coords))

        except Exception as e:
            if str(e) == Line.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e

    def find_intersection(self,aLine):
        
        if not self.is_parallel(aLine):
            #print(self.normal_vector.coordinates)
            A=Decimal(self.normal_vector.coordinates[0])
            B=Decimal(self.normal_vector.coordinates[1])
            C=Decimal(aLine.normal_vector.coordinates[0])
            D=Decimal(aLine.normal_vector.coordinates[1])
            K1=self.constant_term
            K2=aLine.constant_term
            X= (D*K1-B*K2)/(A*D-B*C)
            Y= -(C*K1-A*K2)/(A*D-B*C)
            result = 'X= '+str(round(X,3))    ,'Y= ' + str(round(Y,3))
            return result
        elif self == aLine:
            result = 'Lines are the same line!'
            return result
        else:
            result = 'Lines are parallel, but not the same!, no intersection!'
            return result
    
    def is_parallel(self,aLine):
        r1 = self.normal_vector
        r2 = aLine.normal_vector
        result = r1.is_parallel(r2)
        #print (result)
        return result
    
    def __eq__(self,aLine):
        if not self.is_parallel(aLine):
            return False
        #compute vector connecting the lines base points
        x0 = self.basepoint
        y0 = aLine.basepoint
        #print (type(x0),type(y0))
        basepoint_diff = x0.subtract(y0)
        n = self.normal_vector
        #print(n)
        #if connecting vector is orthogonal then lines are equal
        return basepoint_diff.is_orthogonal(n)

    def __repr__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector
        #print(n)

        try:
            initial_index = Line.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output


    @staticmethod
    def first_nonzero_index(iterable):
        #print(iterable)
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                #print(k)
                return k
        raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        #print(self)
        #print(abs(self) < eps)   
        return abs(self) < eps
