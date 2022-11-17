# How to set up repository for Databricks
In order to integrate repositories in Databricks workspace, click under repos and go under your username.


> Working on other developer's workspace is forbidden

![](/documentation/how-tos/images/repos01.png)

> Generate personal access token in azure devops with the full access on code expiration date : (databricks-pat)

![](/documentation/how-tos/images/databricks_pat.png)

> Copy the token and store it somewhere and further use.

![](/documentation/how-tos/images/databricks_pat1.png)

> The generated token will be visible this like in azure devops

![](/documentation/how-tos/images/databricks_pat2.png)


Head over to databricks

* In the left panel, go to setting -> user settings -> git integration -> git provider should be "azure devops services (personal access token)"
then paste your user name (your email) and the token and hit save.

![](/documentation/how-tos/images/databricks_token3.png)

 * In the left panel only, Now click to repos and under your username, click on add repos.

![](/documentation/how-tos/images/databricks_addrepos.png)

 * Go to azure devops /repos click on clone and make sure you copy the https link.

![](/documentation/how-tos/images/databricks_clone_repo.png)

 * Head over back to databricks and paste the https link and rest be automatically filled up and hit create.

![](/documentation/how-tos/images/databricks_add_url.png)

How to create a new branch
* Now the main branch should be visible in datbricks, click the main branch name.

![](/documentation/how-tos/images/databricks_branch.png)

* Click on + icon and give your branch a suitable name and click on it.

![](/documentation/how-tos/images/databricks_branch1.png)

* You will see your branch is created and the same is reflected in azure devops.

![](/documentation/how-tos/images/databricks_branch2.png)

 How to pull/push
* In the same window, you will see the option of pull and push your changes.

![](/documentation/how-tos/images/databricks_push_pull.png)

 > If you get an error that the changes in remote that you don't have it, try to pull first and then push the commit the changes.

