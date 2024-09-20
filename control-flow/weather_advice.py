answer = input("What's the weather like today? (sunny/rainy/cold):")
recommend = ""
if answer == "sunny":
  recommend = " wear a t-shirt and sunglasses."
elif answer == "rainy":
  recommend = "Don't forget your umbrella and a raincoat."
elif answer == "cold":
  recommend = "Make sure to wear a warm coat and a scarf."
else:
  recommend = "Sorry, I don't have recommendations for this weather."

print(recommend)
