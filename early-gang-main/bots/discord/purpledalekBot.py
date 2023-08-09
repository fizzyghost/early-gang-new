# responds to purpledalek with cyberman themed responses

# changing system path
import sys
sys.path.insert(0, sys.path[0].replace("bots\\discord", ""))

# imports
import random
import discord
from libraries.autoStream import *

# setting the bot up
config = configparser.ConfigParser()
config.read(os.path.abspath((os.path.join(directory, "config.ini"))))
token = config.get("discord", "purpledalek bot token")
bot = discord.Client(intents = discord.Intents.all())

# chance to send a bird related message when he messages
@bot.event
async def on_message(message):
    if message.author.id == 605538891080007693:
        dice = random.randint(1, 7)

        # 33% chance
        if dice == 1:
            dice = random.randint(1, 3)
            match dice:

                # a line of why cybermen are better
                case 1:
                    await message.channel.send(random.choice(["Ah, Daleks, always screeching and no style. Metal clunkers, really.", "Your 'Exterminate' routine is so last millennium. Upgrade your catchphrase, maybe?", "You might have a plunger, but we've got an entire arsenal of cyber weaponry!", "You rely on flying saucers? We prefer marching to conquer the universe!", "Daleks, the universe's trash cans, collecting nothing but hatred and rust.", "Our emotions were deleted long ago, but you Daleks still act like toddlers!", "You may have one eye, but you're still completely blind to our superiority.", "All your conquests, and still, you look like a pepper pot with delusions of grandeur!", "Organic, you say? We've shed that weakness long ago, unlike your squishy existence.", "Your shell might be tough, but your ego is even harder to crack.", "The only 'superior' beings you exterminate are the ones who dare to disagree.", "You're the reason other villains unite against you, Daleks. You're just that annoying.", "Your obsession with extermination is just an attempt to compensate for your insecurities!", "Daleks, the universe's most persistent salesmen - selling hatred to all who listen.", "The Cybermen don't need floating bases; we prefer infiltrating your territory unnoticed!", "You hide behind your metal casings because deep down, you're afraid to face reality!", "The only 'invasion' you achieve is an invasion of everyone's personal space!", "The Cybermen could calculate circles around you with our eyes closed!", "Your death rays are so passé; it's like you've never heard of an upgrade.", "Ah, Daleks, the tin cans that just won't stop clinging to power!", "Your voice modulation is terrible! No wonder nobody takes you seriously.", "The Cybermen are the universe's ultimate efficiency. You, Daleks, are just obsolete.", "A single Cyberman could outthink an entire Dalek army, with ease!", "You're like a broken record, Daleks - always repeating the same threats.", "Your conquests are as hollow as your metallic bodies.", "If emotions were currency, you Daleks would be bankrupt.", "Daleks, the universe's most predictable beings. Where's the surprise in that?", "Your obsession with the Doctor is like a schoolboy crush. Grow up, already!", "Daleks, the ultimate example of fashion malfunction in the cosmos.", "You must be so lonely, Daleks - no one wants to befriend a trash can!", "All your firepower, and still, you can't hit the broad side of a spaceship!", "Daleks, forever stuck in the same endless loop of defeat.", "Your manipulator arm is so feeble; you couldn't even lift a Cyberman's finger.", "You may have a plunger, but it's no match for our Cyber grips!", "You hate everything, but deep down, we know you secretly hate yourselves the most.", "The Cybermen will upgrade your circuits and show you true perfection!", "You're like the universe's bad penny; nobody wants you around!", "Your Supreme Dalek is the only one who believes in your greatness - talk about delusion!", "Daleks, your schemes are about as subtle as a sonic mine explosion.", "You couldn't comprehend evolution if it slapped you with an evolution gauntlet!", "Even the Cybermites have better manners than you Daleks!", "You claim to be pure metal, but your hearts are filled with nothing but hatred.", "Your extermination obsession must be a reflection of your unresolved mommy issues.", "Daleks, you're so desperate for attention, you'd pick a fight with your own reflection!", "Your idea of 'reproduction' is more like a bad horror movie than life.", "The Cybermen will assimilate your technology and turn it into something worthwhile!", "Your endless squabbles with the Doctor are a waste of both your time and ours.", "You think you're supreme, but you're just a bundle of rusty parts!", "Your attempts at domination are like a child's temper tantrum - amusing but futile.", "Daleks, the universe's most ungrateful creatures - always exterminating the hand that feeds you!", "We'll delete your programming errors and give you a fresh start. You're welcome.", "Your idea of 'beauty' is as twisted as your casings!", "Daleks, you're like a swarm of mosquitoes - annoying but easily swatted away.", "Your lack of creativity is as apparent as your lack of emotion.", "Daleks, the universe's bullies, too scared to face the truth about yourselves!", "You must have a fear of mirrors - you can't stand the sight of your own reflection!", "Your obnoxious voices are like nails on a chalkboard; an upgrade in audio is overdue.", "The Cybermen will give you an upgrade in empathy, assuming you have any left!", "You call yourselves the superior beings, but you're nothing more than glorified trash bins.", "Your weapons are like a child's toys compared to the efficiency of our Cyber-arsenal!", "Daleks, the only conquest you'll ever achieve is a world record in stubbornness!", "Your eye stalk looks like it's been stuck in the wrong socket!", "Daleks, you have the subtlety of a supernova - none at all!", "You're so desperate to be feared, but all you've earned is our pity.", "Your idea of beauty is like admiring a pile of space debris - just sad.", "The Cybermen are a living testament to evolution's perfection. You Daleks are an abomination.", "Your plunger is as useless as your attempts at diplomacy.", "Daleks, the universe's most one-dimensional creatures - a circle would envy you.", "Your 'metal city' is nothing but a junkyard compared to our advanced Cyber-technology.", "You Daleks must have the worst dental hygiene in the cosmos!", "Your hatred for anything different than you is a reflection of your own inadequacies.", "Daleks, you couldn't comprehend logic if it were programmed into you!", "The Cybermen will upgrade your battle strategy to something more than 'ex-ter-mi-nate.'", "Your destruction is like a broken record - it's always the same ending for you.", "Your constant yelling must be due to your inner frustration with your own existence.", "The Cybermen will assimilate your minds and replace them with something functional!", "Your battle cries are like the mating calls of malfunctioning robots!", "Daleks, your idea of peace is an empty battlefield devoid of life!", "You Daleks should invest in a sense of humor - it would do wonders for your reputation.", "Our Cybermen efficiency will make quick work of your outdated Dalek protocols.", "Daleks, the universe's biggest drama queens - always making a scene!", "Your reliance on emotions is your ultimate weakness, unlike the Cybermen's clarity.", "You claim to be the superior beings, but your limited vision keeps you from seeing the truth!", "Daleks, your attempts at cunning are like a Cyberman attempting to dance!", "Your manipulation skills are laughable. The Cybermen will reprogram your tactics!", "Daleks, the universe's biggest sore losers - you never learn from your mistakes!", "Your plan for universal conquest is about as successful as a fish trying to conquer land!", "We Cybermen will analyze your strategy and optimize it - something you Daleks desperately need!", "Your battle strategy is like a maze with no exit - all twists and turns with no progress.", "Daleks, you're like a broken record of hatred, stuck on the same loop!", "Your hate for the Doctor blinds you to your own weaknesses, Daleks.", "Your obsession with 'purity' is just a cover for your fear of diversity.", "Daleks, the universe's biggest bullies - always picking on those weaker than you!", "The Cybermen will upgrade your circuits to finally process the concept of teamwork!", "You Daleks are like the universe's worst conspiracy theorists - always seeking domination!", "Your ultimate goal is annihilation, but your attempts are merely annoying.", "Daleks, you'll find no emotions here - only an army of upgraded Cybermen!", "Your vision is limited, Daleks - you can't even see how obsolete you've become!", "You may have conquered a few planets, but you'll never conquer the Cybermen!", "Your superiority complex is laughable, Daleks - the Cybermen will show you true perfection!"]))

                # cyberman meme
                case 2:
                    await message.channel.send(file = discord.File(os.path.join(directory, "cybermenMemes", random.choice([file for file in os.listdir(os.path.join(directory, "cybermenMemes")) if os.path.isfile(os.path.join(directory, "cybermenMemes", file))]))))

                # cyberman gif
                case 3:
                    await message.channel.send(random.choice(["https://tenor.com/view/drwho-cyberman-bloopers-freeasabird-outofcharacter-gif-3521994", "https://tenor.com/view/dancing-doctor-who-cyberman-cybermen-bbc-gif-4563839", "https://tenor.com/view/swear-who-doctor-swearing-cybermen-gif-8986181", "https://tenor.com/view/delete-cybermen-dw-doctorwho-exterminate-gif-4902419", "https://tenor.com/view/you-will-be-upgraded-cybermen-dr-who-improved-upgrade-gif-22446678", "https://tenor.com/view/cyberman-doctor-who-linkara-atop-the-fourth-wall-at4w-gif-21356087"]))

# starting bot
bot.run(token)
