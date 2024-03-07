#!/bin/bash

# Stop the instances of montycoin.py running on ports 5000-5003
for port in {5000..5003}
do
    lsof -ti tcp:$port | xargs kill -9
done