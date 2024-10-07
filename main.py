import requests

API_KEY = 'live_H35oNnIfXHw0lvjeesVPj09zDMpTSL4WKr0o8wqXjQ2UzjPGnuiPtlutanRTqACL'


def headers_request():
    headers_request = {
        'x-api-key': API_KEY,
    }
    return headers_request


def get_id_image(response):
    response_json = response.json()
    image_id = response_json[0]['id']
    return image_id


def get_id_image_for_delete(response):
    response_json = response.json()
    image_id = response_json.get('id')
    return image_id


def print_response(response):
    print(response.status_code)
    print(response.text)


def send_request_get_search():
    url = 'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url)
    return response


def send_request_get_image_for_id():
    response = send_request_get_search()
    image_id = get_id_image(response)
    url = f'https://api.thecatapi.com/v1/images/{image_id}'
    response = requests.get(url)
    return response


def send_request_get_image_for_id_analysis():
    response = send_request_get_search()
    image_id = get_id_image(response)
    url = f'https://api.thecatapi.com/v1/images/{image_id}/analysis'
    response = requests.get(url)
    return response


def send_request_get_my_uploads():
    url = 'https://api.thecatapi.com/v1/images/?limit=10&page=0&order=DESC'
    headers = headers_request()
    response = requests.get(url, headers=headers)
    return response


def send_request_post_images_upload():
    url = 'https://api.thecatapi.com/v1/images/upload'
    headers = headers_request()
    with open("5hs.jpg", 'rb') as file:
        files = {'file': ('5hs.jpg', file, 'image/jpeg')}
        response = requests.post(url, headers=headers, files=files)
    return response


def send_request_del_images_upload():
    response = send_request_post_images_upload()
    image_id = get_id_image_for_delete(response)
    url = f'https://api.thecatapi.com/v1/images/{image_id}/'
    headers = headers_request()
    response = requests.delete(url, headers=headers)
    return response


def send_request_get_images_breeds():
    response = send_request_get_search()
    image_id = get_id_image(response)
    url = f'https://api.thecatapi.com/v1/images/{image_id}/breeds'
    headers = headers_request()
    response = requests.get(url, headers=headers)
    return response


def send_request_post_images_breeds():
    response = send_request_post_images_upload()
    image_id = get_id_image_for_delete(response)
    url = f'https://api.thecatapi.com/v1/images/{image_id}/breeds'
    headers = headers_request()
    data = {
        'breed_id': 'beng'
    }
    response = requests.post(url, headers=headers, json=data)
    return response


def send_request_del_images_breeds():
    response = send_request_post_images_upload()
    image_id = get_id_image_for_delete(response)
    headers = headers_request()
    url = f'https://api.thecatapi.com/v1/images/{image_id}/breeds/'
    breed_id = 'beng'
    data = {
        'breed_id': breed_id
    }
    response = requests.post(url, headers=headers, json=data)
    url = f'https://api.thecatapi.com/v1/images/{image_id}/breeds/{breed_id}'
    response = requests.delete(url, headers=headers)
    return response


if __name__ == '__main__':
    response_search = send_request_get_search()  ### GET /images/search
    print_response(response_search)
    response_get_image_for_id = send_request_get_image_for_id()  ### GET /images/:image_id
    print_response(response_get_image_for_id)
    response_image_analysis = send_request_get_image_for_id_analysis()  ###  GET /images/:image_id/analysis
    print_response(response_image_analysis)
    response_my_uploads = send_request_get_my_uploads()  ### GET /images/ (Your uploads)
    print_response(response_my_uploads)
    response_post_images_upload = send_request_post_images_upload()  ### POST /images/upload
    print_response(response_post_images_upload)
    response_del_images_upload = send_request_del_images_upload()  ### DEL /images/:image_id
    print_response(response_del_images_upload)
    response_get_breeds = send_request_get_images_breeds()  ### GET /images/:image_id/breeds
    print_response(response_get_breeds)
    response_post_images_breeds = send_request_post_images_breeds()  ### POST /images/:image_id/breeds
    print_response(response_post_images_breeds)
    response_del_images_breeds = send_request_del_images_breeds()  ### DEL /images/:image_id/breeds/:breed_id
    print_response(response_del_images_breeds)
