# Hungry Herbivore

Hungry Herbivore is a website designed for individuals who are looking to expand their their vegan cooking knowledge and in my opinion the best way to do this is to see what other people are doing. Vegan food is really starting to take off becoming bigger and bigger each year but it can still be hard being a new vegan trying to find recipes that are tasty and provide a variety of ingredients (known from experience).

This is where Hungry Herbivore comes in and saves the day with its recipes being shared and its easy readability it can allow you to get that inspiration you need to cook an exciting meal. Including a search feature based on difficulty also allows you to pick how adventurous you're feeling that day and get cooking!

## UX

The users were my main focus for this site,I wanted Hungry Herbivore to be very visually appealing  so I picked nice simple colors that go well together, I decided white and a soft purple and I think they fit perfectly. The homepage has accordions, though the recipe is viewed on a separate page to reduce the contend being cramped and look cleaner. Another feature is that it is easy to use, will notice you can get to any desired page within minimal clicks (with the only exception of mobile) but still this saves the site user time on navigating and gives them more time to use the website for its purpose.

### user stories

- As someone who does not eat plant based everyday, it would be convenient to be able to find simpler meals that allow for my skill range.
- As an experienced vegan, I would like to be able to focus on more difficulty and complex recipes to bring the excitement back to cooking!
- As somebody who is less experienced with technology, I would like a site that it not only displayed simply but also easy to use.

I believe that Hungry Herbivore meets all of these users preferences.

### display testing

The /wireframes file will show two templates of how I planned the site, little has changed but I changed what was needed. For example the key now being at the top of the page takes less space and is easier to see. As with the accordion information I decided to give each recipe its own page to view. The accordion still displays a comment about the recipe which leaves the homepage telling you the recipe name, difficulty, cooking time and comment which I believe is plenty of information.

## Features

- Viewing recipes, do this by choosing a recipe and clicking 'recipe' on desktop or the icon in mobile.
- Adding recipe, do this by clicking the '+' icon in the nav bar, completing form and clicking 'add recipe'.
- Edit a recipe, click edit next to recipe button on chooses recipe on desktop or recipe then edit for mobile and change the forms content. Then click 'update recipe'.
- Delete a recipe, do this by going into the edit page and there you will find a red delete button which removes the content from the database.
- Filter recipes, by clicking the dropdown under the key and selecting a difficulty and hitting 'go' you can filter the page results for the skill level you've chosen.

### Future features

- More filters to get a more refined search and even adding more variables to the forms and database such as cuisine styles or allergy friendly recipes.
- A way to filter the form text, I did not want to be restrictive when adding a recipe so as long as the input fields are not empty they will submit, in future I'd hope to filter this to make sure the information added makes sense.

## Technologies used

- HTML5
    - My templates are forms were all written using html.
- CSS3
    - My site was styled using css.
- JavaScript
    - My site used javascript to implement Materialize code with jQuery.
- Flask
    - This was used to install required libraries for python.
- Python 
    - Python was used to connect my site to MongoDB and connect my HTML code.
- MongoDB 
    - This was used to host all data for my site on a database.
- Materialize
    - Provides documentation templates for html and css.
- Google fonts
    - Used to get specific fonts for text on my site.


## Testing 

My first testing stage was python debug set to true. This proves to me that the code syntax was correct and the code ran. If not the application wouldn't run and I would be able to visually see the errors and as is done by the computer is much more reliable then testing by hand. You need to be able to add recipes for this site to have purpose and with a form that requires mostly text it can be hard to validate, to combat this I used a select form to set a difficulty to the recipe as the difficulty has to be within a specific range of values for the site to work properly and using a select form eliminates the risk of a typo causing an issue.  If you attempt to submit a form with an empty field/s you will be reminded by a subtle popup that the field cannot be empty, this was achieved using the 'required' this is a simple HTML command but perfectly and simply fixes my problem. 

One of my user experiences mentions how more challenging recipes would be the reason they use the site so they wouldn't need to sit and scroll through the easy ones. The search function is the solution but required a lot of testing. It originally had a separate @ route for the search submit but after this was functioning the tests resulted in it being opened in a separate page instead of an extension of the page its already on, testing allowed me to correct this and delete this @ route and instead add it to the original get_recipes route which allowed the search submit button to become an extension of the homepage and not a new page entirely.

After this I knew the search would find a 'novice' level difficulty as there was one but was unsure if I searched for a recipe difficulty that had no content so I followed simple steps.
- Search function:
    1. Search for difficulty that has content (returns expected recipe)
    2. Search for difficulty that has no content (searches but returns a visually unpleasing empty box)
    3. Created if function using jinja to return 'No recipes here' if recipe count == 0
    4. Search again for difficulty that has no content (returns 'No recipes here' instead of empty box which provides information to the user instead of no content) 
     
My site is designed to work and have a high UX on all resolution, this was made much easier with chromes developer tools allowing me to test the display on specific products but also responsively so I can see it change from a small size to and medium then large. Materialize's 'col' class was my main use of displaying sizes of elements under different sizes but would also use custom CSS to hide elements on specific sizes also.



I ran into a small issue with testing and that was the live view of my code. For some reason the AWS cloud 9 live link for my code was not connecting to monogdb. This meant that when I would view my code using AWS half of the content would not load in and would not give an proper view of how my site actually looked. I could simply solve this issue by pushing to heroku for every change of my code however this meant everything took slightly more time and left me with an excessive number of commits. If this problem was to reoccur I would look to solve it at the beginning to increase my functionality and reduce the commits needed for my site.

## Deployment 

AWS cloud 9 was where I chose to write my code. Heroku was my deployment platform of choice as I had experience with it in the course so had an understanding of how it worked. Due to my issue with my live code it also effectively became how I would test my code and would replace the live view entirely also. I used to config vars to connect my mongo database to AWS but I also used it to set up an environment variable for my database password to increase security.

## Credit 

### Content
- The template for the accordion in my recipes.html was acquired from materialize.
- The template for my form in addrecipe.html and modifyrecipe.html was acquired from materialize.
- The template for my nav bar was acquired from materialize.
- The font for my nav bar logo was acquired from Google fonts.

### Acknowledgements
I decided to choose one of the project ideas for my site as ideas began flooding in as soon as I read it and was something I wanted to pursue. The idea of a veganism website came from my own lifestyle and my friends also so imagining the target audience became much easier.
















