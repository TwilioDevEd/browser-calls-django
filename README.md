# Browser Calls (Django)

[![Build Status](https://travis-ci.org/TwilioDevEd/browser-calls-django.svg?branch=master)](https://travis-ci.org/TwilioDevEd/browser-calls-django)
[![Coverage Status](https://coveralls.io/repos/TwilioDevEd/browser-calls-django/badge.svg?branch=master&service=github)](https://coveralls.io/github/TwilioDevEd/browser-calls-django?branch=master)

Learn how to use [Twilio Client](https://www.twilio.com/client) to make browser-to-phone and browser-to-browser calls with Python. The unsatisfied customers of the Birchwood Bicycle Polo Co. need your help!

**Full Tutorial:** https://www.twilio.com/docs/howto/walkthrough/browser-calls/python/django

## Quickstart

### Create a TwiML App

This project is configured to use a **TwiML App**, which allows us to easily set the voice URLs for all Twilio phone numbers we purchase in this app.

Create a new TwiML app at https://www.twilio.com/user/account/apps/add and use its `Sid` as the `TWIML_APPLICATION_SID` environment variable wherever you run this app.

![Creating a TwiML App](http://howtodocs.s3.amazonaws.com/call-tracking-twiml-app.gif)

Once you have created your TwiML app, configure your Twilio phone number to use it ([instructions here](https://www.twilio.com/help/faq/twilio-client/how-do-i-create-a-twiml-app)). If you don't have a Twilio phone number yet, you can purchase a new number in your [Twilio Account Dashboard](https://www.twilio.com/user/account/phone-numbers/incoming).

### Local development

This project is built using the [Django](https://www.djangoproject.com/) web framework. It runs on Python 2.7+ and Python 3.4+.

To run the app locally, first clone this repository and `cd` into its directory. Then:

1. Create a new virtual environment:
    - If using vanilla [virtualenv](https://virtualenv.pypa.io/en/latest/):

        ```
        virtualenv venv
        source venv/bin/activate
        ```

    - If using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/):

        ```
        mkvirtualenv browser-calls-django
        ```

1. Install the requirements:

    ```
    pip install -r requirements.txt
    ```
1. Copy the `.env_example` file to `.env`, and edit it to include your [Twilio API credentials](https://www.twilio.com/user/account/voice) and the phone number and TwimL App Sid you made above

1. Run `source .env` to apply the environment variables (or even better, use [autoenv](https://github.com/kennethreitz/autoenv))

1. Start a local PostgreSQL database and create a database called `browser_calls`:
    - If on a Mac, we recommend [Postgres.app](http://postgresapp.com/). After install, open psql and run `CREATE DATABASE browser_calls;`
    - If Postgres is already installed locally, you can just run `createdb browser_calls` from a terminal

1. Run the migrations with:

    ```
    python manage.py migrate
    ```

1. Be sure to create a superuser so you can access the Support Dashboard and the Django admin:

    ```
    python manage.py createsuperuser
    ```
1. Start the development server:

    ```
    python manage.py runserver
    ```

To actually forward incoming calls, your development server will need to be publicly accessible. [We recommend using ngrok to solve this problem](https://www.twilio.com/blog/2015/09/6-awesome-reasons-to-use-ngrok-when-testing-webhooks.html).

Once you have started ngrok, update your TwiML app's voice URL setting to use your ngrok hostname, so it will look something like this:

```
http://88b37ada.ngrok.io/support/call
```

## Run the tests

You can run the tests locally through [coverage](http://coverage.readthedocs.org/):

```
$ coverage run manage.py test --settings=twilio_sample_project.settings.test
```

You can then view the results with `coverage report` or build an HTML report with `coverage html`.
