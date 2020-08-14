import json
from datetime import datetime
from repurchase.repurchase_data import Client, Purchase

def main():
	with open('client_data.json') as f:
		data = json.load(f)
		client = Client.decode(data)
		client.estimate_repurchases()
		client.print_purchases()
		

if __name__ == '__main__':
    main()