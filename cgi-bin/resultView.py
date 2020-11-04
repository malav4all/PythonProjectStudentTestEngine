import cgi
import model
import base

form = cgi.FieldStorage()
id = form.getvalue('id')
name  = form.getvalue('name')
test_id = form.getvalue('test_id')
num_ques = form.getvalue('num_ques')

keys = form.keys()
answere = []
keys = sorted(keys)
for i in range(len(keys)):
    answere.append(form.getvalue(keys[i]))


# count,correct_ans = model.checkAns(answere,test_id)
correct_ans = model.checkAns(answere,test_id)

# model.storeResult(id,test_id)
answers = []
attempted = 0
unattempted = 0
for i in range(int(num_ques)):
    ans = form.getvalue('ques_{}'.format(i+1))
    if ans:
        answers.append(str(ans).replace('+',' '))
        attempted += 1
    else: unattempted += 1

print("""
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <title>Result</title>
  </head>
  <body>
  <div class='container'>
  <h2 class='text-center'>{} Your Result is Declared</h2>
  <hr>
    <h2 class='text-center'>Questions</h2>
    <ul class='list-group'>
  """.format(name))
count = 0
for i in range(len(correct_ans)):
    if correct_ans[i][0] == answers[i]:
        count += 1
wrong_count = 0
for i in range(len(answers)):
    if answers[i] == correct_ans[i][0]:
        col = 'green'
    else:
        col = 'red'
        wrong_count += 1
    print("""
        <li class='list-group-item'>
            <h5 style='color:{};'>Ques {} => Your ans : {} | Correct ans : {}</h5>
        </li>
    """.format(col,i+1,answers[i],correct_ans[i][0]))

model.storeResult(id,name,test_id,count)

print("""
     <h1 class="text-center">Test Submitted</h1>
    <hr>
    <h2>Number of questions : {}</h2>
    <h4>Attempted : {}</h4>
    <h4>Unattempted : {}</h4>
      """.format(num_ques, attempted, unattempted))


print("</ul>")
print("<br>")
print("<h4 class='text-center'>Final Result :</h4>")
print("<h5 class='text-center'>Correct Ans : {}".format(count))
print("<h5 class='text-center'>Wrong Ans : {}".format(wrong_count))
print("<h5 class='text-center'>Total : {}".format(count + wrong_count))
print("""
</body>
</html>
""")