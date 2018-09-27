import func_defs
import sys


def loader():
    start_date, end_date = sys.argv[1:]
    func_defs.create_tr_graph_and_visualize(start_date,end_date)



# arg1 : start_date
# arg2 : end_date
if __name__ == '__main__':
    loader()
