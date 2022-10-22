# Command to return current date/time
import datetime

def command(shell, args):
    date_time = datetime.datetime.now()
    print(date_time.strftime("%d/%m/%Y %X %p"))

def help():
    return ("time", "Returns the current date and time in the format: DD/MM/YYYY HH:MM:SS")