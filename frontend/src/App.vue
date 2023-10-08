<template>
  <div>
    <h1>Hasil Pemindaian Jaringan Wi-Fi</h1>
    <ul>
      <li v-for="(network, index) in wifiNetworks" :key="index">
        <h2>Nama Jaringan: {{ network.ssid }}</h2>
        <p>Jenis Keamanan: {{ network.security }}</p>
        <p v-if="network.isOpen">Status: Terbuka (Tidak Aman)</p>
        <p v-else>
          Status: Private (Aman)
          <p v-if="network.security === 'WEP'">Penjelasan: Jaringan WEP adalah jaringan yang tidak aman. Disarankan untuk menggunakan jaringan yang lebih aman.</p>
          <p v-else-if="network.security === 'Open'">Penjelasan: Jaringan terbuka adalah jaringan tanpa enkripsi dan tidak aman. Disarankan untuk menggunakan jaringan yang lebih aman.</p>
        </p>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      wifiNetworks: [], // Menyimpan daftar jaringan Wi-Fi dari server
    };
  },
  created() {
    // Lakukan permintaan ke server Express.js untuk mendapatkan daftar jaringan Wi-Fi
    this.fetchWifiNetworks();
  },
  methods: {
    async fetchWifiNetworks() {
      try {
        const response = await fetch('http://localhost:3000/api/wifi/networks');
        if (response.ok) {
          const data = await response.json();
          this.wifiNetworks = data.networks.map(network => {
            return {
              ssid: network.ssid,
              security: network.security,
              isOpen: network.security === 'Open' // Tambah properti isOpen
            };
          });
        } else {
          console.error('Response not OK:', response.status, response.statusText);
        }
      } catch (error) {
        console.error('Error:', error);
      }
    },
  },
};
</script>


<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
