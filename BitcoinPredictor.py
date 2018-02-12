"""
import pandas as pd

EPSILON = .02
 #   table_size = 15572 accum = 0
def main():
    table = pd.read_csv("BitcoinData.csv")
    table_size = 15600
    data_container = []

    for i in range(1, table_size):
        open_value = table.iloc[i, 1]
        close_value = table.iloc[i, 4]
        percent_difference = (close_value - open_value) / open_value * 100
        data_container.append(percent_difference)

    accum_match = 0
    accum_increase_list = []
    accum_decrease_list = []
    current_avg = (data_container[table_size - 4] + data_container[table_size - 3] + data_container[table_size - 2]) / 3
    print("Current Average: ", current_avg)

    for i in range(2, table_size - 2):
        past_avg = (data_container[i - 2] + data_container[i - 1] + data_container[i]) / 3
        if current_avg - EPSILON < past_avg and current_avg + EPSILON > past_avg:
            accum_match += 1
            if data_container[i + 1] > 0:
                accum_increase_list.append(data_container[i + 1])
            else:
            	accum_decrease_list.append(data_container[i + 1])

    accum_increase = len(accum_increase_list)
    accum_decrease = len(accum_decrease_list)

    print(accum_match)
    if accum_match == 0:
    	print("Current: ", table.iloc[table_size - 1, 4])
    	print("Probability of Increase is 50%")
    	print("Probability of Decrease is 50%")
    	exit()

    probability_increase = (accum_increase / accum_match) * 100
    probability_decrease = (accum_decrease / accum_match) * 100

    print("Probability of Increase is", format(probability_increase, '.1f'), "%")
    print("Probability of Decrease is", format(probability_decrease, '.1f'), "%")

    avg_pos_change = ((sum(accum_increase_list) / accum_increase)) /100
    avg_neg_change = ((sum(accum_decrease_list) / accum_decrease)) /100
    print("sumPos: ", sum(accum_increase_list) / accum_increase)
    print("sumDec: ", sum(accum_decrease_list) / accum_decrease)
    print("avgPosCh: ", avg_pos_change)
    print("avgNegCh: ", avg_neg_change)
    print("Pos: ", avg_pos_change*probability_increase)
    print("Neg: ", avg_neg_change*probability_decrease)
    print("Current: ", table.iloc[table_size - 1, 4])
    predicted_value = table.iloc[table_size - 1, 4] + (avg_pos_change*probability_increase) + (avg_neg_change*probability_decrease)
    print(predicted_value)

    if probability_increase > probability_decrease:
        print("Bitcoin is expected to increase in price from $" + str(table.iloc[table_size - 1, 4]), "to $" + str(format(predicted_value, '.2f')))
    elif probability_decrease > probability_increase:
        print("Bitcoin is expected to decrease in price from $" + str(table.iloc[table_size - 1, 4]), "to $" + str(format(predicted_value, '.2f')))
    else:
        print("The price of Bitcoin is not expected to change a significant amount.")

main()


"""
import sqlite3
import pandas as pd
import math
from GUI import *
from tkinter import Tk

class BitcoinPredictor:
	def __init__(self):
		df = pd.read_csv('coinmarket.csv')
		#print(df)
		#data starts at index 1
		#15672
		epsilon = .03
		maxSize = 1750
		counter = 0

		dataContainer = []
		compareContainer = []
		currentTimeAverage = 1

		accumMatch = 0;
		accumInc = 0;
		accumDec = 0;

		for i in range(1, maxSize):
			openValue = df.iloc[i,1] 
			closeValue = df.iloc[i,4]
			percent = ((closeValue - openValue) / openValue) * 100
			dataContainer.append(percent)

		for i in range(2, maxSize-2):
			data = dataContainer[i]
			data2 = dataContainer[i-1]
			data3 = dataContainer[i-2]
			dataAverage = (data + data2 + data3) / 3
			data4 = dataContainer[i+1]
			if((dataAverage - epsilon) < currentTimeAverage and (dataAverage + epsilon) > currentTimeAverage):
				accumMatch +=1
				if(data4 > 0):
					accumInc += 1

		if(accumMatch != 0):
			accumDec = accumMatch - accumInc
			probabilityInc = accumInc / accumMatch
			probabilityDec = accumDec / accumMatch

		root = Tk()
		MyGUI(probabilityInc, probabilityDec, root).appOpen()
		root.mainloop()

def main():
	BitcoinPredictor()
main()
