# use http.client to send a GET request to the server
import http.client

serverHost = "10.0.0.114"

# create a connection to the server using serverHost and port
conn = http.client.HTTPConnection(serverHost, 6789)
# send a GET request to the server
conn.request("GET", "/HelloWorld.html")
# get the response from the server
response = conn.getresponse()
# print the status and reason of the response
print(response.status, response.reason)
print(response.read().decode())

# close connection
conn.close()