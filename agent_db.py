import sqlite3
from dataclasses import dataclass
from typing import List, Optional

DB_NAME = 'agents.db'

@dataclass
class Agent:
    id: Optional[int]
    name: str
    role: str

class AgentDatabase:
    def __init__(self, db_name: str = DB_NAME):
        self.conn = sqlite3.connect(db_name)
        self._create_table()

    def _create_table(self):
        self.conn.execute(
            """CREATE TABLE IF NOT EXISTS agents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                role TEXT NOT NULL
            )"""
        )
        self.conn.commit()

    def add_agent(self, name: str, role: str) -> Agent:
        cur = self.conn.cursor()
        cur.execute("INSERT INTO agents (name, role) VALUES (?, ?)", (name, role))
        self.conn.commit()
        agent_id = cur.lastrowid
        return Agent(id=agent_id, name=name, role=role)

    def list_agents(self) -> List[Agent]:
        cur = self.conn.cursor()
        cur.execute("SELECT id, name, role FROM agents")
        rows = cur.fetchall()
        return [Agent(id=row[0], name=row[1], role=row[2]) for row in rows]

    def get_agent(self, agent_id: int) -> Optional[Agent]:
        cur = self.conn.cursor()
        cur.execute("SELECT id, name, role FROM agents WHERE id=?", (agent_id,))
        row = cur.fetchone()
        if row:
            return Agent(id=row[0], name=row[1], role=row[2])
        return None

    def delete_agent(self, agent_id: int) -> bool:
        cur = self.conn.cursor()
        cur.execute("DELETE FROM agents WHERE id=?", (agent_id,))
        self.conn.commit()
        return cur.rowcount > 0

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Simple agent database")
    subparsers = parser.add_subparsers(dest="command")

    add = subparsers.add_parser("add", help="Add a new agent")
    add.add_argument("name", help="Agent name")
    add.add_argument("role", help="Agent role")

    list_p = subparsers.add_parser("list", help="List all agents")

    get = subparsers.add_parser("get", help="Get an agent by id")
    get.add_argument("id", type=int)

    delete = subparsers.add_parser("delete", help="Delete an agent by id")
    delete.add_argument("id", type=int)

    args = parser.parse_args()
    db = AgentDatabase()

    if args.command == "add":
        agent = db.add_agent(args.name, args.role)
        print(f"Added agent {agent}")
    elif args.command == "list":
        for agent in db.list_agents():
            print(agent)
    elif args.command == "get":
        agent = db.get_agent(args.id)
        if agent:
            print(agent)
        else:
            print("Agent not found")
    elif args.command == "delete":
        success = db.delete_agent(args.id)
        if success:
            print("Agent deleted")
        else:
            print("Agent not found")
    else:
        parser.print_help()

    db.close()
