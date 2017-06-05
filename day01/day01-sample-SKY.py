#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author:SKY


def main():
	who='SKY 的妈妈'
	good_price=5  #小贩的价格
	good_description='西双版纳大白菜' #小贩的招牌

	is_cheap=False  #是否便宜
	reasonable_price=5 # 老妈接受的价格
	buy_amount=2

	print "%s 上街看到了 %s,卖 %d 元/斤 " % (who,good_description,good_price)

	if good_price<=reasonable_price:
		print "她认为便宜"
		is_cheap=True
		print "她买了 %d 斤" % (buy_amount)
	else:
		print '她认为贵了'
		is_cheap=False
		print "她并没与买，扬长而去"


if __name__=='__main__':
	main()