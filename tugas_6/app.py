from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.route('/keranjang-belanja')
def keranjang_belanja():
    return render_template('keranjang-belanja.html')

@app.route('/konfirmasi-pesanan')
def konfirmasi_pesanan():
    return render_template('konfirmasi-pesanan.html')

@app.route('/status-pesanan')
def status_pesanan():
    return render_template('status-pesanan.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login', methods = ["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    
    if request.method == "POST":
        username = "Amelia"
        password = "1234"
        
        data_input = request.form.to_dict()
        
        print (data_input['password'])
        
        if (data_input['username'] == username) and (data_input['password'] == password):
            return  redirect(url_for("admin"))
        else :
             return redirect(url_for("login"))
         
@app.route('/pesanan_masuk')
def pesanan_masuk():
    return render_template('pesanan_masuk.html')

@app.route('/tambah_pesanan')
def tambah_pesanan():
    return render_template('tambah_pesanan.html')
         
if __name__ == '__main__':
    app.run(debug=True)
