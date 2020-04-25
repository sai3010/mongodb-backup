import os,subprocess,datetime,json,requests

def create_bkp():
    try:
        if os.environ.get('MONGO_HOST',None):
            if os.environ.get('MONGO_USER',None) and os.environ.get('MONGO_PASS',None):
                query = "mongodump -h"+os.environ['MONGO_HOST'] +" -u "+os.environ['MONGO_USER']+" -p " +os.environ['MONGO_PASS']
            else:
                query = "mongodump -h"+os.environ['MONGO_HOST']
            cur_date = datetime.datetime.now().strftime("%d-%m-%y")
            cur_time = datetime.datetime.now().strftime("%H:%M:%S")
            file_name = os.environ['FILENAME']+"_"+cur_date+"_"+cur_time+".zip"
            res = os.system(query)
            if res ==0:
                os.system("zip -r "+file_name+" dump")
                upload_bkp(file_name,cur_date)
            else:
                print("Error while creating mongo backup")
        else:
            print("No host")
    except Exception as e:
        print(e)

def upload_bkp(file_name,cur_date):
    try:
        query = "az storage blob upload --container-name "+os.environ['CONTAINER_NAME']+" -f "+file_name+" --name "+os.environ['BACKUP_FOLDER']+"/"+cur_date+"/"+file_name+" --account-name "+os.environ['ACCOUNT_NAME']+" --account-key "+os.environ['ACCOUNT_KEY']
        upstatus = os.system(query)
        if upstatus == 1:
            os.system("rm "+file_name+" && "+ "rm -rf dump")
        else:
            print("Upload failed")
    except Exception as e:
        print("Error: "+str(e))

create_bkp()      