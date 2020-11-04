import cgi
import model


form = cgi.FieldStorage()

name = form.getvalue('name')
id  = form.getvalue('id')
password = form.getvalue('password')
course = form.getvalue('course')
semester = form.getvalue('semester')
picture = form['profile']


user = model.register(id,name,password,course,semester,picture)
data = model.login(id,password)


print("""
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <script src="https://kit.fontawesome.com/b06605e970.js"></script>
    <link href="https://fonts.googleapis.com/css?family=Amiri&display=swap" rel="stylesheet">
    <title>Student Test Engine</title>
    <style>
        #reg {
            text-align: center;
            margin-top: 50px;
        }
        #reg .succes i{
            font-size: 70px;
            color: green;
        }
        #reg .succes h3 {
            font-family: 'Amiri', serif;
            font-size: 35px;
        }
        h4 {
            font-family: 'Tinos', serif;
        }
    </style>
  </head>
  <body>
  """)
def userId():
    print("""   
         <div id="reg">
        <div class="container">
            <div class="succes">
                <i class="fas fa-check-circle"></i>
                <h3>Registration Successfully</h3>
                <div class="row">
                    <div class="col-md-8">
                        <h4>Name : {}</h4>
                        <h4>Your Login Id : {}</h4>
                        <h4>Password : {}</h4>
                        <a href="./index.html" class="btn btn-danger">Login Now</a>
                    </div>
                </div>

            </div>
        </div>
    </div>
    
    """.format(data[0][1],data[0][0],data[0][2]))

if isinstance(user,str):
    # print("<h2>Registered Successfully...</h2>")
    print("<a href='../index.html'>Login Now</a>")

else:
    userId()


print("""
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
  </body>
</html>
""")
