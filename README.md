# Overview

In this software, users can add income or expesnses through input and incldue details such as the source, category, amount, and date. When inputted the info is stored in the Firestore database.

My purpose for writing this software is to familiarize myself with using key value dictionaries in Python as well as how to properly Create, Read, Update, and Delete (CRUD) data.

[Software Demo Video](https://youtu.be/ZfhbqBohLag)

# Cloud Database

The cloud database used in this project is Firestore, which is a NOSQL database provided by Google's Firebase. Firebase is able to sync and store data in real-time. 

I have created collections, documents, and fields in this project which emulates a tree structure. The collections consist of the incomes and expenses. Documents are a single entry of either these incomes or expenses.
Finally, fields are the actual data that is stored into teh income or expense entry such as source, amount, and date. Also each document is assigned a unique ID so users, can choose how to manipulate said document.

# Development Environment

The tools that I used to develop this software was Visual Studio Code as an IDE, the modules firebase admin, and Google's Firebase.

Some key libraries used in this software:

firebase_admin: This library provides Python developers with the necessary tools to interact with Firebase services such as Firestore, Authentication, and Cloud Storage. It allows for managing Firebase projects, initializing Firebase apps, and performing various operations on Firestore data.
firebase-adminsdk: This library is part of the Firebase Admin SDK for Python and is used for initializing the Firebase app with the appropriate credentials, enabling access to Firebase services securely.

# Useful Websites

- [Firebase](https://console.firebase.google.com/u/0/)
- [Real Python](https://realpython.com/crud-operations/#:~:text=effective%20data%20management.-,In%20Short%3A%20CRUD%20Stands%20for%20Create%2C%20Read%2C%20Update%2C,new%20entries%20to%20your%20database.)

# Future Work

- Feedback Mechanisms: Provide more informative feedback to users.
- Data visualization: Using graphs to display income vs expense trends.
- User Authentication: Restrict access to deleting or added data based on permissions.