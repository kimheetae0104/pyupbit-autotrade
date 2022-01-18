import pyupbit

access = "V4kg51zW8O2rwxWyYec1wVny999c3Ux9zVZmQgLM"          # 본인 값으로 변경
secret = "DymtZvOKVfq4xnbrrSdLyWwf45N4JxxBPvVxvbze"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회