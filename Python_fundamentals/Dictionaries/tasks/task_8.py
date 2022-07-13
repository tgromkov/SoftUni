data = input()
company_user_dict = {}

while not data == 'End':
    company, user = data.split(' -> ')

    if company not in company_user_dict:
        company_user_dict[company] = []
    if user not in company_user_dict[company]:
        company_user_dict[company].append(user)

    data = input()

for company, user in sorted(company_user_dict.items(), key=lambda x: x[0]):
    print(company)

    for user_id in user:
        print(f'-- {user_id}')
