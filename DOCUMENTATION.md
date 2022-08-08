# Belgeler
#### Dosya uzantısı: `.med`
#### Tercihen yazım biçimi: `snake_case`

## Temel Operatörler
`+`, `-`, `*`, `/`, `%`, `==`, `!=`, `>`, `<`,`>=`, `<=`, `&&`, `||`.

## Yorum Satırı
`//`

## Değişkenlar
### Oluşturma - Değer atama
Yazım:
```
<değer> <isim> =
```
Örnek:
```
20 yaş =
```
### Kullanma
Yazım:
```
<isim> ?
```
Örnek:
```
yaş ? yaz
// çıktı: 20
```

## Girdi - çıktı
### Ekrana yazma
Yazım:
```
<değer> yanyaz
<değer> yaz
```
Örnek:
```
10 yanyaz 11 yanyaz
// çıktı: 10 11

10 yaz 11 yaz
// çıktı:
// 10
// 11
```
### Girdi alma
Yazım:
```
oku
```
Örnek:
```
oku yaş =
yaş ? yaz
// çıktı: kullanıcıdan alınan girdi
```
### Programdan çıkma
#### `0 çık`: 0 hata koduyla çıkar.
#### `1 çık`: 1 hata koduyla çıkar.

## Metodlar
#### `takasla`: yığının tepesindeki iki değeri alır, yerlerini değiştirip geri iter. (`[0, 1] => [1, 0]`)
#### `kopyala`: yığının tepesindeki değerin kopyasını yığına geri iter. (`[0, 1] => [0 , 1, 1]`)
#### `düşür`: yığının tepesindeki değeri yığından atar. (`[0, 1] => [0]`)

## Koşullar
### `ise-değilse (if-else)`
Yazım:
```
<şart> ise
    <işlem>
    <işlem>
değilse
    <işlem>
    <işlem>
bitir
```
Örnek:
```
10 10 + 20 == ise
    1 yaz
değilse
    0 yaz
bitir
// çıktı: 1
```

### `eşleştir-ile (switch-case)`
Yazım:
```
<değer> eşleştir
    <durum> ile
        <işlem>
        <işlem>
    bitir
    <durum> ile
        <işlem>
        <işlem>
    bitir
bitir
```
Örnek:
```
oku puan =

puan ? eşleştir
    100 ile
        100 yaz
    bitir
    85 ile
        85 yaz
    bitir
    50 ile
        50 yaz
    bitir
bitir
```

## Döngüler
### `iken-yap (while-do)`
Yazım:
```
iken <şart> yap
    <işlem>
    <işlem>
bitir
```
Örnek:
```
5 x =

iken x ? 0 > yap
    x ? kopyala yanyaz
    1 - x =
bitir
// çıktı 5 4 3 2 1 0
```