import cgi
import model
import base
import footer

form = cgi.FieldStorage()

id = form.getvalue("id")
password = form.getvalue("password")
data = model.login(id,password)
course = data[0][3]
name = data[0][1]

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
    <title>Student || Dashboard</title>
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
  <body>
  """)
base.header()
def showProfile():
    print("""
    <section id="dash">
      <div class="container"> 
        <h2>Student Dashboard</h2>
        <hr>
        <div class="row">
          <div class="col-md-4">
            <div class="card" style="width:20rem;">
              <img class="w-100"  src='../upload_profilepic/{}'>
            </div>
          </div>
          <div class="col-md-6">
            <h5> Name : {}</h5>
            <h5> Id : {}</h5>
            <h5> course : {}</h5>
            <h5> Semester : {}</h5> 
            <a href='giveTest.py?id={}&course={}&name={}' class="btn btn-dark">Give Test</a>    
          </div>     
        </div>
      </div>
      
    </section>
     """.format(data[0][-1],data[0][1],data[0][0],data[0][3],data[0][4],id,course,name))


if isinstance(data,str):
    print("<h2>Login Failed....</h2>")
    print("<a href='../index.html'>Try Again</a>")

else:
    showProfile()

footer.footer()
print("""
</body>
</html>
""")




