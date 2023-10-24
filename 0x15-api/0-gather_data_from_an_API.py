#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # Make the API request for user information
    user_response = requests.get(url + "users/{}".format(employee_id))
    if user_response.status_code != 200:
        print("Error: User not found")
        sys.exit(1)
    user = user_response.json()

    # Make the API request for todos
    todos_response = requests.get(url + "todos", params={"userId": employee_id})
    if todos_response.status_code != 200:
        print("Error: Todos not found for this user")
        sys.exit(1)
    todos = todos_response.json()

    completed = [t.get("title") for t in todos if t.get("completed")]
    total_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), total_tasks))
    
    for task in completed:
        print("\t{}".format(task))
