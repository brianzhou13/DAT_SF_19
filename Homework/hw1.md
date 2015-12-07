#H1 Homework 1 Answers

1. Using the Chipotle.tsv file:
  * The rows are the unique items made per order_id, and the columns represent the details for each one of the unique order_id.
  * Following the order_id column, there seems to be 1834 orders.
  * Using wc - l chipotle.tsv , there are 4623 lines.
  * Using cut -f 3 "chipotle.tsv" | sort | uniq -c | grep "Chicken Burrito" , there are 553
  * Using cut -f 3 "chipotle.tsv" | sort | uniq -c | grep "Steak Burrito" , there are 368

2. Make a list of the CSV or TSV files.
  * find . | wc - l , There are 139 files in DAT_SF_19
  
3. Count the number of occurrences of the word "dictionary" (regardless of case) across all files in the DAT/repo
  * find . | grep -r "dictionary" . | uniq -c | wc -w , gives us 126 occurrences
  * grep -r "dictionary" . | wc - w , gives us 121 occurrences

  
