What does the Dockerfile do?
FROM python:3.10
Docker images can be inherited from other images. Therefore, instead of creating your own base image, you will use the official Python image python:3.10 that already has all the tools and packages that you need to run a Python application.

WORKDIR /app
To facilitate the running of your commands, let's create a working directory /app. This instructs Docker to use this path as the default location for all subsequent commands. By creating the directory, you do not have to type out full file paths but can use relative paths based on the working directory.

COPY requirements.txt requirements.txt
Before you run pip3 install, you need to get your requirements.txt file into your image. You can use the COPYcommand to transfer the contents. The COPYcommand takes two parameters. The first parameter indicates to the Docker what file(s) you would like to copy into the image. The second parameter indicates to the Docker the location where the file(s) need to be copied. You can move the requirements.txt file into your working directory /app.

RUN pip3 install –no-cache-dir -r requirements.txt
Once you have your requirements.txt file inside the image, you can use the RUN command to execute the command pip3 install --no-cache-dir -r requirements.txt. This works exactly the same as if you were running the command locally on your machine, but this time the modules are installed into the image.

COPY
At this point, you have an image that is based on Python version 3.10 and you have installed your dependencies. The next step is to add your source code to the image. You will use the COPY command just like you did with your requirements.txt file above to copy everything in your current working directory to the file system in the container image.

CMD ["python", "demo.py"]
Now, you have to indicate to the Docker what command you want to run when your image is executed inside a container. You use the CMD command. Docker will run the python demo.py command to launch your app inside the container.

Now that all three files have been created, let's bring in the Code Engine for building the container image.