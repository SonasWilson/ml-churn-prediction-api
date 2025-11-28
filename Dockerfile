# Step 1: Start from a Python image
FROM python:3.12-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy the rest of the project
COPY . .

# Step 5: Expose the port FastAPI will run on
EXPOSE 8000

# Step 6: Run the API
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
