try:
    num = int(input())
    result = 10/num
except ZeroDivisionError: # run if zerodivision error
    print("Don't provide Zero")
except ValueError: # run if type error
    print("Value Error")
else: # Runs if no exception occurs.
    print("Result is", result)
finally: # Runs always, whether exception occurs or not.
    print("Execution Finished")