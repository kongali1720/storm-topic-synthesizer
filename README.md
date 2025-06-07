<h1 align="center">🌩️ STORM — Synthesis of Topic Outlines through Retrieval Methods</h1>

<p align="center">
  <img src="https://img.shields.io/github/repo-size/kongali1720/storm-topic-synthesizer?style=flat-square" />
  <img src="https://img.shields.io/github/stars/kongali1720/storm-topic-synthesizer?style=flat-square" />
  <img src="https://img.shields.io/github/forks/kongali1720/storm-topic-synthesizer?style=flat-square" />
  <img src="https://img.shields.io/github/license/kongali1720/storm-topic-synthesizer?style=flat-square" />
  <img src="https://img.shields.io/badge/python-3.8%2B-blue?style=flat-square" />
</p>

> **STORM** adalah alat pintar yang menyusun kerangka/topik secara otomatis dari input kata kunci, menggunakan metode pencarian dan kekuatan AI (GPT). 🚀  
>  
> **STORM** is a smart tool that automatically generates topic outlines from keyword inputs, using retrieval methods and AI power (GPT). 🚀

<p align="center"> Made with 💻 + ☕ by <b>Kongali1720</b> </p>

---

## 🎬 Demo / Demo

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3MTgxbXZsd3p5bm90MG1ocTRyaXpneXR0NmIzZ2oyYzZ4eXZ5cnpqMiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/LyV4cw0vDtAgc8xTHQ/giphy.gif" alt="STORM Demo" />
</p>

---

## ✨ Fitur Utama / Key Features

- 🔍 **Web Retrieval** (mocked for now, can use API later)  
- 🧠 **GPT-3.5/4 Integration** via LangChain  
- 🗣️ **Input Natural Language**  
- 📜 **Multi-Level Outline Generator**  
- 🖥️ **Command Line Interface**  
- 🧪 **Example & Testing Outline JSON**  
- ☁️ **Roadmap: Web UI, Export PDF/Markdown**

---

## 📦 Struktur Proyek / Project Structure

storm-topic-synthesizer/


├── storm_core/

│ ├── retriever.py # Fetch references (mock or API)

│ ├── synthesizer.py # Use GPT to create outline

├── cli.py # CLI interface

├── requirements.txt # Dependencies

├── examples/

│ └── example_outline.json

└── README.md

---


---

## 🚀 Cara Instalasi / Installation Guide

1. Clone this repo:

       git clone https://github.com/kongali1720/storm-topic-synthesizer.git  
       cd storm-topic-synthesizer

2. Install dependencies:

       pip install -r requirements.txt

3. Set GPT API Key:

       export OPENAI_API_KEY="your-openai-key"

---

## ▶️ Cara Menjalankan / How to Run

    python cli.py

Example Input:

    Masukkan topik utama: Teknologi Blockchain untuk Pemula  
    (Enter main topic: Blockchain Technology for Beginners)

---

## 🌐🛡️ Contoh Kerangka / Sample Outline: Cybersecurity for Teens

| 🔢 Bagian / Section | 🧩 Subbagian / Subsection | 📚 Judul / Title |
|:-------------------:|:-------------------------:|:----------------|
| **I. 🚀 Pendahuluan / Introduction** | **A** | 🔍 Apa Itu Keamanan Siber? / What is Cybersecurity? |
|                                   | **B** | 👩‍💻 Kenapa Penting Buat Kita (Remaja)? / Why It Matters to Teens? |
| **II. ⚠️ Ancaman Umum di Dunia Digital / Common Digital Threats** | **A** | 🎣 Phishing: Jangan Sampai Kecantol! / Phishing: Don’t Get Hooked! |
|                                                         | **B** | 🦠 Malware: Virus Ga Cuma di Dunia Nyata / Malware: Viruses Aren’t Just Real-World |
|                                                         | **C** | 💔 Cyberbullying: Komentar Bisa Menyakiti / Cyberbullying: Words Can Hurt |
| **III. 🔐 Tips Dasar untuk Keamanan Akun / Basic Account Security Tips** | **A** | 🔑 Bikin Password Seperti Ninja! / Make Passwords Like a Ninja! |
|                                                        | **B** | ✅ Aktifin Autentikasi 2 Langkah / Enable Two-Factor Authentication |
|                                                        | **C** | 🧐 Hati-Hati Klik Link & Lampiran Asal / Beware of Suspicious Links & Attachments |
| **IV. 🧠 Pentingnya Kesadaran Digital Sejak Dini / Importance of Early Digital Awareness** | **A** | 🏫 Belajar Keamanan Siber di Sekolah / Learn Cybersecurity at School |
|                                                  | **B** | 👨‍👩‍👧 Peran Orang Tua & Guru Itu Penting / Parents & Teachers Role Matters |
| **V. 📚 Sumber Daya & Referensi / Resources & References** | **A** | 🌐 Website Edukasi Keren / Cool Educational Websites |
|                                         | **B** | 💡 Kursus Online Buat Nambah Ilmu / Online Courses to Learn More |

---

## 🔧 Konfigurasi .env (opsional) / Optional .env Configuration

Store your key safely with `.env`:

    OPENAI_API_KEY=your-openai-key

---

## 🧠 Teknologi yang Digunakan / Technologies Used

| 💻 No | 🛠️ Teknologi / Technology | 📌 Keterangan / Description |
|:-----:|:-------------------------:|:---------------------------|
| 1 | **Python 3.8+**          | Bahasa utama / Main language |
| 2 | **LangChain**            | Integrasi pemrosesan informasi / Information processing integration |
| 3 | **OpenAI GPT**           | Mesin AI untuk sintesis topik / AI engine for topic synthesis |
| 4 | **CLI-based Interface**  | Antarmuka awal berbasis terminal / Initial terminal-based UI |
| 5 | **(Coming Soon) Flask Web UI** | UI berbasis web interaktif / Interactive web UI |

---

## 🔮 Roadmap

| 🔢 Tahap / Phase | 🎯 Fitur / Feature | 📈 Status / Status |
|:----------------:|:-----------------:|:-----------------:|
| 1 | **Outline Generator berbasis GPT / GPT-based Outline Generator** | ✅ Selesai / Done |
| 2 | **Integrasi LangChain / LangChain Integration** | ✅ Selesai / Done |
| 3 | **Web UI dengan Flask / Flask Web UI** | 🔄 Dalam Pengembangan / In Progress |
| 4 | **Fitur Export (.md / .docx / .pdf) / Export Feature (.md / .docx / .pdf)** | 🧩 Direncanakan / Planned |
| 5 | **Auto Web Crawler / Search (Opsional) / Optional Auto Web Crawler/Search** | 🧪 Eksperimen / Experimental |
| 6 | **Multilingual Support (ID / EN)** | 🌍 Segera Hadir / Coming Soon |

---

## 🙌 Kontribusi / Contribution

Mau bantu bikin STORM makin dahsyat?  
Want to help make STORM even better?  

Yuk open pull request atau DM langsung!  
Open a pull request or DM me directly!  

Kita bikin edukasi digital makin powerful bareng-bareng! 💪  
Let’s make digital education more powerful together! 💪

---

## 📜 Lisensi / License

MIT License — Bebas digunakan, dimodifikasi, dan dikembangkan untuk kebaikan 🌍  
MIT License — Feel free to use, modify, and develop for good 🌍  

Tetap sertakan atribusi ya bro! ✌️  
Please keep attribution! ✌️

---

> Dibuat dengan ❤️ oleh [@kongali1720](https://github.com/kongali1720)  
> Made with ❤️ by [@kongali1720](https://github.com/kongali1720)

---

## 🤝 Kontribusi

Pull request dan issue sangat diterima!  
Pull requests and issues are very welcome!  

Bintang ⭐ juga bikin semangat nambahin fitur baru! 💪  
Stars ⭐ also boost motivation to add new features! 💪

---

## ❤️ Special Thanks

Made with 🔥 by KONGALI1720 Cyber Force.  

“Scan like a ghost, strike like a hammer.”  

---

## ✅ Gaspol coding squad Indonesia! 🚀💻

- Halo, Sobat Koding!  
- Hey, Coding Friends!

- Kumpulan mini project Python yang gak bikin ngantuk!  
- Collection of Python mini projects that won’t bore you!

- Belajar sambil praktek langsung, cocok buat yang suka action daripada teori.  
- Learn by doing, perfect for those who prefer action over theory.

- Langsung eksekusi, langsung paham.  
- Run it directly, understand instantly.

---

<h3 align="center">💡 ☕ Traktir Kopi & Nasi Padang ama nasi Gorengnya ya cuy! 😄</h3>

<div align="center">

## Dukung terus biar semangat bikin karya edukatif lainnya...  
## Keep supporting so I stay motivated to create more educational works...

# 💡 ☕  [Buy Me a Coffee via PayPal](https://www.paypal.com/paypalme/bungtempong99)  

Support with ☕ so I can buy 🍜 and keep being 🧠!

---

<h2>📫 Let’s Connect Like Hackers</h2>

| Platform | Detail |
|:--------|:-------|
| GitHub  | [kongali1720](https://github.com/kongali1720) |
| Email   | [kongali1720@gmail.com](mailto:kongali1720@gmail.com) |
| Site    | [Coming soon — stay curious... ](https://kongali1720.github.io) |

---

## ❤️  💻 INITIATING HUMANITY MODE... for Down Syndrome ❤️

| Item        | Keterangan / Description |
|:------------|:-------------------------|
| 🎯 Target   | Anak-anak Pejuang Down Syndrome / Kids with Down Syndrome |
| 📡 Status   | Butuh Dukungan / Needs Support |
| 🧠 Response | Buka Hati + Klik Link = Satu Senyum Baru / Open Heart + Click Link = One New Smile |

Mereka bukan berbeda — mereka dilahirkan untuk mengajarkan dunia tentang cinta yang murni dan kesabaran yang luar biasa.  
They are not different — they were born to teach the world pure love and extraordinary patience.

<p align="center" style="font-size: 1.5rem;">
  <a href="https://mydonation4ds.github.io/" target="_blank" style="display: inline-block;">
    <img 
      src="https://img.shields.io/badge/SUPPORT--NOW-%23FF6600?style=for-the-badge&logo=heart&logoColor=white&labelColor=white&color=FF6600" 
      alt="Support Now" 
      style="width: 300px; height: auto;" 
    />
  </a>
</p>

</div>


---

<section align="center" style="font-family: Arial, sans-serif;">

<h2 style="margin-bottom: 20px; color: #0070f3;">💳 Dukungan Pembayaran DONASINYA</h2>

<table align="center" aria-label="Metode Pembayaran" style="margin: 0 auto; border-collapse: collapse; box-shadow: 0 4px 10px rgba(0,0,0,0.1); border-radius: 8px; overflow: hidden;">
  <thead style="background-color: #0070f3; color: white;">
    <tr>
      <th style="padding: 12px 25px; font-size: 18px;">Visa</th>
      <th style="padding: 12px 25px; font-size: 18px;">Mastercard</th>
      <th style="padding: 12px 25px; font-size: 18px;">PayPal</th>
    </tr>
  </thead>
  <tbody style="background-color: #f9f9f9;">
    <tr>
      <td style="padding: 15px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Visa_Logo.png/120px-Visa_Logo.png" alt="Logo Visa" width="110" />
      </td>
      <td style="padding: 15px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Mastercard-logo.svg/120px-Mastercard-logo.svg.png" alt="Logo Mastercard" width="110" />
      </td>
      <td style="padding: 15px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/PayPal_logo.svg/120px-PayPal_logo.svg.png" alt="Logo PayPal" width="110" />
      </td>
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

