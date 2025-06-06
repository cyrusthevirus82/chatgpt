# Agent Database

This repository provides a simple Python script (`agent_db.py`) to manage a basic database of agents using SQLite. The script allows you to add, list, retrieve, and delete agents via the command line.

## Requirements

- Python 3.8 or higher (standard library only, so no external dependencies)

## Usage

```bash
# Add an agent
python agent_db.py add "Agent Name" "Role"

# List all agents
python agent_db.py list

# Get a specific agent by ID
python agent_db.py get 1

# Delete an agent
python agent_db.py delete 1
```

The database is stored in a local file named `agents.db` in the same directory as the script.

## License

This project is released under the MIT License.
