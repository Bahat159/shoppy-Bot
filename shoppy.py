import os
import sys
import time
import requests
import random
from random import randint


# Shoppy bot to help manage and maintain your shoppy.gg page
# Developed at Sandcroft
# This script will evolve and be updated
# All Right Reserved

def pick_proxy():
	lines = open('proxy.txt','r')
	filestream = open('proxy.txt','r')
	randomProxyID = randint(0,sum(1 for row in lines) -1)
	for proxyID,proxy in enumerate(filestream):
		if(proxyID == randomProxyID):
			currentProxy = proxy
			break
		else:
			currentProxy = ''
	filestream.close()
	lines.close()
	return currentProxy.strip()

def clear_screen():
	if os.name in ['nt','win32','dos']:
		os.system('cls')
	else:
		os.system('clear')

def about_program():
	colors = [36, 32, 34, 35, 31, 37]
	msg00 = '\n\t\t[+] Program Name: Shoppy Shop Bot\n\t\t[+] ShareWare(ALL RIGHT RESERVED)\n\t\t[+] Author: @Just_rudy\n\t\t[+] Version: v1.0\n'
	for i in msg00:
		sys.stdout.write('\x1b[1;%dm%s' %(random.choice( colors),i))
		sys.stdout.flush()
		time.sleep(0.02)

error_log_type = 'debug'
def error_log_msg(self,message,err=''):
	if error_log_type == 'debug':
		inv = open('debug_log.html','a')
		inv.write(message+str(err))
		inv.close()

def get_product_list(header,proxy):
	product_url = 'https://shoppy.gg/api/v1/products/'
	try:
		print('\n[+] Getting Product Details\n')
		req = requests.get(product_url,headers=header,proxies=proxy)
		#print(req.text)
		if 'json' in req.headers.get('Content-Type') and req.status_code == requests.codes.ok:
			prod = req.json()
			for data in prod:
				if 'title' in data:
					print('[+] Product Name => {}'.format(data['title']))
		else:
			print('[+] Problem with API Connection')
	except Exception as e:
		print('\n[+] Exception Occured! => ',e)
	else:
		pick_options(header,proxy)

def get_order_keys(header,proxy):
	order_url = 'https://shoppy.gg/api/v1/orders/'
	try:
		print('\n[+] All Order Product Serial\n')
		req = requests.get(order_url,headers=header,proxies=proxy)
		if req.status_code == 200:
			if 'json' in req.headers.get('Content-Type') and req.status_code == requests.codes.ok:
				js = req.json()
				for data in js:
					if 'id' in data:
						print('[+] All Product Order Serial => ',data['id'])
				print('\n[+] ORDER Names/Payment/Payment ID\n')
				for data in js:
					if 'product' in data:
						print('[+] Order Name => {}\n[+] Paid At => {}\n[+] Pay ID => {}\n'.format(data['product']['title'],data['paid_at'],data['pay_id']))
		else:
			print('\n[+] Problem with requests!')
	except Exception as e:
		print('\n[+] Excpetion Type => ',e)
	else:
		pick_options(header,proxy)


def get_order_list(header,proxy):
	order_url = 'https://shoppy.gg/api/v1/orders/'
	try:
		req = requests.get(order_url,headers=header,proxies=proxy)
		if req.status_code == 200:
			if 'json' in req.headers.get('Content-Type') and req.status_code == requests.codes.ok:
				js = req.json()
				index = js[1]
				p_serial = index['id']
				p_id = index['product_id']
				p_pinfo = index['product']
				p_title = index['product']['title']
				p_desc = index['product']['description']
				price = index['price']
				address = index['shipping_address']
				
				
				print('\n\n[+] Product Serial => ',p_serial)
				print('[+] Product ID => ',p_id)
				print('[+] Product Title => ',p_title)
				print('[+] Product Price => ',price)
				print('[+] Product Shipping Address => ',address)
				
				
		elif req.status_code != 200:
			print('\n[+] Error in Data communication! check your code...')
		else:
			print('\n\n',req.text)
	except Exception as Err:
		print('\n[+] Exception Occured >> ',Err)
	else:
		pick_options(header,proxy)

def pick_options(header,proxy):
	msg01 = '\n\t\t[+] Option List.\n\t\t[1] Show your recent order\n\t\t[2] All Product list\n\t\t[3] Show Order Serial/Names/Payment Date\n\t\t[4] Back to Main Menu\n\t\t[5] Exit Bot\n'
	for i in msg01:
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.02)
	opt = input('\n[+] Select an Option >>')
	try:
		if opt == '1':
			msg02 = '[+] Getting Order List....'
			for i in msg02:
				sys.stdout.write(i)
				sys.stdout.flush()
				time.sleep(0.02)
			get_order_list(header,proxy)
		elif opt == '2':
			get_product_list(header,proxy)
		elif opt =='3':
			get_order_keys(header,proxy)
		elif opt =='4':
			clear_screen()
			pick_options(header,proxy)
		elif opt == '5':
			sys.exit('\n[+] Good Bye!\t Thanks for choosing X_hammer Shoppy Bot!')
		else:
			print('[+] Unknown option....')
	except Exception:
		print('[+] Invalid Selection')
		sys.exit()


def main():
	api = 'WHBK7OfoqUpax1LJHL1RJJPpkyC65hbBx1UBzngouC5msN27yj'
	header ={'Authorization':api,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0','Accept': 'application/json'}
	url = 'https://shoppy.gg/api/v1/orders/'
	order_page = '/api/v1/orders/?page=1'
	proxy = {'http':pick_proxy()}

	clear_screen()
	about_program()
	pick_options(header,proxy)

if __name__ =='__main__':
	main()
