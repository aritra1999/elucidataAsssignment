# Elucidata Asssignment

Assignment Details: [Elucidata Assignment](https://docs.google.com/document/d/1wqUXBWqtLFiFewj7jbyzLjrQ_B5HMtJpNmab5p94b-M/edit?usp=sharing)  
Dashboard | File Uplaod 
![File Upload](https://github.com/aritra1999/Elucidata-Asssignment/blob/master/static/AssignmentFiles/plan.png)
Dashboard | File Upload
:-------------------------:|:-------------------------:
![Dashboard](https://github.com/aritra1999/Elucidata-Asssignment/blob/master/static/AssignmentFiles/dash.png)  |  ![File Upload](https://github.com/aritra1999/Elucidata-Asssignment/blob/master/static/AssignmentFiles/dash_file.png)


## API Endpoints
### Task 1 
Endpoint: ```/task1/<file_name>/```  
Task Details: In the third column “Accepted Compound ID”, you need to filter out all the data for metabolite ids ending with:  ‘PC’, ‘LPC’ and ‘plasmalogen’, and create 3 child datasets (1 for each compound id) from the data in the input file. 

### Task 2 
Endpoint: ```/task2/<file_name>/```  
Add a new column in the parent dataset with the name “Retention Time Roundoff (in mins)”. This column  should have rounded-off values of the corresponding retention time. Retention time should be rounded-off to the nearest natural number. 

### Task 3 
Endpoint: ```/task3/<file_name>/```  
After this, you should find the mean of all the metabolites which have the same "Retention Time Roundoff"  across all the samples. The result of the above operation should be a new data-frame where you have to include the "Retention Time Roundoff" column and all samples. You don't have to include columns like m/z,  Accepted Compound Id, and Retention time. 

### Process Log
Endpoint: ```/logs/```     
Displays the log of all process.
![Process Log](https://github.com/aritra1999/Elucidata-Asssignment/blob/master/static/AssignmentFiles/log.png)
