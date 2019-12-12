# Kinetic GMM Cloud Scripts

This is a simple script on how to use the Kinetic GMM API and get data about deployed Cisco gateways (IR829, IR809, IR807, IR1101) into a python script.

Basically the script has two functions:

1. getgateways(): Get information about all the gateways of your organization
2. gatewayconnectivity(): Check proactively if all gateways are connected

## Getting Started

1. Create an API token in the Kinetic Cloud and put the data in the script. You can find more in the [Kinetic documentation](https://developer.cisco.com/docs/kinetic/#!generate-api-keys/generate-api-keys).
2. Check your Kinetic Cloud organization ID: Login to the portal, click on the main Dashboard and in the URL you can see it:

```
https://eu.ciscokinetic.io/organizations/{your organization ID}
```
3. Run the script (& definitely check the [API Documentation](https://developer.cisco.com/docs/kinetic-api/))

## Built With

* Kinetic Gateway Management Module (Kinetic Cloud)
* Paho-MQTT

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE.md](LICENSE.md) file for details

## Further Links

Cisco DevNet Website: https://developer.cisco.com

Kinetic Documentation: https://developer.cisco.com/docs/kinetic/

API Documentation: https://developer.cisco.com/docs/kinetic-api/

Kinetic Cloud EU: https://eu.ciscokinetic.io
Kinetic Cloud US: https://us.ciscokinetic.io
