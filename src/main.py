from util.zip import create_zip
from util.dir import get_data_dir

def main ():
    # get the location of the data directory
    data_dir = get_data_dir()

    # zip the files in the data directory
    create_zip('data.zip', data_dir)
    


if __name__ == '__main__':
    main()