![Ireland Recommends Logo]()

# Milestone 3 Project - Ireland Recommends

The purpose of this project is to develop an interactive website where users can create, read, update and delete reviews on places to eat, drink, stay and visit in Ireland. This website will allow users to both get and give recommendations and is designed to be responsive and accessible on desktop and mobile devices.

Elements of this website were developed from the Code Institute coursework as well recommendations from my mentor and independent online research and observations.

You can view the live website here: [Ireland Recommends](https://ireland-recommends.herokuapp.com/)

![Ireland Recommends mockups on various devices](/docs/screenshots/IrelandRecommends_mockup.jpg)

## Contents

- <a href="#ux">1. User Experience </a>
- <a href="#data">2. Data Architecture </a>
- <a href="#tech">3. Technologies Used </a>
- <a href="#test">4. Testing </a>
- <a href="#deploy">5. Deployment </a>
- <a href="#credit">6. Credits </a>

<span id="ux"></span>

## 1. User Experience

Ireland Recommends is a consumer to consumer website that allows users to filter and read other users reviews as well as create, edit and delete their own reviews of tourism focused establishments in Ireland.

### 1.1 User Stories
- As a read only or first time user, I am able to easily navigate the Ireland Recommends website. I can view reviews posted by other users and filter or search for reviews from the homepage. I can also "like" reviews left by other users. Should I wish to leave a review I can easily register as a user of the site and login without diffciulty. From my profile page, I can add a review and see it posted.

- As a regular user, I can log in to the Ireland Recommends site easily and view my posted reviews. I can edit or delete reviews that I have posted in the past as well as add new reviews.

- As an administrator of the site, I can log in to the site as an admin user and view all reviews that have been posted by users. I can also edit or delete any review posted by users.

### 1.2 Strategy
The goal of this project is to create an interactive website where users can view reviews, upvote their popularity, add their own reviews and then edit or delete those reviews at any time. An administrator can edit or delete any reviews posted by users on the site. Ireland Recomments uses the Flask framework and is connected to a MongoDB database for the creation, reading, updating and deleting of information present on the site.

### 1.3 Scope 

* Base HTML
    - The base template contains a Navbar that utilises an IF Statment which changes the links displayed depending on whether a user is logged in or out or if they are an administrator. The navbar is fixed to the top of the page when a user scrolls on each page. Using Materialize, the navbar is responsive on small screens and converts to an interactive burger icon. This icon triggers a menu that slides from the right hand side of the screen. It is easy to use and visually appealing.
    - Flash messages are displayed using Flask's flash feauture. This feature displays messages to the user when they interract with the site.
    - A footer is also contained in the base template. Social media icons are located in the footer. For the purpose of this project these icons are linked to the each social media sites homepage which opens in a seperate tab.

* Reviews Page
    - The reviews page is the main landing page of the Ireland Recommends site. It contains the base template content as well as a hero image and the following elements. 
    - Filter icons are located below the hero image on the reviews page, these filters allow users to see reviews from the four categories associated with the filters.
    - In order to improve a the sites usability and user experience, a search bar located below the filters allows users to search for keywords within the reviews and display the related reviews on the page.
    - Each review is displayed on a card that is generated using a Jinja for loop. The card is tyled using Materialize and contains an image relating to the review, a short description of the review, the review date and a "Like" upvote button. Using a Python sort function, cards are displayed with the newest review first.

* Individual Review Page    
    - Each review card is linked to an indiviudal review page. This page contains a simple layout featuring a large image associated with the review, the review name, its long description and the details of the user that added or edited the review. When a user is logged in to the site, they have the ability to edit or their delete the review if they are the user who originally posted it. In addition, there is a 'return to home' button which acts as an additional navigation option for ease of use. 

* Login / Register Page
    - A simple card design for both logging in and registering with the site. Both pages contain a form to add in the desired username and password. The username and password must be 
    alphanumerical and be of a length between 5 and 15 characters.

* Profile Page
   - Instead of a flash message, users are welcomed by a message which includes their username over the background of an image 
    of Ireland.
    - Reviews that the user has already added will appear on this page in the form of cards. These cards will also include the option for users to edit and delete their own reviews. 
    - As part of defensive programming, the delete button is followed by a modal which asks the user if they are sure that they 
    want to delete the review.

* Add/Edit Review Page
    - Both of these pages have a similar design and allow users to add or edit informaion about theire reviews. Each entry into the form uses the 
    required attribute except for the images URL field. Some have min and max values to ensure that the layout remains consistent. As well as text 
    entries, there is a date selection function to choose the date that the reviewip has been added. Extra JQuery has been added to ensure 
    that the category name is not left blank. This was taken from Code Institute coursework. Should a review be added without an image attached, a default image will be displayed.

* Manage All Page
    - For the Admin user only, there is a Manage All button in the Navbar where the user is able to read, update and delete all reviews 
    added by any user.

### 1.4 Structure
* The Ireland Recommends site is split into seperate pages for each function. For all users, different pages exist for the home, reviews, login and register page. For a logged in user, the Profile and Edit Tip page exists, and for the Manage all page exists for the administrator. Each page has the same footer and the responsive Navbar to ensure a consistent user experience across the site.

### 1.5 Skeleton
A mobile first approach was taken to designing the website. The original wireframes were created using Balsamiq and can be found below:

- Mobile Wireframe PDF - <a href="https://drive.google.com/file/d/1mZFBJaE9AHte7Ps6IZO7y6owGuUefVHX/view?usp=sharing" rel="noopener" target="_blank">mobile version in PNG</a>.
- Desktop Wireframe PDF - <a href="https://drive.google.com/file/d/1pcw1GKw0YcSmr4G45tPgPNvmSDhIfQSt/view?usp=sharing" rel="noopener" target="_blank">desktop version in PNG</a>.

The wireframe mockups gave me a basic idea of how best to lay out each individual element that I wanted to incorporate into the project and how that would impact and enhance the user experience. As the project progressed, how best to place each of these elements became apparent.

### 1.6 Surface
* Colour scheme
- In keeping with the Irish theme of the site, I decidedto use a green and white colour scheme throughout the site. The type of colour is from the Materialize Light Green Colour Palette which has been lightened to improve visual appearance. Warning flash messages appear in red on the site and welcome and departure messages appear in black. The hover css attribute changes the colour of the category and social media icons when the user hovers over them.

* Logo
- The logo used for the Ireland Recommends website is a Triskell Celtic Symbol, a free to use image from PlumePloume and Pixabay, available **[here](https://pixabay.com/vectors/triskell-symbol-celtic-logo-1194004/)**

* Font
- I selected the Josefin font from Google Fonts for this project as it is reminiscent of classic minimalist travel posters and fits in with the styling of the website. This font is backed up by the sans-serif font.

* Images
- The hero images and background images were all taken from [Pexels](https://www.pexels.com/). The images for the individual reviews 
    are added via a URL link by the user. 
***

<span id="data"></span>

## 2. Data Architecture 

### 2.1 Header

***
<span id="tech"></span>

## 3. Technologies Used

### 3.1 Languages 

I used the following languages for the project:
- **[HTML/HTML5](https://en.wikipedia.org/wiki/HTML5)**
  - The project used **HTML/HTML5** as this is the essential language of websites.

- **[CSS/CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)** 
  - The project used **CSS/CSS3** to provide the styles for the website.

- **[Javascript](https://en.wikipedia.org/wiki/JavaScript)** 
  - The project used **Javacsript** to provide the functionality and customisation for the contact forn, card toggle, Google Maps API and the Openweathermap forecast.

### 3.2 Frameworks, Libraries and Programs
- **[MongoDB](https://www.mongodb.com/1)**
    - MongoDB was used to host the data used on the site and was chosen due to the non-relational nature of the data.
- **[Flask](https://flask.palletsprojects.com/en/1.1.x/)**
    - The Flask framework was used to import the Flask, flash, render_template, redirect, request, session, and url_for 
    functions that are used throughout the site.
- **[BSon](http://bsonspec.org/)**
    - This was imported in order to access the data used across the site.
- **[Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)**
    - This was imported to include the password control and to enhance security on the site.
- **[Jinja Templating](https://jinja.palletsprojects.com/en/2.11.x/templates/)**
    - This was used predominantly for the with, for loops and if statements in order to display all of the relevant data.
- **[JQuery](https://jquery.com/)**
    - I have used JQuery predominantly to initialise the components used in the Materialize framework. In addition, I used 
    code taken from the Data Centric Development Module with the Code Institute in order to ensure that the category names are 
    a required attribute.
- **[Materialize 1.0.0](https://materializecss.com/)**
    - Materialize was used to assist with the responsiveness and styling of the website, such as the navbars for desktop and 
    mobile, buttons, forms, cards and colours.
- **[Google Fonts](https://fonts.google.com/)**
    - Google fonts were used to import the 'Sarala' font which is used on all pages throughout the project.
- **[Font Awesome](https://fontawesome.com/)**
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes. 
- **[Balsamic](https://balsamiq.com/)**
    - Balsamiq was used to create the wireframes during the design process.


### 3.3 IDE

- **[GitPod](https://www.gitpod.io/)**
    - Gitpod was used to develop the website and style each element before deployment.

### 3.4 External Hosting

- **[GitHub](https://github.com/)**
    - This project uses the GitHub hosting service and is saved in a GitHub repository.

- **[Heroku](https://dashboard.heroku.com/apps)**
    - Heroku is used for the hosting of the site and is deployed through here.

- **[Google Drive](ttps://drive.google.com/)**
    - The Testing Document and Wireframe PNG files are saved to a Google Drive account and are openly accessible.
***
<span id="test"></span>

## 4. Testing

[Please follow this link to view the full testing document](https://drive.google.com/file/d/1WEF8KH6VIpwU_CcmEMLlib4j6u0sbjgr/view?usp=sharing)

- **[Balsamiq](https://balsamiq.com/)**
    - I used Balsamiq to design the original wireframes for the project and test how the layout looked. I reverted to Balsamiq when considering changes in the project's design.

- **[GTMetrix](https://gtmetrix.com/)**
    - GTMetrix was used to test the loading speed of the site and to find out if any elements were creating long loading times.

- **[W3C HTML Validator](https://validator.w3.org/)**
    - The W3C HTML Validator checked the website for HTML validity errors.

- **[W3C CSS Validator](https://jigsaw.w3.org/css-validator/)**
    - The CSS Validator checked for validity errors in the website's CSS page.

- **[Autoprefixer CSS Online](https://autoprefixer.github.io/)**
    - The Autoprefixer ensured that vendor prefixes were added to my CSS.

- **[Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)**
    - Google Chrome's DevTools were used to inspect elements of the website and adjust them to ensure that they were effective and responsive at different screen sizes. DevTools was also used to identify errors in my code and to test how changing certain elements would effect the overall look and feel of the website.

### 4.2 Testing User Stories

1. As a visitor to East Cork seeking information on the area:
     - I am given an introduction to the website and how to use it.
     - I can access information on local areas by clicking the "Show More" button on the Area cards.
     - The "Show More" button also directs me to the relevant area on the map where I can see local amenities.
     - I can search for other establishments locally using the search bar.
     - Should I require assistance or further information, I can contact the site owner via the funcitoning contact form.


2. As a resident of East Cork:
    - I can find out information about my locality including amenities near me.
    - I can search for local businesses on the map and then contact those businesses.
    - I can contact the website owner through the functioning contact form should I require further information the local area.
    - I can check the upcoming weather forecast for the local area.


3. As a local business owner:
    - I can see that the website owner can showcase local businesses through custom map markers.
    - I can find out which local businesses are promoting their offering on the website.
    - I can contact the website owner via the functioning contact form to enquire about showcasing my business.


### 4.3 Device Testing

I utilised Google Chrome's DevTools to test the responsivness of the website at different screen sizes throughout the project. Once the project was approximately 70% complete, I tested it using a Huawei P9 Lite and an Apple iPhone 11 mobile device and an Acer tablet device. The website worked well on all devices.
I tested the desktop functionality of the Visit East Cork website on Google Chrome and Microsoft Edge.

#### On screen sizes of tablet size and below: 
- Cards and divs are responsive and will align with the mobile view. 

### Further Testing

[Please follow this link to view the full testing document](https://drive.google.com/file/d/1WEF8KH6VIpwU_CcmEMLlib4j6u0sbjgr/view?usp=sharing)

**W3C HTML Validator**
* Ran index.html through validator to check there were no syntax errors: 
    * Failed – 2 images are missing SRC attributes however these attributes are filled by the Google Place API at line 165 and by the Open Weather Map API at line 225.
    * Failed – W3C Validator does not recognise a phone number as an anchor tag however this is recognised by browsers.

**W3C CSS Validator**
W3C CSS Validator
* Ran style.css through validator to check there were no syntax errors: 
    * Passed with no errors

### 4.4 Bugs

I encountered the following bugs while developing the Visit East Cork website:

### Google Maps API
- In order to safeguard your API Key, Google advised that you register your websites that will be using your key on the Google API credentials page. I registered my GitPod demo site and the Maps API worked fine but when I restarted GitPod and opened a new demo page, the Maps API stopped working. I later realised that I needed to re-regsiter my site with  Google MAps API credential and it worked fine after this.

### Google Autocomplete Places
- Although the Autcomplete has set boundaries within the area of East Cork, occasionally search results appear from outside the area. This requires further investigation.

<span id="deploy"></span>
## 5. Deployment

The Visit East Cork website is hosted on GitHub Pages and was developed using the GitPod IDE using the following steps:

1. An initial repository was created in my GitHub account for the Visit East Cork Project.
2. Using the GitPod Chrome extension, the project was launched from the GitHub repository.
3. All development on the project was carried out on the GitPod IDE.
4. Changes to the project were committed and pushed regularly from GitPod to the Github repository.
5. The Master Branch was the sole branch used to edit the project and the GitHub pages website was created from this branch. A link to the site is available **[here](https://d-mcalpin.github.io/visit-east-cork/)**.
6. To create a local copy of this repository, click "clone or download" on the Visit East Cork respository page and copy the provided URL. Open the Command Line Interface in your editor and type **git clone** and paste the URL copied earlier. Pressing enter creates a local clone of the Visit East Cork repository.
***
<span id="credit"></span>
## 6. Credits

### 6.1 Content
The design and style of my project was initially inspired by elements of the following Milestone 2 projects:
- [michellelclement's Mykonos Recommended ](https://github.com/michellelclement/mykonos-recommended-MS2)
- [samc85's Milestone2-project](https://github.com/samc85/Milestone2-project)

The following sources were used for code snippets or inspiration throughout the project:
- **Main Image**
    - The hero image and jumbotron were inspired by the Love Running project of the Code Institute Full Stack Web Developer Course.

    - **Carousel**
    - The homepage carousel for the main hero image section was designed using [Bootstrap 4's documentation](https://getbootstrap.com/docs/4.0/components/carousel/).
    
- **Area Infrmation Cards**
    - The cards were developed from Bootstrap 4's card documentation.
    - Box shadow effects were inspired by the following from [W3Schools](https://www.w3schools.com/cssref/css3_pr_box-shadow.asp).
    - The toggle feature on the Area Informaion cards was inspired by the followng from [JQuery](https://api.jquery.com/toggle/).
    - Box shadow effects were inspired by the following from [W3Schools](https://www.w3schools.com/cssref/css3_pr_box-shadow.asp).

- **Google Maps API**
    - The Google Maps API documentation, available [here](https://developers.google.com/maps/documentation/javascript/overview) was used to develop the map feature of the Visit East Cork website. Additionally the following resources were used to style and add functionality to the map:
        - Embedding the search bar within the map was inspired by the followinf from [Stack Overflow](https://stackoverflow.com/questions/58870022/google-maps-how-do-you-embed-it-with-search-bar) along with the following from [Google Developers](https://developers.google.com/maps/documentation/javascript/places-autocomplete).
        - Custom markers were deveoped using he followig video tutorials on Youtube:[Google Maps Tutorial](https://www.youtube.com/watch?v=Zxf1mnP5zcw) and [Google Maps Places Tutorial](https://www.youtube.com/watch?v=oVr6unKZbg4). The map icons were generated using the custom marker maker on [Mapsmaker.com](https://mapicons.mapsmarker.com/)
        - Info Windows were designed from the video tutorials linked above as well as Google's documentation on [InfoWindows](https://developers.google.com/maps/documentation/javascript/infowindows) and the following from [Stackoverflow](https://stackoverflow.com/questions/43544741/google-map-close-info-window-when-another-marker-is-clicked)
        - The map reset button took information from the following thread on [Stackoverflow](https://stackoverflow.com/questions/42151253/reinitialize-restart-google-map-api).
        - The search boundaries on the map search were installed with assistance from the following thread on [Stackoverflow](https://stackoverflow.com/questions/46136800/how-to-set-bounds-for-google-places-autocomplete-using-drop-down) as well as the [Google Maps Documentation](https://developers.google.com/maps/documentation/javascript/examples/control-bounds-restriction).

- **EmailJS API and Contact Form**
    - The EmailJS documention, available [here]() provided all information for activating the API. Styling for the contact form was developed using content from the Code Institute Full Stack Web Developer course.

- **Open Weather Map API**
    - Information on how to set up and install the Open Weather Map API wsa taken from the [official documentaion](https://openweathermap.org/guide) and the following from [Stackoverflow](https://stackoverflow.com/questions/36174177/show-local-weather-using-openweathermap-api)

    - The hyperlink code for phone numbers was discovered at [Stackoverflow Overlays](https://stackoverflow.com/questions/53270766/how-do-i-hyperlink-a-phone-number).

### 6.2 Media

- **Images**
    - The Visit East Cork Icon and Logo was sourced from PlumePloume on Pixabay, available [here](https://pixabay.com/vectors/triskell-symbol-celtic-logo-1194004/).
    - All images for local attractions were sourced from each individual establishment's public Facebook page with the exception of The Ballycotton Cliff Walk which was sourced from Tripadvisor and Garryvoe Beach which was sourced from Twitter.

- **Text**
    - All the text for the website was written by myself.

- **Mockups**
    - [Techsini](Techsini.com) was used to generate the desktop and mobile mockups.

### 6.3 Acknowledgements

- **Oluwafemi Medale** (My Mentor) - Thank you for your assistance with this project.
- **The Code Institute Slack Community** - The community was a great source of inspiration and assistance throughout the project.
- **Lucy, Neil and Ulysses from Student Support** for their assistance throughout this project.

***

