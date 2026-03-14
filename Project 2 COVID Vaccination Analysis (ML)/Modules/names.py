# Generating Fake Names fotr the datesets :
import indian_names

def get_names():
    return indian_names.get_full_name()

if __name__ == '__main__':
    print(get_names())
