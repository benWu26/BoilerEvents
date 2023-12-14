# BoilerEvents
#### Video Demo:  https://youtu.be/fmgfUlb6tVU
#### Description: This website centralizes websites at Purdue.
The main purpose of the app is to centralize all the websites at Purdue. Because there are many different sources of information at Purdue, there is not a single website which has most events. These events are scattered on different websites so this website allows users to post these events all in one place. This makes it easier for students to see events. This website depends on students to spread the word around.

This website allows users to creates accounts to upload to the SQL database. They can also submit requests which will send an email to an administrator. This then allows the administrator to review the request and upload the information to the database which the user can see. To navigate the website, first register. Then once you are logged in, you can see the different events on the main page. Once logged in, you can also request to add events. To do this an administrator recieves and email about the events and then can log in to upload this.

There are different templates that represent different page. The about page gives information about the page. The admin page is the page that allows an administrator to submit information into the SQL database. The contact page is the page where the user can submit a request. The index page is the main page. The login page and register page help the user to login and register when logged out.

For the python or flask used, I have used app.py and the helpers.py. The helpers.py is used mainly for helping to track if a user is logged in or not. Although this was based off the finance helpers function, but I created mine in a way which I could understand. The app.py is used for all the main functions of the website. It detects for errors and posts and gets the html.

The static folder also includes the images used in the website and also links the css files to the html.

I based the project off the CS50 finance website because I thought that was a good layout. I also used elements from the other page I created in CS50. For this project, I also chose to include the CS50 libary so it would be easier to manage the SQL database. For this same reason, I also chose to use flask for this project as it was familiar. One of the best features of the website is sending the email. Although it seems pretty simple, it took me a decent amount of time to implement this feature into the website.

I also have implemented many smaller features into my app. For example, as discussed earlier, I implemented the email function. I also have included things like redirecting to my linkedin on the footer and redirecting to an email app when you click the link in the about page.

Although there are many things that still needed to be changed for this website comes to fruition, the website reflects the hard work I have put in to complete CS50.

