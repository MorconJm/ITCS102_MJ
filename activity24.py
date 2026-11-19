fruit = ["longgan","lipule","tysa"]

fruits_d = {"bilog":"longgan","maasim":"lipule","kalbo":"tysa"}
print(fruit[2])
print(fruits_d["maasim"])

for x,y in fruits_d.items():
    print("key is",x,"--value is",y)