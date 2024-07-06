from smartphone import Smartphone

catalog = [
    Smartphone('Samsung', 'Galaxy S21', '9123456789'),
    Smartphone('Apple', 'iPhone 12', '9234567890'),
    Smartphone('Xiaomi', 'Mi 11', '9345678901'),
    Smartphone('Google', 'Pixel 5', '9456789012'),
    Smartphone('OnePlus', '8T', '9567890123')
]

for smartphone in catalog:
    print(smartphone)