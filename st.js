import { SmartThingsClient } from '@smartthings/core-sdk';

const client = new SmartThingsClient({
  accessToken: '372563b7-09f8-485b-8c95-261793424ad9'
});
async function listDevices() {
  const devices = await client.devices.list();
  console.log(devices);
}

listDevices();