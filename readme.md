
<h1 align="center">
The User Management System Final Project 🎯🏆🌟
</h1>

## Learning Outcomes from the Project:📚
    - I have gained good hands on experience with building API using fastAPI along with things like request handling, dependency injection, middleware integration.
    - Learned about implementing RESTful endpoints following industry standards like HATEOS BREAD.
    - Learnings about how to design and implement normalized relational database schemas using SQLAlchemy ORM.
    - Learned to manage the asynchronous database sessions with AsyncSession and connection pooling.
    - Explored how the querying works using SQLAlchemy like joins, filters and paginations.
    - Learned how to use Pydantic models to validate the API input and serialise database responses into JSON.
    - Implementing QR code generation using qrcode library using custom parameters like encoded and decoded information.
    - Encoding user data securely using base64 and integrating it to the QR codes.
    - Implementing BREAD HATEOS principles, provides the self descpritive links for navigation.
    - Tackled complex issues like base64 handling, managing database transactions, aligning SQLalchemy models with pydantic schemas.
    - Worked on the User Profile Management feature in which I have implemented API endpoints for users to update their profile fields.
    - Created a separate API endpoint for managers and admins to upgrade a user to professional status.
    - Added the feature of Send notifications to users when their professional status is upgraded.
    - Improved my analytical skills by debugging intricate tracebacks and resolving the issues raised while testing.
    - Conducting manual testing for the API endpoints to ensure if they are behaving the expected way in different scenarios.
    - Simulating real world scenarios including QR code scanning and invalid input handling.

## Submissions: 📝✏️📈

here is the link for the main branch of the final project to access the completed code.
[GitHub Repository Link](https://github.com/SamuelSudeepAyyala/user_management/tree/main)

Here is the link to Check the DockerHub repository in which the working project with all github actions successful is deployed.
[DockerHub Repository Link](https://hub.docker.com/repository/docker/samuelsudeepayyala/user_management/general)

A detailed document in which I have mentioned my reflections and submission of the work I have gone through in the working of the project.
[Reflection Document](./IS601_Final_Project.docx)

I have worked on few QA issues that I have found in the application and 2 features I have selected from the list of features given.

### Features:
    - [👤 User Profile Management](https://github.com/SamuelSudeepAyyala/user_management/issues/9)
    - [🎫 QR Code Generation User Invites with Minio](https://github.com/SamuelSudeepAyyala/user_management/issues/3)
    Associated all the commits to the branch that I have worked on. Commited the changes to main branch only after everything is good on the feature branch.

### GitHUB Issues:
    - 🪲 [Bug Report: Error While Installing libc-bin in Docker Build](https://github.com/SamuelSudeepAyyala/user_management/issues/1)
        When building a Docker image for running FastApi then while installing the dependencies, the build fails with an error of a specific version of libc-bin. This issue is that is shown is related to package downgrade restriction.
    - 🪲 [Bug Report - UserID is being passed as None in the verification email URL ](https://github.com/SamuelSudeepAyyala/user_management/issues/5)
        When testing the verify-email API have got the bug the URL that is being formed is sending UserID as None for email send.
    - 🪲 [Bug Report - Nickname mismatch](https://github.com/SamuelSudeepAyyala/user_management/issues/6)
        When trying to creating a new user i have observed that the nickname that is being shown on the API response and the nickname that is stored on the Database are different.
    - 🪲 [Bug Report : Failure of Update User API when is_professional is passed](https://github.com/SamuelSudeepAyyala/user_management/issues/7)
        The end point Update User is failing when we try to update the User Data with the is_professional attribute. May be there is a schema mis match.
    - 🪲 [Bug Report: Null values for Github and LinkedIn URLS on update](https://github.com/SamuelSudeepAyyala/user_management/issues/8)
        Update User API is returning null values after updation for Github profile URL and LinkedIn Profile URL.
    - 🪲 [Bug Report : Vulnerabilities found on Docker Scan](https://github.com/SamuelSudeepAyyala/user_management/issues/13)
        Docker Scan has raised below issues:
        Python (python-pkg)
        ===================
        Total: 3 (HIGH: 2, CRITICAL: 1)
        ![image](https://github.com/user-attachments/assets/ff6444b0-ea6c-4d3e-94c9-e13c08aa2a8b)



## Goals and Objectives: Unlock Your Coding Superpowers 

Get ready to ascend to new heights with this legendary project:

1. **Practical Experience**: Dive headfirst into a real-world codebase, collaborate with your teammates, and contribute to an open-source project like a seasoned pro! 💻👩‍💻🔥
2. **Quality Assurance**: Develop ninja-level skills in identifying and resolving bugs, ensuring your code quality and reliability are out of this world. 🐞🔍⚡
3. **Test Coverage**: Write additional tests to cover edge cases, error scenarios, and important functionalities - leave no stone unturned and no bug left behind! ✅🧪🕵️‍♂️
4. **Feature Implementation**: Implement a brand new, mind-blowing feature and make your epic mark on the project, following best practices for coding, testing, and documentation like a true artisan. ✨🚀🎆
5. **Collaboration**: Foster teamwork and collaboration through code reviews, issue tracking, and adhering to contribution guidelines - teamwork makes the dream work, and together you'll conquer worlds! 🤝💪🌍
6. **Industry Readiness**: Prepare for the software industry by working on a project that simulates real-world development scenarios - level up your skills to super hero status  and become an unstoppable coding force! 🔝🚀🏆⚡

## Submission and Grading: Your Chance to Shine 

1. **Reflection Document**: Submit a 1-2 page Word document reflecting on your learnings throughout the course and your experience working on this epic project. Include links to the closed issues for the **5 QA issues, 10 NEW tests, and 1 Feature** you'll be graded on. Make sure your project successfully deploys to DockerHub and include a link to your Docker repository in the document - let your work speak for itself! 📄🔗💥

2. **Commit History**: Show off your consistent hard work through your commit history like a true coding warrior. **Projects with less than 10 commits will get an automatic 0 - ouch!** 😬⚠️ A significant part of your project's evaluation will be based on your use of issues, commits, and following a professional development process like a boss - prove your coding prowess! 💻🔄🔥

3. **Deployability**: Broken projects that don't deploy to Dockerhub or pass all the automated tests on GitHub actions will face point deductions - nobody likes a buggy app! 🐞☠️ Show the world your flawless coding skills!

## Managing the Project Workload: Stay Focused, Stay Victorious ⏱️🧠⚡

This project requires effective time management and a well-planned strategy, but fear not - you've got this! Follow these steps to ensure a successful (and sane!) project outcome:

1. **Select a Feature**: [Choose a feature](features.md) from the provided list of additional improvements that sparks your interest and aligns with your goals like a laser beam. ✨⭐🎯 This is your chance to shine!

2. **Quality Assurance (QA)**: Thoroughly test the system's major functionalities related to your chosen feature and identify at least 5 issues or bugs like a true detective. Create GitHub issues for each identified problem, providing detailed descriptions and steps to reproduce - the more detail, the merrier! 🔍🐞🕵️‍♀️ Leave no stone unturned!

3. **Test Coverage Improvement**: Review the existing test suite and identify gaps in test coverage like a pro. Create 10 additional tests to cover edge cases, error scenarios, and important functionalities related to your chosen feature. Focus on areas such as user registration, login, authorization, and database interactions. Simulate the setup of the system as the admin user, then creating users, and updating user accounts - leave no stone unturned, no bug left behind! ✅🧪🔍🔬 Become the master of testing!

4. **New Feature Implementation**: Implement your chosen feature, following the project's coding practices and architecture like a coding ninja. Write appropriate tests to ensure your new feature is functional and reliable like a rock. Document the new feature, including its usage, configuration, and any necessary migrations - future you will thank you profusely! 🚀✨📝👩‍💻⚡ Make your mark on this project!

5. **Maintain a Working Main Branch**: Throughout the project, ensure you always have a working main branch deploying to Docker like a well-oiled machine. This will prevent any last-minute headaches and ensure a smooth submission process - no tears allowed, only triumphs! 😊🚢⚓ Stay focused, stay victorious!

Remember, it's more important to make something work reliably and be reasonably complete than to implement an overly complex feature. Focus on creating a feature that you can build upon or demonstrate in an interview setting - show off your skills like a rockstar! 💪🚀🎓

Don't forget to always have a working main branch deploying to Docker at all times. If you always have a working main branch, you will never be in jeopardy of receiving a very disappointing grade :-). Keep that main branch shining bright!

Let's embark on this epic coding adventure together and conquer the world of software engineering! You've got this, coding rockstars! 🚀🌟✨
