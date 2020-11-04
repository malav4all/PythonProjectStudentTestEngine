import cgi
import model
import base
import footer

form = cgi.FieldStorage()

id = form.getvalue('id')
name = form.getvalue('name')
course = form.getvalue('course')
subjects = model.getSubjects(course)


print("""
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link href="https://fonts.googleapis.com/css?family=Dancing+Script|Shadows+Into+Light&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../assests/stylesheet/main.css">
    <title>Select||Subjects</title>
    <style>
    body {
    overflow-x :hidden;
    }
    #header {
    padding: 17px 0px;
    background-color: #5c5d61;
    }
    #header .ram{
    padding: 10px 74px;
    }
    #dash {
        border: 1px solid #3333;
        margin: 49px 100px;
      }
      #dash h2 {
          text-align: center;
          font-family: 'Dancing Script', cursive;
          font-size: 67px;
          font-weight: bold;
      }
      #dash h5 {
        font-family: 'Dancing Script', cursive;
        font-weight: bold;
      }
    </style>
  </head>
  <body>   """)

base.header()

print("""
    <h2 class="text-center">Start Test</h1>
    <hr>
    <div class="text-center">
    <form action='showTest.py' method='post'>
        <input type='hidden' value={} name='course'>
        <input type='hidden' value={} name='id'>
        <input type='hidden' value={} name='name'>
        <table class="text-center">
            <tr>
                <td>Choose Subject</td>
                <td>
                    <select name='subject' class="form-control">
                        <option>Choose Subject</option>""".format(course,id,name))


for i in range(len(subjects)):
    print("""
    <option value={}>{}</option>
    """.format(subjects[i][0],subjects[i][0]))

print("""
                    </select>
                </td>
            </tr>
            <tr>
                <td></td>
                <td>
                    <input type='submit' class="btn btn-info">
                </td>
            </tr>
        </table>
    </form>
    </div>
""".format(id))
footer.footer()

print("""
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
  </body>
</html>
""")