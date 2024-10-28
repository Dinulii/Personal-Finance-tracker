USER  MANUAL  
(Instructions for running the application)

	
	FinanceTrackerGUI is a basic and user-friendly application for monitoring your income and expenses so that you can track your personal finances in an organized way. The basic features of this application consist of an option to remove or add transactions, to check your balances, to search, sort, and summarize the data. 

	This is a versatile tool designed to help users manage their financial transactions .Whether you prefer a Graphical User Interface (GUI) or a Command-Line Interface (CLI), this application offers both options to suit your preferences.





Installation
1.	The application requires Python installed on your system (version 3.x or higher)
2.	Tkinter Python library comes with Python thus no additional installing is required
3.	Ensure that the transactions.json file containing transaction data is in the same directory as the Python script.
4.	Run your Python script with the command  “Finance_tracker_GUI.py” in your terminal or command line.
5.	The application window consists of various widgets and buttons to perform different actions related to managing transactions and viewing summaries.

USAGE

•	When running the program, the FinanceTrackUserInterface application window will open.
•	Explore the buttons and input fields to undertaken different functionalities.
•	Close the GUI window using the close button (X) 
•	The program automatically returns to the CLI menu, allowing the user to continue working from the command line.

Features Overview

1.	 Displaying Transactions
Transactions are shown in a table layout with the help of columns for category, date, amount and type.
Scroll the transactions with the scrollbar at the right side of the table.

2.	Viewing Transactions
Check the "Look Up Transactions" button next to it to open a new window with all transactions.
Each transaction is placed under the proper category: date, amount, and type are listed.

3.	Loading transactions
The application automatically loads transactions from the "transactions.json" file at the startup.
Ensure that the "transactions.json" file is present in the same location as the Python scrip

4.	Searching Transactions
Type the search term for classification of transactions on date, category, amount, or type using the search bar.
Enter the criteria in a dropdown menu.
Press the search button to display the transactions in the list.

5.	Sorting Transactions
To the sorting transactions by category, date, amount, or their type, the table by clicking the columns headers.
Clicking on a column header multiple times toggles between ascending and descending order.

6.	  Clearing Search Results
Press the "Clear Text" button to flush the search bar and show up all transactions.

7.	Closing the application.
Close the GUI window by clicking the close button (X) to return to the CLI menu automatically.
8.	Open GUI app again
In CLI main menu, by choosing the option (Open GUI application) GUI will re launch 

Structure of Transactions in ‘transactions.json’ file as follows ,
 
Ex: 

{
  "Foods": [
    {
      "amount": 250.0,
      "date": "2024-04-12",
      "transaction_type": "Expense"
    },
    {
      "amount": 560.0,
      "date": "2024-03-28",
      "transaction_type": "Expense"
    }
  ],
  "Clothes": [
    {
      "amount": 2500.0,
      "date": "2024-04-15",
      "transaction_type": "Expense"
    }
  ]
}

Conclusion :
In conclusion, the Finance Tracker GUI provides a convenient and user-friendly solution for effectively managing personal finances. With its intuitive interface and robust features, users can easily organize, track, and analyze their financial transactions. Through the use of python and Tkinter, Finance Tracker GUI can be used on all the platforms thereby maintain a smooth user experience. Whether it is budgeting, tracking expenses and financial planning; Finance Tracker makes the financial process easier for all.
Thanks for choosing FinanceTrackerGUI! 
