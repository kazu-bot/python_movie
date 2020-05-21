#testの際に役立つ、効率化できる書き方を学習
#これはdoctest。簡易的なもの。作りながらちょこちょこやる用かな？
class Cal(object):
    def add_num_and_double(self,x,y):
        """Add and double
        下記のような書き方で途中から対話型シェルの立ち上げが可能
        >>> c = Cal()
        >>> c.add_num_and_double(1,1)
        4

        >>> c.add_num_and_double('1','1')
        Traceback(most recent call last):
        ...
        ValueError
        """
        if type(x) is not int or type(y) is not int:
            raise ValueError

        result = x + y
        result *= 2
        return result
#
# if __name__ =='__main__':
#     import doctest
#     doctest.testmod()