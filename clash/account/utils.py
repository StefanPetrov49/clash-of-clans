import requests

headers = {
    'Accept': 'application/json',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjU5YjRmYWVhLTM5MjMtNDFkYy1iNTgwLWRhMmFiYzRiMjNkOSIsImlhdCI6MTY3ODc5MjkxNSwic3ViIjoiZGV2ZWxvcGVyL2IxMWRmYTVkLWZhNzUtNTIxZS04NGMzLTQ0Zjc1ZDZmMWVkNCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjk1LjExMS45Ny4yMjUiXSwidHlwZSI6ImNsaWVudCJ9XX0.gYVdUYSw0dpcbPbuSvxuI7eE_eTYeYqUbMDiJZq6ri63PnMzfJSwuY2q_GXQGapXxDMt04FtzVk672nYqOwlzA'
}
def get_user(tag):
    url = f'https://api.clashofclans.com/v1/players/%23{tag}'
    response = requests.get(
       url, headers=headers)
    user_json = response.json()
    context = [user_json['name'], user_json['trophies'], user_json['league']['iconUrls']['small']]
    return context
