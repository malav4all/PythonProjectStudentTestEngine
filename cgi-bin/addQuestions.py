import cgi
import base
import footer
import model
form = cgi.FieldStorage()

Tid = form.getvalue('Tid')

if form.getvalue('test'):
    form_state = True
    subject = form.getvalue('sub')
    course = form.getvalue('course')
    model.insertTest(Tid, subject, course)
else:
    form_state = False

if form.getvalue('test_id'):
    test_id = form.getvalue('test_id')
    ques = form.getvalue('question')
    opt_1 = form.getvalue('option_1')
    opt_2 = form.getvalue('option_2')
    opt_3 = form.getvalue('option_3')
    opt_4 = form.getvalue('option_4')
    ans = form.getvalue('answere')
    model.insertQuestion(test_id,ques,opt_1,opt_2,opt_3,opt_4,ans)

data = model.getTest(Tid)

print("""
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
        <title>Student Test Engine</title>
        <script src="../assests/javascript/main.js"></script>
        <link rel="stylesheet" href="../assests/stylesheet/main.css">

        <style>
        #header {
             padding: 17px 0px;
             background-color: #5c5d61;
        }
        #header .ram{
        padding: 10px 74px;
        }
        .genrate {
            text-align: center;
            margin: 132px 0px;
        }

    </style>
  </head>
  <body>
  """)
base.header()

if not form_state:
    print("""
     <section id="test_id">
      <div class="container">
        <form action="addQuestions.py" method="post">
          <input type='hidden' name='Tid' value={}>
          <input type='hidden' value='create' name='test'>
          <hr>
          <h3 class="text-center">Select Subject To create a Test </h3>
          <div class="form-row">
            <div class="col">
               <select class="form-control" name="sub">
                <option>Choose Subject</option>
                <option>Java</option>
                <option>JavaScript</option>
                <option>Python</option>
                <option>Php</option>
                <option>C++</option>
                <option>.net</option>
              </select>
            </div>
            <div class="col">
              <select class="form-control" name="course">
                <option>Choose Course</option>
                <option>BCA</option>
                <option>MCA</option>
                <option>Btech</option>
                <option>Mtech</option>
                <option>BBA</option>
                <option>MBA</option>
              </select>
            </div>
            <input type="submit" value="Insert Question" class="btn btn-primary">
        </form>
      </div>
      <hr>
    </section>
    """.format(Tid))




print("""
    <h2>Start Inserting Questions</h2>
    <form action="addQuestions.py" method="post">
     <input type='hidden' value={} name='Tid'>
     <table cellpadding=10>
            <tr>
                <td>Enter Test ID</td>
                <td>
                    <select name='test_id'>
                    """)
for i in range(len(data)):
    print("""
    <option value = {}>{}</option>
    """.format(data[i][0], data[i][0]))

print("""
        </select>
        </td>
        </tr>
        </table>
      <div class="form-group">
        <label for="ques">Enter question</label>
        <input type="text" class="form-control" name="question" id="ques"  placeholder="Enter the question here" >
      </div>
      <div class="form-row">
        <div class="form-group col-md-6">
          <label for="opt_1">Option 1</label>
          <input type="text" class="form-control" name="option_1" id="opt_1" >
        </div>
        <div class="form-group col-md-6">
          <label for="opt_2">Option 2</label>
          <input type="text" class="form-control" name="option_2" id="opt_2" >
        </div>
      </div>
      <div class="form-row">
        <div class="form-group col-md-6">
          <label for="opt_3">Option 3</label>
          <input type="text" class="form-control"  name="option_3"  id="opt_3">
        </div>
        <div class="form-group col-md-6">
          <label for="opt_4">Option 4</label>
          <input type="text" class="form-control" name="option_4" id="opt_4">
        </div>
      </div>
      <div class="form-group">
        <label for="ans">Enter Answere</label>
        <input type="text" class="form-control" name="answere" id="ans" placeholder="Enter the answer here" >
      </div>
      <button class="btn btn-primary w-25" id="ins_ques" value="submit">Submit</button>
      </form>
  </div>
""")




footer.footer()
print("""
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
  </body>
</html>
""")