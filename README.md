Dockerized Python Web Scraper 
A simple, containerized Python script that scrapes the title of a website. This project serves as a basic introduction to running Python applications within a Docker container.

Description
This project contains three key files:

scraper.py: A Python script that uses the requests and BeautifulSoup libraries to fetch the HTML from http://example.com and print its <title>.

requirements.txt: A list of Python dependencies required by the script.

Dockerfile: A set of instructions to build a Docker image containing the Python environment and the scraper script.

The goal is to package the Python script into a self-contained, portable Docker image that can be run on any machine with Docker installed, without needing to set up a Python environment manually.

Prerequisites
You must have Docker installed on your system.

Install Docker

How to Run
Follow these steps to build the Docker image and run the container.

Clone the Repository
If this project is on a platform like GitHub, clone it. Otherwise, just make sure you are in the project directory containing the Dockerfile.

Bash

git clone <your-repository-url>
cd <your-repository-name>
Build the Docker Image
Open your terminal in the project's root directory and run the following command. This will create a Docker image named python-scraper based on the instructions in the Dockerfile.

Bash

docker build -t python-scraper .
Run the Docker Container
Once the image is built, run it as a container. The container will start, execute the scraper.py script, print the output, and then stop.

Bash

docker run python-scraper
Expected Output
You should see the following output in your terminal:

The title of the page is: 'Example Domain'
