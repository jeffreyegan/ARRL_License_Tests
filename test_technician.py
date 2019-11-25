import sqlite3
import random
import re
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

db_file = "arrl_test_questions.db"
conn = sqlite3.connect(db_file)
cur = conn.cursor()

test_comps = {"T1": 6, "T2": 3, "T3": 3, "T4": 2, "T5": 4, "T6": 4, "T7": 4, "T8": 4, "T9": 2, "T0": 3}
questions = []

for key in test_comps:
    q = "SELECT * FROM q_technician WHERE q_id LIKE \""+key+"%\""
    cur.execute(q)
    rows = cur.fetchall()
    q_id_idx = list(range(0, len(rows)))
    random.shuffle(q_id_idx)
    q_ids = q_id_idx[:test_comps[key]]

    for q in q_ids:
        questions.append(rows[q])

random.shuffle(questions)
answer_set = set(["1", "2", "3", "4"])
answer_map = {"1": "A", "2":"B", "3":"C", "4":"D"}
num_correct = 0.0

for q in questions:
    print("\n"+q[0]+"  "+q[1])
    print("    [1] "+q[3])
    print("    [2] "+q[4])
    print("    [3] "+q[5])
    print("    [4] "+q[6])
    m = re.search(r'component (.*) in figure T(.*)', q[1])
    if m:
        plt.figure(figsize=(614/75.0, 458/75.0))  # true fig size is 614 x 458 pixels
        img = mpimg.imread('Fig_T'+m[2][0]+'.png')
        plt.imshow(img)
        print("... Close figure when ready to answer...")
        plt.show()
        del m

    user_ans = input("\n  Enter multiple choice answer [1-4]")
    while not user_ans in answer_set:
        user_ans = input("  Invalid answer, enter multiple choice answer [1-4]")
    if answer_map[user_ans] == q[2]:
        num_correct += 1.0
        # print("  correct!\n")

print("You scored: "+str(round(100.0*num_correct/len(questions)))+"%")
print("You answered "+str(int(num_correct))+" questions correctly.")
if int(num_correct) >= 26:
    print("Congratulations you passed!")
else:
    print("You need to answer 26 questions (74%) correctly to pass, try again!")
