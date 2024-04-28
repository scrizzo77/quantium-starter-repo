import csv

def process_sales_data(daily_sales_csvs,sales_writer):
    for sales_data in daily_sales_csvs:
        with open(sales_data) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count > 0 and row[0] == "pink morsel":
                    sales = float(row[1][1:]) * float(row[2])
                    date = row[3]
                    region = row[4]
                    sales_writer.writerow([sales, date, region])
                line_count += 1
            csv_file.close()

with open('data/sales_file.csv', mode="w", newline='') as sales_file:
    sales_writer = csv.writer(sales_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    daily_sales_csvs = ['data/daily_sales_data_0.csv','data/daily_sales_data_1.csv','data/daily_sales_data_2.csv']
    process_sales_data(daily_sales_csvs,sales_writer)
    sales_file.close()