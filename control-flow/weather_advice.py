weather = input("What's the weather like today? (sunny/rainy/cold):")
if weather == "sunny":
  recommandation = "Wear a t-shirt and sunglasses."
elif weather == "rainy":
  recommandation = "Don't forget your umbrella and a raincoat."
elif weather == "cold":
  recommandation = "Make sure to wear a warm coat and a scarf."
else:
  recommandation = "Sorry, I don't have recommendations for this weather."

print(recommandation)

