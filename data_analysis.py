import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DataAnalysis:

    @staticmethod
    def Income_analyze(frame_plot, user_name):
        # Read data from CSV file
        df = pd.read_csv("data.csv")
        data = pd.DataFrame(df)
        # Filter incomes data
        income = data[(data["type"] == 'Income') & (data["user_name"] == user_name)]
        # Sort incomes by date
        income = income.sort_values(by='date')        

        # Create a new Matplotlib figure
        plt.figure()
        # Plot line chart of incomes
        plt.bar(income['date'], income['amount'], color="green") 
        plt.xlabel('Date')
        plt.ylabel('Amount')
        plt.title('Incomes Over Time')
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

        # Embed the line plot in Tkinter window
        canvas = FigureCanvasTkAgg(plt.gcf(), master=frame_plot)
        canvas.draw()
        canvas.get_tk_widget().pack()

    @staticmethod
    def Expenses_analyze(frame_plot, user_name):
        # Read data from CSV file
        df = pd.read_csv("data.csv")
        data = pd.DataFrame(df)
        # Filter expenses data
        expenses = data[(data["type"] == 'Expensis') & (data["user_name"] == user_name)]
        # Sort expenses by date
        expenses = expenses.sort_values(by='date')

        # Create a new Matplotlib figure
        plt.figure()
        # Plot line chart of expenses
        plt.bar(expenses['date'], expenses['amount'], color="red") 
        plt.xlabel('Date')
        plt.ylabel('Amount')
        plt.title('Expenses Over Time')
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

        # Embed the line plot in Tkinter window
        canvas = FigureCanvasTkAgg(plt.gcf(), master=frame_plot)
        canvas.draw()
        canvas.get_tk_widget().pack()

    @staticmethod
    def Show_Balance(frame_plot, user_name):
        # Read data from CSV file
        data = pd.read_csv("balance.csv")
        df = pd.DataFrame(data)
        # Filter expenses data
        balance = df[df["user_name"] == user_name]
        # Sort expenses by date
        balance = balance.sort_values(by='date')
        #print(balance)
        # Create a new Matplotlib figure
        plt.figure()
        # Plot line chart of expenses
        plt.plot(balance['date'], balance['balance'], marker='o', color="blue") 
        plt.xlabel('Date')
        plt.ylabel('Balance')
        plt.title('Balance Over Time')
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

        # Embed the line plot in Tkinter window
        canvas = FigureCanvasTkAgg(plt.gcf(), master=frame_plot)
        canvas.draw()
        canvas.get_tk_widget().pack()
