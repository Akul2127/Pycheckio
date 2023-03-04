class Sample():
    pass # dont do anything

my_sample = Sample() ## Instance of Sample()

class Dog():

#Attributes are characteristics etc..
    def __init__(self,breed): #<< expects to pass in breed
        
        #Attributes
        #Take in the arguement
        #Assign it using self.attribute_name
        self.breed = breed #instance

d = Dog(breed='Lab')
# d is an instance of Dog() class
print(d.breed)

class dog():

    def __init__(self,name):
        self.name = name

        def speak(self):
            return self.name + "says WOOF"

class cat():

    def __init__(self,name):
        self.name = name
        
        def speak(self):
            return self.name + "says MEOW"

niko = dog("niko")
felix = cat("felix")

print(niko.speak())
print(felix.speak())