from django.conf import settings


def get_comicvine_issue_url(comicvine_id):
    url = settings.COMICVINE_API_ISSUE_URL + str(comicvine_id) + '/?api_key=' + settings.COMICVINE_API_KEY
    if settings.COMICVINE_API_ISSUE_FILTERS:
        url += '&field_list=' + ','.join(settings.COMICVINE_API_ISSUE_FILTERS)
    return url + '&format=json'


# def get_comicvine_volume_url(comicvine_id):
#     url = settings.COMICVINE_API_VOLUME_URL + str(comicvine_id) + '/?api_key=' + settings.COMICVINE_API_KEY
