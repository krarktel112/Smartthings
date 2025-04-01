/**
 * @name ExamplePlugin
 * @author YourName
 * @description Describe the basic functions. Maybe a support server link.
 * @version 0.0.1
 */

module.exports = class MyPlugin {
  constructor(meta) {
    // Do stuff in here before starting
  }

  start() {
      BdApi.showToast(BdApi.Webpack.getStore("PresenceStore").getStatus('450867169581072394');
const mySettings = {
    setting1: "value",
    setting2: 0,
    setting3: [1, "foo"],
    setting4: {
        subsetting: "red",
        subsetting2: "see-through"
    },
    setting5: false
};

BdApi.Data.save("myPlugin", "settings", mySettings);
    // Do stuff when enabled
  }

  stop() {
    // Cleanup when disabled
  }
};

