# Important information for Deadline 1


:bangbang:&nbsp;&nbsp;**This chapter should be completed by Deadline 1** *(see course information at [Lovelace](http://lovelace.oulu.fi/ohjelmoitava-web/ohjelmoitava-web/))*

---
<details>
<summary>
:bookmark_tabs:&nbsp;&nbsp;<strong>Chapter summary</strong>
</summary>

<bloquote>
This chapter must provide a good overview of the Web API that your group is going to develop during the course, and some insight into the (imaginary) microservice architecture it will be a part of. You should not focus in implementation aspects such as database structure,  interfaces or the request/responses formats. We recommend that you look into existing APIs (see Related work below) before writing the description for your own API.

<h3>Chapter GOALS:</h3>
<ol>
<li>Understand what is an API</li>
<li>Describe the project topic API</li>
<li>Describe how the API would be used as part of a larger architecture</li>
</ol>
</bloquote>

</details>

---

<details>
<summary>
:heavy_check_mark:&nbsp;&nbsp;&nbsp;&nbsp; <strong>Chapter evaluation (max 5 points)</strong>
</summary>

<bloquote>
You can get a maximum of 5 points after completing this Chapter. More detailed evaluation is provided in the evaluation sheet in Lovelace.
</bloquote>

</details>

---

# RESTful API description
## Overview
<details>
<summary>
:bookmark_tabs:&nbsp;&nbsp;<strong>Content that must be included in the section</strong>
</summary>

<bloquote>

Describe the API you are going to implement. Also describe the larger imaginary architecture that would exist around that API - while you do not need to implement these other components, they will be helpful in imagining context for your API. Your API will be a component that stores, and offers an interface to, some important data in the larger ecosystem. Think about a larger system, and then take out one key piece to examine - this will be your API.

Describe the API briefly and comment what is the main functionality that it exposes. Focus in the API not in any specific application that is using this API. Take into account that in the end, a WEB API is an encapsulated functionality as well as the interface to access that functionality. Remember that your API is just one part of a larger machine. It does not need to do everything. There will be other components in the system to do those things. This course focuses on creating a small API in detail - thinking too big from the start will drown you in work later. 

A really short version of an overview for the RESTful Web API could be: 

<em>“The discussion forum Web API offers different functionalities to structure non-real-time conversations among the people of a group about topics they are interested in certain topic. Messages are grouped in Threads, that at the same time are grouped in Topics. The messages are accessible to anyone, but posts can only be created by providing credentials of a registered user [...] This API could exist as part of an online learning environment system where it is responsible for offering discussion forum features that can be included in other components of the learning environment. For example, a programming task (managed by a different component) can include its own discussion board managed by the discussion forum API[...]“</em>

</bloquote>

</details>

---

:pencil2: This application provides API endpoints that allow users to monitor and analyze log files for anomalies or signs of malicious attacks. It uses advanced natural language processing techniques to identify patterns in log data and flag potential security threats. The API can be easily integrated into existing systems, making it an efficient and convenient solution for organizations to secure their log data. The application is user-friendly, scalable and provides real-time insights, making it a comprehensive tool for enhancing log security. The LogBot web API offers functionalities that aim to provide a more effective tool for security developers and analysts working on web applications. The primary motivation of the API is to allow developers to get data that matters to them immediately and without the need to perform complex analytics and coding. The API abstracts away the complex logic related to machine learning algorithms and provides an easy to use chat-bot that answers queries related to the log-files.The API endpoints created provide the following functionality:Upload log filesThis endpoint allows the developer to upload their files to the backend server for analysis via ML algorithms. The api returns a summary of the log files uploaded and contains relevant information regarding the required statistics (security, visits, etc) Query log filesThis endpoint allows the developer to query specific segments from the log data file itself. The API endpoint returns the relevant segments from the file to the user. The queries can be used to perform analysis on specific segments of the log file if needed Query Feedback SummaryThis endpoint works to further expand upon the feedback provided by our API on uploaded log files. The user can query, extract and manipulate the feedback returned by the other API via this API endpointThis API could exist as a tool in use by security analyst groups, to aid them in finding vulnerabilities, malicious actions/actors, log trails of malicious behavior, usage patterns, possible logical flaws and a host of other potential vulnerabilities that as of yet remain hidden. This application can potentially be used to pre-emptively stop malicious actions before they happen as well as providing additional support in creating a more secure and protected system.

---


## Main concepts and relations
<details>
<summary>
:bookmark_tabs:&nbsp;&nbsp;<strong>Content that must be included in the section</strong>
</summary>

<bloquote>
<strong>Define</strong> the <strong>main concepts</strong> and describe the <strong>relations</strong> among them textually. Roughly, a concept is a real-world entity that is expected to be of interest to users or other services. This section will be a guideline for choosing your resources to implement in Deadline 3. Students should remember that some of the concepts might not be a resource by themselves, but just a part of it (resource property). In this section, students should not describe the RESTful resources, but identify which are the main ideas of the API. Do not forget to include the relations among the concepts.

A description of the main concepts for the Forum API could be: 

<em>"The API permits users send messages. The forum contains a list of categories and a list of users. Each category specifies a name, a description and a thread. A thread is [...]The forum may contain 0 or more categories… Each category may have 0 or more threads… Users can write and read messages to a forum thread. A user has a profile, basic information, activity information (stores, for instance, all the messages sent by a user, the messages marked as favorites). [...]The user history contains information of the last 30 messages sent by the user.[…]"</em>

Include a diagram which shows the relations among concepts.

This section is important because it outlines the concepts that you will later implement. In particular, the diagram defined here will follow you throughout the project report and you will be adding more details to it. 


</bloquote>

</details>

---

:pencil2: The API's allows the user to upload data and ask interactive questions to the chatbot based on the user's uploaded file. The user can upload multiple files to the platform/Chatbot, and they should be with distinct names. All uploaded files are saved as historical data by indexing it to a database at the backend. The user can ask questions about the previously uploaded files specifying the file name. The user's previous conversation is saved and can be referred back. The user is allowed to make a "small talk" with chatbot API and share relevant insights.The API would use the log file data as input and provide a response based on the group's queries. 

Below diagram explains the overall flow:
![image](https://user-images.githubusercontent.com/34895097/215592972-d46d1a64-b780-4371-bcf0-abcc55d6e868.png)


---

## API uses
<details>
<summary>
:bookmark_tabs:&nbsp;&nbsp;<strong>Content that must be included in the section</strong>
</summary>

<bloquote>
Describe at least one client and one service that could use your Web API. You must explain here what is the functionality provided by the client/service, and how it uses the Web API to implement this functionality. 
</bloquote>

</details>

---

:pencil2: A security analyst group working for a financial organization could use the Web API to analyze log files from their network security devices, such as firewalls, intrusion detection systems, and routers. The group could upload log files to the API and use its natural language processing capabilities to ask questions about the log data. For example, the group could ask questions like "What are the most frequent attack types in the log file?", "What is the distribution of log events by severity?", or "What is the origin of the most severe attacks?". The API's ability to process and analyze large amounts of log data in real-time would allow the group to quickly and efficiently identify anomalies and potential security threats. As mentioned before, the group could upload multiple log files to the API, each with a distinct name, and refer to the previously uploaded files in their queries. The API would save all uploaded files as historical data in a database, allowing the group to refer back to previous conversations and easily compare the results from different log files. In this use case, the Web API serves as a log analysis tool for the security analyst group, allowing them to quickly and easily analyze log data from their network security devices and make data-driven decisions to improve the security of their network.



## Related work
<details>
<summary>
:bookmark_tabs:&nbsp;&nbsp;<strong>Content that must be included in the section</strong>
</summary>

<bloquote>
Find at least one API that resembles the functionality provided by yours. Explain in detail the functionality provided by the API. Classify the API according to its type (RPC, CRUD REST, pure REST, hypermedia driven ...) justifying your selection. Provide at least one example client that uses this API.

The purpose of this task is to get more familiar with what an API is. This will be helpful in describing your own API. Therefore, it is recommended to do this section after you have decided the topic of your project but before writing your API description.
</bloquote>

</details>

---



:pencil2: We would be using CRUD RESTFul API's for this framework. CRUD REST API (Create, Read, Update, Delete Representational State Transfer Application Programming Interface) is a commonly used design pattern for implementing web services. A CRUD REST API provides a way to create, read, update and delete log data entries in a log summarization project through the use of HTTP methods (POST, GET, PUT and DELETE).  The API allows for efficient storage, retrieval, updating, and deletion of summarized log data for analysis. A CRUD REST API is a valuable tool in log summarization projects. This type of API provides a standardized interface for accessing log data, making it easier to integrate with other systems and tools. This standardization helps to streamline data management, making it more efficient to retrieve the data needed for analysis. The security of log data is also improved with a CRUD REST API. Only authorized users are granted access to the data, which reduces the risk of data breaches and unauthorized access. In terms of ease of integration, the CRUD REST API is widely adopted and has strong support in many programming languages. This makes it easy to integrate with other systems and tools, ensuring a seamless process for log data analysis. The standardization and ease of integration of a CRUD REST API help to make log data analysis a more streamlined process.

---


## Resources allocation
|**Task** | **Student**|**Estimated time**|
|:------: |:----------:|:----------------:|
|API provided to upload log files + Python-flask framework| Talha_Zeeshan| Basic - 6/3/2023, final - 27/3/2023| 
|API provided to access/download summary + Database|Kazi_Haque| Basic - 13/2/2023, Final - 27/3/2023| 
|API provided to query summary + UI |justin_seby| Basic - 6/3/2023, final - 1/5/2023| 
|API provided to query uploaded file or small talk + Analysis and generation algorithm| Prasasthy_Balasubramanian|Basic - 6/3/2023, final - 1/5/2023| 
|||| 
