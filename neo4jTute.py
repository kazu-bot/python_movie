#neo4jの書き方
#graphデータベースとの連携を行う。
#neo4j側が最新バージョンで上手くいかなかったため、3.5.15に落として実行してみたら上手くいった。
from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "password"),encrypted = False)

def clear_db(tx):
    tx.run('MATCH (n) DETACH DELETE n')

def add_friend(tx, name, friend_name=None):
    if not friend_name:
        return tx.run('CREATE (p:Person {name:$name}) RETURN p', name = name)
    return tx.run('MATCH (p:Person {name: $name})'
                  'CREATE (p)-[:FRIEND]->(:Person {name:$friend_name})',
                  name=name,friend_name=friend_name)

def print_friend(tx,name):
    for record in tx.run('MATCH (p {name:$name})-[:FRIEND]->(yourFriends)'
                         'RETURN p,yourFriends', name=name):
        print(record)

with driver.session() as session:
    session.write_transaction(clear_db)
    session.write_transaction(add_friend,'kazu')
    for f in ['Mike','Nancy']:
        session.write_transaction(add_friend,'kazu',f)
    session.read_transaction(print_friend,'kazu')