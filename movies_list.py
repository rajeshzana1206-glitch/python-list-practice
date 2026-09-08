movies = ["kgf", "leo", "vikram"]
print("my favorite movies")
print(movies)

# Add movies
movies.append("jailer")

#Remove movies
movies.remove("leo")

#count movies
print("favorite movie:" , len(movies))

#sort an movies
movies.sort()

#display movie one by one
print("\nfinal movies list:")

for movie in movies:
    print("-", movies)
    
