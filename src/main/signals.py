from django.db.models.signals import post_save
from .models import Project
from django.dispatch import receiver


@receiver(post_save, sender=Project)
def post_new_project(sender, instance, created, **kwargs):
    import tweepy
    import requests
    from requests.exceptions import ConnectionError
    from google.cloud import storage

    url = 'https://www.google.com/'

    try:
        data = requests.get(url, timeout=3)
        status = data.status_code
    except ConnectionError:
        status = "404"

    if created and status == "200":
        # Needed authenticate keys
        twitter_auth_keys = {
            "consumer_key": "xhV18SyvvK5UINfEEsuNEfSU8",
            "consumer_secret": "K14bOaui7tcCgZifSrohXLg1GvMuUDykBrPdrYkSeuAUw6oPCM",
            "access_token": "1192177382024724485-xvAVnYx2ML3jKwEdisPuNmGj71VUnM",
            "access_token_secret": "tQtuBUeMXfg91NbwamBZ1o8bn5QMvX2aCa9hoU6IM1wip"
        }
        auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
        )
        auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret'],
        )

        api = tweepy.API(auth)

        post_name = instance.project_name
        source_code = instance.project_url
        post_author = instance.author
        post_date = instance.posted_at

        tweet = """Recent Post on Website Portfolio\nCreated {}\nThe link to the source code is {}\nPosted at {}\n#robot #portfolio #automatic #LokotamaThe""".format(
            post_name, source_code, post_author, post_date)

        status = api.update_status(status=tweet)

    profile_picture = instance.project_picture.url

    client = storage.Client()
    bucket = client.get_bucket('gs://website-portfolio-fc57b.appspot.com')

    blob = bucket.blob(profile_picture)
    blob.upload_from_filename(filename=profile_picture)
