# version: 0.1
# original author (from stack overflow): taleinat & tahoar
# demonstration script author: picklez

def has_admin(): # this function will return an array containing [computer users name, bool for if run at Admin level]
    import os
    if os.name == 'nt':
        try:
            # only windows users with admin privileges can read the C:\windows\temp
            temp = os.listdir(os.sep.join([os.environ.get('SystemRoot','C:\\windows'),'temp']))
        except:
            return (os.environ['USERNAME'],False)
        else:
            return (os.environ['USERNAME'],True)
    else:
        if 'SUDO_USER' in os.environ and os.geteuid() == 0:
            return (os.environ['SUDO_USER'],True)
        else:
            return (os.environ['USERNAME'],False)
            
def has_admin_simply(): # this function will return a bool of whether the user has admin or not (really it is checking if the current Python script is running at Admin level)
    hold = has_admin()
    return hold[1]
            
# comment this print statement out if you want to implement this as a class
print(has_admin_simply())