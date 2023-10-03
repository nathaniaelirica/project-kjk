import cors from 'cors';
import express from 'express';
import wifi from 'node-wifi';
import pkg from 'body-parser';
const { json } = pkg;

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors()); // Menambahkan middleware CORS

app.use(json());

app.get('/api/wifi/networks', async (_req, res) => {
    try {
      wifi.init({ iface: null, sudo: true });
  
      const networks = await wifi.scan();
      res.json({ networks });
    } catch (error) {
      console.error('Error:', error);
      res.status(500).json({ error: 'Gagal mendeteksi jaringan Wi-Fi.' });
    }
});

app.listen(PORT, () => {
  console.log(`Server berjalan di port ${PORT}`);
});
