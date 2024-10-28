import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime
import subprocess



class FinanceTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")     #Set window title
        self.create_widgets()       #Create gui widgets 
        self.transactions = self.load_transactions("transactions.json")      #Loading transactions from JSON file
        


    def create_widgets(self):

        #Heading
        heading_title = ttk.Label(self.root, text= "Finance Tracker", font= ("Helvitica",16),background="black",foreground="yellow")
        heading_title.pack(pady= 10)
        
        # Frame for table and scrollbar
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)


        # Treeview for displaying transactions
        self.tree = ttk.Treeview(self.frame, columns=("Category", "Date", "Amount", "Type"), show="headings")
        self.tree.heading("Category", text="Category", command=lambda: self.sort_column(0))
        self.tree.heading("Date", text="Date", command=lambda: self.sort_column(1))
        self.tree.heading("Amount", text="Amount", command=lambda: self.sort_column(2))
        self.tree.heading("Type", text="Type", command=lambda: self.sort_column(3))
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar for the Treeview
        scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scrollbar.set)
      

         
        #Create a frame for the search-related widgets
        search_frame = ttk.Frame(self.root)
        search_frame.pack()

        # Search bar and buttons for each attribute
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        self.search_entry.pack(side=tk.LEFT)

        self.search_category_button = ttk.Button(search_frame, text="Search Category", command=lambda: self.search_transactions("Category"))
        self.search_category_button.pack(side=tk.LEFT,padx= 1)

        self.search_date_button = ttk.Button(search_frame, text="Search Date", command=lambda: self.search_transactions("Date"))
        self.search_date_button.pack(side=tk.LEFT,padx= 1)

        self.search_amount_button = ttk.Button(search_frame, text="Search Amount", command=lambda: self.search_transactions("Amount"))
        self.search_amount_button.pack(side=tk.LEFT,padx= 1)

        self.search_type_button = ttk.Button(search_frame, text="Search Type", command=lambda: self.search_transactions("Type"))
        self.search_type_button.pack(side=tk.LEFT,padx= 1)

        # Button for viewing transactions
        view_button = ttk.Button(self.root, text="View Transactions", command=self.view_transactions)
        view_button.pack()

        # Create a style for changing colors
        style = ttk.Style() 

        # Button for clearing search results
        clear_search_button = ttk.Button(self.root, text="Clear Search", command=self.clear_search)
        clear_search_button.pack(side= tk.BOTTOM, pady= 5)      #Placing the clear search button at the bottom of the root window with padding
        
    
    def view_transactions(self):
        #Function to display transactions in another window
        
        view_window = tk.Toplevel(self.root)          #create a new window for displaying transactions
        view_window.title("View Transactions")

        text_widget = tk.Text(view_window)
        text_widget.pack(fill=tk.BOTH, expand=True)

        #Iterate through transactions and display them in text widget
        for category, transactions_list in self.transactions.items():
            text_widget.insert(tk.END, f"{category}:\n")
            for transaction in transactions_list:
                text_widget.insert(tk.END, f"  Date: {transaction['date']}, Amount: {transaction['amount']},Type: {transaction['transaction_type']}\n")      #Insert transaction details

        text_widget.config(state=tk.DISABLED)       #disable editing
        


    def load_transactions(self, filename):
        #Function to load transactions from a JSON file
        
        try:
            #Open the file and load its data
            
            with open('transactions.json', 'r') as file:
                data = json.load(file)
                print("Transactions loaded successfully.")
                return data
        except FileNotFoundError:

            #Error message when file is not found
            print(f"File '{filename}' not found. Initializing with an empty dictionary.")
            return {}

        except ValueError:
            print(f"Invalid JSON format in file '{filename}'. Initializing with an empty dictionary.")       #Error message when file is invalid
            return {}




    def display_transactions(self, transactions):
        #Function to display transation in treeview
        
        for item in self.tree.get_children():
            self.tree.delete(item)

        print("transactions: ")
        for category, transactions_list in transactions.items():
            print(category)
            for transaction in transactions_list:
                print(transaction)

        # Add transactions to the treeview
        for category, transactions_list in transactions.items():
            for transaction in transactions_list:
                self.tree.insert("", "end",
                                 values=(category, transaction["date"], transaction["amount"],transaction["transaction_type"]))

    
    def search_transactions(self, search_criteria):
        #Function to  search transaction based on input
        
        #select the search term
        search_term = self.search_var.get().strip().lower()

        #Initialize a dictionary to store filtered transactions
        filtered_transactions = {}
        
        #Iterate through each category
        for category, transactions_list in self.transactions.items():
            filtered_transactions[category] = []
            for transaction in transactions_list:

                #Check if the search criteria matches and add transaction to the list
                if search_criteria == "Category" and search_term == category.lower():
                    filtered_transactions[category].append(transaction)
                elif search_criteria == "Date" and search_term == transaction["date"].lower():
                    filtered_transactions[category].append(transaction)
                elif search_criteria == "Amount":
                    try:
                        search_amount = float(search_term)
                        if search_amount == transaction["amount"]:
                            filtered_transactions[category].append(transaction)
                    except ValueError:
                        #Show error message if search term is not valid 
                        messagebox.showinfo("Invalid Amount", "Please enter a valid number for amount.")
                        return
                elif search_criteria == "Type" and search_term == transaction["transaction_type"].lower():
                    filtered_transactions[category].append(transaction)

        #Display the filtered transactions
        self.display_transactions(filtered_transactions)


           
    def clear_search(self):
    #Function to clear the search entry
        self.search_var.set("")
    
        #Review all transactions 
        self.display_transactions(self.transactions)
        
    
    

    def sort_column(self, col):
        #Function to sort the transactions based on the clicked column
        
        data = [(self.tree.set(child, col), child) for child in self.tree.get_children("")]

        # Check if the column is numeric
        is_numeric = col == "Amount"

        #Sort the data
        data.sort(key=lambda x: float(x[0]) if is_numeric else x[0], reverse=self.tree.heading(col)["text"][-1] != "▲")

        #Rearrange the rows based on the sorted data
        for index, (_, child) in enumerate(data):
            self.tree.move(child, "", index)

        #Toggle the arrow for sorting
        arrow = "▲" if self.tree.heading(col)["text"][-1] != "▲" else "▼"

        #Update the column header with the arrow
        for col_id in self.tree["columns"]:
            self.tree.heading(col_id, text=col_id, command=lambda _col_id=col_id: self.sort_column(_col_id))

        #Set the heading text of the clicked column to its ID concatenated with an arrow character (▲ or ▼)
        self.tree.heading(col, text=str(col) + arrow)


                          

def main():
    root = tk.Tk()  #Create the tkinter main window
    app = FinanceTrackerGUI(root)
    #protocol to handle window closing event
    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root))  # Pass root to on_closing function
    app.display_transactions(app.transactions)
    root.mainloop()         #Start to loop


def on_closing(root):
    root.destroy()  #Close the current Tkinter window

    #Open another Python script in a new console
    subprocess.Popen(["python", "personal_finance_tracker(dict).py"], creationflags=subprocess.CREATE_NEW_CONSOLE)  # Open the other script in a new console

if __name__ == "__main__":
    main()



