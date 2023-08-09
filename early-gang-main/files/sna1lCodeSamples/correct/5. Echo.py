import logic as logical
import operators as ops
import notification as nf

def check_and_or_operation(value1, value2, value3):
    result = logical.or_(value1, logical.and_(value2, value3))
    return result

def compare_values(value1, value2):
    if ops.eq(value1, value2):
        return True
    else:
        return False

def send_notification(message):
    nf.send(message)

value1 = True
value2 = False
value3 = True

result = check_and_or_operation(value1, value2, value3)
comparison = compare_values(5, 10)
send_notification("This is a notification")

print("Result:", result)
print("Comparison:", comparison)
