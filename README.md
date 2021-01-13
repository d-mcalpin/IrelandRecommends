![Ireland Recommends Logo](/static/images/veclogo.png)

# Milestone 3 Project - Ireland Recommends

The purpose of this project is to develop an interactive website where users can create, read, update and delete reviews on places to eat, drink, stay and visit in Ireland. This website will allow users to both get and give recommendations and is designed to be responsive and accessible on desktop and mobile devices.

The Visit East Cork website is responsive and contains a number of interactive elements including its main functionality based on the Google Maps Javascript API. Elements of this website were developed from the Code Institute coursework as well recommendations from my mentor and independent online research and observations.

You can view the live website here: [Ireland Recommends](https://ireland-recommends.herokuapp.com/)

![Visit East Cork mockups on various devices](assets/images/mockups/vecMockup.jpg)

## Contents

- <a href="#ux">1. User Experience </a>
- <a href="#features">2. Features </a>
- <a href="#tech">3. Technologies Used </a>
- <a href="#test">4. Testing </a>
- <a href="#deploy">5. Deployment </a>
- <a href="#credit">6. Credits </a>

<span id="ux"></span>

## 1. User Experience

Visit East Cork is a business to consumer website that allows users to discover the local area of East Cork and find out about local facilities, businesses and attractions. The Google Maps element contains a number of custom markers with info windows that can be edited. This would allow the website owner the opportunity to generate advertising revenue from recommended locations in the area while also allowing website users the opportunity to interact with the map and find out more information about the area themselves.

### 1.1 User Stories
- As a local business owner in the East Cork area, I can showcase my business on the Visit East Cork homepage via the Google Maps API interface. This can display images, information and links about my business. 

- As a tourist seeking to find more information about East Cork, I can interact with the map aswell as reading the information about local areas displayed on the homepage. Should I wish to find out more information I can contact the website owner directly from the contact form. I can also view the current weather forecast in Cork.

- As a local resident of East Cork, I can interact with the Visit East Cork website to find out more information about my local area, particularly relating to attractions or facilities that I may not know about. I can also view the local weather forecast and contact the site owner if I have any queries.

### 1.2 Strategy
The goal of the project is to create an informative website that has the potential to generate revenue for the website owner through sponsored recommendations visible on the Google Maps API. The website intends to keep users interested through continuously updated local information with the potential to offer special deals on local businesses to website users.

### 1.3 Scope 
All of Visit East Cork's content is contained within a single webpage. Users do not have to navigate away from the page to use different elements including contacting the website owner and interacting with the Google Maps API. Elements of the homepage are interactive including the buttons which showcase the local area. These toggle information and interact with the map to show users where these areas are located.

### 1.4 Structure
Based on the Scope Plane, Visit East Cork was developed to provide users with information within moments of arriving at the page. A welcome image entices users to scroll down and the Google Maps API invites them to click on custom markers to discover the local area. A contact form and contact information is within a scroll of the map.

### 1.5 Skeleton
A mobile first approach was taken to designing the website. The original wireframes were created using Balsamiq and can be found below:

- Mobile Wireframe PDF - <a href="https://drive.google.com/file/d/1TqIiR8u5vYMyz_Q2usJRWyE0L0NCeRrr/view?usp=sharing" rel="noopener" target="_blank">mobile version in PNG</a>.
- Desktop Wireframe PDF - <a href="https://drive.google.com/file/d/1rjnoTlbCzB_b-Os8TaWMGbwpYFu89ySf/view?usp=sharing" rel="noopener" target="_blank">desktop version in PNG</a>.

The wireframe mockups gave me a basic idea of how best to lay out each individual element that I wanted to incorporate into the project and how that would impact and enhance the user experience. As the project progressed, how best to place each of these elements became apparent.

### 1.6 Surface
A blue and white colour scheme was initially decided upon to give a clean and crisp image to the site, I decided to add a teal colour, particularly for buttons and hover elemenets. I chose the Josefin font from Google Fonts as I found that it reminded me of the text on classic travel posters.  Shadows and rounded borders appear on a number of elements on the site to add depth and to keep it interesting.

***Logo*** 
The logo used for the Visit East Cork website is a Triskell Celtic Symbol, a free to use image from PlumePloume and Pixabay, available **[here](https://pixabay.com/vectors/triskell-symbol-celtic-logo-1194004/)**

***Font*** 
I selected the Josefin font from Google Fonts for this project as it is reminiscent of classic minimalist travel posters and fits in with the styling of the website. This font is backed up by the sans-serif font.

***Colours:***
The colour scheme for this project is bright and airy so a blue and white theme was selected. The following colours are used in the project:

* Light Blue: rgba(87, 202, 255, 1)
* Hover Teal for contrast: rgba(0, 136, 122, 1)

***

<span id="features"></span>

## 2. Features 

### 2.1 Header
Following the advice of my mentor, it was decided that the header would simply contain the website name and logo centred. As this is a short single page website, a navbar is not neccessary.

### 2.2 Welcome Image
Users are welcomed to the page with a large hero or welcome image and a Jumbrotron containing a welcome message. The image zooms slowly towards to user when the page loads.
There are three welcome images rotating on a Bootstrap Carousel. Text below the main image gives users instructions on how to use the site.

### 2.3 Information Cards with Toggle and Map Zoom Features
The information cards below the site instructions utilise JQuery Toggle to provide users with information on areas of East Cork. When the user clicks on the "Show More" button on each card, more informaiton will appear about that location and the map will centre on that location also.

### 2.4 Google Maps API
The Google Maps section of the website contains a large map with preloaded, customised markers that show a particular point of interst on the map. When w user clicks on the custom icon, an information window will be displayed showcasing an image of the point of interest and its name.

### 2.5 Google Places Autocomplete Search
A custom search bar is embedded in the top left corner of the map. This search bar allows users to search the area of the map for other points of interest that are not highlighted by custom markers. This search will show local businesses including shops, bars, restaurants, hotels and other businesses within the boandaries of the map.

### 2.6 Contact Form
Below the map, a contact form invites users to send a message to the site owner if the require further information. This is a functional and opeerational contact form powered by EmailJS. When users submit their query after filling out the required boxed, a message will display in the browser window telling them if their message was sent successfully or if it failed.

### 2.7 Footer
The footer of the Visit East Cork webpage contains contact informaion and social media links that invite users to keep in contact with the site owner. A weather forecast and current temperature display for the Cork area is also contained within the footer. This is a custom forecast provided by the Openweathermap API.

### 2.8 Features Left to Implement
After reading the Google Maps Javascript API, there is an incredible amount of functionality that can be added to custom maps. In order to monetise the website richer and more detailed information on local businesses could be added to the map, this would provide the website owner with more opportunities to showcase local businesses on the Visit East Cork website.
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

### 3.2 Frameworks 
- **[BootStrap 4](https://getbootstrap.com/)**
  - I used the **Bootstrap 4** Framework to design the website and add useful components and utilities including:
    - [Flexbox](https://getbootstrap.com/docs/4.5/utilities/flex/)
    - [Jumbotron](https://getbootstrap.com/docs/4.5/components/jumbotron/)
    - [Cards](https://getbootstrap.com/docs/4.5/components/card/)
    - [Images](https://getbootstrap.com/docs/4.5/content/images/)

### 3.3 Libraries

- **[JQuery](https://jquery.com)**
    - The project uses **JQuery** to add toggle functionality to the East Cork Area information cards.

- **[Fontawesome](https://fontawesome.com/)**
    - The project uses **Fontawesome** to add attractive icons to each of thearea information cards and the social media links.

- **[Google Fonts](https://fonts.google.com/)**
    - The Quicksand Font from Google Fonts is used throughout the project in different weights and colours.

- **[Google Places Library](https://developers.google.com/maps/documentation/javascript/places)**
    - The Google Places Library allows users to seacrh for places using the search function on the map and can return information on those places including addresses, images, user reviews and opening hours.

### 3.4 APIs

- **[Google Maps Javascript API](https://developers.google.com/maps/documentation/javascript/overview)**
    - The project uses **Google Maps Javascript** to generate the primary website attraction, the local area map. In order to use this API on a website, a developed must create a billing account and generate an API key. This key and account allows the owner to access the maps database. In order to access places through the Autocomplete Search, the developer must also link the Google Place Library to their API key and billing account. This can be challenging as it is advised that developers restrict their keys do that they are not abused by a third party. This can sometimes cause the Gogole Maps API to fail if Google does not recognise the website that is trying to load the map. 

- **[EmailJS API](https://www.emailjs.com/)**
    - The project uses **EmailJS** to add functionality to the website contact form. This API was utilised in a Code Institute Project and it allows the developer to link the contact form to their email address and inturn provides a method of communication for the website users. EmailJS requires developers to set up an account and link it to their email address.

- **[Open Weather Map API](https://openweathermap.org/api)**
    - The project uses **Open Weather Map API** to add weather forecast functionality to the footer of the Visit East Cork website. Like the Google Maps API, this API requires developers to set up an account and use an API Key to access weather information specific to their area. This is a straightforward process.

### 3.4 IDE

- **[GitPod](https://www.gitpod.io/)**
    - Gitpod was used to develop the website and style each element before deployment.

### 3.5 External Hosting

- **[GitHub](https://github.com/)**
    - This project uses the GitHub hosting service and is saved in a GitHub repository.

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

