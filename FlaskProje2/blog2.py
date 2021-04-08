from types import resolve_bases
from MySQLdb import cursors
from MySQLdb.cursors import Cursor
from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
import flask
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt
import wtforms
from wtforms.fields.html5 import EmailField
from functools import wraps

# Kullanıcı giriş decorator'ı
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)

        else:
            flash("Lütfen Giriş Yapınız.","danger")
            return redirect(url_for("login"))
    return decorated_function


# Kullanıcı kayıt formu
class RegisterForm(Form):
    name = StringField("İsim Soyisim:")
# isim, soyisim 3 ile 20 karakter arasında olacak.
    username = StringField("Kullanıcı Adınız:", validators=[validators.length(min=4, max=20)])
    email = EmailField('Mail Adresiniz:', [validators.DataRequired(), validators.Email("Lütfen geçerli bir mail adresi giriniz.")])
    password = PasswordField("Parola Oluşturunuz:",validators=[validators.DataRequired(message="Lütfen Bir Parola Belirleyin..."),
    validators.EqualTo(fieldname="confirm",message="Parolanız Uyuşmamaktadır.") # iki şifrenin uyuşup, uyuşmadığını kontrol ediyoruz.
    ])
    confirm = PasswordField("Parolayı Yeniden Giriniz:")


# Login formu
class LoginForm(Form):
    username = StringField("Kullanıcı Adınız:")
    password = PasswordField("Parolanız:")



# Yazı Oluşturma Formu

class ArticleForm(Form):
    title = StringField("Başlık Giriniz:", validators=[validators.length(min=4, max=50)])
    content = TextAreaField("İçerik Giriniz:", validators=[validators.data_required()])



myapp = Flask(__name__)
myapp.secret_key= "blog2"


myapp.config["MYSQL_HOST"] = "localhost"
myapp.config["MYSQL_USER"] = "root"
myapp.config["MYSQL_PASSWORD"] = ""
myapp.config["MYSQL_DB"] = "blogdb"
myapp.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(myapp) #DB Bağlantısı kurulup, bir objeye tanımladık.





@myapp.route("/")
def index():
    return render_template("index.html")
    


@myapp.route("/about")
def about():
    return render_template("about.html")


@myapp.route("/articles")
def articles():
    cursor = mysql.connection.cursor()
    sorgu = "Select * From articles"
    result = cursor.execute(sorgu)
    
    if result > 0:
        articles = cursor.fetchall()
        return render_template("articles.html",articles = articles)
    else:
        return render_template("articles.html")



@myapp.route("/article/<string:id>")
def article(id):
    cursor = mysql.connection.cursor()
    sorgu = "Select * from articles where id = %s"
    result = cursor.execute(sorgu,(id,))
    if result > 0:
        article = cursor.fetchone()
        return render_template("article.html",article=article)
    else:
        return render_template("article.html")




@myapp.route("/delete/<string:id>")
@login_required
def delete(id):
    cursor = mysql.connection.cursor()
    sorgu = "Select * from articles where author = %s and id = %s"
    result = cursor.execute(sorgu,(session["username"],id))
    
    if result > 0:
        sorgu2 = "Delete from articles where id = %s"
        cursor.execute(sorgu2,(id,))
        mysql.connection.commit()
        return redirect(url_for("dashboard"))
    else:
        flash("Böyle Bir Makale Bulunmamaktadır.","warning")
        return redirect(url_for("index"))





@myapp.route("/edit/<string:id>", methods = ["GET","POST"])
@login_required
def update(id):
    if request.method == "GET":
        cursor = mysql.connection.cursor()
        sorgu = "Select * from articles where id = %s and author = %s"
        result = cursor.execute(sorgu,(id,session["username"]))
        if result == 0:
            flash("Makale Bulunmamaktadır.","danger")
            return redirect(url_for("index"))
        else:
            article = cursor.fetchone()
            form = ArticleForm()
            form.title.data = article["title"]
            form.content.data = article["content"]
            return render_template("update.html",form = form)
    else:
        form = ArticleForm(request.form)
        newTitle = form.title.data
        newContent = form.content.data
        sorgu2 = "Update articles Set title = %s, content = %s where id = %s"
        cursor = mysql.connection.cursor()
        cursor.execute(sorgu2,(newTitle,newContent,id))
        mysql.connection.commit()
        cursor.close
        flash("Makale Güncellendi","success")
        return redirect(url_for("dashboard"))





@myapp.route("/dashboard")
@login_required # Kullanıcı girişi var mı, yok mu kontrol etmesi için yukarıda tanımını yaptıgımız decorator sayesinde kontrol ediyoruz.
def dashboard():
    cursor = mysql.connection.cursor()
    sorgu = "Select * from articles where author = %s"
    result = cursor.execute(sorgu,(session["username"],))
    if result > 0:
        articles = cursor.fetchall()
        return render_template("dashboard.html",articles=articles)
    else:
        return render_template("dashboard.html")





# Yazı Ekleme
@myapp.route("/addarticle", methods= ["GET","POST"])
def addarticle():
    form = ArticleForm(request.form)
    if request.method == "POST" and form.validate():
        title = form.title.data
        content = form.content.data
        
        cursor = mysql.connection.cursor()
        sorgu = "Insert into articles(title,author,content) VALUES(%s,%s,%s)"
        cursor.execute(sorgu,(title,session["username"],content))
        mysql.connection.commit()
        cursor.close
        flash("Yazı Başarıyla Eklendi.", "success")
        return redirect(url_for("dashboard"))

    return render_template("addarticle.html",form = form)



# Kayıt Pathi
@myapp.route("/register", methods = ["GET","POST"]) # Bu pathe sadece get ve post request yapılabileceğini belirttik.
def register():
    form = RegisterForm(request.form)

    if request.method == "POST" and form.validate():
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(form.password.data)

        cursor = mysql.connection.cursor()
        sorgu = "Insert into users(name,email,username,password) VALUES(%s,%s,%s,%s)"
        cursor.execute(sorgu,(name,email,username,password))
        mysql.connection.commit()
        cursor.close
        flash("Başarıyla Kayıt Oldunuz.","success")
        return redirect(url_for("login")) # login fonksiyonuna gidecek.

    else:
        return render_template("register.html",form = form)




# Login İşlemi
@myapp.route("/login",methods =["GET","POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST":
        username = form.username.data
        password_entered = form.password.data
        cursor = mysql.connection.cursor()
        sorgu ="Select * From users where username = %s"
        result = cursor.execute(sorgu,(username,))

        if result > 0:
            data = cursor.fetchone()
            real_password = data["password"]
            if sha256_crypt.verify(password_entered,real_password):
                flash("Giriş Yapıldı.","success")
                session["logged_in"] = True
                session["username"] = username
                return redirect(url_for("index"))
            else:
                flash("Girilen Parola Yanlış.","danger")
                return redirect(url_for("login"))
        else:
            flash("Böyle Bir Kullanıcı Bulunmamaktadır.","danger")
            return redirect(url_for("login"))

    return render_template("login.html", form = form)


@myapp.route("/search",methods = ["GET","POST"])
def search():
    if request.method == "GET":
        return redirect(url_for("index"))
    else:
        keyword = request.form.get("keyword")
        cursor = mysql.connection.cursor()
        sorgu = "Select * from articles where title  like '%" + keyword +"%' "
        result = cursor.execute(sorgu)
        if result == 0:
            flash("Böyle bir makale bulunmamaktadır.","danger")
            return redirect(url_for("articles"))
        else:
            articles = cursor.fetchall()
            return render_template("articles.html",articles=articles)

#logout işlemi
@myapp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))



if __name__ == "__main__":
    myapp.run(debug=True)
