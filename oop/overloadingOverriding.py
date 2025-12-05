class Demo:
    def add(self, *args):
        total = 0
        for i in args:
            total = total + i
        return total
    
d =Demo()
print(d.add(2,3,4,5,6,7,8,9))
print(d.add(2,3,4,5))
print(d.add(4,5))

#all add functions returning same functionality but with diff parameters, method overloading

class Father:
    # def add(self, *args):
    #     total = 0
    #     for i in args:
    #         total = total + i
    #     return total
    def sleep(self):
        print("Father sleeps from 11pm-7am")

class Son(Father):
    def sleep(self):
        print("Son sleeps from 2am-10am")
        super().sleep()


s = Son()
s.sleep()

#overriding same parameters and same function name using MRO calls latest function in inheritance. 
#using super function call parent's coonstructor and it's same named function as well. 


