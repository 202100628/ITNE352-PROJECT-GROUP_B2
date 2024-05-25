ITNE 352 Group B2
--- 
Multithreaded News Client/Server Information System 
Project Overview
This project is part of the Network Programming course (ITNE352) at the University of Bahrain. It involves creating a client-server system to retrieve and display current news. The focus is on client/server architecture, network communication, multithreading, and API integration, with an emphasis on good coding practices.
 Table of Contents:
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

Features:
- Client/Server Architecture: The project includes a server capable of handling multiple clients simultaneously.
- Multithreading: The server supports at least three concurrent connections.
- API Integration: The server fetches news from [NewsAPI.org](https://newsapi.org/).
- User-friendly Client: The client script offers an interactive menu for users to request news based on keywords, categories, or countries.
- Data Management: Retrieved data is saved in JSON files for evaluation purposes.


Technologies Used:
•	Python
•	Socket Programming
•	Multithreading
•	JSON
•	RESTful API

Installation:
1.	Clone the repository:
‘’’bash
git clone https://github.com/Maryaam/group-B2.git
cd group-b2
2.	Navigate to the project directory:
‘’’bash
cd news-client-server
Install the required packages:
‘’’bash
pip install -r requirements.txt
Usage
1.	Start the server:
‘’’bash
python server.py 
‘’’
2.	Start the client:
‘’’bash
python client.py 
‘’’
3.	Follow the on-screen instructions in the client menu to request news.

Project Structure
•	server.py: Manages client connections, fetches news data from the API, and handles client requests.
•	client.py: Connects to the server, sends requests, and displays results to the user.
•	ITNE352-PROJECT-GROUP-B2_Aysha_get_news. json: Sample JSON data file with retrieved news articles for testing.
Contributing:
1.	Fork the repository.
2.	Create a new branch (git checkout -b feature/your-feature).
3.	Commit your changes (git commit -am 'Add some feature').
4.	Push to the branch (git push origin feature/your-feature).
5.	Create a new Pull Request.
License:
This project is licensed under the MIT License.
Contact:
•	Instructor: Dr. Mohammed Almeer (malmeer@uob.edu.bh)
•	Team Members:
•	Member 1: 202100628@stu.uob.edu.bh
•	Member 2: 202100815@stu.uob.edu.bh

