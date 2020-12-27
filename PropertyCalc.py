
price = int(input("Give me the price of this place! "))
rent = int(input("and what's the rent per week? "))
bodyC = int(input("and the body corporate per quarter? "))


def conv(x):
    return(price * float(0.07) / 52)
def rconv(x):
    return(rent * 52 / price * 100)
def pconv(y):
    return(((rent * 52) - (bodyC * 4)) / price * 100)


yearly_yield_BC = pconv(bodyC)
yearly_rent = rconv(rent)
yearly_yield = conv(price)
 
print(f"\nThis is your rental yield excluding Body Corporate {yearly_rent}% ")
print(f"This is your rental yield including Body Corporate {yearly_yield_BC}% ")
print(f"The rent needs to be ${yearly_yield} per week to be at 7%.\n")