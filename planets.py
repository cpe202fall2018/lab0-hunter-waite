def weight_on_planets():
    weight =  float(input("What do you weigh on earth? "))
    print("\nOn Mars you would weigh",mars_weight(weight),"pounds.")
    print("On Jupiter you would weigh",jupiter_weight(weight),"pounds.")

def mars_weight(weight):
    return weight * .38
def jupiter_weight(weight):
    return weight * 2.34
   
   
if __name__ == '__main__':
   weight_on_planets()
