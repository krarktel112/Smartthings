// Using setInterval to change the bot's status every 10 seconds
setInterval(() => {
    const randomActivity = activities[Math.floor(Math.random() * activities.length)];
    bot.change_presence({
        activities: [{ name: randomActivity, type: "PLAYING" }],
        status: "online"
    });
}, 10000);
