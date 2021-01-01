
price = int(input("Give me the price of this place! "))
rent = int(input("and what's the rent per week? "))
bodyC = int(input("and the body corporate per quarter? "))
RatesLand = int(input("What do the land rates look like per quarter? "))
RatesWater = int(input("Finally, I'll need the water rates per quarter? "))


def conv(x):
    return(price * float(0.07) / 52)
def rconv(x):
    return(rent * 52 / price * 100)
def pconv(y):
    return(((rent * 52) - (bodyC * 4)) / price * 100)
def lconv(z):
    return(((rent * 52) - (bodyC * 4) - (RatesLand * 4)) / price * 100)
def wconv(y):
    return(((rent * 52) - (bodyC * 4) - (RatesLand * 4) - (RatesWater * 4)) / price * 100)

Yearly_Water = wconv(RatesWater)
Yearly_Land = lconv(RatesLand)
yearly_yield_BC = pconv(bodyC)
yearly_rent = rconv(rent)
yearly_yield = conv(price)
 
print(f"\nThis is your rental yield excluding Body Corporate {yearly_rent}% ")
print(f"This is your rental yield including Body Corporate {yearly_yield_BC}% ")
print(f"Body Corporate and land rates is {Yearly_Land}% yield. ")
print(f"\nSo you're final yield will be at {Yearly_Water}% compared to {yearly_rent}% ")
