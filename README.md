# Overview

<TODO: complete this with an overview of your project>

## Project Plan
<DONE: Project Plan

* A link to a Trello board for the project
- https://trello.com/b/tZuUaiyV/azure-cicd
* A link to a spreadsheet that includes the original and final project plan>
- ![excel](project-management-template.xlsx)

## Instructions

<DONE:  
* Architectural Diagram (Shows how key parts of the system work)>
![image](Azure achitectural diagram)

<DONE:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:
 
- firstly clone the project in Github using git clone https://github.com/JorelJordan/Azure-BuildingCI-CD
- create the the virtual environment using
python -m venv ~/.myrepo
source ~/.myrepo/bin/activate
- run `make all` to make the fles.
- Then open the https://ci-cd-appservice.azurewebsites.net
* Project running on Azure App Service
![image](Azure azuredployed)
* Project cloned into Azure Cloud Shell
![image](cicdclone)

* Passing tests that are displayed after running the `make all` command from the `Makefile`
![image](makeall)
* Output of a test run
![image](testpassed)
* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).
![image](Azure azuredployed)
* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction ![image]
(Azure azuredployed)from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```
![image](makeprediction)



## Enhancements

<DONE: A short description of how to improve the project in the future>
It will be good to add more lessons on deploying the app with pipelines to give more details to the student
## Demo 

<TODO: Add link Screencast on YouTube>
- https://youtu.be/cVZ4JyGnLco


