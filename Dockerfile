##  Step 1: Use an official Python base image
FROM python:3.11-slim

##  Step 2: Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

##  Step 3: Set working directory
WORKDIR /app

##  Step 4: Copy project files
COPY . /app/

##  Step 5: Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

##  Step 6: Expose port
EXPOSE 8000

## Step 7: Run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
