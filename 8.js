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
