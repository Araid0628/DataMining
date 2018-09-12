import csv
import pandas as pd
# camp = pd.read_csv(r"E:\nlp\week2\abc.csv", encoding='gbk')

def loadData():
    dataMat = []
    with open(r"E:\nlp\week2\abc.csv", encoding='gbk') as fr:
        csv_reader = csv.reader(fr)
        data_list = list(csv_reader)
    return data_list

def cleanData(csv_data):
    splitList = []
    temp = ''
    for i in range(len(csv_data)):
        temp = str(csv_data[i]).strip("[").strip("]").strip("'").strip().replace("????", "")
        splitList.append(temp.split("。"))
    return splitList

def writeList2CSV(myList,filePath):
    try:
        file=open(filePath,'w')
        for items in myList:
            for item in items:
                file.write(item)
                file.write(",")
            file.write("\n")
    except Exception :
        print("数据写入失败，请检查文件路径及文件编码是否正确")
    finally:
        file.close();

def main():
    csv_data = loadData()
    splitList = cleanData(csv_data)
    filePath = r"E:\nlp\week2\final.csv"
    writeList2CSV(splitList, filePath)

if __name__ == "__main__":
    main()
