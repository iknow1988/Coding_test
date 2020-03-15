import pandas as pd

def read_file(fileName):
	df = pd.read_excel(fileName)

	return df

def write_to_file(df):
	df.to_csv('Test.csv')
	pritn("File written")

if __name__ == "__main__":
	print("Hello")