import { SmartThingsClient } from '@smartthings/core-sdk';

token = '372563b7-09f8-485b-8c95-261793424ad9'
const client = new SmartThingsClient({
  accessToken: 'YOUR_PERSONAL_ACCESS_TOKEN'
});
async function listDevices() {
  const devices = await client.devices.list();
  console.log(devices);
}

listDevices();