<a href="https://www.twilio.com">
  <img src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg" alt="Twilio" width="250" />
</a>

# Browser Calls (Django)

> This repository is now archived and is no longer being maintained. 
> Check out the [JavaScript SDK Quickstarts](https://www.twilio.com/docs/voice/sdks/javascript/get-started) to get started with browser-based calling. 

## About

Learn how to use [Twilio's JavaScript SDK](https://www.twilio.com/docs/voice/sdks/javascript) to make browser-to-phone and browser-to-browser calls with ease. The unsatisfied customers of the Birchwood Bicycle Polo Co. need your help!

## Set up

### Requirements

- [Python](https://www.python.org/) **3.6**, **3.7** or **3.8** version
- [Sqlite3](https://www.sqlite.org/)
- [Nodejs](https://nodejs.org/) v10 or v12

### Twilio Account Settings

This application should give you a ready-made starting point for writing your own application.
Before we begin, we need to collect all the config values we need to run the application:

| Config Value | Description            |
| :----------- | :----------------------|
| TWILIO_ACCOUNT_SID  | Your primary Twilio account identifier - find this [in the Console](https://www.twilio.com/console).|
| TWILIO_NUMBER | A Twilio phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164) - you can [get one here](https://www.twilio.com/console/phone-numbers/incoming) |
| TWIML_APPLICATION_SID | The TwiML application with a voice URL configured to access your server running this app - create one [in the console here](https://www.twilio.com/console/voice/twiml/apps). Also, you will need to configure the Voice "REQUEST URL" on the TwiML app once you've got your server up and running. |
| API_KEY / API_SECRET | Your REST API Key information needed to create an [Access Token](https://www.twilio.com/docs/iam/access-tokens) - create [one here](https://www.twilio.com/console/project/api-keys). |

### Create a TwiML App

This project is configured to use a **TwiML App**, which allows us to easily set the voice URLs for all Twilio phone numbers we purchase in this app.

Create a new TwiML app at https://www.twilio.com/console/voice/twiml/apps and use its `Sid` as the `TWIML_APPLICATION_SID` environment variable wherever you run this app.

Once you have created your TwiML app, configure your Twilio phone number to use it ([instructions here](https://support.twilio.com/hc/en-us/articles/223180928-How-Do-I-Create-a-TwiML-App-)). If you don't have a Twilio phone number yet, you can purchase a new number in your [Twilio Account Dashboard](https://www.twilio.com/console/phone-numbers/incoming).

### Local development

1. Clone this repo and `cd` into it.

   ```bash
   git clone https://github.com/TwilioDevEd/browser-calls-django.git
   cd browser-calls-django
   ```

2. Create a new virtual environment, load it and install dependencies.

   ```bash
   make install
   ```


3. Install the twilio-client js library.

   ```bash
   npm install
   ```

4. Set your environment variables. Copy the env.example file and edit it.

   ```bash
   cp .env.example .env
   ```

   See [Twilio Account Settings](#twilio-account-settings) to locate the necessary environment variables.

5. Run the migrations.

    ```bash
    make serve-setup
    ```

6. Start the development server (will run on port 8000). Before running the following command, make sure the virtual environment is activated.

    ```bash
    make serve
    ```

7. Expose your application to the wider internet using [ngrok](http://ngrok.com). This step
   **is important** because the application won't work as expected if you run it through
   localhost.

   ```bash
   $ ngrok http 8000
   ```

8. Once you have started ngrok, update your [TwiML app's](#create-a-twiml-app) voice URL setting to use
   your ngrok hostname, so it will look something like this:

   ```bash
   http://<your-ngrok-subdomain>.ngrok.io/support/call
   ```

9. Everything is setup, now you can open two tabs:
    - The support agent: http://localhost:8000/support/dashboard
    - The customer: http://localhost:8000

    When the customer click on the "Call Support" button, the support agent will see the call immediatly and be able to pick up the call with the "Answer Call" button.

    Another scenario is the customer fill out the form to open a ticket, the support agent can refresh the dashboard and we'll be able to click the "Call customer" button which will start a call to the phone number listed in the ticket.

That's it!

### Tests

You can run the tests locally through [coverage](http://coverage.readthedocs.org/), before running the following command, make sure the virtual environment is activated.

```
$ coverage run manage.py test --settings=twilio_sample_project.settings.test
```

You can then view the results with `coverage report` or build an HTML report with `coverage html`.                        |

## Resources

- The CodeExchange repository can be found [here](https://github.com/twilio-labs/code-exchange/).

## License

[MIT](http://www.opensource.org/licenses/mit-license.html)

## Disclaimer

No warranty expressed or implied. Software is as is.

[twilio]: https://www.twilio.com
