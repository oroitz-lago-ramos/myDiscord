import client
import server

database = server.Database()
my_discord = client.Client(database)
my_discord.run()