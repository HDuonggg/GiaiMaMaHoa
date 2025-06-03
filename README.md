# DES File Encryptor Web App

Ứng dụng web này cho phép bạn mã hóa và giải mã file sử dụng thuật toán DES (Data Encryption Standard). Tất cả quá trình xử lý file đều diễn ra trên máy chủ của bạn, đảm bảo an toàn và riêng tư.

## Tính năng

- **Mã hóa file**: Tải lên file và mã hóa bằng khóa DES do bạn nhập.
- **Giải mã file**: Tải lên file đã mã hóa và giải mã bằng đúng khóa đã sử dụng.
- **Giao diện hiện đại**: Thiết kế đẹp, dễ sử dụng, hỗ trợ tiếng Việt.
- **Bảo mật**: Không lưu trữ file trên server lâu dài, chỉ xử lý tạm thời.

## Cấu trúc dự án
Collecting workspace information```markdown
# DES File Encryptor Web App

Ứng dụng web này cho phép bạn mã hóa và giải mã file sử dụng thuật toán DES (Data Encryption Standard). Tất cả quá trình xử lý file đều diễn ra trên máy chủ của bạn, đảm bảo an toàn và riêng tư.

## Tính năng

- **Mã hóa file**: Tải lên file và mã hóa bằng khóa DES do bạn nhập.
- **Giải mã file**: Tải lên file đã mã hóa và giải mã bằng đúng khóa đã sử dụng.
- **Giao diện hiện đại**: Thiết kế đẹp, dễ sử dụng, hỗ trợ tiếng Việt.
- **Bảo mật**: Không lưu trữ file trên server lâu dài, chỉ xử lý tạm thời.

## Cấu trúc dự án

```
.
├── app.py                  # Flask backend xử lý mã hóa/giải mã
├── requirements.txt        # Thư viện Python cần thiết
├── templates/
│   └── index.html          # Giao diện web (Flask render)
├── aes-web-app/
│   ├── public/
│   │   └── index.html      # Giao diện React (nếu dùng frontend riêng)
│   ├── src/
│   │   ├── app.ts          # React app chính
│   │   ├── components/     # Các component React
│   │   ├── styles/         # CSS
│   │   └── utils/          # Hàm AES (nếu dùng frontend AES)
│   ├── package.json        # Cấu hình npm
│   └── tsconfig.json       # Cấu hình TypeScript
└── .vscode/                # Cấu hình cho VSCode
```

## Hướng dẫn cài đặt và chạy

### 1. Chạy backend Flask

```bash
pip install -r requirements.txt
python app.py
```

- Mặc định server chạy tại `http://localhost:5000`

### 2. (Tùy chọn) Chạy frontend React

Nếu bạn muốn phát triển hoặc chạy giao diện React riêng:

```bash
cd aes-web-app
npm install
npm start
```

- Ứng dụng sẽ chạy tại `http://localhost:3000`

## Sử dụng

1. Truy cập trang web.
2. Chọn file cần mã hóa/giải mã.
3. Nhập khóa (8 ký tự, nên đủ mạnh).
4. Chọn thao tác: Mã hóa hoặc Giải mã.
5. Nhấn "Xử lý File" và tải về file kết quả.

## Yêu cầu

- Python 3.6+
- Node.js (nếu chạy frontend React)
- Trình duyệt hiện đại

## Bản quyền

MIT License.

---

**Liên hệ:** Nếu có thắc mắc hoặc góp ý, vui lòng liên hệ qua sansieuga02@gmail.com
```
![image](https://github.com/user-attachments/assets/65893673-5566-4a31-b46a-56690b8b760b)

