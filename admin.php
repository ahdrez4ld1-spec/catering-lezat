<?php
include 'koneksi.php';
$result = mysqli_query($conn, "SELECT * FROM pesanan ORDER BY tanggal_pesan DESC");
?>
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <title>Admin - Daftar Pesanan</title>
  <style>
    body { font-family: 'Poppins', sans-serif; background: #f3f4f6; margin: 0; padding: 20px; }
    h1 { text-align: center; color: #4c1d95; }
    table { width: 100%; border-collapse: collapse; background: white; border-radius: 10px; overflow: hidden; }
    th, td { border: 1px solid #ddd; padding: 10px; text-align: center; }
    th { background: #6d28d9; color: white; }
  </style>
</head>
<body>
  <h1>📋 Daftar Pesanan Catering</h1>
  <table>
    <tr>
      <th>No</th>
      <th>Nama</th>
      <th>Telepon</th>
      <th>Alamat</th>
      <th>Waktu</th>
      <th>Total</th>
      <th>Tanggal Pesan</th>
    </tr>
    <?php
    $no = 1;
    while ($row = mysqli_fetch_assoc($result)) {
      echo "<tr>
        <td>{$no}</td>
        <td>{$row['nama']}</td>
        <td>{$row['telepon']}</td>
        <td>{$row['alamat']}</td>
        <td>{$row['waktu']}</td>
        <td>Rp " . number_format($row['total'],0,',','.') . "</td>
        <td>{$row['tanggal_pesan']}</td>
      </tr>";
      $no++;
    }
    ?>
  </table>
</body>
</html>
