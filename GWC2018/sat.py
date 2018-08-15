import school_scores
list_of_record = school_scores.get_all()

print(list_of_record[0])
for i in list_of_record:
    print(i["State"]["Name"],i["Year"])
    print(i["GPA"]["A"]["Math"],i["GPA"]["A"]["Verbal"])

Math = []
list_of_record["GPA"]["A"]["Math"]
for i in list_of_record["GPA"]["A"]["Math"]
    if list_of_record[]
