import os
import requests
from mmdb_func import MMDB

if not (
    os.path.exists("mmdb/GeoLite2-ASN.mmdb")
    and os.path.exists("mmdb/GeoLite2-City.mmdb")
    and os.path.exists("mmdb/GeoLite2-Country.mmdb")
):
    print("Downloading MaxMind DBs...")
    os.makedirs("mmdb", exist_ok=True)

    def download_mmdb(url: str, path: str):
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

    # get latest urls
    req = requests.get(
        "https://api.github.com/repos/P3TERX/GeoLite.mmdb/releases/latest"
    )
    req.raise_for_status()
    urls = req.json()["assets"]

    if not os.path.exists("mmdb/GeoLite2-ASN.mmdb"):
        download_mmdb(urls[0]["browser_download_url"], "mmdb/GeoLite2-ASN.mmdb")
        print("Downloaded GeoLite2-ASN.mmdb.")

    if not os.path.exists("mmdb/GeoLite2-City.mmdb"):
        download_mmdb(urls[1]["browser_download_url"], "mmdb/GeoLite2-City.mmdb")
        print("Downloaded GeoLite2-City.mmdb.")

    if not os.path.exists("mmdb/GeoLite2-Country.mmdb"):
        download_mmdb(urls[2]["browser_download_url"], "mmdb/GeoLite2-Country.mmdb")
        print("Downloaded GeoLite2-Country.mmdb.")


mmdb = MMDB(
    "mmdb/GeoLite2-ASN.mmdb",
    "mmdb/GeoLite2-City.mmdb",
    "mmdb/GeoLite2-Country.mmdb",
)


def struct_ip_info(ip: str) -> dict:
    return {
        "ip": ip,
        "asn": {
            "num": mmdb.get_asn_num(ip),
            "org": mmdb.get_asn_org(ip),
        },
        "country": {
            "iso": mmdb.get_country_iso(ip),
            "name": mmdb.get_country_name(ip),
        },
        "city": {
            "name": mmdb.get_city_name(ip),
            "latitude": mmdb.get_latitude(ip),
            "longitude": mmdb.get_longitude(ip),
        },
    }


def struct_ip_info_str(ip: str) -> str:
    return (
        f"{ip}\n"
        + f"{mmdb.get_country_iso(ip)} / {mmdb.get_country_name(ip)}\n"
        + f"{mmdb.get_city_name(ip)} / {str(mmdb.get_latitude(ip))},{str(mmdb.get_longitude(ip))}\n"  # noqa: E501
        + (
            f"AS{mmdb.get_asn_num(ip)} / {mmdb.get_asn_org(ip)}\n"
            if mmdb.get_asn_num(ip) != "N/A"
            else "N/A"
        )
    )
