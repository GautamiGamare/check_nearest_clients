# check_nearest_clients
In this project we can check the nearest clients from particular locations.
In this project we can see 11 locations . If we click one location we can able to see 100 nearest clients from that particular location.
Here I have installed geopy. From there I got geocode,latitude and longitude of all locations as well as clients.
I had all clients details in tsv file. I open that tsv file into exel and then using django-import-export I imported that data into database.
Here I have used sqlite database to store the data.
Then by using geodesic I got proper distance of each client from perticular locations.
I saved that data into database.
In this way using python,geopy we can get nearest clients details and their distance from particular locations.
