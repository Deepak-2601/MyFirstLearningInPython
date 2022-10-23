class math_class:

    def fun_fab(self, limit: int):
        v = 0
        v1 = 1
        for i in range(1, limit):
            f1 = v + v1
            v = v1
            v1 = f1
            print (f1)

    def function_prime(self, prime: int):
        w = False
        for i in range(2, prime):
            if prime % 2 == 0:
                w = True
        if w == True:
            print("It is not a prime number")
        else:
            print ("It is a prime number")



if __name__=="__main__":
    n1 = math_class()
    a = int(input("Please enter the number: "))
    n1.fun_fab(a)
    print(a)
    b = int(input("Please enter the input: "))
    q= n1.function_prime(b)
    print(b)