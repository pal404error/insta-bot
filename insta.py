from instabot import Bot
import os 
import glob
cookie_del = glob.glob("config/*cookie.json")

os.system("rm -rf config")

bot = Bot()

bot.login(username = "#",
		password = "#")
bot.upload_photo("./img/quote1.jpg",
				caption ="Enjoy, Inspire and motivate \n @citinghub\n \n #quotes are #quotation #quotess #quites #quotestagram #quoteslife #dailyquotes #quoted #quotestoliveby #quoteoftheday #quote")

bot.upload_photo("./img/quote2.jpg",
				caption ="Enjoy, Inspire and motivate \n @citinghub\n \n #quotes are #quotation #quotess #quites #quotestagram #quoteslife #dailyquotes #quoted #quotestoliveby #quoteoftheday #quote")

bot.upload_photo("./img/quote3.jpg",
				caption ="Enjoy, Inspire and motivate \n @citinghub\n \n #quotes are #quotation #quotess #quites #quotestagram #quoteslife #dailyquotes #quoted #quotestoliveby #quoteoftheday #quote")

bot.upload_photo("./img/quote4.jpg",
				caption ="Enjoy, Inspire and motivate \n @citinghub\n \n #quotes are #quotation #quotess #quites #quotestagram #quoteslife #dailyquotes #quoted #quotestoliveby #quoteoftheday #quote")

bot.upload_photo("./img/quote5.jpg",
				caption ="Enjoy, Inspire and motivate \n @citinghub\n \n #quotes are #quotation #quotess #quites #quotestagram #quoteslife #dailyquotes #quoted #quotestoliveby #quoteoftheday #quote")

bot.upload_photo("./img/quote6.jpg",
				caption ="Enjoy, Inspire and motivate \n @citinghub\n \n #quotes are #quotation #quotess #quites #quotestagram #quoteslife #dailyquotes #quoted #quotestoliveby #quoteoftheday #quote")

bot.upload_photo("./img/quote7.jpg",
				caption ="Enjoy, Inspire and motivate \n @citinghub\n \n #quotes are #quotation #quotess #quites #quotestagram #quoteslife #dailyquotes #quoted #quotestoliveby #quoteoftheday #quote")

bot.upload_photo("./img/quote8.jpg",
				caption ="Enjoy, Inspire and motivate \n @citinghub\n \n #quotes are #quotation #quotess #quites #quotestagram #quoteslife #dailyquotes #quoted #quotestoliveby #quoteoftheday #quote")

bot.upload_photo("./img/quote9.jpg",
				caption ="Enjoy, Inspire and motivate \n @citinghub\n \n #quotes are #quotation #quotess #quites #quotestagram #quoteslife #dailyquotes #quoted #quotestoliveby #quoteoftheday #quote")

bot.upload_photo("./img/quote10.jpg",
				caption ="Enjoy, Inspire and motivate \n @citinghub\n \n #quotes are #quotation #quotess #quites #quotestagram #quoteslife #dailyquotes #quoted #quotestoliveby #quoteoftheday #quote")

