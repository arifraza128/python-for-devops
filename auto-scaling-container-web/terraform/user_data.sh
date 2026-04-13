#!/bin/bash
yum update -y
yum install -y docker
service docker start

docker run -d -p 80:5000 ${docker_image}
