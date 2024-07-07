from address import Address
from mailing import Mailing

index_from = '654321'
city_from = 'Москва'
street_from = 'Арбат'
house_from = '22'
apartment_from = '8'
from_address = Address(index_from, city_from, street_from, house_from, apartment_from)

index_to = '123456'
city_to = 'Владивосток'
street_to = 'Светланская'
house_to = '10'
apartment_to = '20'
to_address = Address(index_to, city_to, street_to, house_to, apartment_to)

cost = 500
track_number = 'RU123456789CN'

mailing = Mailing(to_address, from_address, cost, track_number)

print("Отправление " + track_number + " из " + index_from + ", " + city_from + ", " +
      street_from + ", " + house_from + " - " + apartment_from + " в " + index_to + ", " +
      city_to + ", " + street_to + ", " + house_to + " -" + apartment_to +
      ". Стоимость " + str(cost) + " рублей.")
