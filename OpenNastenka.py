local com = require("component")
local computer = require("computer")
local term = require("term")
local event = require("event")
local fs = require("filesystem")
local io = require("io")

local gpu = com.gpu
local cb = com.chat_box

-- event "chat_message"
function ReadChat()
  local _, _, Nickname, Message = event.pull(1, "chat_message", nil, "dispeloff") -- msg РїСЂРёРЅРёРјР°РµС‚СЃСЏ С‚РѕР»СЊРєРѕ РѕС‚ РјРµРЅСЏ
  if Message == nil then
  return

  elseif Message == "@help" then
    cb.say("В§bРЎРїРёСЃРѕРє РґРѕСЃС‚СѓРїРЅС‹С… РєРѕРјР°РЅРґ: \n   В§c1.В§a help В§6 - РЎРїРёСЃРѕРє РґРѕСЃС‚СѓРїРЅС‹С… РєРѕРјР°РЅРґ \n   В§c1.В§a stop В§6 - РћСЃС‚Р°РЅРѕРІРєР° Р±РѕС‚Р°\n")
  return

  elseif Message == "@stop" then
    cb.say("В§cРњРѕСЏ РћСЃС‚Р°РЅРѕРІРѕС‡РєР°")
    os.exit()
  end
end

-- main loop function
function MainLoop()
  while true do
    ReadChat()
  end
end

cb.say("В§6РџСЂРёРІРµС‚ dispeloff!")
os.sleep(0.3)

MainLoop()




--test