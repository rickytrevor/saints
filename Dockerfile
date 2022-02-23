FROM python
RUN pip3 install requests
RUN pip3 install flask
RUN pip3 install waitress
RUN pip3 install wheel
RUN pip3 install flask
COPY . /src
WORKDIR /src

CMD flask run --host 0.0.0.0
