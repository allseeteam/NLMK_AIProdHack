from datetime import datetime, timezone


def extract_date(item):
    # article:published_time
    # article:modified_time
    # date_scraped
    date = None
    try:
        date = item['item']['metatags'][0]['article:published_time']
    except:
        pass
    if date:
        return date
    try:
        date = item['item']['metatags'][0]['article:modified_time']
    except:
        pass
    if date:
        return date
    try:
        date = item['date']
    except:
        pass
    if date:
        return date
    return None


def parse_date(date):
    if date:
        try:
            date = date.rstrip('Z')
            date = datetime.fromisoformat(date)
            date = date.astimezone(timezone.utc).replace(tzinfo=None)
            return date
        except:
            pass
    return None