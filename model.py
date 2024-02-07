import streamlit as st


readme = "./README.md"

default_questions = [
    "How many messages were sent by each contact?",
    "Show the content of the table messages",
    "How many messages did John Doe received ?"
]

ddl_tab = {
    "contacts" : """
CREATE TABLE Contacts (
    contact_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    phone_number TEXT UNIQUE NOT NULL)
""",
    "messages" : """
CREATE TABLE Messages (
    message_id INTEGER PRIMARY KEY,
    sender_id INTEGER,
    receiver_id INTEGER,
    message_text TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sender_id) REFERENCES Contacts(contact_id),
    FOREIGN KEY (receiver_id) REFERENCES Contacts(contact_id)
)
"""
}
