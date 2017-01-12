<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<title>웹 프로그래밍</title>
	</head>
<body>
웹 프로그램 테스트
http://127.0.0.1/a.php

<?
	$total = 0;
	for($i = 1; $i <=100; $i++)
	{
		echo "$i<br>";	
	}
	echo "total = $total<br>";	
?>

<table border=1>
<?
	for($i = 1; $i<=35; i++)
	{
		echo "<td sidth=50>$i</td>"
	}
?>
</table>
</body>
