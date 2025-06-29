# 🌐 FUTUREINTERN TASK 2

**Task**: Build a file upload/download portal with AES encryption to secure files at rest and in transit.  
**Skills Gained**: Web development, encryption implementation, secure file handling, key management.  
**Tools**: Python Flask, PyCryptodome, Git & GitHub, Postman/curl.  
**Deliverable**: GitHub repo, walkthrough video, and a security overview document.

---

# 🔐 Secure File Sharing System (Flask + AES Encryption)

This is a secure file upload and download portal built with **Python Flask** that uses **AES encryption** to protect files both at rest and in transit.

---

## 🚀 Features

- 🔐 Upload and store encrypted files using AES-128
- 🧾 View a list of encrypted files
- ⬇️ Download encrypted files
- 🔓 Decrypt and download files on request
- 📂 Files saved in `uploads/` (encrypted) and `decrypted/` (temporarily)
- 🧠 Simple and user-friendly interface
- 🧪 Test with Postman or browser

---

## 🛠️ Tech Stack

| Component      | Technology            |
|----------------|------------------------|
| 💻 Backend      | Python Flask           |
| 🔐 Encryption   | AES (ECB, PyCryptodome) |
| 🎨 Frontend     | HTML (Jinja2 Templates) |
| 📦 Storage      | Local FileSystem       |
| 🧪 Testing Tools| Postman / curl         |

---

## 🔐 Encryption Details

- **Algorithm**: AES (Advanced Encryption Standard)
- **Mode**: ECB (Electronic Codebook)
- **Key Length**: 128-bit
- **Library**: PyCryptodome
- **Padding**: Manual (space-padded to 16-byte blocks)

⚠️ **Note**: ECB mode is used for simplicity. In production, switch to AES-CBC or AES-GCM for stronger security.

---

## 🧩 How It Works

1. **Upload**: User uploads a file using the home page.
2. **Encrypt**: The file is encrypted using AES and stored in the `uploads/` folder.
3. **View Files**: User can visit `/files` to see a list of all encrypted files.
4. **Download Encrypted**: User can download the raw AES-encrypted file.
5. **Decrypt & Download**: User clicks decrypt to generate and download a usable (decrypted) version.

---

## 📁 Folder Structure

