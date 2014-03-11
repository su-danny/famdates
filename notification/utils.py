import string
import random


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def localize_html_email_images(message):
    """Replace linked images served locally with attached images"""

    import re, os.path
    from email.MIMEImage import MIMEImage

    from django.conf import settings

    image_pattern = """<img\s*.*src=['"](?P<img_src>%s[^'"]*)['"].*\/>""" % settings.STATIC_URL

    image_matches = re.findall(image_pattern, message.alternatives[0][0])

    added_images = {}

    for image_match in image_matches:

        if image_match not in added_images:
            img_content_cid = id_generator()
            on_disk_path = os.path.join(settings.MEDIA_ROOT, image_match.replace(settings.STATIC_URL, ''))
            img_data = open(on_disk_path, 'rb').read()
            img = MIMEImage(img_data)
            img.add_header('Content-ID', '<%s>' % img_content_cid)
            img.add_header('Content-Disposition', 'inline')
            message.attach(img)

            added_images[image_match] = img_content_cid

    def repl(matchobj):
        x = matchobj.group('img_src')
        y = 'cid:%s' % str(added_images[matchobj.group('img_src')])
        return matchobj.group(0).replace(matchobj.group('img_src'), 'cid:%s' % added_images[matchobj.group('img_src')])

    if added_images:
        message.alternatives = [(re.sub(image_pattern, repl, message.alternatives[0][0]), 'text/html')]
        message.body = re.sub(image_pattern, repl, message.body)
        
        