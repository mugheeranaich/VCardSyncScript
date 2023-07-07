import vobject

with open('.vcf', 'r', encoding='utf-8') as f:
    vcard_data = f.read()

vcard = vobject.readOne(vcard_data)

with open('contact_list.py','a') as f:
    content = f.write('''
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="excel"
)\n''')

    content2 = f.write("cursor = conn.cursor()\n")


for line in vcard_data.splitlines():
    if line.startswith('FN:'):
        full_name = line.replace('FN:','Name:')


    elif line.startswith('TEL;'):
        telephone = line.replace('TEL;CELL:','Telephone:')

        with open('contact_list.py','a') as f:
            content3 = f.write(f'''query = "INSERT INTO contact (name, phone_number) VALUES (%s,%s,)"
cursor.execute(query, ("{full_name}", "{telephone}"))
conn.commit()\n''')
            print('Behold! A magnificent creation has come into existence—a meticulously crafted Python script, artfully generated with resounding success.')
