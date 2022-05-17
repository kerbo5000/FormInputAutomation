from bot.formInput import FormInput

with FormInput() as bot:
        bot.land_first_page()
        # bot.login('kerby','1234')
        bot.tabs('signup')
        bot.signup()
        bot.add_account()
