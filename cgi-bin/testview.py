import cgi
import model
import base


form = cgi.FieldStorage()
# quesData = model.getQuestions()
id = form.getvalue('id')
name = form.getvalue('name')
test_id = form.getvalue('test_id')
question = model.getQues(test_id)

print("""
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <title>Hello, world!</title>
    <style>
        .card {
            border: none;
        }
        .product {
            border: 1px solid #eee;
            margin: 10px;
        }
        #header {
             padding: 17px 0px;
            background-color: #5c5d61;
         }
        #header .ram{
            padding: 10px 74px;
        }
        h2 {
            font-size : 55px;
        }
    </style>
  </head>
  <body>
""")
base.header()
print("""
  <div class='container'>
    <h2 class='text-center'>Questions</h2>
    <hr>
    <h3 class='text-center'>Welcome {}</h3>
    <hr>
    <form action='resultView.py' method='post'>
    <input type='hidden' value={} name=id>
    <input type='hidden' value={} name=name>
    <input type='hidden' value={} name=test_id>
    <input type='hidden' value={} name='num_ques'>
    <ul class='list-group'>
  """.format(name,id,name,test_id,len(question)))
opt_id = 0
for i in range(len(question)):
    print("""
        <h4> Ques=>{} {}</h4>
    """.format(i+1,question[i][1]))
    for j in range(2,len(question[i]) -1):
        opt_id += 1
        print("""
            <li class='list-group-item'>
            <input type = 'radio' value={} name = 'ques_{}' id = '{}'>
            <label for = '{}'> {} </label>
             </li>
        """.format(question[i][j].replace(' ','+'),i+1,opt_id,opt_id, question[i][j]))


print("""
</form>
<br>
<button class='btn btn-primary'>Submit Test</button>
    </div>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>
""")