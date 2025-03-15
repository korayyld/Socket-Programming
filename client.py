import socket

HOST = 'localhost'
PORT = 8888

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        
        try:
            message = client_socket.recv(1024).decode()
            print(message)
            
            while True:
                guess = input("Enter your price prediction or type 'END' to exit: ")
                client_socket.send(guess.encode())

                response = client_socket.recv(1024).decode()
                print(response)
                
                # Exit loop if the server sends a termination message
                if "Connection terminated" in response or "Correct guess" in response or "Three attempts over" in response:
                    break

        except ConnectionAbortedError:
            print("Server has closed the connection.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
