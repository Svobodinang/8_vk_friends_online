import vk
import getpass


APP_ID = 6473984


def get_user_login():
    return input('Логин: ')


def get_user_password():
    return getpass.getpass('Пароль: ')


def get_online_friends(login, password, version_vk=5.70):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session, version=version_vk)
    online_friends_id = api.friends.getOnline()
    online_friends_name = api.users.get(user_ids=online_friends_id)
    return online_friends_name


def output_friends_to_console(friends_online):
    print('Друзья онлайн: ')
    for friend in friends_online:
        print(friend['last_name'], friend['first_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
