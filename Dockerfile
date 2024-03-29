ARG OPENAI_API_KEY
ARG SEVER_IP

FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apt update && apt install -y libsndfile1
RUN apt-get update && apt-get upgrade -y

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Set up a new user named "user" with user ID 1000
RUN useradd -m -u 1000 user

# Switch to the "user" user
USER user

# Set home to the user's home directory
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH \
    OPENAI_API_KEY=$OPENAI_API_KEY \
    SEVER_IP=$SEVER_IP 


# Set the working directory to the user's home directory
WORKDIR $HOME/app

# Copy the current directory contents into the container at $HOME/app setting the owner to the user
COPY --chown=user . $HOME/app

RUN mkdir audio

RUN pip install --force-reinstall soundfile

ENV GRADIO_SERVER_NAME=0.0.0.0

EXPOSE 7860

CMD ["python", "src/app2.py"]