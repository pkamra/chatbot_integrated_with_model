/**
 * Copyright (c) Microsoft Corporation. All rights reserved.
 * Licensed under the MIT License.
 */
var request = require('request');
const axios = require('axios');
module.exports = function(controller) {

    // controller.hears('sample','message,direct_message', async(bot, message) => {
    //     await bot.reply(message, 'I heard a sample message.');
    // });

    // controller.on('message,direct_message', async(bot, message) => {
    //     await bot.reply(message, `Echo: ${ message.text }`);
    // });

    controller.on('message,direct_message,message_received',async(bot,message) => {
        if (message.text == 'Fill in the Contact Me Form For Opt Out'){
            await bot.reply(message,'Here is a Contact Me for Opt Out Form for you to use!\n\n[Contact Me Opt Out Form](https://www.optoutprescreen.com/)');
          }else if (message.text == 'Show me the advantages of staying enrolled in managed accounts'){
            await bot.reply(message,'Here is our Investment Methodology extensively documented! Following are some useful links:\n\n[Rockstar Youtube video](https://www.youtube.com/embed/8sujx2Gl1xA)\n\n[Methodology Anywhere README](https://money.usnews.com/money/Investment/articles/Investment-accounts-you-should-consider)\n\n[Preparing for Investment Guide](https://www.thebalance.com/prepare-for-Investment-success-2894361)');
          }else if (message.text == 'Contact Us'){
            await bot.reply(message,'Contact Us Here !!!');
          }else if (message.text == 'Fees Analyzer Tool'){
            await bot.reply(message, 'Here is a fees analyzer tool for you to use!\n\n[Fees analyzer Tool](https://www.feex.com/en/solutions?section=Fee_analyzer)');
          }else if (message.text == 'Investment Manager FAQ Links'){
            await bot.reply(message, 'Here are our FAQs extensively documented! Following are some useful links:\n\n[Rockstar Investment Product ](https://www.Rockstar.com/products/Investment-manager)\n\n[Website Usage FAQ](https://www.shopify.com/blog/120928069-how-to-create-faq-page)\n\n[Preparing for Investment Guide](https://www.thebalance.com/prepare-for-Investment-success-2894361)');
          }else if (message.text == 'Sign Up Video'){
            await bot.reply(message,'Here is our Investment Website Sign Up Video\n\n[Rockstar Youtube video](https://www.youtube.com/embed/8sujx2Gl1xA)');
          }else if (message.text == 'Functionality Documentation'){
            await bot.reply( message,
                { text: 'For your questions regarding Usage of the website I can point you to the following resources, or connect you with experts who can help.',
                  quick_replies: [
                    { title: 'Investment Manager FAQ',
                      payload: 'Investment Manager FAQ Links',
                    },
                    {
                      title: 'Expert Help',
                      payload: 'Contact Us',
                    }
                  ]
                }
            )
          }else if (message.text == 'Join The Investment Community'){
            await bot.reply(message, 'Here is a fees analyzer tool for you to use!\n\n[Fees analyzer Tool](https://www.feex.com/en/solutions?section=Fee_analyzer)');
          }else 
          {
            const data = JSON.stringify({
              // Validation data coming from a form usually
              input: message.text
            });
            console.log(data);
            const response = await axios({
              url: 'https://lsekse7qt0.execute-api.us-east-1.amazonaws.com/api/',
              method: 'POST',
              headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
              },
              data: data,
            });
            console.log('Axios response:', response.data.prediction);
            const responseBody =  response.data.prediction;
            if (responseBody === 'Investment Advice') {
              await bot.reply(message, 'Here is our Investment Methodology extensively documented! Following are some useful links:\n\n[Rockstart Youtube video](https://www.youtube.com/embed/8sujx2Gl1xA)\n\n[Methodology Anywhere README](https://github.com/howdyai/botkit-starter-web/blob/master/readme.md#botkit-anywhere)\n\n[Preparing for Investment Guide](https://github.com/howdyai/botkit/blob/master/readme.md#build-your-bot)');
            } else if (responseBody === 'Fees') {
              await bot.reply(message, {
                text: 'For your questions regarding Fees I can point you to the following resources, or connect you with experts who can help.',
                quick_replies: [
                  {
                    title: 'Fee Analyzer tool',
                    payload: 'Fees Analyzer Tool',
                  },
                  {
                    title: 'Expert Help',
                    payload: 'Contact Us',
                  }
                ]
              });
            } else if (responseBody === 'Close their Account') {
              await bot.reply(message, {
                text: 'For help with Opting Out of Managed Accounts, I can point you to the following respources, or connect you with experts who can help.',
                quick_replies: [
                  {
                    title: 'Contact Me Form For Opt Out',
                    payload: 'Fill in the Contact Me Form For Opt Out',
                  },
                  {
                    title: 'Advantages of staying enrolled in Managed Accounts',
                    payload: 'Show me the advantages of staying enrolled in managed accounts',
                  },
                  {
                    title: 'Expert Help',
                    payload: 'Contact Us',
                  }
                ]
              });
            } else if (responseBody === 'Functionality') {
              await bot.reply(message, {
                text: 'For your questions regarding Functionality I can point you to the following resources, and connect you with experts who can help.',
                quick_replies: [
                  {
                    title: 'Read the Docs',
                    payload: 'Functionality Documentation',
                  },
                  {
                    title: 'Join our Investment Community',
                    payload: 'Join The Investment Community',
                  },
                  {
                    title: 'Expert Help',
                    payload: 'Contact Us',
                  }
                ]
              });
            } else if (responseBody === 'Sign-Up') {
              await bot.reply(message, {
                text: 'For your questions regarding Sign-Up I can point you to the following resources, and connect you with experts who can help.',
                quick_replies: [
                  {
                    title: 'How to sign Up',
                    payload: 'Sign Up Video',
                  },
                  {
                    title: 'Expert Help',
                    payload: 'Contact Us',
                  }
                ]
              });
            } else {
              await bot.reply(message, {
                text: 'I do not know how to respond to that message yet.  Define new features by adding skills in my `features` folder.\n\n',
                quick_replies: [
                    {
                      title: 'Help',
                      payload: 'Help',
                    }
                  ]
                });
            }
        }


    })

}
