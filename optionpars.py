# 実行時のオプションを作成することができるoptionparseを使ってみる。
# ↓はファイル名を渡したらそれを変数で受けて表示するもの
from optparse import OptionParser
# Optionparserはオプションのグループ化も可能
# 特定の処理毎にオプショングループを分けたい場合等に役立ちそう
from optparse import OptionGroup


def main():
    usage = 'usage: %prog [options] arg1 arg2'
    parser = OptionParser(usage=usage)
    parser.add_option('-f', '--file', action='store', type='string',
                      dest='filename', help='File name')
    parser.add_option('-n', '--num', action='store', type='int', dest='num')
    parser.add_option('-v', action='store_false', dest='verbose')
    # store_const：オプション入力で定数を設定できる(使う機会あるんか？)
    # user_nameに「root」を格納する
    parser.add_option('-r', action='store_const', const='root', dest='user_name')

    # callbackで関数を呼び出す
    # '-e prd'を引数として渡すと、is_release関数を呼び出し、エラ〜メッセージを返す。
    parser.add_option('-e', dest='env')

    def is_relase(option, opt_str, value, parser):
        if parser.value.env == 'prd':
            raise parser.error("Can't release")
        setattr(parser.values, options.dest, True)

    parser.add_option('--release', action='callback', callback=is_relase, dest='release')

    # オプショングループを作成してみる
    group = OptionGroup(parser, 'Dangerous option')
    group.add_option('-g', action='store_true', help='Group option')

    options, args = parser.parse_args()
    print(options)
    print(type(args))


if __name__ == '__main__':
    main()
