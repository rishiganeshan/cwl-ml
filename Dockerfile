FROM tensorflow/tensorflow:latest

RUN apt-get update && \
    apt-get install -y curl gnupg

RUN echo "deb http://storage.googleapis.com/tensorflow-serving-apt stable tensorflow-model-server tensorflow-model-server-universal" | tee /etc/apt/sources.list.d/tensorflow-serving.list && \
    curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-serving.release.pub.gpg | apt-key add -

RUN apt-get update && \
    apt-get install -y tensorflow-model-server

RUN pip install --no-cache-dir requests matplotlib

COPY serve_model.py /serve_model.py
COPY make_requests.py /make_requests.py

CMD ["bash"]
