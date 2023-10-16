# ip-info-lookup-server
self-host ip information lookup server


## Usage
GET / get ip info from your ip address

POST / get json-formatted ip info from your ip address

GET /ip/{ip} get ip info from provided ip address

POST /ip/{ip} get json-formatted ip info from provided ip address

Example:
```bash
curl ip.qqs.tw
curl ip.qqs.tw/ip/119.39.65.141
```