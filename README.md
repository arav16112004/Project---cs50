# College Essay Organizer
#### Video Demo:  <https://youtu.be/fZt0V5LLuck>
#### Description:
My name is Arav Mehta. I am a student in the 12th Grade. I am from Mumbai, India, and this is my Cs50 project.
I felt that one crucial time in each high school student's life is the time of college applications. During such times organizing tasks can be very difficult. I have made a college essay organizer.

I have made this web application building on much of what i learnt from week 9 of the course.

starting at the home page. There are 2 buttons to register and login. Clicking on register will open a page called register.html to register with your name and desired password. The page will take the input via post and store it in a database .The password is then converted to a hash and stored in the database as well. On opening the login page, a page called login.html will open. the page asks for the users password and username and after checking it with the database, logs the user into their account. If the wrong password or username is used the page will return a message accordingly using the return functuin.

Note: The data for the tasks of each user is stored in a separate table called essays. Their password and username is stored in another table called users.

Login

After logging in, the app takes the user to their account homepage using session["user_id"]. The index function will look for the user's name in the database and bring back the data from the database regarding their tasks. Throughout all of this, the page always shows options such as logout, view essay,add tasks etc. The index function opens a page called index.html which forms a table. The html file has a for function that is linked to app.py that creates rows based on the number of tasks there are in the user's account.

On clicking on the add tasks button - the page will direct the user to another page called input.html. The page has 4 fields. one is to name the essay in one word for ease of access. The second is the field for the name of the prompt of the essay, the 3rd is the name of the university/college the essay is for the and the 4th is the deadline for the task to be completed. Below all of this is a submission button - which submits the data to the server. Through app.py and the input function, the system will take the input from the site and enter it into the essay table.

The top right has a view essay option which brings the users tasks from their table from the database and shows it in the form of a table. the table also has checkboxes for each task so that the essays can be checked when complete.

Further on, the delete essay option on the top right of the essay allows users to delete tasks. The button will redirect the user to delete.html where in a dropdown menu is present with all of the tasks in their account. Pressing the delete button removes the task from the database. Going to view essays and refreshing it will remove the essay from the table as well.

the logout button opens ends the session and takes the user back to the login/register page

I did face some design issues. In the beginning i did not know how to get all the essays from the database but i eventually figured it out. Furthermore, i also faced problems creating a drop down menu for the user to select the essay to delete and take the selected value as input to delete but with a bit of research i figured it out.
