from vector import Vector

def main():
   x = Vector([8.218,-9.341])
   y = Vector([-1.129,2.111])
   x.add(y)

   x = Vector([7.119,8.215])
   y = Vector([-8.223,.878])
   x.subtract(y)

   x = Vector([1.671,-1.012,-.318])
   multiplier= 7.41
   x.scalar_multiply(multiplier)
   

if __name__ == "__main__":
   main()

