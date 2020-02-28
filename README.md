"# SFIA2" 

## The Brief:
Create an application that generates “Objects” upon a set of predefined rules.  These “Objects” can be from whatever domain you wish.

You are required to create a micro-service orientated architecture for your application, this application must be composed of at least 4 services that work together:

1) The core service – this will render the Jinja2 templates you need to interact with your application, it will also be responsible for communicating with the other 3 services, and finally for persisting some data in an SQL database.
2/3) These will both generate a random “Object”, this object can be whatever you like as we encourage creativity in this project.
4) This service will also create an “Object” however this “Object” must be based upon the results of service #2 + #3 using some pre-defined rules.

### Scope 
**The requirements of the project are as follows: **

> An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.   
  *This could also provide a record of any issues or risks that you faced creating your project. /*
  
> An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.   
  *If a change is made to a code base, then Web hooks should be used so that Jenkins recreates and redeploys the changed application/* 
  
> The project must follow the Micro Services architecture that has been asked for. 

> The project must be deployed using containerisation and an orchestration tool.

> As part of the project you need to create an Ansible Playbook that will provision the environment that your application needs to run.

### Constraints
1) Kanban Board: Asana or an equivalent Kanban Board 
2) Version Control: Git 
3) CI Server: Jenkins 
4) Configuration Management: Ansible
5) Cloud server: GCP virtual machines 
6) Containerisation: Docker 
7) Orchestration Tool: Docker Swarm 

## The concept
A 'Life Simulator' text game.

There is a game I have been playing for a couple of years called 'Money Race 2'

I have always been a little upset about how the numbers don't align with real life scenarios, and so I would like to program an analogue which performs the same functions but with a text interface.

## Draft idea

___Service 1___
The basic website with register/login functionality. Service 2 available as standars, service 3 behind login wall.

___Service 2/3___

A page where you have the option to either create a player profile or have one randomly generated. This will set your income and expenses.

Button for random event which will pull back a random event in a table:

Rolls:
1 - Category
1) Dayjob
2) Surprise expense
3) Surprise gift
4) Investment opportunity
5) 'Charity'

for 1-4, each will have 25 things that could happen,which will effect the amount of money that is in player 'account'.

The aim of the game is to get enough investments that the monthly return is over 100% of the monthly expenses on top of money coming in from day job.

___Service 4___


## Kanban
For this project I elected to use airtable, and contained the risk register in the project board there.
This can be viewed at: https://airtable.com/shrBM6xlxHXKH4AWA
The reason for this is that flexibility with regards to the layout, the ease of use and the mobile interface.
The downside to this one is that it can't be accessed when offline.

## Docker diagram

## ERD diagram


