import json
import traceback

__author__ = 'lacquay'
import sys

def convert_binary_to_decimal(data):
    print data
    binary_value = (json.loads(data)).get("binary_value")
    # print sys.stdout>> binary_value
    result = 0
    if binary_value is not None:
        try:
            if isinstance(int(binary_value), int):
                value_check = str(binary_value)
                exponential = len(value_check) - 1
                for i in range(len(value_check)):
                    result = result + int(value_check[i]) * (pow(2, exponential))
                    exponential = exponential - 1
        except:
            traceback.print_exc()

    print "result", result
    return result

if __name__ == '__main__':
    convert_binary_to_decimal(json.dumps({"binary_value": "11111"}))
