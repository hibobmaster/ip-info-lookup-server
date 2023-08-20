# ip-info-lookup-server
仿照 ip.p3terx.com 样式构建的ip信息查询服务


## Usage
GET / get ip info from your ip address

POST / get json-formatted ip info from your ip address

GET /ip/{ip} get ip info from provided ip address

POST /ip/{ip} get json-formatted ip info from provided ip address

Example:
```bash
curl ip.qqs.tw
curl ip.qqs.tw/ip/114.114.114.114
```