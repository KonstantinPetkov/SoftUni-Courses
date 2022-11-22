contest_dict = {}

while True:
    contest_command = input()
    if contest_command == "end of contests":
        break
    contest, password_contest = contest_command.split(":")
    if contest not in contest_dict.keys():
        contest_dict[contest] = 0
    contest_dict[contest] = password_contest

user_dict = {}
while True:
    user_command = input()
    if user_command == "end of submissions":
        break
    contest, password, user, points = user_command.split("=>")
    if contest_dict.get(contest) == password:
        if user not in user_dict.keys():
            user_dict[user] = {}
        user_dict[user][contest] = user_dict[user].get(contest, 0)
        if user_dict[user][contest] < int(points):
            user_dict[user][contest] = int(points)

candidates = {name : sum(user_dict[name].values()) for name in user_dict}
best_candidate = max(candidates)
print(f"Best candidate is {best_candidate} with total {candidates[best_candidate]} points. \nRanking:")

for name_of_student in sorted(user_dict.keys()):
    print(f"{name_of_student}")
    for key, value in sorted(user_dict[name_of_student].items(), key=lambda item: -item[1]):
        print(f"#  {key} -> {value}")

