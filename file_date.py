#The file_date function creates a new file in the current working directory, 
#checks the date that the file was modified, and returns just the date portion of the timestamp in the format of yyyy-mm-dd.

import os
import datetime

def file_date(filename):
    # Create the file
    with open(filename, "w") as file:
        pass
    
    # Get the timestamp of when the file was modified
    timestamp = os.path.getmtime(filename)
    
    # Convert the timestamp to a datetime object
    date_modified = datetime.datetime.fromtimestamp(timestamp)
    
    # Return the date in the format yyyy-mm-dd
    return date_modified.strftime("%Y-%m-%d")

print(file_date("newfile.txt"))
