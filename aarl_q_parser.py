import sqlite3

db_file = "arrl_test_questions.db"
conn = sqlite3.connect(db_file)
cur = conn.cursor()

f = open("2018_2022_Tech_Pool.txt")

line = f.readline()
if line == "START\n":
    questions = True
else:
    questions = False

while questions:
    q_id_str = f.readline()
    q_text = f.readline()[:-1].replace('"', "'")
    q_a = f.readline()[2:-1].replace('"', "'")
    q_b = f.readline()[2:-1].replace('"', "'")
    q_c = f.readline()[2:-1].replace('"', "'")
    q_d = f.readline()[2:-1].replace('"', "'")
    f.readline()  # ~~
    tester = f.readline()  # \n 
    if tester == "END":
        questions = False

    q_id_str = q_id_str.split(" ")
    q_id  = q_id_str[0]
    q_correct  = q_id_str[1][1]

    q = "INSERT OR REPLACE INTO q_technician (q_id, q_text, q_ans, q_a, q_b, q_c, q_d) VALUES (\""+q_id+"\", \""+q_text+"\", \""+q_correct+"\", \""+q_a+"\", \""+q_b+"\", \""+q_c+"\", \""+q_d+"\")"
    print(q)
    cur.execute(q)

f.close()
conn.commit()
conn.close()
