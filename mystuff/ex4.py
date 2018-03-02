#定义汽车的数量
cars = 100
#定义一个汽车的容量
space_in_a_car = 4.0
#定义司机的数量
drivers = 30
#定义乘客的数量
passengers = 90
#计算空车的数量
cars_not_driven = cars - drivers
#计算能开动的汽车的数量
cars_driven = drivers
#计算总的载客量
carpool_capacity = cars_driven * space_in_a_car
#计算每辆车平均的乘客数
average_passengers_per_car = passengers / cars_driven


#分别输出汽车的数量、司机的数量、空车的数量、总载客量、乘客数和每辆车上的平均乘客数
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
