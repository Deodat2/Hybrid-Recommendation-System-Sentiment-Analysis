# 1. We start from a lightweight Python image
FROM python:3.9-slim

# 2. We define the working directory in the container
WORKDIR /app

# 3. We copy the dependencies file
COPY requirements.txt .

# 4. We are installing the libraries
RUN pip install --no-cache-dir -r requirements.txt

# 5. We copy everything else (your code and your .pkl files)
COPY . .

# 6. We expose the port that FastAPI uses
EXPOSE 8000

# 7. The command to start the API when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]