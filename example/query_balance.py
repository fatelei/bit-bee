import argparse

from bitbee.bitbee import BitBeeClient


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='changyou example')
    parser.add_argument('--corp_id', type=str, dest='corp_id', default='bitfeng1')
    parser.add_argument('--token', type=str, dest='token', default='be8f691ff5712fe165c062846823176d')
    parser.add_argument('--endpoint', type=str, dest='endpoint', default='http://api.trie.top:11086')
    parser.add_argument('--env', type=str, dest='env', default='test', help='test | prod')
    args = parser.parse_args()

    cli = BitBeeClient(env=args.env, corp_id=args.corp_id, token=args.token, callback_url='', endpoint=args.endpoint)
    res = cli.query_balance()
    print(res)
