FROM python:3.11
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY app.py /app
COPY path/to/model.h5 /app
CMD ["python", "app.py"]

# FROM python:3.11 It goes to Docker Hub and downloads the base image from there
# WORKDIR /app It creates a working directory within the instance, and a folder named app within the directory.
# COPY requirements.txt /app. Copies in the working directory the requirements.txt file.
# RUN pip install -r ./requirements.txt Installs all the required packages that requirements.txt file contains.
# COPY app.py /app Copies in the working directory of the file app.py which contains the model.
# CMD ["python","app.py"] Runs the app.py file using the Python image.