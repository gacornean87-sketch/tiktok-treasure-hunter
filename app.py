
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="TikTok Treasure Hunter")

@app.get("/", response_class=HTMLResponse)
def dashboard():
    return """
    <!DOCTYPE html>
    <html lang="id">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>TikTok Treasure Hunter</title>
      <style>
        body {
          background: #101827;
          color: white;
          font-family: Arial, sans-serif;
          padding: 25px;
          text-align: center;
        }
        .panel {
          background: #1e293b;
          padding: 25px;
          border-radius: 15px;
          margin-top: 25px;
        }
        h1 { color: #facc15; }
        p { line-height: 1.7; }
      </style>
    </head>
    <body>
      <h1>🎁 TikTok Treasure Hunter</h1>
      <p>Website Pemantau Kotak Harta Karun TikTok</p>
      <div class="panel">
        <h2>Dashboard Pemantauan</h2>
        <p>Website berhasil dijalankan.</p>
        <p>Status: Menunggu koneksi data TikTok.</p>
        <p>Target: Hadiah besar, penonton sedikit,
        dan waktu kotak hampir habis.</p>
      </div>
    </body>
    </html>
    """

@app.get("/health")
def health():
    return {"status": "online"}
  
