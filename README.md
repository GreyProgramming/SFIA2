# Prideinyourself.com
V1.1

## The brief

To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.

### Required:
>	A Trello board (or equivalent Kanban board tech) with full expansion on user stories, use cases and tasks needed to complete the project. It could also provide a record of any issues or risks that you faced creating your project.

>	A relational database used to store data persistently for the project, this database needs to have at least 2 tables in it, to demonstrate your understanding, you are also required to model a relationship. 

>	Clear Documentation from a design phase describing the architecture you will use for you project as well as a detailed Risk Assessment.

>	A functional CRUD application created in Python, following best practices and design principles, that meets the requirements set on your Kanban Board 

>	A functioning front-end website and integrated API’s, using Flask.

>	Code fully integrated into a Version Control System using the Feature-Branch model which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.

<>	Fully designed test suites for the application you are creating, as well as automated tests for validation of the application. You must provide high test coverage in your backend and provide consistent reports and evidence to support a TDD approach.

## The concept

I have been sat on the domain prideinyourself.com for over a year, with a plan to do *something* with it, though that plan has changed and evolved as I have started to work on other projects.

As such, I plan to create a resource which houses stories about historical LGBTQ+ figures there so that teens are able to quickly and easily find examples of role models.

## The architecture

For this project, I will be running a Virtual Machine (VM) via google cloud platform.

This VM will be running Debian Linux, and from there I will be programming the webpages in html, which will be calling python functionality to talk to SQL.

The programs and python modules used are all stored in <a href="https://github.com/GreyProgramming/flask-app/blob/master/requirements.txt">the requirements.txt doc</a>

## Risk assessment

The risk assessment document is available at:
https://docs.google.com/spreadsheets/d/12DpUkGZ0152ZuV0DZSnLNX3tmoqrbppeXTm1YRkpS1k/edit?usp=sharing

17/02/2020 - Numerous system crashes including both chrome and BSODs.
https://drive.google.com/file/d/1A9-sd0B1qiLT1Zj9ty1mQqaGHmKYDdgI/view?usp=sharing

<!-- ## Stakeholder analysis

The stakeholder analysis document is available at:
https://docs.google.com/document/d/11yscW6LF6Znjg37G4HJLpUCfrppOapm-UVRhJOHsnOI/edit?usp=sharing
-->
## ERD

The ERD was created using draw.io is available at:
https://drive.google.com/file/d/11u3hhtPX3J5yBtt9x3uxw0sZ7yX8f5mE/view?usp=sharing

17/02/2020 update:

Updated ERD generated: https://drive.google.com/file/d/1OHQjoHsLBJ4SMFNm69zsRSY3vFUwKZDn/view?usp=sharing

## Trello

The trello board for the project is available at:
https://trello.com/b/wRzLUNag/prideinyourselfcom



### Future possibilities
Lesson Plans - "Like for schools to use, if you make it user friendly teachers would use that kind of thing for gay pride month as it's on the curriculum" - C.L-C
Promotion via content creators by hosting links to their work - pivot with stonewall, podcasts & unions.


### Update Log

21/02/2020
Port 5000 requirement removed - http://prideinyourself.com

Testing script failing due to chrome driver not being able to read the Xpath. As a result, unable to perform tests and deploy then to Jenkins. 

20/02/2020
Actual functionality implemented. CSS cleaned up, redundant code removed, functionality manually tested.

18/02/2020
Users able to create account, read their name and email, update those details and delete their account. MVP attained.
Progress branch pulled to master.

17/02/2020 
Changed the layout.html for better visuals.
Created a new footer linking to linkedin.
Url now points to VM when running: http://prideinyourself.com:5000/home

Noted need to change the CSS as the CSS link provided by Bob is not able to create the visuals wanted.
Need to check whether there is a print function in the home page as it is printing in the console whenever loaded.
Need to alter users table for admin column + allow admins to delete posts from users as they are actioned.
