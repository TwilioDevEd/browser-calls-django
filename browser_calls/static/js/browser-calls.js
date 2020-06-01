/**
 * Twilio Client configuration for the browser-calls-django
 * example application.
 */

// Store some selectors for elements we'll reuse
var callStatus = $("#call-status");
var answerButton = $(".answer-button");
var callSupportButton = $(".call-support-button");
var hangUpButton = $(".hangup-button");
var callCustomerButtons = $(".call-customer-button");

var device;

/* Helper function to update the call status bar */
function updateCallStatus(status) {
  callStatus.attr('placeholder', status);
}

console.log("Requesting Access Token...");

$(document).ready(function() {
  $.get("/support/token", {forPage: window.location.pathname})
    .then(function(data) {
      // Setup Twilio.Device
      device = new Twilio.Device(data.token, {
        // Set Opus as our preferred codec. Opus generally performs better, requiring less bandwidth and
        // providing better audio quality in restrained network conditions. Opus will be default in 2.0.
        codecPreferences: ["opus", "pcmu"],
        // Use fake DTMF tones client-side. Real tones are still sent to the other end of the call,
        // but the client-side DTMF tones are fake. This prevents the local mic capturing the DTMF tone
        // a second time and sending the tone twice. This will be default in 2.0.
        fakeLocalDTMF: true,
        // Use `enableRingingState` to enable the device to emit the `ringing`
        // state. The TwiML backend also needs to have the attribute
        // `answerOnBridge` also set to true in the `Dial` verb. This option
        // changes the behavior of the SDK to consider a call `ringing` starting
        // from the connection to the TwiML backend to when the recipient of
        // the `Dial` verb answers.
        enableRingingState: true
      });

      device.on("ready", function(device) {
        console.log("Twilio.Ready");
        updateCallStatus("Ready");
      });

      device.on("error", function(error) {
        console.log("Twilio.Device Error: " + error.message);
        updateCallStatus("ERROR: " + error.message);
      });

      device.on("connect", function(conn) {
        // Enable the hang up button and disable the call buttons
        hangUpButton.prop("disabled", false);
        callCustomerButtons.prop("disabled", true);
        callSupportButton.prop("disabled", true);
        answerButton.prop("disabled", true);

        // If phoneNumber is part of the connection, this is a call from a
        // support agent to a customer's phone
        if ("phoneNumber" in conn.message) {
            updateCallStatus("In call with " + conn.message.phoneNumber);
        } else {
            // This is a call from a website user to a support agent
            updateCallStatus("In call with support");
        }
      });

      device.on("disconnect", function(conn) {
        // Disable the hangup button and enable the call buttons
        hangUpButton.prop("disabled", true);
        callCustomerButtons.prop("disabled", false);
        callSupportButton.prop("disabled", false);

        updateCallStatus("Ready");
      });

      device.on("incoming", function(conn) {
        updateCallStatus("Incoming support call");

        // Set a callback to be executed when the connection is accepted
        conn.accept(function() {
            updateCallStatus("In call with customer");
        });

        // Set a callback on the answer button and enable it
        answerButton.click(function() {
            conn.accept();
        });
        answerButton.prop("disabled", false);
      });

    })
    .catch(function(err){
      console.log(err);
      console.log("Could not get a token from server!");
    })
});

/* Call a customer from a support ticket */
function callCustomer(phoneNumber) {
  updateCallStatus("Calling " + phoneNumber + "...");

  var params = {"phoneNumber": phoneNumber};
  device.connect(params);
}

/* Call the support_agent from the home page */
function callSupport() {
  updateCallStatus("Calling support...");

  // Our backend will assume that no params means a call to support_agent
  device.connect();
}

/* End a call */
function hangUp() {
  device.disconnectAll();
}
