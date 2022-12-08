import sqlite3
import os

def database_setup(anime_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+anime_name)
    cur = conn.cursor()
    return cur, conn 


def avg_anime(cur, conn):
    cur.execute("SELECT * FROM anime_list ORDER BY id LIMIT 10")
    rows=cur.fetchall()
    print()
    conn.commit()

    sum = 0 
    for row in rows:
        print(row)
        # sum += row[2]
        # print(sum)
        # avg_row = sum /len(rows)
        # print(avg_row)

    # calculating the top ten score and popularity 

    cur.execute("SELECT * FROM anime_list ORDER BY id DESC LIMIT 10")
    print(cur.fetchall())
    print()
    conn.commit()






def main():
    cur, conn = database_setup('anime.db')
    avg_anime(cur, conn)

if __name__ == "__main__":
    main()
