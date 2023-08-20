from mmdb_func import MMDB, ip_validator

mmdb = MMDB("mmdb/GeoLite2-ASN.mmdb", "mmdb/GeoLite2-Country.mmdb")
real_ip = "114.114.114.114"
bad_ip = "aaa.xxx.ccc.ddd"


class TestClass:
    def test_ip_validator(self):
        assert ip_validator(real_ip) is True
        assert ip_validator(bad_ip) is False

    def test_get_asn(self):
        assert mmdb.get_asn_num(real_ip) == 174
        assert mmdb.get_asn_org(real_ip) == "COGENT-174"

    def test_get_country(self):
        assert mmdb.get_country_iso(real_ip) == "CN"
        assert mmdb.get_country_name(real_ip) == "China"
