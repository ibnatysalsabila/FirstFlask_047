from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nim = request.form['nim']
        nama = request.form['nama']
        tempat_lahir = request.form['tempat_lahir']
        tanggal_lahir = request.form['tanggal_lahir']
        program_studi = request.form['program_studi']
        alamat = request.form['alamat']
        nomor_telepon = request.form['nomor_telepon']
        email = request.form['email']
        
        
        return f'NIM: {nim}, Nama: {nama}, Tempat Lahir: {tempat_lahir}, Tanggal Lahir: {tanggal_lahir}, Program Studi: {program_studi}, Alamat: {alamat}, Nomor Telepon: {nomor_telepon}, Email: {email}'

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)