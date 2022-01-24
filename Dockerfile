FROM python
RUN pip3 install requests
RUN pip3 install flask
RUN pip3 install waitress
RUN pip3 install wheel
RUN pip3 install flaskr-1.0.0-py3-none-any.whl

COPY . /src
WORKDIR /src

CMD python3 santi.py
