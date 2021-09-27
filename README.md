# Avanta-scrapy

Scraping all recipes from https://www.avantgardevegan.com/ 
</br>
</br>
Examples for extracted formats

```
{
		"url": "https://www.avantgardevegan.com/recipes/seared-watermelon-tuna-steak-salad/",
		"title": "Seared Watermelon 'Tuna' Steak Salad",
		"image": "https://www.avantgardevegan.com/wp-content/uploads/2021/07/tuna1-1638x2048.jpg",
		"video": "https://www.youtube.com/watch?v=TdyeTK-hJhA",
		"category": "Mains, Salads & Veg",
		"stats": [
			"Serves: 4-6",
			"Cooks in: 60 minutes + marinading",
			"Difficulty: 5/10",
			"Can be gluten free"
		],
		"ingredients": {
			"Watermelon": [
				"1 Medium sized Watermelon, peeled then cut into appox 6cm x 4cm x 2.5cm steaks",
				"1 tbs Sea Salt"
			],
			"Marinade": [
				"2 tsp Tahini",
				"6 tbs Soy Sauce or Tamari (to keep gluten free)",
				"2 tbs Rice Vinegar",
				"Juice 1/2 Lime",
				"1 tsp Dried Chilli Flakes",
				"1 cloves Garlic",
				"1 tbs Sriracha",
				"Thumb Sized Piece Ginger",
				"2 Spring Onions",
				"3 tbs Sesame Oil"
			],
			"Noodle Salad Ingredients": [
				"1/2 a Cucumber, cut into batons",
				"5 Spring Onions, cut fine",
				"Handful Sugar-snap Peas, sliced fine lengthways",
				"300g/10.58oz Rice Noodles, cooked",
				"Hand full Thai Basil Leaves",
				"2 tbs Sesame Seeds"
			]
		}
```
</br>
</br>
Type this command to extract all recipes

```
scrapy crawl avanta -o jsonfilename.json
```
