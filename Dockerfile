# image (debian)
FROM python:3.13-slim

# changing directory to /app
WORKDIR /app

# copying dependencies
COPY requirements.txt .

# RUN running commads when building image
# installing dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copying whole project
COPY . .

# compiling static
RUN python WorldITSocialNetwork/manage.py collectstatic --noinput

# expose port to reach app
EXPOSE 8000

# CMD running commads when running image
# running project
CMD ["python", "WorldITSocialNetwork/manage.py", "runserver", "0.0.0.0:8000"]