anime_type = ["isekai","isekai","sci fi", "manhwa"]
anime_title =[ ]

while True:
    ans = input("Do you know any anime?(YES/NO)")
    if ans.lower() == 'yes':
        for x in anime_type:
            print(x)
        a_type = input("type -->")
    
        title = input("What is the title of the anime -->")
        anime_title.append(title)
        continue
    else:
        print("THANK YOU")
        break
    
    