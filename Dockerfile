# Step 1: Start with a basic Python environment
FROM python:3.11-slim

# Step 2: Set up a working directory inside the container
WORKDIR /app

# Step 3: Copy our requirements list into the container
COPY requirements.txt .

# Step 4: Install all the tools our reporter needs
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy our reporter script into the container
COPY scraper.py .

# Step 6: Tell the container what to do when it starts
CMD ["python", "scraper.py"]