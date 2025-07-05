from crawler import get_all_gx_data_realtime
from db import DB

def main():
    db = DB()
    get_all_gx_data_realtime(db)
    db.close()

if __name__ == '__main__':
    main() 