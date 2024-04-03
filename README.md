Second oblig from course DATA2410 Networking and cloud computing

<h1>Task 1</h1>
This is a web server that handles one HTTP request at a time.
To run the file you type <code>python3 task1.py</code></br>

![Server running](Task1_server.png)</br>
Go to your browser and open localhost:8000 og localhost:8000/index.html to view the index page </br>

![File found](Task1_localhostWorks.png)
Image showing when localhost find index.html file

If you try to find a file that is not in the directory you will se a 404 Not Found message in the browser.

![File Not Found](Task1_localhostWrongFile.png) Image showing the result then localhost:8000/index.html is removed. Also works if you type wrong file-name localhost:8000/indexx.html

<h1>Task 2</h1>
Task 2 is a HTTP client that can connect to the server with TCP connection. The client send a HTTP request to the server and display the response in the terminal. The client takes command line arguments specifying server IP address/hostname, the port the server is listening and the path to the requested file with the required command format <code>python3 client.py -i server\_ip -p server\_port -f filename</code>
</br></br>
To run the client type into the terminal:</br>
<code>python3 task2.py -i 127.0.0.1 -p 8000 -f /index.html</code></br></br>

![Terminal showing response messages](Task2.png)<br>
Image showing the client run with both responses

<h1>Task 3</h1>
This is a multithreades server that is capable of serving multiple request simultaneously.



