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
- As a read only or first time user:
    - I am able to easily navigate the Ireland Recommends website. 
    - I can view reviews posted by other users and filter or search for reviews from the homepage. 
    - I can also "like" reviews left by other users. 
    - Should I wish to leave a review I can easily register as a user of the site and login without diffciulty. 
    - From my profile page, I can add a review and see it posted.

- As a regular user:
    - I can log in to the Ireland Recommends site easily and view my posted reviews. 
    - I can edit or delete reviews that I have posted in the past as well as add new reviews.

- As an administrator of the site:
    - I can log in to the site as an admin user and view all reviews that have been posted by users. 
    - I can also edit or delete any review posted by users.

### 1.2 Strategy
 - The goal of this project is to create an interactive website where users can view reviews, upvote their popularity, add their own reviews and then edit or delete those reviews at any time. An administrator can edit or delete any reviews posted by users on the site. Ireland Recomments uses the Flask framework and is connected to a MongoDB database for the creation, reading, updating and deleting of information present on the site.

### 1.3 Scope 

#### Current Features

**Base HTML**
- The base template contains a Navbar that utilises an IF Statment which changes the links displayed depending on whether a user is logged in or out or if they are an administrator. The navbar is fixed to the top of the page when a user scrolls on each page. Using Materialize, the navbar is responsive on small screens and converts to an interactive burger icon. This icon triggers a menu that slides from the right hand side of the screen. It is easy to use and visually appealing.
- Flash messages are displayed using Flask's flash feauture. This feature displays messages to the user when they interract with the site.
- A footer is also contained in the base template. Social media icons are located in the footer. For the purpose of this project these icons are linked to the each social media sites homepage which opens in a seperate tab.

**Reviews Page**
- The reviews page is the main landing page of the Ireland Recommends site. It contains the base template content as well as a hero image and the following elements. 
- Filter icons are located below the hero image on the reviews page, these filters allow users to see reviews from the four categories associated with the filters.
- In order to improve a the sites usability and user experience, a search bar located below the filters allows users to search for keywords within the reviews and display the related reviews on the page.
- Each review is displayed on a card that is generated using a Jinja for loop. The card is tyled using Materialize and contains an image relating to the review, a short description of the review, the review date and a "Like" upvote button. Using a Python sort function, cards are displayed with the newest review first.

**Individual Review Page**    
 - Each review card is linked to an indiviudal review page. This page contains a simple layout featuring a large image associated with the review, the review name, its long description and the details of the user that added or edited the review. When a user is logged in to the site, they have the ability to edit or their delete the review if they are the user who originally posted it. In addition, there is a 'return to home' button which acts as an additional navigation option for ease of use. 

**Login / Register Page**
- A simple card design for both logging in and registering with the site. Both pages contain a form to add in the desired username and password. The username and password must be 
  alphanumerical and be of a length between 5 and 15 characters.

**Profile Page**
- Instead of a flash message, users are welcomed by a message which includes their username over the background of an image 
    of Ireland.
- Reviews that the user has already added will appear on this page in the form of cards. These cards will also include the option for users to edit and delete their own reviews. 
- As part of defensive programming, the delete button is followed by a modal which asks the user if they are sure that they 
    want to delete the review.

**Add/Edit Review Page**
- Both of these pages have a similar design and allow users to add or edit informaion about their reviews. Each entry into the form uses the 
    required attribute except for the images URL field. Some have min and max values to ensure that the layout remains consistent. As well as text 
    entries, there is a date selection function to choose the date that the reviewip has been added. Extra JQuery has been added to ensure 
    that the category name is not left blank. This was taken from Code Institute coursework. Should a review be added without an image attached, a default image will be displayed.

**Manage All Pages**
- For the Admin user only, there is a Manage All button in the Navbar where the user is able to read, update and delete all reviews added by any user. 


#### Possible Features Left to Implement

### 1.4 Structure
- The Ireland Recommends site is split into seperate pages for each function. For all users, different pages exist for the home, reviews, login and register page. For a logged in user, the Profile and Edit Tip page exists, and for the Manage all page exists for the administrator. Each page has the same footer and the responsive Navbar to ensure a consistent user experience across the site.

### 1.5 Skeleton
A mobile first approach was taken to designing the website. The original wireframes were created using Balsamiq and can be found below:

- Mobile Wireframe PDF - <a href="https://drive.google.com/file/d/1mZFBJaE9AHte7Ps6IZO7y6owGuUefVHX/view?usp=sharing" rel="noopener" target="_blank">mobile version in PNG</a>.
- Desktop Wireframe PDF - <a href="https://drive.google.com/file/d/1pcw1GKw0YcSmr4G45tPgPNvmSDhIfQSt/view?usp=sharing" rel="noopener" target="_blank">desktop version in PNG</a>.

The wireframe mockups gave me a basic idea of how best to lay out each individual element that I wanted to incorporate into the project and how that would impact and enhance the user experience. As the project progressed, how best to place each of these elements became apparent.

### 1.6 Surface

#### Design
* Colour scheme
- In keeping with the Irish theme of the site, I decidedto use a green and white colour scheme throughout the site. The type of colour is from the Materialize Light Green Colour Palette which has been lightened to improve visual appearance. Warning flash messages appear in red on the site and welcome and departure messages appear in black. The hover css attribute changes the colour of the category and social media icons when the user hovers over them.

* Logo
- The logo used for the Ireland Recommends website is a Triskell Celtic Symbol, a free to use image from PlumePloume and Pixabay, available **[here](https://pixabay.com/vectors/triskell-symbol-celtic-logo-1194004/)**

* Font
- I selected the Josefin font from Google Fonts for this project as it is reminiscent of classic minimalist travel posters and fits in with the styling of the website. This font is backed up by the sans-serif font.

* Images
- The hero images and background images were all taken from [Pexels](https://www.pexels.com/). The images for the individual reviews 
    are added via a URL link by the user. 

#### Defensive Design

#### Interactive Design
***

<span id="data"></span>

## 2. Data Architecture 

MongoDB Atlas is used for storing data for this website. The project ahas 3 collections in the MongoDB database.

A diagram of the current schema is available below:

<p><img src="docs/screenshots/dataSchema.jpg"></p>


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
  - The project used **Javacsript** to provide the functionality and customisation for the modal, mobile nav bar and forms.

- **[Python](https://en.wikipedia.org/wiki/Python_(programming_language))**
  - The project used **Python** to provide backend functionality for the project.

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
    - This was used predominantly for the for loops and if statements in order to display all of the relevant data.
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
- **[Balsamiq](https://balsamiq.com/)**
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

### 4.1 Validation 

[Please follow this link to view the full testing document]()

The following  tools validate every page of the project to ensure it did not contain syntax errors.

- **[W3C HTML Validator](https://validator.w3.org/)**
    - The W3C HTML Validator checked the website for HTML validity errors.
    - This same result appears across every page of the site.
    <p> <img src="docs/screenshots/htmlValidator.jpg">  </p> 

- **[W3C CSS Validator](https://jigsaw.w3.org/css-validator/)**
    - The CSS Validator checked for validity errors in the website's CSS page.
    - There is 1 property issue found when checking the site. However, these are being validated from the Materialize 
    link and therefore out of my control.
    <p> <img src="docs/screenshots/cssValidator.jpg">  </p>

- **[JSHint](https://jshint.com/)** 
    - No issues were found on this check.
    <p> <img src="docs/screenshots/JSHint.jpg"></p>

- **[Python Validator](http://pep8online.com/)**
    No issues were found on this check.
    <p> <img src="docs/screenshots/pep8.jpg"></p>  

- **[Autoprefixer CSS Online](https://autoprefixer.github.io/)**
    - The Autoprefixer ensured that vendor prefixes were added to my CSS.

- **[Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)**
    - Google Chrome's DevTools were used to inspect elements of the website and adjust them to ensure that they were effective and responsive at different screen sizes. DevTools was also used to identify errors in my code and to test how changing certain elements would effect the overall look and feel of the website.

### 4.2 Autoprefixer CSS Online

This was used to parse CSS and add vendor prefixes in order to ensure that the CSS styling works properly across all 
browsers. I have added the below header to my CSS styles sheet in order to show this:
<p> <img src="documentation/screenshots/css-prefixer.jpg">  </p>

### 4.3 Lighthouse

<p >Desktop<img src="documentation/screenshots/lighthouse.jpg">
Mobile<img src="documentation/screenshots/lighthouse-mobile.jpg"></p>

From Chrome Developer Tools, this Lighthouse score is based on the homepage while being viewed on desktop and mobile. The 
biggest variant throughout the site is the performance score, which is predominantly due to the image link added by users 
to the site for each individual Tip, making it quite hard to control. 

### 4.4 Testing User Stories

[Please follow this link to view the full testing document]()



### 4.5 Device Testing

I utilised Google Chrome's DevTools to test the responsivness of the website at different screen sizes throughout the project. Once the project was approximately 70% complete, I tested it using a Huawei P9 Lite and an Apple iPhone 11 mobile device and an Acer tablet device. The website worked well on all devices.
I tested the desktop functionality of the Visit East Cork website on Google Chrome and Microsoft Edge.

#### On screen sizes of tablet size and below: 
- Cards and divs are responsive and will align with the mobile view. 

### Further Testing

- **[Balsamiq](https://balsamiq.com/)**
    - I used Balsamiq to design the original wireframes for the project and test how the layout looked. I reverted to Balsamiq when considering changes in the project's design.

- **[GTMetrix](https://gtmetrix.com/)**
    - GTMetrix was used to test the loading speed of the site and to find out if any elements were creating long loading times.

### 4.6 Bugs


<span id="deploy"></span>

## 5. Deployment

### Requirements 
- Python3 
- Github account 
- MongoDB account 
- Heroku account

### Clone the project 
To make a local clone and deploy this project in your GitHub Desktop, follow the following steps. 
1. Log in to GitHub and go to the repository. 
2. Click on the green button with the text **“Code”.**
3. Click on **“Open with GitHub Desktop”** and follow the prompts in the GitHub Desktop Application or follow the instructions from **[this link](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop)** to see how to clone the repository in other ways. 

### Working with the local copy
1. Install all the requirements: Go to the workspace of your local copy. In the terminal window of your IDE type: **pip3 install -r requirements.txt**.
2. Create a database in MongoDB  
    - Signup or login to your MongoDB account.
    - Create a cluster and a database.
    - Create four collections in the db: **categories, recipes, subscribers, users.**
    - Add string values for the collections. See <a href="#ux-architecture">my Information architecture</a> how the database is set up for this project.
3. Create the environment variables 
    - Create a .gitignore file in the root directory of the project.
    - Add the env.py file in the .gitignore.
    - Create the file env.py. This  will contain all the envornment variables.
    ```
    Import os
    os.environ.setdefault("IP", "Added by developer")
    os.environ.setdefault("PORT", "Added by developer")
    os.environ.setdefault("SECRET_KEY", "Added by developer")
    os.environ.setdefault("MONGO_URI", "Added by developer")
    os.environ.setdefault("MONGO_DBNAME", "Added by developer")
    ```
4. Run the app: Open your terminal window in your IDE. Type python3 app.py and run the app.

#### Heroku Deployment  
1. Set up local workspace for Heroku 
    - In terminal window of your IDE type: **pip3 freeze -- local > requirements.txt.** (The file is needed for Heroku to know which filed to install.)
    - In termial window of your IDE type: **python app.py > Procfile** (The file is needed for Heroku to know which file is needed as entry point.)
2. Set up Heroku: create a Heroku account and create a new app and select your region. 
3. Deployment method 'Github'
    - Click on the **Connect to GitHub** section in the deploy tab in Heroku. 
        - Search your repository to connect with it.
        - When your repository appears click on **connect** to connect your repository with the Heroku. 
    - Go to the settings app in Heroku and go to **Config Vars**. Click on **Reveal Config Vars**.
        - Enter the variables contained in your env.py file. it is about: **IP, PORT, SECRET_KEY, MONGO_URI, MONGO_DBNAME**
4. Push the requirements.txt and Procfile to repository. 
     ```
    $ git add requirements.txt
    $ git commit -m "Add requirements.txt"

    $ git add Procfile 
    $ git commit -m "Add Procfile"
    ```
5. Automatic deployment: Go to the deploy tab in Heroku and scroll down to **Automatic Deployments**. Click on **Enable Automatic Deploys**. By **Manual Deploy** click on **Deploy Branch**.

Heroku will receive the code from Github and host the app using the required packages. 
Click on **Open app** in the right corner of your Heroku account. The app wil open and the live link is available from the address bar. 

***
<span id="credit"></span>
## 6. Credits

### 6.1 Content


### 6.2 Media

- **Images**
    
- **Text**
    

- **Mockups**
    

### 6.3 Acknowledgements



***

