const menu = [
  { nama: "Nasi Ayam Bakar", harga: 25000, img: "https://i.pinimg.com/736x/f3/2f/89/f32f89f740c277406b11b089b53ea907.jpg" },
  { nama: "Nasi Ikan Bumbu Bali", harga: 27000, img: "https://i.pinimg.com/736x/c1/e4/b1/c1e4b1ea45613d65400828d2de1251fe.jpg" },
  { nama: "Paket Prasmanan Hemat", harga: 50000, img: "https://i.pinimg.com/1200x/34/0b/e4/340be45acb3a916e46ffe1d5870489cb.jpg" },
  { nama: "Gurame Asam Manis ", harga: 65000, img: "https://i.pinimg.com/736x/55/96/b8/5596b8262ee9a527edd235c7b5242292.jpg" },
  { nama: "Snack Box", harga: 15000, img: "https://i.pinimg.com/736x/6f/0f/53/6f0f53d61ef443ae7d7ee9fd6e35b6d7.jpg" },
  { nama: "Minuman Segar", harga: 8000, img: "https://i.pinimg.com/736x/8b/c4/78/8bc478c9f38c58382b328df6b1a1a6da.jpg" }
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