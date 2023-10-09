<!-- <template>
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
</template> -->

<template>
  <div id="app">
    <h1>Info WiFi</h1>
    <!-- <button @click="checkWifi">Check WiFi</button> -->
    <div class="card">
      <div class="row">
        <div class="col-md-3 mb-3" v-for="(network, index) in wifiNetworks" :key="index">
          <ul class="list-group list-group-flush">
            <li class="list-group-item border">
              <div class="network-info">
                <div class="ssid">SSID: {{ network.ssid }}</div>
                <div class="security">Security: {{ network.security }}</div>
                <div class="status" :style="{ backgroundColor: network.isOpen ? 'red' : 'green', color: 'white' }">
                  Status: {{ network.isOpen ? 'Terbuka (Tidak Aman)' : 'Private (Aman)' }}
                </div>
                <br>
                <button @click="showDetail(network)">Detail</button> <!-- Tambahkan tombol Detail -->
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
    
    <!-- Komponen AlertDefaultVue yang Anda buat -->
    <AlertDefaultVue :visible="showModal" variant="primary">
    <div>
      <div class="modal-body">
        <div class="ssid">SSID: {{ selectedNetwork.ssid }}</div>
        <div class="security">Security: {{ selectedNetwork.security }}</div>
        <div class="status">
          <p>Status: {{ selectedNetwork.isOpen ? 'Terbuka (Tidak Aman)' : 'Private (Aman)' }}</p>
          <!-- <p v-if="selectedNetwork.security === 'WEP'">Penjelasan: Jaringan WEP adalah jaringan yang tidak aman. Disarankan untuk menggunakan jaringan yang lebih aman.</p>
          <p v-else-if="selectedNetwork.security === 'Open'">Penjelasan: Jaringan terbuka adalah jaringan tanpa enkripsi dan tidak aman. Disarankan untuk menggunakan jaringan yang lebih aman.</p> -->
          <p v-if="selectedNetwork.security === 'WEP'">Penjelasan: Jaringan WEP adalah jaringan yang tidak aman. Disarankan untuk menggunakan jaringan yang lebih aman.</p>
          <p v-else-if="selectedNetwork.security === 'Open'">Penjelasan: Jaringan terbuka adalah jaringan tanpa enkripsi dan tidak aman. Disarankan untuk menggunakan jaringan yang lebih aman.</p>
        </div>
      </div>
      <div class="modal-footer">
        <button type="button" @click="closeModal" class="btn btn-secondary">Tutup</button>
      </div>
    </div>
  </AlertDefaultVue>

  </div>
</template>

<script>
import AlertDefaultVue from './components/AlertDefault.vue';

export default {
  name: 'App',
  components: {
    AlertDefaultVue
  },
  data() {
    return {
      wifiNetworks: [], // Menyimpan daftar jaringan Wi-Fi dari server
      showModal: false,
      selectedNetwork: null,
      OpenClose: this.visible
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
    showDetail(network) {
      // Menampilkan modal ketika tombol "Detail" ditekan
      this.selectedNetwork = network;
      this.showModal = true;
      console.log("detail");
    },
    closeModal(){
      this.showModal = false;
    }
  },
};
</script>

<style scoped>
.green-bg {
  background-color: green;
  color: white;
}

.red-bg {
  background-color: red;
  color: white;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

button {
  font-size: 1em;
  padding: 10px 20px;
  background-color: #4c60af;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-bottom: 20px;
}

button:hover {
  background-color: #4c60af;
}

ul {
  list-style-type: none;
  padding: 0;
}

.ssid, .security, .wps {
  margin: 5px 0;
}

.no-wifi {
  color: #514c4b;
  font-weight: bold;
  margin-top: 20px;
}

</style>