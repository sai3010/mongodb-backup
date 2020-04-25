# mongodb-backup
A solution to automate mongodb backup

# How it works 
* There is a python script ```mongo-bkp.py``` which connects to mongo db and takes mongo dump.
* After the execution of the mongo dump , it zip's the folder by appending current datetime and uploads to azure blob storage.
    * It is saved in azure blob as ```containername/date/backup_date.zip```
* It accepts following environment variables
    * ```MONGO_HOST```: Mongo host url.
    * ```MONGO_USER```: Mongo user is required if mongo is secured with user credentials
    * ```MONGO_PASS```: Mongo user's password
    * ```BACKUP_FOLDER```: Name of the root folder to be uploaded in blob storage
    * ```FILENAME```: zip folder name appended with date and uploaded under backup_folder in blob storage
    * ```CONTAINER_NAME```: Azure container name
    * ```ACCOUNT_NAME```: Azure storage account name
    * ```ACCOUNT_KEY```: Azure storage account key

# How to excecute
* ```docker pull ```
*  ```docker run --net=host --rm -e MONGO_HOST="localhost" -e BACKUP_FOLDER="test" -e FILENAME="backup" -e CONTAINER_NAME="mongo" -e ACCOUNT_NAME="data" -e ACCOUNT_KEY="Y76I9TacyJALGJLeEw2cIFw" -it mongo-azure-backup```
    * When the container is run , it connects to mongo , takes a dump and uploads to blob storage.

## Note : Preffered method of using this docker image effectively is by running it through a schedular or cron jobs
