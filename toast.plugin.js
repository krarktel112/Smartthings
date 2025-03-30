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
      BdApi.showToast("This is a success message!", { type: "success" });
      BdApi.showToast("Be careful!", { type: "warning" });
      BdApi.showToast("An error occurred!", { type: "error" });
    // Do stuff when enabled
  }

  stop() {
    // Cleanup when disabled
  }
};

