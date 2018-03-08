# product_api
Product Api built with python, flask

Python Software Developer Code Test
For this API the following programs and python modules need to be installed, ideally in a virtual environment:

Python
pip
pandas
numpy
Flask
requests
json

To run the code simply go in the command line to product_api/src and type python main.py
This will display the linw
"Geting data from sources", and "Done" when finished.
It will then display that the server is running and will give an address:
  Running on http://127.0.0.1:5002/ (Press CTRL+C to enter)

In main.py there is a commented out function one_endpoint(): (an app route) that reads in json from a http request
{ "id":"xxx"}. The result is available at the url http://127.0.0.1:5002/id


The uncommented function api_users(id_str) allows many endpoints and the user has to type the id they are searching for into the url.
for example the url http://127.0.0.1:5002/6403465 will return the json for the product with that specific id (and a message if it doesn't exist)

Happy "API-ing"
![Alt Text](giphy.gif)
