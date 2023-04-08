import datetime

# create a file to store the usernames
log_file = "usernames.log"


# function to log the username
def log_username(username):
    # open the file in append mode
    with open(log_file, "a") as f:
        # get the current date and time
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # write the username and timestamp to the file
        f.write(f"{timestamp}: {username}\n")
