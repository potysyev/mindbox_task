def group_id_zero(n_customers):
    groups_data = {}
    for id in range(n_customers + 1):
        group_id = sum([int(number) for number in str(id)])
        if group_id in groups_data.keys():
            groups_data[group_id] = groups_data[group_id] + 1
        else:
            groups_data[group_id] = 1
    return groups_data


def group_id_arbitrary(n_customers, n_first_id):
    groups_data = {}
    for id in range(n_first_id, n_customers + 1):
        group_id = sum([int(number) for number in str(id)])
        if group_id in groups_data.keys():
            groups_data[group_id] = groups_data[group_id] + 1
        else:
            groups_data[group_id] = 1
    return groups_data


if __name__ == "__main__":
    try:
        n_customers = int(input("Input a number of customers for 0 based enumeration test: "))
    except:
        print("Please input a number")

    groups_zero = group_id_zero(n_customers)
    print('Group : Number of IDs')
    for key, value in groups_zero.items():
        print(key, ' : ', value)

    try:
        n_first_id = int(input("Input a number of customer to start ID enumeration: "))
        n_customers = int(input("Input a number of customers for group test: "))
    except:
        print("Please input a number")

    groups_arbitrary = group_id_arbitrary(n_customers, n_first_id)
    print('Group : Number of IDs')
    for key, value in groups_arbitrary.items():
        print(key, ' : ', value)
