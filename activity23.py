months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

print(months)
for i in months:
    print(f"{i},2025")

months.reverse()
print(months)

fullname = "Daniel C. Oco"

newlist = list(fullname)
newlist.reverse()
print(newlist)

newlist.sort()
print(newlist)
