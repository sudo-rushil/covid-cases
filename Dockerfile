FROM python
COPY . /usr/src/
WORKDIR /usr/src/
RUN apt-get update && apt-get clean
RUN make install
EXPOSE 8080
