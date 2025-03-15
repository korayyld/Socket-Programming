# Stock Price Prediction Robot

## Table of Contents

1. [Introduction](#introduction)
2. [Project Description](#project-description)
3. [Technologies Used](#technologies-used)
4. [Application Structure](#application-structure)
   - [Server Code](#server-code)
   - [Client Code](#client-code)
5. [Terminal Operations](#terminal-operations)
6. [How to Run the Project](#how-to-run-the-project)

---

## 1. Introduction

This project is a stock price prediction robot developed using Python. The application consists of a simple **client-server model** where users predict stock prices in real-time. Users send their predictions to the server, and the server evaluates their guesses and responds accordingly.

---

## 2. Project Description

- The system **randomly selects a stock** and its price.
- Users have **3 attempts** to guess the correct stock price.
- If all **3 attempts fail**, the system **reveals the correct answer**.
- The user has a **5% tolerance range**, meaning if the real stock price is **100**, predictions between **95 and 105** are considered correct.
- If the user types `END`, the system **closes the connection** for both client and server.

### Example:
- **Real stock price**: 100 units
- **Valid predictions**: 95, 100, 105

### Goals:
- Provide users with **real-time stock price information**.
- Implement a **feedback mechanism** to enhance prediction accuracy.

---

## 3. Technologies Used

The project is developed in **Python** with the following key libraries:

- **Pandas**: For **data processing and analysis** (used to read Excel files).
- **Socket Module**: For **client-server communication** over **TCP protocol**.

---

## 4. Application Structure

### **A) Server Code**

The **server** processes incoming requests from the client.

#### **Key Functionalities:**
- **Loads stock data** from an **Excel file**.
- **Handles client requests**, receiving stock symbols and price data.
- **Prediction validation**: Checks if the user’s guess is within the **5% tolerance**.
- **Provides hints** (`Higher` / `Lower`) if the guess is incorrect.
- **Terminates** the connection after 3 failed attempts or when the user types `END`.

### **B) Client Code**

The **client** connects to the server and interacts with it.

#### **Key Functionalities:**
- **Establishes connection** to the server.
- **Sends stock price predictions** and receives feedback.
- **Handles termination** when the correct answer is found or after 3 failed attempts.

---

## 5. Terminal Operations

### Example Scenarios:

1. **User guesses incorrectly 3 times** → The system reveals the correct price and closes the connection.
2. **User types `END`** → The connection is closed immediately.
3. **User guesses within the 5% tolerance** → The system accepts the answer as correct.

---

## 6. How to Run the Project

### **Prerequisites:**
Ensure you have **Python 3.x** installed and the required libraries:
```sh
pip install pandas
```

### **Running the Server:**
```sh
python server.py
```

### **Running the Client:**
```sh
python client.py
```

The client will connect to the server and allow you to start making stock price predictions.

---

### 📌 **Future Improvements:**
- Adding **real-time stock price retrieval** from external APIs.
- Enhancing the **user interface** with a GUI.
- Implementing a **database** to track user performance.

---





