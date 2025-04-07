# Example Intent Handler (Conceptual)
def turn_off_switch_handler(handler_input):
    # Get the device ID from the user request
    device_id = handler_input.request_envelope.request.context.device.deviceId
    # Get the namespace for the device (e.g., "Alexa.PowerController")
    namespace = "Alexa.PowerController"
    # Construct the API call
    command = {
        "header": {
            "namespace": namespace,
            "name": "TurnOff",
            "payloadVersion": "3",
            "correlationToken": handler_input.request_envelope.request.requestId
        },
        "payload": {
            "deviceId": device_id
        }
    }
    # Call the Alexa Smart Home API
    handler_input.request_envelope.request.context.device.capabilities.powerController.turnOff(command)
    # Return a response to the user
    handler_input.response_builder.speak("OK, I've turned off the switch").set_should_end_session(True)
    return handler_input.response_builder.response
