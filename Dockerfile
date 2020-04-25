FROM python:3.6-slim
ADD mongo-bkp.py /
RUN apt-get update --fix-missing && pip install requests
RUN apt-get -y install mongo-tools curl zip && curl -sL https://aka.ms/InstallAzureCLIDeb | bash
CMD python mongo-bkp.py