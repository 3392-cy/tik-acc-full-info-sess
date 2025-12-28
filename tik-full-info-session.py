import requests
import json
import datetime

def conv(ts):
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

def balance(sess):
    url = "https://webcast.tiktok.com/webcast/wallet_api/fs/diamond_buy/permission_v2"
    params = {"aid": "1988"}
    headers = {"Cookie": (f"sessionid={sess}"),
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"}
    gqpgqpg1 = requests.get(url, headers=headers, params=params)
    return gqpgqpg1
def generalinfo(sess):
    url = "https://www.tiktok.com/passport/web/account/info/"
    headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "cookie": (
        f"sessionid={sess}"
    ),
    "sec-ch-ua": '"Microsoft Edge";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    "sec-ch-ua-platform": '"Windows"',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"
}
    rp = requests.get(url, headers=headers)
    data = rp.text
    gqpgqpg2 = json.loads(data)
    return gqpgqpg2

def main(gqpgqpg2, gqpgqpg1, sess, geo1, geo2,pay):
    if gqpgqpg2.get('message') == 'success':
        geo2 = gqpgqpg2.get('data', {})
    else:
        print("Error: Invalid session or API response")
    if json.loads(gqpgqpg1.text).get('status_code') == 0:
        geo1 = json.loads(gqpgqpg1.text).get("data", {})
        if str(geo1.get("quick_payment_available")) == 'True' or str(geo1.get("has_google_recharge"))=='True':
            pay="Payment method available ✔️"
        elif str(geo1.get("quick_payment_available")) == 'False' or str(geo1.get("has_google_recharge"))=='False': 
            pay='No payment mathod found ✖️ '
        else:
            print("Error")
    else:
        print("Error. Check session or api patched")
    created = geo2.get('create_time', 0)
    message = f'''
TikTok Full Info Session
Session: {sess}
-------------------------
General Info:
    Username: {geo2.get('username', 'N/A')},
    User ID: {geo2.get('user_id', 'N/A')},
    Sec User ID: {geo2.get('sec_user_id', 'N/A')},
    Screen name: {geo2.get('screen_name', 'N/A')},
    Profile Picture: {geo2.get('avatar_url', 'N/A')},
    Bio: {geo2.get('description', 'N/A')}
    Mobile: {geo2.get('mobile', 'N/A')},
    Email: {geo2.get('email', 'N/A')},
    Created At: {conv(int(geo2.get('create_time', 0))) if created else "N/A"},
    Connections: {geo2.get('connects', [])},
    Session Key: {geo2.get('session_key', 'N/A')},
    Is Employee: {geo2.get('is_employee', False)},
    External Employee Platform: {geo2.get('external_employee_platform', 'N/A')}
-------------------------
Balance Info:
    Coins:              {geo1.get("coins")}
    Frozen coins:       {geo1.get("frozen_coins")}
    Blocked:            {geo1.get("block_coin_page")}
    Allow status:       {geo1.get("is_allow")}
    Email confirmed:    {geo1.get("is_email_confirmed")}
    First web recharge: {geo1.get("is_first_web_recharge")}
    Periodic payout:    {geo1.get("is_periodic_payout")}
    Show page:          {geo1.get("is_show")}
    PC web status:      {geo1.get("pc_web_recharge_status")}
    PWA category:       {geo1.get("pwa_user_category")}
    Quick payment:      {geo1.get("quick_payment_available")}
    Google recharge:    {geo1.get("has_google_recharge")}
    Tooltip shown:      {geo1.get("show_input_tooltip")}
    Redeem info :       {geo1.get("redeem_info", {})}
    Web option:         {geo1.get("web_recharge_input_option")}
    {pay}
'''
    print(message)

if __name__ == "__main__":
    sess = input("Enter session: ")
    main(generalinfo(sess), balance(sess), sess, None, None, None)