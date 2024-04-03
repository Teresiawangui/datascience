# Add
fruits =("apple","mango","kiwi")
newfruits = fruits + ("dates",)
print(newfruits)

# remove
vegetables =("kales","tomato","carrots") 
nwevegetables = list(vegetables)
nwevegetables.remove("carrots")
vegetables = tuple(nwevegetables)
print(vegetables)