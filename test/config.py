main_url = 'https://www.kinopoisk.ru/'
api_url = 'https://api.kinopoisk.dev/'
cookie_string = 'yashr=9518928831720450410; yandexuid=9872028181719431375; gdpr=0; _ym_uid=172045041226378597; yuidss=9872028181719431375; _csrf=J9zf7zemULTNt3Q_0cODl6kp; PHPSESSID=ef74dfb1000f19f2817ddecc290a2e4f; yandex_gid=2; uid=75398729; my_perpages=%5B%5D; _csrf_csrf_token=RjNP1ZtWFH1jo8FK9nCF1BR-9DMl_pYfquBfd3AkQk0; mda_exp_enabled=1; users_info[check_sh_bool]=none; i=YQ1+3fq1QTTJs60MOzYtz23pZDx7RlJiEGoXsaYxFmZepXgqbbnspfi1IgfiFBhLiLQ0ar2eCfpdfh4g65wXMWDdl5o=; result_type=simple; mykp_button=movies; mykpFolderFormat=full; mykpFolderOrder=asc; mykpFolderSort=premier_rus; mobile=no; yp=1738750377.yu.9872028181719431375; ymex=1741255977.oyu.9872028181719431375; no-re-reg-required=1; yandex_login=matroSka0-0; L=QXZZZQBWcw53RglkcnZhRlxdZHxXDEBGJAAwJFo4MVZYVAE=.1738667244.16042.393003.c29950a8878db644367d857b259e4735; desktop_session_key=4b6418bf25df03c9e0a48942bba17b0e2add8adde92b105fe20eafad3a1101fde6156fcd70a16999de3e1e67da34db8f273601d129016d1bd6e183e84234853c6352fe258b902de0c9b37d0c902651c9691fb275981a7fa9108219a14a5f681f16a2d561ea6ebf80d8d995d3c5f4cf7560e32220437579ba55792be81e320fa4d331598355a46a07825bf307c03f8ab28454fa1970e061cefdd41290757c8e435c15a1a5c941335b7365bdba21bdee72; desktop_session_key.sig=DQUOci11nYRoXzE2E2QQqUlFvq8; ya_sess_id=3:1738747781.5.0.1738667244527:OO3DsA:471c.1.2:1|30074702.0.2.3:1738667244|30:10232260.684646.rBGxKKO6nLLBA5rvmzCAMC5RY5M; sessar=1.1198.CiCenm5RiLWgJ0iKGOTTMhSnF27MJzGcFpM6LeyW0O-JBw.BOJKHpZi7BUmz7EcyGtaK6apC0d_To2WCPTofGefy9U; ys=c_chck.3716187845#udn.cDptYXRyb1NrYTAtMA%3D%3D; mda2_beacon=1738747781992; sso_status=sso.passport.yandex.ru:synchronized; _ym_d=1738747783; _ym_isad=2; _yasc=u8+/ir53Vmc2JHE2p+bWKbmurQq0EF9YaOPqYANZR+TppHZYIECCZlxof89i2zW0; sgst=searchRequest-%D0%B0%D0%B2%D0%B0%D1%82%D0%B0%D1%80; cycada=G80poHo7PQiE6NxVYmcmexGDEi26wU4MUjHeDo4cbWQ='


def parse_cookies(cookie_string):
    cookies = []
    for cookie in cookie_string.split(';'):
        name, value = cookie.strip().split('=', 1)
        cookies.append({'name': name, 'value': value, 'path': '/'})
    return cookies


cookies = parse_cookies(cookie_string)
