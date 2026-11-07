"""
Create a scholarship eligibility checker for a college. Students are selected based on
marks, family income, and attendance.
"""
name=input("Enter the name :")
marksPer=int(input("Enter the marks :"))
income=int(input("Enter the Annual fimaly income :"))
attenPer=int(input("Enter the Attendence percentage :"))


if (marksPer >= 75 and income <= 400000 and attenPer >= 75):
    status = "Eligible"
    reason = "-"
    if marksPer >= 90:
        category = "Full Scholarship"
    else:
        category = "Partial Scholarship"
else:
    status = "Not Eligible"
    category = "None"
    reason = ""
    if marksPer < 75:
        reason = reason + "Percentage is below 75%. "
    if income > 400000:
        reason = reason + "Family income is above 4,00,000. "
    if attenPer < 75:
        reason = reason + "Attendance is below 75%. "

print("\n----- Scholarship Result -----")
print("Student Name        :", name)
print("Eligibility Status  :", status)
print("Scholarship Category:", category)
print("Reason              :", reason)