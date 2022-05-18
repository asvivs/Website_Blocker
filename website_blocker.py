import time
from datetime import datetime as dt

local_machine_ip = "127.0.0.1"
# websites we need to block
blocking_websites = ["www.instagram.com", "instagram.com", "www.facebook.com",
                     "facebook.com", ]
host_file_path = r"C:\Windows\System32\drivers\etc\hosts"
starting_time = "08:0:0"
ending_time = "20:0:0"

now = dt.now()
current_time = now.strftime("%H:%M:%S")
print(current_time)

while True:
    if (starting_time <= current_time) and (current_time <= ending_time):
        print(f"Time is now {current_time}.You are in your working hours!!!")
        with open(host_file_path, "r+") as file:
            content = file.read()
            for website in blocking_websites:
                if website in content:
                    pass
                else:
                    file.write(local_machine_ip + " " + website + "\n")
    else:
        print(f"Time is now {current_time}. It's your free time!!!")
        with open(host_file_path, "r+") as file:
            content = file.readlines()
            file.seek(0)  # to write the file from the top that this to print the original file.
            for line in content:
                if not any(website in line for website in blocking_websites):
                    file.write(line)

                file.truncate()  # to remove the websites in free time

    time.sleep(10)

