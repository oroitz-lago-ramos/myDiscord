from server import Server

def main():
    host = "localhost"
    port = 8080
    server = Server(host, port)
    server.start()

if __name__ == "__main__":
    main()
