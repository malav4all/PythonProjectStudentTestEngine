import cgi
import model
import base
import footer

form = cgi.FieldStorage()
Tid = form.getvalue('Tid')
Password = form.getvalue('Password')
data = model.t_login(Tid,Password)
name = data[0][0]
all_test = model.fetchAllTest()
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
print("""
<h1 class="text-center">Login Successful</h1>
    <h3 class="text-center">Welcome {}</h2>
""".format(name))


    # Query String
print("""
<div class="text-center">
    <a href='teacherLoginDashboard.py?Tid={}&name={}' class="btn btn-info">Teachers Dashboard</a>
</div>
""".format(Tid,name))

print("""
<hr>
<h2 class="text-center">All Teacher Test created by  Here : </h2>
<table width='100%' border=2 cellpadding=10>
    <tr>
        <th>Test ID</th>
        <th>Subject</th>
        <th>Grade</th>
        <th>Visit Test</th>
    </tr>
""")
for i in range(len(all_test)):
    print("""
        <tr>
            <td> {} </td>
            <td> {} </td>
            <td> {} </td>
            <td> Visit Test </td>
    """.format(all_test[i][0], all_test[i][2], all_test[i][3]))

print("</table>")

footer.footer()

print("""
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
  </body>
</html>
""")
