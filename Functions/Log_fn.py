# LOGGING

# Logging can keep track of our activities (log messages) of application.
# behaviour of our application, whats happening in each statement or
# information of errors happened.
'''
ie, we can keep a record of various log messages.
- warning
- debug messages
- error
- critical error etc......
'''
# INBUILT python module is available in python.
'''
diff. log message states are,
- info - we get this message when everything working properly.
- debug - we get this message when we debug any statements.
- warning - we get this when we get any warnings.
- errors - we get if there is any error.
- critical - we get when some kind of error that completely stops
the application.
'''

import logging
# print(dir(logging))
# Capital letter - constants
# first letter capital - Class
# small letter - Functions
'''To create a logg message, we need to create a logger object of logging module'''
# creating a logger obj

# logger = logging.getLogger()
# print(logger)  # It will be in warning stage by default. We can change it later if we want.
#
# logging.basicConfig(filename="mylogs.log")  # file to store logg msgs. (.log is the ext)
# logger.info("This is an info message")
# logger.error("This is an error message")
# logger.warning("This is a warning message")

"""
We said we have 5 faces, for each face we have a level.
# if no level set - 0
# for Debug - 10
# for info  - 20
# for warning - 30
# for error - 40
# for critical - 50
by def logger is in warning face/state.
ie; if we have any warning message, that will store to our file,
But we have only 'info' message. So it will not store.
"""
# logger = logging.getLogger()
# logging.basicConfig(filename="mylogs.log", level=logging.DEBUG)
# logger.info("this is an info message")
# print(logger.level)

# We can customize the logg message using 'format'. (adding level name, date etc)
# Creating a log format.

# log_format = "%(levelname)s %(asctime)s - %(message)s"  # Giving attributes as a string
# logger = logging.getLogger()
# logging.basicConfig(filename="mylogs.log", level=logging.DEBUG, format=log_format)
# logger.info("this is an info message")
# print(logger.level)

# FORMAT = "%(asctime)-15s %(clientip)s %(user)-8s %(message)s"
# logger = logging.getLogger()
# logging.basicConfig(filename="mylogs.log", level=logging.DEBUG, format=FORMAT)
# d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
# logger.warning('Protocol problem: connection reset', extra=d)

###
# log_format = "%(levelname)s %(asctime)s - %(message)s"
# logger = logging.getLogger()
# logging.basicConfig(filename="mylogs.log", level=logging.NOTSET, format=log_format)
# logger.info("This is an info msg..")
# logger.debug("This is a debug msg....")
# logger.error("This is an error msg....")
# logger.warning("This is a warning msg...")
# logger.critical("This is a critical msg...")

# ## Example 1
# If we want to write an exception occurred to our log record

log_format = "%(levelname)s %(asctime)s - %(message)s"
logger = logging.getLogger()
logging.basicConfig(filename="mylogs.log", level=logging.NOTSET, format=log_format)
'''NB: If we didn't set the level as NOTSET, then python by default will set it to warning level (30)
 and hence the faces above WARNING ie; ERROR & CRITICAL can only be saved into the log. The lower level faces such as
 DEBUG & INFO cannot be saved to the log file...'''

# try:
#     a = 0
#     b = 10/a
# except Exception as e:
#     logger.exception(msg="Error occurred...")


class AccountNumberError(Exception):  # We are inheriting this error to the class exception.
    pass
class NotEnoughFundError(Exception):
    pass
accInfo = {"111": 1000, "222": 2000}

def withdraw(accountNumber, amount):
    logger.info(msg="Withdraw fn - start")
    if accountNumber not in accInfo:
        logger.debug("Account number is"+accountNumber)
        raise AccountNumberError()
    if amount > accInfo[accountNumber]:
        logger.debug("Withdrawal amount :"+str(amount))
        raise NotEnoughFundError()
    return amount
def call(a, m):
    try:
        amountRecieved = withdraw(a, m)
        print("ACC NO :", a)
        print("Rs.", amountRecieved, "withdrawn")
        logger.info(msg="amount withdrawn")
    except AccountNumberError:
        print("Incorrect account number...")
        logger.exception(msg="Incorrect Account number...")
    except NotEnoughFundError:
        print("Insufficient fund...")
        logger.exception(msg="Insufficient fund")
    except Exception:
        print("Sorry something went wrong!!!")
        logger.exception(msg="Sorry, something went wrong!!!")
    finally:
        print("Thank you, Visit Again!!!\n")

call("111",2000)
# call("1112", 2000)
call("111", 200)
# call("222", 1500)
# call("2221", 500)
# call("222", 2500)




