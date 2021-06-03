# In this assignment, you will load the first 100 Pokémon JSON documents from the PokéAPI and store them in a table.


from re import I
import psycopg2
import hidden
import time
import myutils
import requests
import json

# load secrets
secrets = hidden.secrets()

conn = psycopg2.connect(host=secrets['host'],
        port=secrets['port'],
        database=secrets['database'],
        user=secrets['user'],
        password=secrets['pass'],
        connect_timeout=3)

cur = conn.cursor()

defaulturl = ''

sql = '''
DROP TABLE IF EXISTS pokeapi CASCADE;
CREATE TABLE IF NOT EXISTS pokeapi
(id INTEGER, body JSONB);
'''
print(sql)
cur.execute(sql)

conn.commit()

# get 1..100 using Pokemon API and insert to pokeapi table
URL_BASE = 'https://pokeapi.co/api/v2/pokemon/'

text = "None"
count = 0
fail = 0
idx = 0
total = 100
for i in range(1,total+1):
    idx = i
    url = URL_BASE + str(idx)
    try:
        print('=== Url is', url)
        response = requests.get(url)
        text = response.text
        # print('=== Text is', text)
        status = response.status_code
        print(f'id={idx}, status={status}')
        sql = 'insert into pokeapi (id,body) values (%s,%s);'
        row = cur.execute(sql, (idx,text,))
        count = count + 1
    except KeyboardInterrupt:
        print('')
        print('Interrupted by YOU!')
        break
    except Exception as e:
        print("Unable to retrieve or parse page", url)
        print("error", e)
        fail = fail+1
        if fail > 5: break
        break

    if count % 25 == 0:
        conn.commit()
        print(count, 'loading...')
        time.sleep(1)
        continue

print(f'idx={idx}, count={count}, fail={fail}, total={total}')
print('Closing database connection...')
conn.commit()
cur.close()