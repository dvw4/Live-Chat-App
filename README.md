# Live-Chat-App
This app is a simple live chat application built using Flask and Socket.IO. It allows users to communicate with each other in real-time by sending and receiving messages.

Here's how the app works:

When a user opens the app, they are prompted to enter their name.
The user interface consists of a message box, where the messages will be displayed, and an input box with a "Send" button.
When the user enters a message and clicks "Send", the message is sent to the server using Socket.IO.
The server receives the message and broadcasts it to all connected clients.
Each connected client, including the sender, receives the message and appends it to the message box in their UI.
All clients also receive the initial set of messages when they connect to the server.
The app continuously polls the server for new messages every few seconds to keep the UI updated in real-time.
By running the app, multiple users can open the app in their browsers, enter their names, and start sending messages to each other. The messages will be displayed in real-time for all users, creating a live chat experience.
