import graduates
list_of_grad_major = graduates.get_majors()

print(list_of_record[0])
for i in list_of_record:
    print(i["State"]["Name"],i["Year"])
# histogram
reason = []
numberPeople = []

for i in range(len(list_of_record))
    reason = int(i["Employment"]["Reason for Not Working"])
    numberPeople = int(i["Employment"]["Reason for Not Working"]["No need/want"])
    numberPeople = int(i["Employment"]["Reason for Not Working"]["Layoff"])
    numberPeople = int(i["Employment"]["Reason for Not Working"]["Family"])
    numberPeople = int(i["Employment"]["Reason for Not Working"]["No Job Available"])
    numberPeople = int(i["Employment"]["Reason for Not Working"]["Student"])
    reason.append(reason)
    numberPeople.append(numberPeople)

#histogram
import matplotlib.pyplot as plt
#bins are increments
plt.hist(reason)
plt.hist(numberPeople)
plt.xlabel('reason')
plt.ylabel('numberPeople')
plt.title('Histogram of Reasons of Unemployment')
plt.axis([-1.1, 1.1, 0, 55000])
plt.grid(True)
plt.show()
