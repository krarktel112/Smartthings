npm install @smartthings/core-sdk
const { SmartThingsClient } = require('@smartthings/core-sdk');

async function executeScene(sceneId) {
  const client = new SmartThingsClient({
    accessToken: 'YOUR_PERSONAL_ACCESS_TOKEN',
  });

  try {
    await client.scenes.execute(sceneId);
    console.log('Scene executed successfully!');
  } catch (error) {
    console.error('Error executing scene:', error);
  }
}

// Example usage
executeScene('YOUR_SCENE_ID');
const { SmartThingsClient, BearerTokenAuthenticator } = require('@smartthings/core-sdk');

const PERSONAL_ACCESS_TOKEN = '372563b7-09f8-485b-8c95-261793424ad9';
const ROUTINE_ID = 'YOUR_ROUTINE_ID';

const client = new SmartThingsClient(new BearerTokenAuthenticator(PERSONAL_ACCESS_TOKEN));

async function executeRoutine() {
  try {
    await client.routines.execute(ROUTINE_ID);
    console.log('Routine executed successfully!');
  } catch (error) {
    console.error('Error executing routine:', error);
  }
}

executeRoutine();
