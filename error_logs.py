# parsing logs
# find which user has how many errors on that day

logs = [
    "2024-01-01T10:15:30 INFO user1 login",
    "2024-01-01T11:00:00 ERROR user2 failed",
    "2024-01-01T12:30:00 ERROR user2 timeout",
    "2024-01-01T12:15:30 ERROR user1 timeout",
    "2024-01-02T09:00:00 ERROR user1 failed",
    "2024-01-02T10:00:00 ERROR user1 crash",
    "2024-01-02T11:00:00 INFO user2 success"
]

#output
#{'2024-01-01': {'user2': 2, 'user1': 1}, '2024-01-02': {'user1': 2}}

def logs_summary(logs):
    result={}
    for log in logs:
        parts=log.split()
        log_date=parts[0][0:10]
        level=parts[1]
        user=parts[2]

        if level=='ERROR':
            if log_date not in result:
                result[log_date]={}
            result[log_date][user]=result[log_date].get(user,0)+1
    return result

print(logs_summary(logs))

