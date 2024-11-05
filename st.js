import { SmartThingsClient } from '@smartthings/core-sdk';

const client = new SmartThingsClient({
  accessToken: 'YOUR_PERSONAL_ACCESS_TOKEN'
});
async function listDevices() {
  const devices = await client.devices.list();
  console.log(devices);
}

listDevices();