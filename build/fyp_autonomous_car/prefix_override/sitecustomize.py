import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/tudor/Desktop/fyp/install/fyp_autonomous_car'
