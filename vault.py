import hvac


def init_server():

    client = hvac.Client(url='http://localhost:8200')
    print(f"Is client authenticated? {client.is_authenticated()}")


init_server()


def write_secret():
    client = hvac.Client(url='http://localhost:8200')
    response = client.secrets.kv.v2.create_or_update_secret(path="hello",secret=dict(foo="bar"))
    print(response)


write_secret()


def read_secret():
    client = hvac.Client(url='http://localhost:8200')
    response = client.secrets.kv.v2.read_secret_version(path='hello')
    password = response['data']['data']['foo']
    print(password)

read_secret()



