const menu = [
  { nama: "Nasi Ayam Bakar", harga: 25000, img: "https://i.imgur.com/7HP7h1V.jpg" },
  { nama: "Nasi Ikan Bumbu Bali", harga: 27000, img: "https://i.imgur.com/9uK1X8B.jpg" },
  { nama: "Paket Prasmanan Hemat", harga: 50000, img: "https://i.imgur.com/9vDyo4y.jpg" },
  { nama: "Paket Prasmanan Premium", harga: 65000, img: "https://i.imgur.com/CTbyuOa.jpg" },
  { nama: "Snack Box", harga: 15000, img: "https://i.imgur.com/gsyPKiB.jpg" },
  { nama: "Minuman Segar", harga: 8000, img: "https://i.imgur.com/sm9tW8A.jpg" }
];

let total = 0;
const menuList = document.getElementById('menuList');
const totalHarga = document.getElementById('totalHarga');

menu.forEach((item, i) => {
  const div = document.createElement('div');
  div.classList.add('menu-item');
  div.innerHTML = `
    <img src="${item.img}" alt="${item.nama}">
    <h4>${item.nama}</h4>
    <p>Rp ${item.harga.toLocaleString()}</p>
    <button onclick="tambahPesanan(${i})">Tambah ke Pesanan</button>
  `;
  menuList.appendChild(div);
});

function tambahPesanan(i) {
  total += menu[i].harga;
  totalHarga.textContent = total.toLocaleString();
}

document.getElementById('orderForm').addEventListener('submit', function(e) {
  e.preventDefault();

  if (total === 0) {
    alert("Silakan pilih menu terlebih dahulu!");
    return;
  }

  const data = {
    nama: document.getElementById('nama').value,
    telepon: document.getElementById('telepon').value,
    alamat: document.getElementById('alamat').value,
    waktu: document.getElementById('waktu').value,
    total: total
  };

  fetch('simpan_pesanan.php', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(data)
  })
  .then(res => res.text())
  .then(res => {
    alert(res);
    document.getElementById('orderForm').reset();
    total = 0;
    totalHarga.textContent = "0";
  });
});
