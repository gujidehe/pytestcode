import yaml

# f = open("config/data.yml",'r',encoding='utf-8')
# data = yaml.safe_load(f)
# print(data)
# print(data['heros_NameAndWord'])

def get_data():
    f = open("F:\PycharmProjects\pytestcode\config\data.yml", 'r', encoding='utf-8')
    data = yaml.safe_load(f)
    return data['heros_NameAndWord']
d=get_data()
print(d)