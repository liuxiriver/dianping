
def cookie_conv(cookies):
    cookies = cookies
    cookie_dict = {}
    cookie_list = cookies.split(";")
    # print(cookie_list)
    for cookie in cookie_list:
        x = cookie.split("=")
        cookie_dict[x[0]]= x[1]
    return cookie_dict

