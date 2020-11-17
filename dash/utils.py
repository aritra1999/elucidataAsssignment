import pandas as pds
from xlrd import *

from .models import ProcessLog

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



def log(message):
    print("[ Process LOG ] " + str(message))



def cal_mean(data_list):
    len = data_list.shape[0]
    sum = 0.0
    for ele in data_list:
        sum += ele
    return sum/len;

      