months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December"]
items = ["NIL"]
l = []

file = open("sales-data.txt", "r")  # file = open("sales-data.csv","r")  # To read csv file

idx = 0
for i in file:
    l.append(list(map(str, i.split(","))))
    l[idx][4] = l[idx][4].rstrip("\n")

    # Add Year, Month, Day column
    if (idx == 0):
        l[idx].insert(len(l[idx]), "Year")
        l[idx].insert(len(l[idx]), "Month")
        l[idx].insert(len(l[idx]), "Day")
    else:
        date = list(l[idx][0].split("-"))
        l[idx].insert(len(l[idx]), date[0])
        l[idx].insert(len(l[idx]), months[int(date[1])])
        l[idx].insert(len(l[idx]), date[2])

        # Retrieve name of all the food items
        if (l[idx][1] not in items):
            items.append(l[idx][1])
    idx += 1
file.close()

total_sales = 0
idx = 1
for i in l[1:]:
    total_sales += int(i[4])  # Sum of the total price

print("1. Total sales of the store :", total_sales)

month_total = [0] * len(months)
for i in l[1:]:
    month_total[months.index(i[6])] += int(i[4])  # Sum of the total price for each month

print("\n2. Month wise sales totals :")
print("Month : Total Sales")
for i in range(1, len(month_total)):
    print(months[i], ":", month_total[i])

month_days = [0] * len(months)
month_items = [["Item", "Frequency"]]
month_revenue = [["Item", "Revenue"]]

for m in range(1, len(months)):
    item_freq = [0] * (len(items))
    item_revenue = [0] * (len(items))
    for i in l[1:]:
        if (months[m] != i[6]):  # Checking loop for each month
            continue
        month_days[m] = int(i[7])
        idx = items.index(i[1])
        item_freq[idx] += int(i[3])  # Add all the item Quantity for each month
        item_revenue[idx] += int(i[4])  # Add all the item total price for each month

    # Calculate popular item with most quantity sold in each month
    month_items.append([items[item_freq.index(max(item_freq))], max(item_freq)])

    # Calculate item generating most revenue in each month
    month_revenue.append([items[item_revenue.index(max(item_revenue))], max(item_revenue)])

print("\n3. Most popular item (most quantity sold) in each month :")
print("Month -> Popular Item -> Quantity")
for i in range(1, len(month_items)):
    print(months[i], "->", month_items[i][0], "->", month_items[i][1])

print("\n4. Items generating most revenue in each month: ")
print("Month -> Item with most revenue -> Revenue")
for i in range(1, len(month_revenue)):
    print(months[i], "->", month_revenue[i][0], "->", month_revenue[i][1])

pop_item_max_ord = [0]
pop_item_min_ord = [0]
pop_item_avg_ord = [0]

for m in range(1, len(months)):
    popular_item_orders = [0] * (month_days[m] + 1)

    for i in l[1:]:
        # Count all the Quantities of popular item in each month per day
        if (months[m] == i[6] and month_items[m][0] == i[1]):
            popular_item_orders[int(i[7])] += int(i[3])  # popular_item_orders[int(i[7])]+=1  # to count per day orders

    # Checking if each month has any popular item or not
    if (len(popular_item_orders) > 1):
        pop_item_max_ord.append(max(popular_item_orders[1:]))  # Calculating maximum orders in a day in each month
        pop_item_min_ord.append(min(popular_item_orders[1:]))  # Calculating minimum orders in a day in each month
        pop_item_avg_ord.append(sum(popular_item_orders[1:]) // month_days[m])  # Calculating average orders per month
    # print(months[m],popular_item_orders)

print("\n5. For the most popular item in each month:")
print("Month : Popular Item : Max Order : Min Order : Average Order")

for i in range(1, len(pop_item_max_ord)):

    # Checking if each month has popular item or not
    if (pop_item_max_ord[i] > 0):
        print(months[i], ":", month_items[i][0], ":", pop_item_max_ord[i], ":", pop_item_min_ord[i], ":",
              pop_item_avg_ord[i])
