user_0 ={
    'username' : 'dharti770',
    'first' : 'Dharti',
    'last' : 'Patel'
}
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)


my_dict = {
    "name" : "Troy Aikman",
    "Position" : "QB",
    "team" : "Dallas Cowboys",
    "age" : 54,
    "weight" : 220.,
    "superbowls" : ["XXVII" , "XXVIII" , "XXX"],
    "awards" : {
        "super_bowl_mvp" : "XXVII",
        "probowl" : [1991, 1992, 1993, 1994, 1995, 1996],
        "man_of_the_match" : 1997
    }
}

a_list = []

for k, v in my_dict["awards"].items():
    if k == "super_bowl_mvp" or k == "man_of_the_match" : 
        a_list.append(v)
print(a_list)
