# Elucidata Asssignment

Assignment Details: [Elucidata Assignment](https://docs.google.com/document/d/1wqUXBWqtLFiFewj7jbyzLjrQ_B5HMtJpNmab5p94b-M/edit?usp=sharing)  
![File Upload](https://github.com/aritra1999/Elucidata-Asssignment/blob/master/static/AssignmentFiles/plan.png)
Dashboard | File Upload
:-------------------------:|:-------------------------:
![Dashboard](https://github.com/aritra1999/Elucidata-Asssignment/blob/master/static/AssignmentFiles/dash.png)  |  ![File Upload](https://github.com/aritra1999/Elucidata-Asssignment/blob/master/static/AssignmentFiles/dash_file.png)


## API Endpoints
### Task 1 
Endpoint: ```/task1/<file_name>/```  
Task Details: In the third column “Accepted Compound ID”, you need to filter out all the data for metabolite ids ending with:  ‘PC’, ‘LPC’ and ‘plasmalogen’, and create 3 child datasets (1 for each compound id) from the data in the input file.   
Final Files:  
```media/process1/child1_<file_name>```      
```media/process1/child2_<file_name>```      
```media/process1/child3_<file_name>```      

My approach:    
```python

def task1(file_name):
    raw_file_path = "media/raw/" + file_name
    file = str(raw_file_path)
    try:
        data = pds.read_excel(file, sheet_name='Raw Data')
    except:
        log("File Not Found")
        ProcessLog.objects.create(
            source_file=file_name,
            file_created=0,
            verdict=False,
            task=1
        ).save()
        return ('error', 'File not found!')

    child1 = []
    child2 = []
    child3 = []
    row_number = 0

    log(data.shape)
    for row in data['Accepted Compound ID']:
        try:
            comp_id = (row.split(' '))[-1]
            if comp_id == "PC":
                child1.append(data.iloc[row_number])
            elif comp_id == "LPC":
                child2.append(data.iloc[row_number])
            elif comp_id == "plasmalogen":
                child3.append(data.iloc[row_number])
        except:
            continue
            # log("Error processing row: " + str(row_number))
        row_number += 1

    log("Child Datasets Created")

    child1 = pds.DataFrame(child1)
    child2 = pds.DataFrame(child2)
    child3 = pds.DataFrame(child3)

    child1.to_excel('media/process1/child1_' + file_name , header=True, index=False)
    child2.to_excel('media/process1/child2_' + file_name , header=True, index=False)
    child3.to_excel('media/process1/child3_' + file_name , header=True, index=False)

    log("Child Datasets Saved")
    ProcessLog.objects.create(
        source_file=file_name,
        file_created=3,
        verdict=True,
        task=1
    ).save()

    return ('success', 'Task 1 successful, 3 Child Dataframes created, 3 Files created.')

```

### Task 2 
Endpoint: ```/task2/<file_name>/```  
Add a new column in the parent dataset with the name “Retention Time Roundoff (in mins)”. This column  should have rounded-off values of the corresponding retention time. Retention time should be rounded-off to the nearest natural number.   
Final File: ```media/process2/roundoff_<file_name>```   
My approach:   
```python
def task2(file_name):
    raw_file_path = "media/raw/" + file_name
    file = str(raw_file_path)
    try:
        data = pds.read_excel(file, sheet_name='Raw Data')
    except:
        log("File Not Found")
        ProcessLog.objects.create(
            source_file=file_name,
            file_created=0,
            verdict=False,
            task=2
        ).save()
        return ('error', 'File not found!')
    log(data.shape)

    data_instance = data

    retention_time_roundoff = []
    for row in data['Retention time (min)']:
        retention_time_roundoff.append(round(float(row)))

    log("Roundoff Datasets Created")

    data_instance.insert(2, "Retention Time Roundoff (min)", retention_time_roundoff)
    data_instance.to_excel('media/process2/roundoff_' + file_name, header=True, index=False)

    log("Roundoff Datasets Saved")
    ProcessLog.objects.create(
        source_file=file_name,
        file_created=1,
        verdict=True,
        task=2
    ).save()

    return ('success', 'Task 2 successful, 1 Child Dataframes created, 1 File created.')

```

### Task 3 
Endpoint: ```/task3/<file_name>/```  
After this, you should find the mean of all the metabolites which have the same "Retention Time Roundoff"  across all the samples. The result of the above operation should be a new data-frame where you have to include the "Retention Time Roundoff" column and all samples. You don't have to include columns like m/z,  Accepted Compound Id, and Retention time.  
Final File: ```media/process3/mean_<file_name>``` 
My approach:   
```python

def task3(file_name):
    roundoff_file_path = "media/process2/roundoff_" + file_name
    file = str(roundoff_file_path)
    try:
        data = pds.read_excel(file)
    except:
        log("File Not Found")
        ProcessLog.objects.create(
            source_file=file_name,
            file_created=0,
            verdict=False,
            task=3
        ).save()
        return ('error', 'File not found!')

    mean_dict = {}

    row_number = 0

    log(data.shape)

    
    for row in data['Retention Time Roundoff (min)']:
        if 0 in mean_dict.keys():
            mean_dict[row] = ((cal_mean(data.iloc[row_number][4:-1]) + mean_dic[row])/2)
        else:
            mean_dict[row] = cal_mean(data.iloc[row_number][4:-1])
        row_number += 1
    


    final_dataframe = pds.DataFrame({
        "Retention Time Roundoff (min)": mean_dict.keys(),
        "Mean": mean_dict.values()
    })
    final_dataframe.to_excel('media/process3/mean_' + file_name , header=True, index=False)


    ProcessLog.objects.create(
        source_file=file_name,
        file_created=0,
        verdict=True,
        task=3
    ).save()

    return ('success', 'Task 3 successful, 1 Child Dataframes created, 1 File created.')


```

### Process Log
Endpoint: ```/logs/```     
Displays the log of all process.
![Process Log](https://github.com/aritra1999/Elucidata-Asssignment/blob/master/static/AssignmentFiles/log.png)
