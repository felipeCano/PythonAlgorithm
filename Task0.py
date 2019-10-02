"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

def firstText(texts):
    reciverCall = calls[0][1]
    sendingCall = calls[0][0]
    timestamp = calls[0][2]
    message1 = 'First record of texts, {0} texts {1} at time {2}'.format(
        reciverCall,
        sendingCall,
        timestamp,
    )
    print(message1)

def lastCalls(calls):   
    index = len(calls) - 1
    reciverCall = calls[index][1]
    sendingCall = calls[index][0]
    timestamp = calls[index][2]
    segundsCall = calls[index][3]
    message = 'Last record of calls, {0} calls {1} at time {2}, lasting {3} seconds'.format(
        reciverCall,
        sendingCall,
        timestamp,
        segundsCall
    )
    print(message)


firstText(texts)


lastCalls(calls)