#!/bin/bash

#Uses the Open weather api to get json data and extract the temerature part of it

echo "Enter the city name : "
read city

#City names involving whitespaces pose a problem in the url so the whitespacs needs to be replaced with %20 so the url query is passed without problems
city=${city// /'%20'}

data=$(curl -s "https://api.openweathermap.org/data/2.5/weather?q=$city&appid=4a9fa4138744420bacdfc4e4e1553ddd&units=metric" | jq '.main.temp')


echo "The temperature in $city is $data degrees Celsius."


