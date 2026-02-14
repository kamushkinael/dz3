# dz3

## 0.Написать однострочник который раз в секунд дергает https://mirror.yandex.ru/debian/tools/ и выводит код ответа, timestamp и время запроса
while true; do curl -s -o /dev/null -w "%{http_code} %{time_total}s " https://mirror.yandex.ru && date +"%Y-%m-%d %H:%M:%S"; sleep 1; done

## 1. Раздача статичных файлов через nginx
Для проверки требуется ввести адрес с указанием порта, для просмотра файлов следует написать ручку /files

## 2. Написать собственный модуль
Написан модуль, который принимает в качестве параметра порт для nginx и подставляет его в конфигурацию, файл nginxconfig.py в library

### Проверка на локальной машине
ansible-playbook lopi.yml -e "i_port=7001" -K
