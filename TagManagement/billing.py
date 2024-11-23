import requests, json

def get_bill_data(bill_number, period):
    params = {
        "bill_number": bill_number,
        "period": period
    }
    headers = {
        "User-Agent": "okhttp/3.10.0",
        "Host": "api.tagihan.me"
    }
    response = requests.get("https://api.tagihan.me/api/pln", params=params, headers=headers)
    json_data = json.loads(response.text)

    if len(json_data['bill_name']) == 0:
        return {
            'error': json_data['print'].capitalize().replace("EXT: ", "")
        }
    else:
        return {
            'bill_name': json_data['bill_name'].capitalize(),
            'bill_period': json_data['bill_period'],
            'daya': json_data['daya'],
            'tarif': json_data['tarif'],
            'bill_amount': "{:,.2f}".format(float(json_data['bill_amount'])).replace(",", "."),
            'stan_meter': json_data['stan_meter'],
            'print': 'EXT: Tagihan belum dibayar',
        }