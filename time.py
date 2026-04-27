from datetime import datetime

def time_delta(t1, t2):
    # Format: Day dd Mon yyyy hh:mm:ss +xxxx
    time_format = '%a %d %b %Y %H:%M:%S %z'
    
    # Parse strings into timezone-aware datetime objects
    dt1 = datetime.strptime(t1, time_format)
    dt2 = datetime.strptime(t2, time_format)
    
    # Calculate absolute difference in seconds
    delta = abs(dt1 - dt2)
    return int(delta.total_seconds())

# Example usage with Sample Input 0
if __name__ == '__main__':
    # Testcase 1
    print(time_delta('Sun 10 May 2015 13:54:36 -0700', 'Sun 10 May 2015 13:54:36 -0000'))
    # Testcase 2
    print(time_delta('Sat 02 May 2015 19:54:36 +0530', 'Fri 01 May 2015 13:54:36 -0000'))
