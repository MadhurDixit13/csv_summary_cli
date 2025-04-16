import sys
import re
import csv

def summary(csv_files):
  num_rows = 0
  num_cols = 0
  col_names = []
  col_types = []
  for csv_file in csv_files:
    with open(csv_file, 'r') as f:
      print(f'Summarizing {csv_file}')
      # count number of columns
      first_line = f.readline()
      f.readline()
      second_line =  f.readline()
      # split first line by comma to get column names
      col_names = first_line.split(',')
      # remove newline character from last column name
      col_names[-1] = col_names[-1].strip()
      # type of each column
      for i in second_line.split(','):
        if(i.isdigit()):
          col_types.append('int')
        else:
          col_types.append('str')
      num_cols = len(first_line.split(','))
      # count number of rows
      for line in f:
        num_rows += 1
      print(f'Number of rows: {num_rows}')
      print(f'Number of columns: {num_cols}')
      print(f'Column names: {col_names}')
      print(f'Column types: {col_types}')
      # reset file pointer to beginning of file  
      f.seek(0)
      # summarize the cols where type is int
      reader = csv.reader(f)
      header = next(reader) 
      for i in range(len(header)):
        column_data = [row[i] for row in reader]
        if(col_types[i] == 'int'):
          column_data = [int(x) for x in column_data if x != '']
          mean = sum(column_data)/len(column_data)
          std = (sum([(x-mean)**2 for x in column_data])/len(column_data))**0.5
          mini = min(column_data)
          maxi = max(column_data)
          median = sorted(column_data)[len(column_data)//2]
          print(f"Column {header[i]}: Mean = {mean}, Std = {std}, Min = {mini}, Max = {maxi}, Median = {median}")
        # Reset file reader after each column iteration
        f.seek(0)
        next(csv.reader(f))
      
    
    print('')
  
  
    

# user inputs csv files via command line which we read and summarize
# print (sys.argv[1:])
csv_files = [] 
for file in sys.argv[1:]:
  is_csv = re.search(r'\.csv$', file)
  if(is_csv):
    csv_files.append(file)
summary(csv_files)