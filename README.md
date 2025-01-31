# [MyRecipeApp: Personal Recipe Collection App](https.herokuapp.com)


# Project Overview

[MyRecipeApp](https:.herokuapp.com) is a [Flask](https://flask.palletsprojects.com/en/stable/)-based [CRUD](https://www.codecademy.com/article/what-is-crud) application that lets users manage their recipe collection with ease of use. Users can create secure accounts or log in using hashed passwords powered by [bcrypt](https://flask-bcrypt.readthedocs.io/en/1.0.1/), and perform actions like adding, editing, deleting, and searching for recipes that havebeen stored in a [MongoDB](https://www.mongodb.com/) database. The app features a dynamic and responsive interface styled with custom css, while [JavaScript](https://www.w3schools.com/js/DEFAULT.asp) enhances interactivity by animating the flashing effect when searching for recipes. My Reciep App allows for an intuitive experience for managing your recipes in a secure account authenticated by a password and data that is managed in a collection. This allows for posiitve user experiences and ease of use.

**Key Features:**
- User Authentication & Security: Leverages Flask-Bcrypt for secure password hashing and implements a safe login and registration process.
- Dynamic Recipe Management: Easily add, edit, delete, and view recipes in a personalized collection with full CRUD functionality.
- User-Centric Dashboard: Provides a customized experience where users can manage their recipes efficiently.
- Recipe Search Optimization: Fast and intuitive recipe search feature, allowing users to quickly find their dishes.
- MongoDB Integration: Utilizes MongoDB to store and manage user and recipe data, ensuring scalability and performance.
- Role-Based Access Control: Ensures secure access with session management, limiting recipe modifications to authenticated users.
- Responsive & Accessible Design: Built with a mobile-first approach, ensuring seamless navigation on all devices with a clean and modern UI.


![amIresponsive: MyRecipeApp](documentation/screenshots/.png)

## UX

When designing a CRUD-based application, a recipe management system offers a compelling and user-centric experience. It allows users to efficiently create, view, edit, and delete their own recipes in a structured, easy-to-navigate environment. The key UX challenge lies in creating a seamless flow for users to interact with their recipe collection, whether they are adding new recipes, searching through them, or modifying existing entries.

The project also introduces personalized user authentication, giving users the ability to manage their own recipes securely. This adds an extra layer of complexity, as the design must account for features like login, session management, and ensuring that users can only access their own recipes. This personalized experience strengthens user interaction, providing the feeling of ownership and control over the data they create.

### Color Scheme

The chosen color palette is designed to create a visually engaging and user-friendly experience while maintaining a clean and modern look. The combination of contrasting colors ensures clear readability, intuitive navigation, and an aesthetically pleasing interface that enhances the overall usability of the application.

**1. Background Colors (#343a40, #69aaf9):
The dark grey header (#343a40) provides a strong and structured feel, creating a sense of focus and organization. In contrast, the vibrant blue background (#69aaf9) adds a fresh and inviting atmosphere, making the interface feel approachable and easy to navigate.

**2. Action Buttons (#dc3545, #4CAF50, #007bff):
Key actions are color-coded to improve usability. The red (#dc3545) is used for actions requiring caution, such as "delete," ensuring users can easily distinguish critical functions. The green (#4CAF50) is used for positive actions like saving or submitting, reinforcing a sense of confirmation. Blue (#007bff) highlights interactive elements like editing, making them easily identifiable.

**3. Text & Highlight Colors (#fff, #ff6347, #eeecec):
White (#fff) text is used against dark backgrounds to maximize readability. Titles and key elements feature a striking coral shade (#ff6347), adding a dynamic and engaging touch. The soft grey (#eeecec) in recipe cards ensures content remains clear and easy to read without overwhelming the user.

By combining bold contrast with subtle highlights, this color scheme creates an intuitive and visually appealing experience while maintaining clarity and ease of use.