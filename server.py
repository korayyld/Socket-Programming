import socket
import pandas as pd
import random
import threading

HOST = 'localhost'
PORT = 8888
TOLERANCE = 0.05  # 5% tolerance

def load_stock_data():
    df = pd.read_excel("stock.xlsx")
    return df

def handle_request(client_connection, stock, actual_price):
    attempts = 1
    while True:
        guess = client_connection.recv(1024).decode()
        
        if guess.upper() == "END":
            print("Connection terminated.")
            client_connection.send("Connection terminated.".encode())
            break
        
        try:
            guess_price = float(guess)
            difference = abs(actual_price - guess_price) / actual_price

            if difference <= TOLERANCE:
                client_connection.send(f"Congratulations! Correct guess: {actual_price}".encode())
                print("Connection terminated.")
                break
            elif guess_price < actual_price:
                client_connection.send("Higher".encode())
            else:
                client_connection.send("Lower".encode())

            attempts += 1
            if attempts >= 3:
                client_connection.send(f"Three attempts over. Correct price: {actual_price}".encode())
                print("Connection terminated.")
                break

        except ValueError:
            client_connection.send("Please enter a valid number.".encode())

def serve_forever():
    stock_data = load_stock_data()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print("Server started, awaiting connection...")

        while True:
            client_connection, client_address = server_socket.accept()
            print(f"Connection established: {client_address}")
            
            selected_stock = stock_data.sample(1).iloc[0]
            stock_name = selected_stock['Stock Symbol']
            actual_price = selected_stock['Price']
            
            client_connection.send(f"Make a price prediction for {stock_name}.".encode())
            threading.Thread(target=handle_request, args=(client_connection, stock_name, actual_price)).start()

if __name__ == '__main__':
    serve_forever()
