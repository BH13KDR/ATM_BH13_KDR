#balance : 초기 잔액을 설정하는 변수 설정 : 금액은 마음대로 설정해도 됨.
#사용자로부터 atm 기계 사용 목적에 맞는 기능을 선택할 수 있도록
#기능 입력을 받는 기능을 구현.

balance = 300000
receipts = []

while True : #아래에 무슨 조건이 오던 무한히 실행.
        num = input("사용하실 기능의 번호를 입력해주세요. (1.입금, 2.출금, 3.영수증 보기, 4.종료) :")
        if num == '4': #input에서 들어오는건 str이기 때문에
            break
        if num == '1':
            deposit_amount = int(input("입금할 금액을 입력해주세요."))
            balance += deposit_amount
            print(f'입금하신 금액{deposit_amount}원. 현재잔액은 {balance}입니다.')
            receipts.append(("입금",deposit_amount,balance))
            #입력한 입금 금액을 튜플의 형태로 receipts리스트 안에 튜플로 저장한다.

        if num == '2':
            withdraw_amount = int(input("출금할 금액을 입력해주세요."))
            withdraw_amount = min(balance,withdraw_amount)
            balance -= withdraw_amount
            print(f'출금하신 금액{withdraw_amount}원. 현재잔액은 {balance}입니다.')
            receipts.append(("출금",withdraw_amount,balance))

        if num == '3':
            if receipts: #라고만 적어도 컴퓨터는 값에 접근해 값이 있는지T 없는지F판단.
                  #print(receipts) 으로 해도 되지만 예쁘게
                  for i in receipts:
                        print(f"{i[0]} : {i[1]}원 : 잔액 : {i[2]}원")
                        # i = ('입금', 3000, 303000)
                        # i[0] = '입금'
            else :
                  print("거래내역이 없습니다.")
        

print(f'서비스를 종료합니다. 현재 잔액 : {balance}')