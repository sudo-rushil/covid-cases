FROM continuumio/miniconda3
COPY . /usr/src/
WORKDIR /usr/src/
RUN apt-get update && apt-get clean
RUN make install
EXPOSE 5050 8080
CMD make run
