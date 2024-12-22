import sys
import scrape

try:
    print("Program started...") 
    scrape.pull_revenue_data()
    print("program ended.")
except Exception as e:
    print("Error occured during program execution: ", e)
    sys.exit()