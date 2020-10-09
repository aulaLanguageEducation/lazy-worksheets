# List of URLs for news sites with their respective 'main body of text' HTML tags
ACCEPTED_NEWS_SITES = {


    'theguardian.com': 'article-body-commercial-selector',
    'bbc.co.uk': 'story-body__inner',
    'nytimes.com': 'meteredContent css-1r7ky0e',
    'news.sky.com': 'sdc-site-layout-wrap site-wrap site-wrap-padding',
    'metro.co.uk': 'article-body',
    'huffingtonpost.co.uk': 'page__content__row row--no-border',
    'inews.co.uk': 'article-padding article-content',
    'telegraph.co.uk': 'articleBodyText section',
    'mirror.co.uk': 'article-body',
    'independent.co.uk': 'main-content',

}

DANGEROUS_URL_REGEX = '[a-z]+(%s)|(%s)[.\\w]'
