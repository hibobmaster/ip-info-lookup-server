import ipaddress
import geoip2.database
import geoip2.errors


class MMDB:
    def __init__(self, asn_db_path: str, city_db_path: str, country_db_path: str):
        self.asn_reader = geoip2.database.Reader(asn_db_path)
        self.city_reader = geoip2.database.Reader(city_db_path)
        self.country_reader = geoip2.database.Reader(country_db_path)

    def get_asn_num(self, ip: str) -> int:
        try:
            return self.asn_reader.asn(ip).autonomous_system_number
        except geoip2.errors.AddressNotFoundError:
            return "N/A"

    def get_asn_org(self, ip: str) -> str:
        try:
            return self.asn_reader.asn(ip).autonomous_system_organization
        except geoip2.errors.AddressNotFoundError:
            return "N/A"

    def get_country_iso(self, ip: str) -> str:
        try:
            return self.country_reader.country(ip).country.iso_code
        except geoip2.errors.AddressNotFoundError:
            return "N/A"

    def get_country_name(self, ip: str) -> str:
        try:
            return self.country_reader.country(ip).country.name
        except geoip2.errors.AddressNotFoundError:
            return "N/A"
        
    def get_city_name(self, ip: str) -> str:
        try:
            return self.city_reader.city(ip).city.name
        except geoip2.errors.AddressNotFoundError:
            return "N/A"

    def get_latitude(self, ip: str) -> float:
        try:
            return self.city_reader.city(ip).location.latitude
        except geoip2.errors.AddressNotFoundError:
            return "N/A"
        
    def get_longitude(self, ip: str) -> float:
        try:
            return self.city_reader.city(ip).location.longitude
        except geoip2.errors.AddressNotFoundError:
            return "N/A"

def ip_validator(ip: str):
    try:
        return True if ipaddress.ip_address(ip) else False
    except ValueError:
        return False
