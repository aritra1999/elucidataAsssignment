import pandas as pds
from xlrd import *

from .models import ProcessLog

def task1(file_name):
    raw_file_path = "media/raw/" + file_name
    file = (raw_file_path)
    data = pds.read_excel(file, sheet_name='Raw Data')

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

    child1.to_excel('media/process1/' + file_name + '_child1.xlsx', header=True, index=False)
    child2.to_excel('media/process1/' + file_name + '_child2.xlsx', header=True, index=False)
    child3.to_excel('media/process1/' + file_name + '_child3.xlsx', header=True, index=False)

    log("Child Datasets Saved")
    ProcessLog.objects.create(
        source_file=file_name,
        file_created=3,
        verdict=True,
        task=1
    ).save()



def task2(file_name):
    raw_file_path = "media/raw/" + file_name
    file = (raw_file_path)
    data = pds.read_excel(file, sheet_name='Raw Data')
    log(data.shape)

    data_instance = data

    retention_time_roundoff = []
    for row in data['Retention time (min)']:
        retention_time_roundoff.append(round(float(row)))

    log("Roundoff Datasets Created")

    data_instance.insert(2, "Retention Time Roundoff (min)", retention_time_roundoff)
    data_instance.to_excel('media/process2/' + file_name + '_roundoff.xlsx', header=True, index=False)

    log("Roundoff Datasets Saved")
    ProcessLog.objects.create(
        source_file=file_name,
        file_created=1,
        verdict=True,
        task=2
    ).save()


def task3(file_name):
    raw_file_path = "media/raw/" + file_name
    file = str(raw_file_path)
    data = pds.read_excel(file, sheet_name='Raw Data')
    log(data.shape)


def log(message):
    print("[ Process LOG ] " + str(message))
