my_list=[1,2,3,4,5,6,7,8,9,0]
mini=maxi=my_list[0]
for element in my_list:
    if element>=maxi:
        maxi=element
    elif element<mini:
        mini=element

print("The maximum element is",maxi)
print("The minimum element is",mini)

