FROM python:3.6-alpine
MAINTAINER Daniel Kurniadi "daniel.thekurniadi@gmail.com"

# always upgrade pip version
RUN pip install -U pip

# prepare library dependency of the application
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt

####################################### ENVIRONMENT VARIABLE ######################################
# Application level
ARG PORT
ENV PORT=$PORT
ARG HOST
ENV HOST=$HOST
ARG DEBUG
ARG ENV
ENV DEBUG=$DEBUG
ENV PYTHONUNBUFFERED=1
# Run the application
EXPOSE ${PORT}
CMD ["python", "run.py"]
