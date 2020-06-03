FROM python:3
COPY . /my_project
WORKDIR /my_project
RUN pip3 install --upgrade setuptools
RUN pip3 install pysimplegui
EXPOSE 3333
CMD [ "python", "./main0.2.py"]


