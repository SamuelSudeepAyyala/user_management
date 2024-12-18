
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

here is the link for the main branch of the final project to access the completed code.<br>
[GitHub Repository Link](https://github.com/SamuelSudeepAyyala/user_management/tree/main)

Here is the link to Check the DockerHub repository in which the working project with all github actions successful is deployed.<br>
[DockerHub Repository Link](https://hub.docker.com/repository/docker/samuelsudeepayyala/user_management/general)

A detailed document in which I have mentioned my reflections and submission of the work I have gone through in the working of the project.<br>
[Reflection Document](./IS601_Final_Project.docx)

I have worked on few QA issues that I have found in the application and 2 features I have selected from the list of features given.

### Features:
- [👤 User Profile Management](https://github.com/SamuelSudeepAyyala/user_management/issues/9)<br>
- [🎫 QR Code Generation User Invites with Minio](https://github.com/SamuelSudeepAyyala/user_management/issues/3)<br>
    Associated all the commits to the branch that I have worked on. Commited the changes to main branch only after everything is good on the feature branch.

### GitHUB Issues:
- 🪲 [Bug Report: Error While Installing libc-bin in Docker Build](https://github.com/SamuelSudeepAyyala/user_management/issues/1)<br>
    When building a Docker image for running FastApi then while installing the dependencies, the build fails with an error of a specific version of libc-bin. This issue is that is shown is related to package downgrade restriction.
- 🪲 [Bug Report - UserID is being passed as None in the verification email URL ](https://github.com/SamuelSudeepAyyala/user_management/issues/5)<br>
    When testing the verify-email API have got the bug the URL that is being formed is sending UserID as None for email send.
- 🪲 [Bug Report - Nickname mismatch](https://github.com/SamuelSudeepAyyala/user_management/issues/6)<br>
    When trying to creating a new user i have observed that the nickname that is being shown on the API response and the nickname that is stored on the Database are different.
- 🪲 [Bug Report : Failure of Update User API when is_professional is passed](https://github.com/SamuelSudeepAyyala/user_management/issues/7)<br>
    The end point Update User is failing when we try to update the User Data with the is_professional attribute. May be there is a schema mis match.
- 🪲 [Bug Report: Null values for Github and LinkedIn URLS on update](https://github.com/SamuelSudeepAyyala/user_management/issues/8)<br>
    Update User API is returning null values after updation for Github profile URL and LinkedIn Profile URL.
- 🪲 [Bug Report : Vulnerabilities found on Docker Scan](https://github.com/SamuelSudeepAyyala/user_management/issues/13)<br>
    Docker Scan has raised below issues:
    Python (python-pkg)
    Total: 3 (HIGH: 2, CRITICAL: 1)
- 🪲[Bug Report : New User create failure SMTP connection failure](https://github.com/SamuelSudeepAyyala/user_management/issues/16)<br>
    Connection closure while sending email on user creation with below logs<br>
    ```
    fastapi-1 | ERROR:root:Failed to send email: Connection unexpectedly closed
    fastapi-1 | INFO: 192.168.16.6:34546 - "POST /register/ HTTP/1.0" 500 Internal Server Error
    ```

I have added Test Cases to increase the coverage to cover edgr cases and error scenarios which may be unexpected.🕵️‍♂️
