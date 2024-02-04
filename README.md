# fitness_ticketing_system
This is a Fitness Ticketing System to solve a Scheduling issue with the Fitness App SportsBuilder

# Overview
The Fitness Ticketing System is a command-line interface (CLI) based help desk ticketing system for a fitness app. This system allows users to report issues and submit tickets, which are then managed by the support team.

# Features
User Registration and Authentication: Users can register with the system and log in securely using hashed passwords.

Ticket Creation: Authenticated users can create tickets by providing details about the issue they are facing.

View Open Tickets: Support staff can view open tickets to prioritize and address user issues.

# Project Structure

 fitness_ticketing_system/
 |-- db/
 |   |-- init_db.sql
 |-- backend/
 |   |-- ticketing_system.py
 |-- cli/
 |   |-- ticket_cli.py
 |-- ticket_system.sh
 |-- README.md

 DB: Contains the SQLite database initialization script.

 Backend: Contains the backend script handling ticket creation and database interactions.

 CLI: Holds the CLI interface scripts.

 Ticket_system.sh: The entry script to run CLI commands.

# Getting Started
1. Clone the repository:

git clone https://github.com/your-username/fitness_ticketing_system.git
cd fitness_ticketing_system

2. Initialize the database:

sqlite3 db/ticketing.db < db/init_db.sql

3. Run the system:

./ticket_system.sh create
./ticket_system.sh view

# Dependencies

Python (>=3.6)
SQLite
Click (for CLI)

# Install dependencies:

- pip install click

# Security Considerations
- Passwords are hashed using SHA-256 for secure user authentication.
