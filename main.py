import roboter
import os

class main:
    def start_massage(self):
        print('こんにちは！私はRobokoです。あなたの名前はなんですか？')
        name = str(input('名前を入力：'))
        if name == "":
            while name == "":
                name = str(input('名前を入力：'))
        return name

    def end_message(name):
        print(name+'さん。ありがとうございました。¥n良い一日を！さようなら。')

    person_name = start_massage()
    endFlag = False
    if os.path.exists('restaurant.csv'):
        endFlag = roboter.recommend
    if not endFlag:
        roboter.restaurantInput
    end_message(person_name)
