// Using setInterval to change the bot's status every 10 seconds
setInterval(() => {
    let x = BdApi.Webpack.getStore("PresenceStore").getStatus('450867169581072394')
    if (x != "offline") {
        const {
            setting1: BdApi.Webpack.getStore("PresenceStore").getStatus('450867169581072394')
    });
}, 1000);
