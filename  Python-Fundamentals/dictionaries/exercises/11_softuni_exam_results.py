exam = {}
submissions = {}

while True:
    command = input()
    if command == "exam finished":
        break
    command = command.split("-")
    username = command[0]
    language = command[1]
    if language == "banned":
        del exam[username]
        continue
    points = int(command[2])

    if username not in exam:
        exam[username] = 0
    if language not in submissions:
        submissions[language] = 0

    if points > exam[username]:
        exam[username] = points
    submissions[language] += 1

sorted_exam = sorted(exam.items(), key=lambda kvp: (-kvp[1], kvp[0]))
sorted_submissions = sorted(submissions.items(), key=lambda kvp: (kvp[0], kvp[1]))

print("Results:")
for name, points in sorted_exam:
    print(f"{name} | {points}")
print("Submissions:")
for lang, submission_count in sorted_submissions:
    print(f"{lang} - {submission_count}")