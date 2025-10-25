<?php
include 'koneksi.php';

$data = json_decode(file_get_contents("php://input"), true);

$nama = $data['nama'];
$telepon = $data['telepon'];
$alamat = $data['alamat'];
$waktu = $data['waktu'];
$total = $data['total'];

$sql = "INSERT INTO pesanan (nama, telepon, alamat, waktu, total) VALUES ('$nama','$telepon','$alamat','$waktu','$total')";
if (mysqli_query($conn, $sql)) {
  echo "✅ Pesanan berhasil dikirim! Terima kasih, $nama.";
} else {
  echo "❌ Gagal menyimpan pesanan: " . mysqli_error($conn);
}
?>
