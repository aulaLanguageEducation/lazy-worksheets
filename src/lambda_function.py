import json
"""
from lazy_worksheets import utils
from lazy_worksheets import gap_filler
"""
import utils
import gap_filler

print('Loading function')


def lambda_handler(event, context):
    input_url = event['queryStringParameters']['url']

    boilerplate_response = {
        "statusCode": 500,
        "headers": {
            "my_header": "my_value"
        },
        "body": '',
        "isBase64Encoded": False
    }

    # check for dangerous url
    if not utils.url_safety_check(input_url):
        boilerplate_response['body'] = 'unsupported url'
        boilerplate_response['statusCode'] = 400
        return boilerplate_response

    # check for supported news source
    if not utils.supported_news_site_check(input_url):
        boilerplate_response['body'] = 'unsupported url'
        boilerplate_response['statusCode'] = 400
        return boilerplate_response

    try:
        url_data_dict = utils.get_body(input_url)
    except Exception as e:
        boilerplate_response['body'] = 'server error'
        boilerplate_response['statusCode'] = 400
        return boilerplate_response

    gap_filler_obj = gap_filler.GapFiller()

    try:
        worksheet_data_dict = gap_filler_obj.fill_gaps(url_data_dict)
    except Exception as e:
        boilerplate_response['body'] = 'server error'
        boilerplate_response['statusCode'] = 400
        return boilerplate_response

    boilerplate_response['body'] = json.dumps(worksheet_data_dict)
    boilerplate_response['statusCode'] = 200

    return boilerplate_response


if __name__ == '__main__':
    output = lambda_handler(event={'queryStringParameters': {'url': 'https://www.theguardian.com/us-news/2020/nov/13/trump-biden-white-house-defeat-election'}},
                            context='')
