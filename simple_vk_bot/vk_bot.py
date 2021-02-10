import vk_api, random

GROUP_ID = 200421873
TOKEN = '9aa5a842c8732d66f400bad709e212518d693ff5e3e9b6e0d89a81b9739c7e0cc41022ad8cc477e1ce94c'

vk = vk_api.VkApi(token=TOKEN)
vk._auth_token()
# список с 3мя картинками, уже загруженными на сервер и приведенными к нужному названию(айди группы и айди фото)
cats = ['photo-200421873_457239017', 'photo-200421873_457239019', 'photo-200421873_457239020']
while True:
    messages = vk.method('messages.getConversations', {'offset': 0, 'count': 20, 'filter': 'unanswered'})
    if messages['count'] > 0:
        text = messages['items'][0]['last_message']['text']
        user_id = messages['items'][0]['last_message']['from_id']
        if text.lower() == 'привет':
            vk.method('messages.send',
                      {'user_id': user_id, 'message': 'hello my friend', 'random_id': random.randint(1, 1000)})
        elif text.lower() == 'фото':
            # uploader = vk_api.upload.VkUpload(vk)
            # указано название фото, загруженного вручную в папку с ботом
            # img = uploader.photo_messages('3.jpg')
            # id фото, полученное при помощи принта при отправке сообщения
            # media_id = str(img[0]['id'])
            # id группы
            # owner_id = str(img[0]['owner_id'])
            # название, нужное для 'attachment'
            # print('photo'+ owner_id + '_' + media_id)
            vk.method('messages.send',
                      {'user_id': user_id, 'attachment': random.choice(cats), 'random_id': random.randint(1, 1000)})
        else:
            vk.method('messages.send',
                      {'user_id': user_id, 'message': 'i dont understand', 'random_id': random.randint(1, 1000)})
