const Eris = require("eris");
const axios = require("axios");
const cheerio = require("cheerio");

const {
    helpTxt,
    notice
} = require("./help");
const {
    requiredExpByLevel,
    cumulativeExpByLevel,
    EXP_AT_250,
    EXP_AT_275
} = require("./constants/expConsts");

const bot = new Eris(
    "NDE3MzAwNDU3MDQ4NzY4NTEy.DXRA3w.IqK03Ekf68lgBrmy9jl5OKKWRlo"
);

const id = "!테스트";

bot.on("ready", () => {
    console.log("Ready!");
});

bot.on("messageCreate", msg => {
    if (msg.content.startsWith(id)) {
        if (msg.content.includes("ping")) {
            bot.createMessage(msg.channel.id, "pong");
        } else if (msg.content.includes("pong")) {
            bot.createMessage(msg.channel.id, "ping!");
        } else {
            // bot.createMessage(msg.channel.id, {
            //   embed: {
            //     title: "I'm an embed!", // Title of the embed
            //     description:
            //       "Here is some more info, with **awesome** formatting.\nPretty *neat*, huh?",
            //     // author: { // Author property
            //     //     name: msg.author.username,
            //     //     icon_url: msg.author.avatarURL
            //     // },
            //     thumbnail: {
            //       url: "https://zxcvber.com/images/profimg.jpg"
            //     },
            //     color: 0x008000, // Color, either in hex (show), or a base-10 integer
            //     fields: [
            //       // Array of field objects
            //       {
            //         name: "Some extra info.", // Field title
            //         value: "Some extra value.", // Field
            //         inline: true // Whether you want multiple fields in same line
            //       },
            //       {
            //         name: "Some more extra info.",
            //         value: "Another extra value.",
            //         inline: true
            //       }
            //     ],
            //     footer: {
            //       // Footer text
            //       text: "Created with Eris."
            //     }
            //   }
            // });
        }
    }
});

// misc commands
bot.on("messageCreate", msg => {
    if (msg.content.startsWith("!주장봇")) {
        var text = msg.content.substring(5);
        checkGreetings(msg, text);
        checkBark(msg, text);
    } else if (msg.content.startsWith("!정보")) {
        var username = msg.content.substring(4).trim();
        getLevelInfo(msg, username);
    } else if (msg.content.startsWith("!공지사항")) {
        bot.createMessage(msg.channel.id, notice);
    } else if (msg.content.startsWith("!경험치")) {
        var username = msg.content.substring(5).split(" ")[0];
        getUserExpInfo(msg, username);
    } else if (msg.content.startsWith("!도움말")) {
        bot.createMessage(msg.channel.id, helpTxt);
    }
});

const hiWords = ["하이", "하잉", "안녕", "안뇽"];

const checkGreetings = (msg, text) => {
    for (const hi of hiWords) {
        if (text.startsWith(hi)) {
            var nickname = msg.member.nick;
            if (nickname === undefined || nickname === null) {
                nickname = msg.author.username;
            }
            bot.createMessage(msg.channel.id, "안녕! " + nickname + "! :hearts:");
            break;
        }
    }
};

const checkBark = (msg, text) => {
    var i = text.indexOf("물어");
    if (i >= 0) {
        var target = text.substring(0, i).trim();
        if (target.startsWith("그린") || target.startsWith("모이스쳐그린")) {
            bot.createMessage(msg.channel.id, "주인님은 안 물어요! :dog:");
            return;
        }
        if (target.length > 0) {
            target += " ";
        }
        bot.createMessage(msg.channel.id, target + "크앙! :dog:");
    }
};

async function getRanking(username) {
    try {
        return await axios.get(
            "https://maplestory.nexon.com/Ranking/World/Total?c=" + encodeURI(username)
        );
    } catch (error) {
        console.error(error);
    }
}

const getLevelInfo = (msg, username) => {
    getAndSendEmbed(msg, username);
};

const getAndSendEmbed = (msg, username) => {
    getRanking(username).then(html => {
        const $ = cheerio.load(html.data);
        var data = $("tr.search_com_chk").children("td");

        var entries = [];
        data.each(function (i, elem) {
            entries.push($(this));
        });

        // get worldRanking
        var worldRanking = entries[0].children().first().text().trim();
        // console.log(worldRanking);

        // get picture link
        var picLink = entries[1].children().children().attr("src").trim();
        // console.log(picLink);

        // job group and job
        var jobText = entries[1].children("dl").children("dd").text().trim().split("/");
        var jobGroup = jobText[0].trim();
        var job = jobText[1].trim();
        // console.log(jobGroup, job);

        // level
        var level = entries[2].text().trim();
        var levelValue = parseInt(level.split(".")[1]);
        // console.log(levelValue);

        // exp
        var experience = entries[3].text().trim();
        var percentage = getCurrentPercentage(experience, levelValue);
        // console.log(percentage);
        // console.log(experience);

        // popularity
        var popularity = entries[4].text().trim();
        // console.log(popularity);

        // guild
        var guild = entries[5].text().trim();
        // console.log(guild);
        if (guild.length === 0) {
            guild = "-";
        }

        var embed = {
            embed: {
                url: "https://maple.gg/u/" + encodeURI(username),
                title: username,
                description: job + " / " + level,
                thumbnail: {
                    url: picLink.trim()
                },
                color: 0x008000,
                fields: [{
                        name: "EXP",
                        value: experience + " (" + percentage + "%)"
                    },
                    {
                        name: "인기도",
                        value: popularity
                    },
                    {
                        name: "길드",
                        value: guild
                    }
                ],
                image: {
                    url: picLink
                }
            }
        };

        bot.createMessage(msg.channel.id, embed);
    });
};

const getCurrentPercentage = (experience, level) => {
    experience = parseIntFromExpString(experience);
    if (level === 275) {
        return 0.0;
    }
    return roundToTwoDecimalPlaces(
        (experience / requiredExpByLevel[level - 1]) * 100
    );
};

const parseIntFromExpString = experience => {
    return parseInt(experience.replace(/,/g, ""));
};

const getCumulativeExp = (experience, level) => {
    experience = parseIntFromExpString(experience);
    var cumulative = level > 1 ? cumulativeExpByLevel[level - 2] : 0;
    return cumulative + experience;
};

const getAchievedRate = (requiredExp, totalExp) => {
    var requiredRate = roundToTwoDecimalPlaces((requiredExp / totalExp) * 100);
    var achievedRate = 100 - requiredRate;
    return roundToTwoDecimalPlaces(achievedRate);
};

const roundToTwoDecimalPlaces = f => {
    return +f.toFixed(2);
};

const convertIntToCommaFormat = x => {
    return x.toString().replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ",");
};

const getUserExpInfo = (msg, username) => {
    getRanking(username).then(html => {
        const $ = cheerio.load(html.data);
        var data = $("tr.search_com_chk").children("td");

        var entries = [];
        data.each(function (i, elem) {
            entries.push($(this));
        });

        // job group and job
        var jobText = entries[1].children("dl").children("dd").text().trim().split("/");
        var jobGroup = jobText[0].trim();
        var job = jobText[1].trim();

        // level
        var level = entries[2].text().trim();
        var levelValue = parseInt(level.split(".")[1]);

        // exp
        var experience = entries[3].text().trim();
        var percentage = getCurrentPercentage(experience, levelValue);
        var cumulativeExp = getCumulativeExp(experience, levelValue);

        var embed = {
            embed: {
                url: "https://maple.gg/u/" + encodeURI(username),
                title: username,
                description: job + " / " + level,
                color: 0x000080,
                fields: [{
                        name: "EXP",
                        value: experience + " (" + percentage + "%)"
                    },
                    {
                        name: "누적 경험치",
                        value: convertIntToCommaFormat(cumulativeExp)
                    },
                    {
                        name: "Lv.250 까지",
                        value: printAchievedRate(cumulativeExp, EXP_AT_250)
                    },
                    {
                        name: "Lv.275 까지",
                        value: printAchievedRate(cumulativeExp, EXP_AT_275)
                    }
                ]
            }
        };

        bot.createMessage(msg.channel.id, embed);
    });
};

const printAchievedRate = (cumulativeExp, totalExp) => {
    var requiredExp = Math.max(0, totalExp - cumulativeExp);
    var requiredExpString = convertIntToCommaFormat(requiredExp);
    var achievedRate = getAchievedRate(requiredExp, totalExp);
    return requiredExpString + " (" + achievedRate + "% 달성)";
};

bot.connect(); // Get the bot to connect to Discord
