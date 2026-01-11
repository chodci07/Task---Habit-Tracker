from flask import render_template, request

def init_app(app):

    @app.route("/")
    def home():
        return render_template("index.html")
    
    @app.route("/login", methods=["GET", "POST"])
    def login():
        email = request.form["email"]
        password = request.form["password"]
        

        return render_template("login.html")
    
    @app.route("/register", methods=["GET", "POST"])
    def register():
        error = None

        if request.method == "POST":
            email = request.form["email"]
            password = request.form["password"]
            password2 = request.form["password2"]

            if password != password2:
                error = "Hesla se neshodují"
        
            else:
                print("USER OK:", email)

        return render_template("register.html", error=error)