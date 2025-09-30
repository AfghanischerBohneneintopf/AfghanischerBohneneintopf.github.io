<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Meine kostenlose Website</title>
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <header>
    <h1>Willkommen auf meiner Seite</h1>
    <p class="subtitle">Eine einfache, kostenlose Website</p>
  </header>

  <main>
    <section>
      <h2>Über mich</h2>
      <p>Hier kommt ein kurzer Text über dich oder dein Projekt.</p>
    </section>

    <section>
      <h2>Kontakt</h2>
      <p>Email: <a href="mailto:deinname@example.com">deinname@example.com</a></p>
    </section>
  </main>

  <footer>
    <p>© <span id="year"></span> Dein Name</p>
  </footer>

  <script src="script.js"></script>
</body>
</html>
:root{
  --bg:#f7f9fc;
  --card:#ffffff;
  --accent:#0b74de;
  --text:#222;
}
*{box-sizing:border-box}
body{
  margin:0;
  font-family:Inter,system-ui,Segoe UI,Roboto,"Helvetica Neue",Arial;
  background:var(--bg);
  color:var(--text);
  line-height:1.6;
  padding:2rem;
}
header{
  text-align:center;
  margin-bottom:1.5rem;
}
header h1{margin:.2rem 0; font-size:2rem; color:var(--accent)}
main{
  max-width:800px;
  margin:0 auto;
  background:var(--card);
  padding:1.25rem;
  border-radius:8px;
  box-shadow:0 6px 18px rgba(15,25,40,0.06);
}
section + section{margin-top:1rem}
footer{ text-align:center; margin-top:1rem; color:#666; font-size:.9rem}
a{ color:var(--accent); text-decoration:none }


