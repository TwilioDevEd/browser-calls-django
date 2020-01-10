<a href="https://www.twilio.com">
  <img src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg" alt="Twilio" width="250" />
</a>

# Browser Calls (Django)

[![Build Status](https://travis-ci.org/TwilioDevEd/browser-calls-django.svg?branch=master)](https://travis-ci.org/TwilioDevEd/browser-calls-django)
[![Coverage Status](https://coveralls.io/repos/TwilioDevEd/browser-calls-django/badge.svg?branch=master&service=github)](https://coveralls.io/github/TwilioDevEd/browser-calls-django?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> We are currently in the process of updating this sample template. If you are encountering any issues with the sample, please open an issue at [github.com/twilio-labs/code-exchange/issues](https://github.com/twilio-labs/code-exchange/issues) and we'll try to help you.

Learn how to use [Twilio Client](https://www.twilio.com/client) to make browser-to-phone and browser-to-browser calls with Python. The unsatisfied customers of the Birchwood Bicycle Polo Co. need your help!

**Full Tutorial:** https://www.twilio.com/docs/voice/tutorials/browser-calls-python-django

## Quickstart

### Create a TwiML App

This project is configured to use a **TwiML App**, which allows us to easily set the voice URLs for all Twilio phone numbers we purchase in this app.

Create a new TwiML app at https://www.twilio.com/console/voice/twiml/apps and use its `Sid` as the `TWIML_APPLICATION_SID` environment variable wherever you run this app.

Once you have created your TwiML app, configure your Twilio phone number to use it ([instructions here](https://support.twilio.com/hc/en-us/articles/223180928-How-Do-I-Create-a-TwiML-App-)). If you don't have a Twilio phone number yet, you can purchase a new number in your [Twilio Account Dashboard](https://www.twilio.com/console/phone-numbers/incoming).

### Local development

This project is built using the [Django](https://www.djangoproject.com/) web framework. It runs on Python 3.6+.

To run the app locally, first clone this repository and `cd` into its directory. Then:

1. Create a new virtual environment:
    - If using vanilla [virtualenv](https://docs.python.org/3/library/venv.html):

        ```
        python -m venv venv
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

1. Install the twilio-client js library:

    ```
    npm install
    ```

1. Copy the `.env_example` file to `.env`, and edit it to include your [Twilio API credentials](https://www.twilio.com/console) and the phone number and TwimL App Sid you made above. We use [python-dotenv](https://github.com/theskumar/python-dotenv) to load those variables automatically.

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

## Testing it humanly

Once everything is setup, you can open two tabs:
- The support agent: http://localhost:8000/support/dashboard
- The customer: http://localhost:8000

When the customer click on the "Call Support" button, the support agent will see the call immediatly and be able to pick up the call with the "Answer Call" button.

Another scenario is the customer fill out the form to open a ticket, the support agent can refresh the dashboard and we'll be able to click the "Call customer" button which will start a call to the phone number listed in the ticket.

## Run the tests

You can run the tests locally through [coverage](http://coverage.readthedocs.org/):

```
$ coverage run manage.py test --settings=twilio_sample_project.settings.test
```

You can then view the results with `coverage report` or build an HTML report with `coverage html`.

## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.
