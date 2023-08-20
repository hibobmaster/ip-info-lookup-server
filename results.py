from mmdb_func import MMDB

mmdb = MMDB("mmdb/GeoLite2-ASN.mmdb", "mmdb/GeoLite2-Country.mmdb")


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
    }


def struct_ip_info_str(ip: str) -> str:
    return (
        f"{ip}\n"
        + f"{mmdb.get_country_iso(ip)} / {mmdb.get_country_name(ip)}\n"
        + (
            f"AS{mmdb.get_asn_num(ip)} / {mmdb.get_asn_org(ip)}\n"
            if mmdb.get_asn_num(ip) != "N/A"
            else "N/A"
        )
    )
