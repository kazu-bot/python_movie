import os

def recommend():
    #ファイルの内容を読み込んでおすすめのレストランを紹介する。
    #Yesが選択された場合はファイル書き込みに遷移し、処理終了
    #Noが選択された場合は２行目も出力する
    #再度Noが選択された場合はレストラン入力をさせるようmainに返す
    with open('restaurant.csv','a+') as f:
        for row in f:
            fileList = row.readline()
            fileList = sorted(fileList, reverse=True, key=lambda x:x[1])

        i = 0
        for x in fileList:
            print('私のおすすめのレストランは、'+fileList(x[0])+'です。¥n')
            lkrestaurant = input('このレストランは好きですか？[Yes/No]')
            if lkrestaurant == 'Yes':
                f.seek(0)
                rowcnt = 0
                for row in f:
                    rowcnt = rowcnt+1
                    fileRestaurant = row[0]
                    if fileList(x[0]) == fileRestaurant:
                        count = row[1]
                        count = count + 1




    return True

def restaurantInput():
    inputRestaurant = input('おすすめのレストランを教えてください：')
    inputRestaurant = str.capitalize(inputRestaurant)


def restaurantSave():
