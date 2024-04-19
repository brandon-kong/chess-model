from util.compress import (create_zip, create_xz)
from util.dir import get_data_dir

def main ():
    # get the location of the data directory
    data_dir = get_data_dir()

    print(data_dir)

    # compress the data directory
    create_xz('data.xz', data_dir)
    
    


if __name__ == '__main__':
    main()