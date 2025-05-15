from flask import Flask, render_template, request, send_file, jsonify
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import os
import tempfile

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Giới hạn kích thước file: 16MB
app.config['UPLOAD_FOLDER'] = tempfile.gettempdir()

def encrypt_file(file_data, key):
    """Hàm mã hóa file sử dụng DES"""
    # Đảm bảo key đủ 8 bytes
    key = key.encode('utf-8')
    key = pad(key, 8)[:8]
    
    # Tạo đối tượng cipher DES
    cipher = DES.new(key, DES.MODE_ECB)
    
    # Pad dữ liệu để đủ block size
    padded_data = pad(file_data, 8)
    
    # Mã hóa và trả về kết quả
    return cipher.encrypt(padded_data)

def decrypt_file(file_data, key):
    """Hàm giải mã file sử dụng DES"""
    # Đảm bảo key đủ 8 bytes
    key = key.encode('utf-8')
    key = pad(key, 8)[:8]
    
    # Tạo đối tượng cipher DES
    cipher = DES.new(key, DES.MODE_ECB)
    
    # Giải mã
    decrypted_data = cipher.decrypt(file_data)
    
    # Bỏ padding và trả về kết quả
    try:
        return unpad(decrypted_data, 8)
    except ValueError:
        return decrypted_data

@app.route('/')
def index():
    """Trang chủ"""
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_file():
    """API xử lý mã hóa/giải mã file"""
    # Kiểm tra file upload
    if 'file' not in request.files:
        return jsonify({'error': 'Không có file được chọn'}), 400
    
    file = request.files['file']
    key = request.form.get('key', '')
    operation = request.form.get('operation')
    
    # Validate đầu vào
    if not file or file.filename == '':
        return jsonify({'error': 'Không có file được chọn'}), 400
    
    if not key:
        return jsonify({'error': 'Chưa nhập khóa'}), 400
    
    try:
        # Đọc dữ liệu file
        file_data = file.read()
        
        # Xử lý theo operation
        if operation == 'encrypt':
            processed_data = encrypt_file(file_data, key)
            output_filename = f'encrypted_{file.filename}'
        else:
            processed_data = decrypt_file(file_data, key)
            output_filename = f'decrypted_{file.filename}'
        
        # Lưu file tạm thời
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
        with open(output_path, 'wb') as f:
            f.write(processed_data)
        
        # Trả về file đã xử lý
        return send_file(
            output_path,
            as_attachment=True,
            download_name=output_filename
        )
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)