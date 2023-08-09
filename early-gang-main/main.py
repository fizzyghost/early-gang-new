# imports

import traceback
from libraries.charityDonoTTS import *
from libraries.chatPlays import *
from libraries.autoStream import *
from bots.twitch import commandBot

# main code loop
async def main():

    # setting up
    await connectToObs()
    await chatPlays.updateSnatus()

    # so you don't have to restart stream
    if await isLive(yourChannelName):
        await startTTS()
        await startChatPlays()
        await startAutoSave()
        await startInputBot()

    # infinite loop to check stream statuses
    #while True:

        # if streamer goes live
        #if await isLive(yourChannelName) and await isLive(streamerChannelName):

            # shut down everything
            #if ttsOn:
                #await stopTTS()
            #if chatPlaying:
                #await stopChatPlays()
            #if autoSaving:
                #await stopAutoSave()
            #if inputBotPlaying:
                #await stopInputBot()

            # end stream
            #if await isLive(yourChannelName):
                #await raid(yourChannelName, streamerChannelName)
                #await stopStream()

        # if streamer goes offline
        #elif not await isLive(yourChannelName) and not await isLive(streamerChannelName):

            # start stream
            #if not await isLive(yourChannelName):
                #await startStream()
            #if not ttsOn:
                #await startTTS()
            #if not chatPlaying:
                #await startChatPlays()
            #if not autoSaving:
                #await startAutoSave()
            #if not inputBotPlaying:
                #await stopInputBot()

        #await asyncio.sleep(3)

# running command bot for inputs
async def setup():
    await asyncio.gather(commandBot.Bot().start(), main())

# don't touch this
try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(setup())
    loop.run_forever()
except Exception as e:
    print(e)
    traceback.print_exc()