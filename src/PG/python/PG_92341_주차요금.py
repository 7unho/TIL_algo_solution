# result = 14600, 34400, 5000
fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
           "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

# result = 0, 591
# fees = [120, 0, 60, 591]
# records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]

# result = 14841
# fees = [1, 461, 1, 10]
# records = ["00:00 1234 IN"]


def solution(fees, records):
    records = list(map(lambda x : x.split(), records))
    records.sort(key=lambda x : x[1])
    current_number = int(records[0][1])
    current_time = int(records[0][1])
    current_sum = 0

    for i in range(1, len(records)):
        if records[i][1] != current_number:
            currnet_sum = current_sum if current_sum == 0 else current_sum + d
    
solution(fees, records)
