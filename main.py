#ask for todays temreature
tempreature=(int(input("enter todays tempreature: ")))

#decide weather jacket or Tshirt
if tempreature<20:
    outfit="jacket"
    print("it is cold today")
    print("wear a ",outfit)

else:
    outfit="Tshirt"
    print("it is a warm day")
    print("wear a",outfit)

#ask weather it is raining
raining=input("is it raining today yes or no: ")
if raining == "yes" :
    print("bring an umbrella")

#ask for wind speed
wind_speed=(int(input(enter todays wind_speed in km/h)))

#decide wind breaker needed or not
if wind_speed>30:
    wind_breaker="yes"
    print("it is windy today")
    print("wear your wind_breaker over your ",outfit)

else:
    wind_breaker="no"
    print("it is a calm day")
    print("no need to wear your wind_breaker over your ",outfit)

#ask for puddels on the ground
puddels=(input("ask  are there puddels on the ground write yes or no :"))

#decide between boots and sneakers
if puddels=="yes" :
    shoes="boots"
    print("ground is wet")
    print("wear",shoes)

else:
    shoes="sneakers"
    print("the ground id dry")
    print("wear",shoes)

#this message always prints whatever was chosen about
print()
print("wheather check complete")

#final outfit summary
print("-------------wheater out fit picker---------")
print("tempreature:   ",tempreature )
print("outfit chossen:  ",outfit)
print("raining:   ",raining)
print("wind_breaker needed:   ",wind_breaker)
print("shoes chossen:    ",shoes)
print("----------------------------")

