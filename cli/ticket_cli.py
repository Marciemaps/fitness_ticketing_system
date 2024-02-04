#!/usr/bin/env python3
import click
from backend.ticketing_system import create_ticket, get_open_tickets, register_user, authenticate_user

@click.command()
def create_ticket_cmd():
    user_id = click.prompt("Enter user ID:")
    issue = click.prompt("Enter the issue:")
    create_ticket(user_id, issue)
    click.echo("Ticket created successfully.")

@click.command()
def view_tickets():
    tickets = get_open_tickets()
    for ticket in tickets:
        click.echo(f"Ticket #{ticket[0]} - User #{ticket[1]}: {ticket[2]}")

@click.command()
def register():
    username = click.prompt("Enter username:")
    password = click.prompt("Enter password:", hide_input=True)

    register_user(username, password)
    click.echo("User registered successfully.")

@click.command()
def create_ticket_auth():
    username = click.prompt("Enter username:")
    password = click.prompt("Enter password:", hide_input=True)

    user = authenticate_user(username, password)
    if user:
        issue = click.prompt("Enter the issue:")
        create_ticket(user[0], issue)
        click.echo("Ticket created successfully.")
    else:
        click.echo("Authentication failed. Please check your credentials.")

if __name__ == "__main__":
    create_ticket_cmd()
    view_tickets()
    register()
    create_ticket_auth()
