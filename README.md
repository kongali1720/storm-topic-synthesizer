<h1 align="center">🌩️ STORM — Synthesis of Topic Outlines through Retrieval Methods</h1>

<p align="center">
  <img src="https://img.shields.io/github/repo-size/kongali1720/storm-topic-synthesizer?style=flat-square" />
  <img src="https://img.shields.io/github/stars/kongali1720/storm-topic-synthesizer?style=flat-square" />
  <img src="https://img.shields.io/github/forks/kongali1720/storm-topic-synthesizer?style=flat-square" />
  <img src="https://img.shields.io/github/license/kongali1720/storm-topic-synthesizer?style=flat-square" />
  <img src="https://img.shields.io/badge/python-3.8%2B-blue?style=flat-square" />
</p>

> **STORM** adalah alat pintar yang menyusun kerangka/topik secara otomatis dari input kata kunci, menggunakan metode pencarian dan kekuatan AI (GPT). 🚀

<p align="center"> Made with 💻 + ☕ by <b>Kongali1720</b> </p>


## 🎬 Demo

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3MTgxbXZsd3p5bm90MG1ocTRyaXpneXR0NmIzZ2oyYzZ4eXZ5cnpqMiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/LyV4cw0vDtAgc8xTHQ/giphy.gif" alt="STORM Demo" />
</p>

---

## ✨ Fitur Utama

- 🔍 **Web Retrieval** (mocked untuk sekarang, bisa pakai API nanti)
- 🧠 **GPT-3.5/4 Integration** via LangChain
- 🗣️ **Input Natural Language**
- 📜 **Multi-Level Outline Generator**
- 🖥️ **Command Line Interface**
- 🧪 **Contoh & Testing Outline JSON**
- ☁️ **Roadmap: Web UI, Export PDF/Markdown**

---

## 📦 Struktur Proyek

storm-topic-synthesizer/

├── storm_core/

│ ├── retriever.py # Ambil referensi (simulasi atau API)

│ ├── synthesizer.py # Gunakan GPT untuk membuat outline
│
├── cli.py # CLI interface

├── requirements.txt # Dependency

├── examples/

│ └── example_outline.json

└── README.md

---

## 🚀 Cara Instalasi

1. Clone repo ini:

       git clone https://github.com/kongali1720/storm-topic-synthesizer.git
   
       cd storm-topic-synthesizer

2. Install dependensi:
   
        pip install -r requirements.txt

3. Set API Key GPT:

       export OPENAI_API_KEY="your-openai-key"

# ▶️ Cara Menjalankan

      python cli.py

Contoh Input:

    Masukkan topik utama: Teknologi Blockchain untuk Pemula

## 🌐🛡️ Kerangka Contoh: Keamanan Siber untuk Remaja

| 🔢 Bagian | 🧩 Subbagian | 📚 Judul |
|:---------:|:------------:|----------|
| **I. 🚀 Pendahuluan** | **A** | 🔍 Apa Itu Keamanan Siber? |
|                      | **B** | 👩‍💻 Kenapa Penting Buat Kita (Remaja)? |
| **II. ⚠️ Ancaman Umum di Dunia Digital** | **A** | 🎣 Phishing: Jangan Sampai Kecantol! |
|                                          | **B** | 🦠 Malware: Virus Ga Cuma di Dunia Nyata |
|                                          | **C** | 💔 Cyberbullying: Komentar Bisa Menyakiti |
| **III. 🔐 Tips Dasar untuk Keamanan Akun** | **A** | 🔑 Bikin Password Seperti Ninja! |
|                                           | **B** | ✅ Aktifin Autentikasi 2 Langkah |
|                                           | **C** | 🧐 Hati-Hati Klik Link & Lampiran Asal |
| **IV. 🧠 Pentingnya Kesadaran Digital Sejak Dini** | **A** | 🏫 Belajar Keamanan Siber di Sekolah |
|                                                 | **B** | 👨‍👩‍👧 Peran Orang Tua & Guru Itu Penting |
| **V. 📚 Sumber Daya & Referensi** | **A** | 🌐 Website Edukasi Keren |
|                                | **B** | 💡 Kursus Online Buat Nambah Ilmu |

---

# 🔧 Konfigurasi .env (opsional)

Gunakan .env untuk menyimpan key secara aman:

      OPENAI_API_KEY=your-openai-key

---


## 🧠 Teknologi yang Digunakan

| 💻 No | 🛠️ Teknologi | 📌 Keterangan |
|:----:|:------------:|--------------|
| 1 | **Python 3.8+** | Bahasa utama |
| 2 | **LangChain** | Integrasi pemrosesan informasi |
| 3 | **OpenAI GPT** | Mesin AI untuk sintesis topik |
| 4 | **CLI-based Interface** | Antarmuka awal berbasis terminal |
| 5 | **(Coming Soon) Flask Web UI** | UI berbasis web interaktif |

---

## 🔮 Roadmap

| 🔢 Tahap | 🎯 Fitur | 📈 Status |
|:-------:|:--------:|:---------:|
| 1 | **Outline Generator berbasis GPT** | ✅ Selesai |
| 2 | **Integrasi LangChain** | ✅ Selesai |
| 3 | **Web UI dengan Flask** | 🔄 Dalam Pengembangan |
| 4 | **Fitur Export (.md / .docx / .pdf)** | 🧩 Direncanakan |
| 5 | **Auto Web Crawler / Search (Opsional)** | 🧪 Eksperimen |
| 6 | **Multilingual Support (ID / EN)** | 🌍 Segera Hadir |

---

## 🙌 Kontribusi

Mau bantu bikin STORM makin dahsyat?  
Yuk open pull request atau DM langsung!  
Kita bikin edukasi digital makin powerful bareng-bareng! 💪

---

# 📜 License

MIT License — Bebas digunakan, dimodifikasi, dan dikembangkan untuk kebaikan 🌍  
MIT License - feel free to fork, enhance, and contribute!
Tetap sertakan atribusi ya bro! ✌️

---

> Dibuat dengan ❤️ oleh [@kongali1720](https://github.com/kongali1720)  

# 🤝 Kontribusi

  Pull request dan issue sangat diterima!
  Bintang ⭐ juga bikin semangat nambahin fitur baru! 💪
  
---

# ❤️ Special Thanks

  Made with 🔥 by KONGALI1720 Cyber Force.

  “Scan like a ghost, strike like a hammer.”

---

# ✅ Gaspol coding squad Indonesia! 🚀💻

- Halo, Sobat Koding!

- Kumpulan mini project Python yang gak bikin ngantuk!

- Belajar sambil praktek langsung, cocok buat yang suka action daripada teori.

- Langsung eksekusi, langsung paham.

---

<h3 align="center">💡 ☕ Traktir Kopi & Nasi Padang ama nasi Gorengnya ya cuy! 😄</h3>

<div align="center">

## Dukung terus biar semangat bikin karya edukatif lainnya...

# 💡 ☕  [Buy Me a Coffee via PayPal](https://www.paypal.com/paypalme/bungtempong99)  

Support with ☕ so I can buy 🍜 and keep being 🧠!

---

<h2>📫 Let’s Connect Like Hackers</h2>

| Platform | Detail |
|:--------|:-------|
| GitHub  | [kongali1720](https://github.com/kongali1720) |
| Email   | [kongali1720@gmail.com](mailto:kongali1720@gmail.com) |
| Site    | [Coming soon — stay curious... ](https://kongali1720.github.io)|

---

# ❤️  💻 INITIATING HUMANITY MODE... for Down Syndrome ❤️
| Item        | Keterangan |
|:------------|:-----------|
| 🎯 Target   | Anak-anak Pejuang Down Syndrome |
| 📡 Status   | Butuh Dukungan |
| 🧠 Response | Buka Hati + Klik Link = Satu Senyum Baru |

  Mereka bukan berbeda — mereka dilahirkan untuk mengajarkan dunia tentang cinta yang murni dan kesabaran yang luar biasa.

<p align="center" style="font-size: 1.5rem;">
  <a href="https://mydonation4ds.github.io/" target="_blank" style="display: inline-block;">
    <img 
      src="https://img.shields.io/badge/SUPPORT--NOW-%23FF6600?style=for-the-badge&logo=heart&logoColor=white&labelColor=white&color=FF6600" 
      alt="Support Now" 
      style="width: 300px; height: auto;" 
    />
  </a>
</p>

---

| Quotes | Penjelasan |
|:-------|:-----------|
| 🧡 "**Jadi hacker hati bukan cuma soal kode... tapi juga soal peduli.**" |  |
| 🧠 🎧"Ngoding boleh sambil senyum, asal jangan inject SQL sambil ngambek!" |  |


---

  <section id="dukungan-pembayaran">
    <h2>💳 Dukungan Pembayaran DONASINYA </h2>
    <table class="payment" aria-label="Metode Pembayaran">
      <thead>
        <tr>
          <th>Visa</th>
          <th>Mastercard</th>
          <th>PayPal</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Visa_Logo.png/120px-Visa_Logo.png" alt="Logo Visa" /></td>
          <td><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Mastercard-logo.svg/120px-Mastercard-logo.svg.png" alt="Logo Mastercard" /></td>
          <td><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/PayPal_logo.svg/120px-PayPal_logo.svg.png" alt="Logo PayPal" /></td>
        </tr>
      </tbody>
    </table>
  </section>

---

Kalau project ini bantu kamu, jangan lupa kasih bintang ⭐ dan share ke temen-temen ya!  
Follow @kongali1720 buat diskusi dan update seru lainnya 🔥

---

<div class="twitter-badge" style="text-align: center; margin-top: 20px;">
  <a href="https://twitter.com/kongali1720" target="_blank" rel="noopener noreferrer" aria-label="Follow kongali1720 on Twitter">
    <img src="https://img.shields.io/twitter/follow/kongali1720?style=social" alt="Twitter Follow Badge" />
  </a>
</div>

<footer>
