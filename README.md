

<h1 align="center"><a href="https://cesargarciajr.github.io/QuizTmas/" target="_blank">THE ULTIMATE RPS</a></h1> 

The Ultimate RPS is a fun and diferent approach for one of the most famous games of the world. Now as a backend application in a mock terminal you can have fun and chellange the computer for a 5 round game. If you in 3 times out of 5 a surprise is gonna be unlocked. Also pay attention to the hints and make a smart choice to become the RPS Legeng. Have fun!

[**Link to The Ultimate RPS**](https://the-ultimate-rps-75d98298966f.herokuapp.com/)

![Alt text](assets/images/Hero-img.png "Hero image for Readme File")

# Contents

- [The Ultimate RPS](#the-ultimate-rps)
- [Contents](#contents)
  - [User Experience (UX)](#user-experience-ux)
    - [User Stories](#user-stories)
    - [FlowChart](#flowchart)
    - [Site Structure](#site-structure)
    - [Desing Choices](#design-choices)
  - [Features](#features)
    - [Landing Play Page](#landing-play-page)
    - [Welcome Message](#welcome-message)
    - [Main Menu](#main-menu)
    - [Rules](#rules-menu-option)
    - [Credits](#credits-menu-option)
    - [Start Game](#start-game-menu-option)
    - [Game Over Message](#game-over-message)
    - [Selected Valid Option](#selected-valid-option)
    - [Contact Page](#contact-page)
    - [Future Features](#future-features)
  - [Testing](#testing)
    - [Testing Process](#testing-process)
    - [Bugs and Issues](#bugs-and-issues)
  - [Technologies Used](#technologies-used)
  - [Deployment](#deployment)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
  - [Acknowledgments](#acknowledgments)
- [THANK YOU!](#thank-you)

___


## User Experience (UX)

  ### User Stories

  - #### First-Time Visitor Goals
<br>    i.   As a First time user I want to be able to intuitively learn how to play the game without even reading the Rules.
<br>    ii.  But if needed check the Rules and see if its clear.
<br>    iii. I might have to contact the developer for any bug or leave a message.
<br>    iv.  Have fun!

  - #### Returning Visitor Goals
<br>    i.   As returning user I want the be able to play the game.
<br>    ii.  Check if there is any updates to the game.
<br>    iii. Have fun!

  - #### Frequent User Goals
<br>   i.   As frequent user I want the be able to play the game.
<br>   ii.  Check if there is anyupdates to the game.
<br>   iii. Have fun!

  [Back to top](<#contents>)
  
  - ### FlowChart
    The flowchart was a very useful tool to plan ahead and understand how to build the application below you can see the chart that was made using the [**Lucid**](https://lucid.co/)

    ![Alt text](assets/images/rps-flowchart.png "flowchart")

[Back to top](<#contents>)

  - ### Design Choices
      The idea was to build a terminal based application with smooth transitions to make the UX even more seamless and intuitive. I added few diagrams to make the game more user friendly and make look better as you can see the [Features](#features) section.


[Back to top](<#contents>)

## Features

  ### Landing Play Page
As part of the game a landing area presents the Rock, Paper, Scissors and Gun as hints of how to "unlock" the Legend by selecting the gun to win over all options:

  ![Alt text](./assets/images/Hero-img.png "Landing Play Page") 

[Back to top](<#contents>)

  ### Welcome Message
Welcome message gives the user a clear idea of the game and a 4.5 second to see this message while game is loading is a user friendly interaction.

  ![Alt text](./assets/images/welcome-message.png "Welcome Message") 
  
[Back to top](<#contents>)
        
  ### Main Menu
The main menu gives the user clear options to select and navigate through it.

  ![Alt text](./assets/images/main-menu.png "Main Menu") 

[Back to top](<#contents>)

  ### Rules Menu Option
Rules are clear and easy to understand making user experience more effective regarding to know how to play the game and use the system.

  ![Alt text](./assets/images/rules.png "Rules") 
 
[Back to top](<#contents>)

  ### Credits Menu Option
Credits option gives the user to contact the developer in case o bugs or issues found, or to get in touch for futures projects

  ![Alt text](./assets/images/credits.png "Credits") 
 
[Back to top](<#contents>)

  ### Start Game Menu Option
Once the user start the game it prints to the console a Rock, Paper, Scissors diagram to show user the options also prints the Round counter and a score section to keep track the progress of the game. Finally asks the user to input the option as the user can type "r" "R" "rock" respectivly to the options available. If not a "Invalid option will be printed"

  ![Alt text](./assets/images/game-play.png "Game play") 
 
[Back to top](<#contents>)

  ### Selected Valid Option
Once a valid option is selected it will show what was selected and generated randomly by the computer

  ![Alt text](./assets/images/showing-choices.png "Show Choices") 
 
[Back to top](<#contents>)

  ### Comparing Computer vs User choices
The system will compare the computer and the user choice and print an outcome for that round. Also increasing the round and the score if win or lose round

  ![Alt text](./assets/images/win-round.png "Win Round")
  
  ![Alt text](./assets/images/lost-round.png "Lose Round")
 
[Back to top](<#contents>)

  ### Comparing Computer vs User choices
The system will compare the computer and the user choice and print an outcome for that round. Also increasing the round and the score if win or lose round

  ![Alt text](./assets/images/win-round.png "Win Round")
  
  ![Alt text](./assets/images/lost-round.png "Lose Round")
 
[Back to top](<#contents>)


  ### Future Features
We want to implement 2 different surprise cards. So everytime the user picks a card he can either pick a Santa Claus picture, a Grinch picture or a question.
If the user picks a Santa Claus it will give him a 2 points Bonus. If the user picks a Grinch card it will lose 3 points, and if the user picks a question he has a chance either to win one point by picking the right answer or lose a point. 


[Back to top](<#contents>)

## Testing

The game was tested in differents 

- Tested in differents mobile devices and web browsers
- Tested using the [**CCS validador**](https://www.w3.org/)
- Tested using the [**HTML validator**](https://validator.w3.org/nu/)
- Tested using the [**JsHint Validator**](https://jshint.com/)
- Tested using the Lighthouse dev tool from Google Chrome

You can see the reports below as mentioned before:

Css validator report

![Alt text](assets/images/css-validator.png "CSS report")

HTML checker report

![Alt text](assets/images/Html-checker.png "HTML report")

Jshint report

![Alt text](assets/images/JsHint.png "JsHint report")

Lighthouse dev tool from Google Chrome Report

![Alt text](assets/images/lighthouse-testing.png "Chrome LightHouse report")

### Testing Process

  | Test                | Action                   | Success Criteria  |
  | -------------       |-------------             | -----|
  | Landingpage loads      | Navigate to website URL  | Page loads < 5s, no errors |
  | Links            | Click on each Navigation link  | Correct section is redirected action performed |
  | Gameplay  | Click the cards, answers buttons and counting the right, wrong and number of questions | The game is working as it should with no errors and malfunction |
  | Responsiveness | Resize the viewport window from 320px upwards with Chrome Dev Tools. Use Responsive Design Checker to test various mobile, tablet, and large screen sizes | Page layout remains intact and adapts to screen size|
  | Different web browsers | Runned the game in Google Chrome, Mozilla Firefox and Internet Explorer | Game works responsive and layout remains intact no errors or bug detected |
  | Different screen devices | Runned the game using a Samsung Galaxy s20 and Iphone 13 | Game works responsive and layout remains intact no errors or bug detected |

[Back to top](<#contents>)


 ### Unsolved bugs

Debugging and troubleshooting were done constantly throughout development, however still a problem with the website:

When the user reaches the 10th question and tries to open the a new card the Game Over message appears on the modal popup but in the top right corner it counts as a "question" as displayed in the image below. One of the solutions would make the modal popup bigger when the message is displayed so it would cover the tally area. But I was not happy "hiding" the bug, I wanted to have a proper and better idea of solution, but unfurtunatly haven't managed the time to review the code and re-design a best solution yet.

 ![Alt text](./assets/images/game-over-message.png "Game Over Message")


[Back to top](<#contents>)

___

## Technologies Used
I used the following technologies, platforms and support in building my project:
- Wireframes and mockups were designed in [**Balsamiq**](https://balsamiq.com/wireframes/desktop/#)
- The website is built with HTML, CSS and JavaScript.
- The [**Code Institute**](https://codeinstitute.net/) modules/lessons aided my learning and many of the concepts learned were applied in this project.
- [**GitHub**](https://github.com/Cesargarciajr/bloom-of-life) was used for the project repository.
- [**Google Fonts**](https://fonts.google.com/) was used for all fonts on the site.
- [**FontAwesome**](https://fontawesome.com/) was used for the social media icons which then had additional styling applied to them.
- [**Colors CO**](https://coolors.co/) was used to create a colour pallete for this readme file.
- [**Adobe Colors**](https://color.adobe.com/pt/create/color-contrast-analyzer) and contrast was used to pick color and check if the contrast was good enough for users.

[Back to top](<#contents>)

## Deployment

First of all you need to have a [**GitHub**](https://github.com/Cesargarciajr/bloom-of-life) account, I choose [**GitHub**](https://github.com/Cesargarciajr/bloom-of-life) because it's free and easy to create a repository to host your code and share with others.

- To create a repository you just need to go to the main page at the top right you will see a "+" button just click here and then new repository

- Select the name of the project and a description make it public and then create a repository

- Once you created your repository go the settings section and then click on pages

- Select the Branch as main and then save it.

- Finally, your repository is deployed and it should show you a link so you can share it with others.

[Back to top](<#contents>)

## Credits

  ### Content  
  - [**Code Institute**](https://codeinstitute.net/)  - Python Module and Tutor Support.
  - [**GitHub**](https://github.com/) - for deployment and host.
  - [**Code Anywhere**](https://app.codeanywhere.com/) - for IDE and editor of the code.
  - [**Precious Ijege**](https://www.linkedin.com/in/precious-ijege-908a00168/) - Mentor helping with insights and coding fix.
  - [**W3 Schools**](https://www.w3schools.com/) - used for multiples researches and tutorials in HTML and CSS.
  
[Back to top](<#contents>)

  ### Media
- [**Lucid**](https://lucid.co/) - Flowchart used on readme file.

[Back to top](<#contents>)

## Acknowledgments

This project definetly challenge my skills, I've learned so much throughout the process and can say I have a feeling of acomplishment from what I knew when I started this project and from what I know now. It definitly helped better understand concepts in coding also expand my knowledge in JavaScript. It was fun and enjoyable to built this game, I wan to thanks my mentor [**Precious Ijege**](https://www.linkedin.com/in/precious-ijege-908a00168/) for the support, help and guidance during the project.

by [**Cesar Garcia**](https://github.com/Cesargarciajr)

# THANK YOU!

[Back to top](<#contents>)