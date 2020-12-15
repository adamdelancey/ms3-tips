# MS3: Tips.

[View the live project here.](https://adamdelancey.github.io/ms3-tips/)

As my submission for the Code Institute Milestone Project 3, this Tips website is a site where users can create, read, update and delete suggestion of things to do in Stockholm,
for example where to eat and drink, in order to create a database of ideas that locals and tourists can use to maximise their experience in the city.It is designed to be 
responsive and accessible on a range of devices, making it interactive and easy to navigate for potential users.

<p align="center">
    <img src="documentation/screenshots/responsive.jpg">

# Access

View the project live: [here](https://adamdelancey.github.io/ms3-tips/)

View the Github repo: [here](https://github.com/adamdelancey/ms3-tips)

## Contents

- [UX](#ux)
    - [Strategy](#strategy)
        - [Business Objectives](#business-objectives)
        - [User Stories](#user-stories)
            - [First Time Visitor Goals](#first-time-visitor-goals)
            - [Frequent User  Goals](#frequent-user-goals)
    - [Scope](#scope)
        - [Current Features](#current-features)
            - [Navbar](#navbar)
            - [Back to top Button](#back-to-top-button)
            - [Home Page](#home-page)
            - [Property Landing Page](#property-landing-page)
            - [Property Listing Page](#property-listing-page)
            - [Contact Page](#contact-page)
        - [Long-term goals](#long-term-goals)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
        - [Wireframes](#wireframes)
    - [Surface](#surface)
        - [Design](#design)
            - [Colour Scheme](#colour-scheme)
            - [Typography](#typography)
            - [Imagery](#imagery)
            - [Icons](#icons)
- [Accessibility](#accessibility)
    - [Alt Tags](#alt-tags)
    - [Forms](#forms)
- [Technologies used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks, Libraries & Programs Used](#frameworks-libraries-&-programs-used)
- [Testing](#testing)
    - [Validation](#validation)
    - [Autoprefixer CSS Online](#autoprefixer-css-online)
    - [Lighthouse](#lighthouse)
    - [EmailJS API](#emailjs-api)
    - [Testing User Stories from User Experience Section](#testing-user-stories-from-user-experience-section)
    - [Fixed Bugs](#fixed-bugs)
    - [Known Outstanding Bugs](#known-outstanding-bugs)
    - [Further Testing](#further-testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)


# UX

## Strategy

### Business Objectives

1. To create a space where all users, first-time or frequent, can find exciting and new things to do in Stockholm.
2. To create a site where users can add suggestions to the community and find others' suggestions to improve their experience.
3. To create a site that is used by locals and tourists alike to share ideas.
4. To create an exciting database that can be used for further research into life in Stockholm.

### User stories

-   #### First Time Visitor Goals

    As a First Time Visitor, I want to:

    1. Quickly understand the service being provided by Tips and how I can interact with the service.
    2. Be able to easily browse the various 'tips' in Stockholm and find something that interests me.
    3. Be able to register to the website and add my own 'tips'.
    4. Be able to comfortably navigate throughout the site between my own tips and other users'.
    5. Get an instant first-impression that this is a professional, modern and up-to-date site with good UX.



-   #### Frequent User Goals

    As a Frequent User, I want to:
    1. Easily be able to check if any new tips have been added that may interest me.
    2. Login to the account that I had previously set up and see my own submissions.
    3. Add more tips to the website that I may not have done already.
    4. Edit my own tips.
    5. Delete any tips that are no longer relevant.

## Scope

### Current features

* Opening Page 


* Navbar
  

* Landing Page


* Login/Register Page 


* Profile Page


* Add Tip Page


* Update Page 
  

### Long-term goals

Future improvements to the website may include:

* Be able to add reviews to other user's tips and then allow the website to order user suggestions from best to worst.
* Expanding the website to be used across more cities around the world.
* Include a paid service so that hotels or experiences companies can advertise their business on the site.


## Structure

* 1
* 2
* 3
* 4
* 5



## Skeleton

### Wireframes

Desktop View
<p><img src="documentation/screenshots/home-desktop.jpg">
    <img src="documentation/screenshots/browse-desktop.jpg">    
    <img src="documentation/screenshots/tip-view-desktop.jpg">
    <img src="documentation/screenshots/login-view-desktop.jpg">
    <img src="documentation/screenshots/register-desktop.jpg"></p>
    <img src="documentation/screenshots/profile-desktop.jpg"></p>
    <img src="documentation/screenshots/submit-desktop.jpg"></p>
    <img src="documentation/screenshots/edit-desktop.jpg"></p>

Mobile & Tablet Pages
<p><img src="documentation/screenshots/home-tablet-mobile.jpg">
    <img src="documentation/screenshots/browse-tablet-mobile.jpg">    
    <img src="documentation/screenshots/tip-view-tablet-mobile.jpg">
    <img src="documentation/screenshots/login-view-tablet-mobile.jpg">
    <img src="documentation/screenshots/register-tablet-mobile.jpg"></p>
    <img src="documentation/screenshots/profile-tablet-mobile.jpg"></p>
    <img src="documentation/screenshots/submit-tablet-mobile.jpg"></p>
    <img src="documentation/screenshots/edit-tablet-mobile.jpg"></p>

Full wireframes can be accessed here:

-   Desktop Wireframes - [View](documentation/wireframes/tips-desktop.pdf)

-   Mobile & Tablet Wireframes - [View](documentation/wireframes/tips-tablet-mobile.pdf)    


## Surface
   
### Design
-   #### Colour Scheme
    <p><img src="documentation/screenshots/colors.jpg"></p>
    -   XXXX

-   #### Typography
    -   XXXX

-   #### Imagery
    -   XXXX   
    - All photos were put through [Tiny PNG](https://tinypng.com/) to reduce the file size and improve loading time.


-   #### Icons
    -   Contact icons used in the footer and contact page, as well as in the description for each property have been taken 
     from [Font Awesome](https://fontawesome.com/).

# Accessibility

## Alt Tags

In order to ensure that all images are accessible for those using a screen reader, I have ensured that all images used throughout the site include alt tags.

## Forms

The forms on the site used in the modals of "Contact Us" and "Enquire Now" have aria-labels so that screen readers can read out what is the required input in the necessary fields.

# Technologies used

## Languages Used

-   HTML5
-   CSS3
-   JavaScript
-   Python

## Frameworks, Libraries & Programs Used


1. [MongoDB](https://www.mongodb.com/1)
    - MongoDB was used....
1. [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    - Flask was used...
1. [JQuery](https://jquery.com/)
    - I have used JQuery for some JS functions, particularly ones that use event listeners such as for the see more/less buttons 
    on the homepage and the filtering of properties by number of bedrooms.
1. [Bootstrap 4.5.2:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website, such as the navbar, carousels and cards features.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Roboto' font which is used on all pages throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes. 
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the wireframes during the design process.

# Testing

## Validation

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://validator.w3.org/) - [Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fadamdelancey.github.io%2Fms2-ashtreeestates%2Findex.html)
    This same result appears across every page of the site.
    <p> <img src="documentation/screenshots/html-checks.jpg">  </p> 
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - [Results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fadamdelancey.github.io%2Fms2-ashtreeestates%2Findex.html&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) -  
    There are 2 property issues found when checking the site. However, these are being validated from the Bootstrap CDN link and therefore out of my control.
    <p> <img src="documentation/screenshots/css-validator.jpg">  </p> 
-   [JSHint](https://jshint.com/) - 
    <p> <img src="documentation/screenshots/jshint.jpg"></p>      
-   [Python Validator](http://pep8online.com/)

    

## Autoprefixer CSS Online

This was used to parse CSS and add vendor prefixes in order to ensure that the CSS styling works properly across all 
browsers. I have added the below header to my CSS styles sheet in order to show this:
<p> <img src="documentation/screenshots/css-prefix.jpg">  </p>

## Lighthouse

<p >Desktop<img src="documentation/screenshots/lighthouse.jpg">
Mobile<img src="documentation/screenshots/lighthouse-mobile.jpg"></p>

From Chrome Developer Tools, this Lighthouse score is based on the homepage while being viewed on desktop and mobile. I worked hard on
ensuring high scores across the site in particular by putting every image through [Tiny PNG](https://tinypng.com/), and improving 
SEO scores by adding a meta description to each page. The lower 'Best Practices' score is primarily due to the JavaScript
libraries being used for the site, specifically JQuery.

## EmailJS API

I have tested this manually on every page to ensure that the contact form is being sent through successfully. You can see this 
here:

<p> <img src="documentation/screenshots/emailjs.jpg">  </p>


## Testing User Stories from User Experience Section

-   #### First Time Visitor Goals - I want to:

    1. Quickly understand the service being provided by Tips and how I can interact with the service.
        - *XXXX*
    2. Be able to easily browse the various 'tips' in Stockholm and find something that interests me.
        - *XXXX*
    3. Be able to register to the website and add my own 'tips'.
        - *XXXX*
    4. Be able to comfortably navigate throughout the site between my own tips and other users'.
        - *XXXX*
    5. Get an instant first-impression that this is a professional, modern and up-to-date site with good UX.
        - *XXXX*


-   #### Frequent User Goals - I want to:

    1. Easily be able to check if any new tips have been added that may interest me.
        - *XXXX*
    2. Login to the account that I had previously set up and see my own submissions.
        - *XXXX*
    3. Add more tips to the website that I may not have done already.
        - *XXXX*
    4. Edit my own tips.
        - *XXXX*
    5. Delete any tips that are no longer relevant.
        - *XXXX*

## Fixed Bugs
After deployment, I found multiple bugs that needed addressing:

1. Bug 1
    - *Solution 1*
2.  Bug 2
    - *Solution 2*  
3.  Bug 3
    - *Solution 3*

## Known Outstanding Bugs

1. Bug 1
    - *Solution 1*
2.  Bug 2
    - *Solution 2*  

 
## Further Testing

- Throughout the development process, I used the Chrome Developer Tools, specifically for using the console.log function to test 
JavaScript code and also for the various CSS designs, particularly around responsiveness. On especially narrow devices < 300px, some images were 
larger than the width, however I felt this had no effect on UX.
- The website has been tested on various desktop browsers such as Google Chrome, Firefox, Safari and Edge, as mentioned above, I used 
the CSS tool Autoprefixer Online to help with this. 
- Each link has been tested across the site to ensure everything was linked correctly.
- Friends and family were also asked for advice particularly on layout and in order to ensure that the site was being tested across 
various devices. 


# Deployment

The site was published in GitPages using the following steps:
1. First, all code was written on the IDE Gitpod and was then pushed to GitHub using the 'git push' entry in the terminal, where it is now stored in [my repository](https://github.com/adamdelancey/ms2-ashtreeestates).
2. To push the site live, under the Settings section of the repository I selected, I scrolled down to where it says 'GitHub Pages'.
3. I then selected 'Master Branch' under Source and then the page automatically refreshed.
4. This created the URL which can be viewed [here](https://adamdelancey.github.io/ms2-ashtreeestates/index.html).
5. The site was then found by scrolling back to the "GitHub Pages" section where you can see the following:
<p><img src="documentation/screenshots/githubpages.jpg"></p>



To access the code, it can be run locally through a download or cloned.

Initially, I used "git commit" and "git push" for every major change, then at later stages used these functions when de-bugging or making minor editing changes to ensure the live version was the most recent version, as well as to avoid losing any work.

# Credits

- All professional images have been sourced from a combination of [Unsplash](https://unsplash.com/s/photos/bristol) and [Pixabay](https://pixabay.com/).
- All photos related to the properties have been sourced from Ash Tree Estates.
- The Navbar, Forms, Carousels and Cards have been chosen from Bootstrap templates and adapted using CSS.
- Initial instructions for setting up the Google Maps API were taken from the relevant lesson from the [Code Institute](https://codeinstitute.net/).
- Similarly, setting up the EmailJS API was also taken from the relevant lesson from the [Code Institute](https://codeinstitute.net/).
- Instructions for setting up the getNearbyPlaces function was taken from the [Google Codelabs Developer lessons](https://codelabs.developers.google.com/codelabs/google-maps-nearby-search-js#1)
- [Stack Overflow](https://stackoverflow.com/) and [W3C Schools](https://www.w3schools.com/) were used for occasional debugging or issues where I could not initially work out the solution myself.
- Fonts are from [Google Fonts](https://fonts.google.com/) and icons from [Font Awesome](https://fontawesome.com/).


# Acknowledgements

- My mentor, Aaron Sinnott, for his support and mentorship during the project.
- The peer-code-review channel on Slack and their trusty channel leads for both code and design tips.
- Friends and family for testing the site on their various devices.
