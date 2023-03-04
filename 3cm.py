class Dog():

    def __init__(self, breed): #called upon when instance is created
        self.breed=breed


#Running---------------

#my_dog = Dog() #expecting to pass parameter
#breed or it will cause an error

my_dog = Dog(breed='lab')

print(my_dog.breed) #calling this attribute
#== 'lab'

