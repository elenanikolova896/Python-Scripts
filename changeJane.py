import os

# Specify the directory where your files are located
directory = "/path/to/your/data"

# List the files in the directory
files = os.listdir(directory)

# Iterate through the files
for filename in files:
    # Check if the filename contains "jane"
    if "jane" in filename:
        # Replace "jane" with "jdoe" in the filename
        new_name = filename.replace("jane", "jdoe")
        
        try:
            # Construct the full paths
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)
            
            # Rename the file
            os.rename(old_path, new_path)
            print("Renamed '{}' to '{}'".format(filename, new_name))
        except FileNotFoundError:
            print("Error: '{}' not found.".format(filename))
        except Exception as e:
            print("An error occurred: {}".format(e))
