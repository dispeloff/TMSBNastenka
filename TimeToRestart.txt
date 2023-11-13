

--[[

  --=component.chat_box.setName("В§4 В§oBOTВ§7 В§o] В§8[ В§6* * *   В§bINFAMOUS   В§6* * * ")
  --=component.chat_box.say(": РњРµРЅСЋ\nВ§6РЎРїРёСЃРѕРє РґРѕСЃС‚СѓРїРЅС‹С… СЂР°Р·РґРµР»РѕРІ: \n   В§c1.В§b Industrial Craft 2 \n   В§c2.В§d Thermal Expansion \n   В§c3.В§b EnderIO ")
  --=component.chat_box.say(": РњРµРЅСЋ -> РўРµР»РµРїРѕСЂС‚Р°С†РёСЏ РІ СЂР°Р·РґРµР»\n\n                  В§aРЎРїРёСЃРѕРє РґРѕСЃС‚СѓРїРЅС‹С… СЂР°Р·РґРµР»РѕРІ\n\n                        В§a1.   В§6 Industrial Craft 2 \n                        В§a2.   В§2 Thermal Expansion \n                        В§a3.   В§3 EnderIO \n\nВ§d В§nР§С‚РѕР±С‹ С‚РµР»РµРїРѕСЂС‚РёСЂРѕРІР°С‚СЊСЃСЏ РІРІРµРґРёС‚Рµ С†РёС„СЂСѓ РІ С‡Р°С‚!\n")

=component.chat_box.say(": РњРµРЅСЋ -> РўРµР»РµРїРѕСЂС‚Р°С†РёСЏ РІ СЂР°Р·РґРµР»\n\n                  В§aРЎРїРёСЃРѕРє РґРѕСЃС‚СѓРїРЅС‹С… СЂР°Р·РґРµР»РѕРІ\n\n                        В§a1   В§6 Industrial Craft 2\n                        В§a2   В§6 Thermal Expansion\n                        В§a3   В§6 Ender IO\n\nВ§d В§nР§С‚РѕР±С‹ С‚РµР»РµРїРѕСЂС‚РёСЂРѕРІР°С‚СЊСЃСЏ РІРІРµРґРёС‚Рµ С†РёС„СЂСѓ РІ С‡Р°С‚!\n")
=component.redstone.setOutput(1,15)
=component.redstone.setOutput(1,0)

=component.redstone.setOutput(2,15)
=component.redstone.setOutput(2,0)

--РўРµР»РµРїРѕСЂС‚ РЅР° СЃРїР°РІРЅ (Рё РЅРёР¶РЅРёР№) (Р±РµР»Р°СЏ РіР»РёРЅР°)
=component.redstone.setOutput(3,15)
=component.redstone.setOutput(3,0)

=component.redstone.setOutput(4,15)
=component.redstone.setOutput(4,0)

=component.redstone.setOutput(5,15)
=component.redstone.setOutput(5,0)

=component.redstone.setOutput(6,15)
=component.redstone.setOutput(6,0)



       .
С„РёРЅР°Р» / \
       |
       |


=component.chat_box.say(": РњРµРЅСЋ -> РўРµР»РµРїРѕСЂС‚Р°С†РёСЏ РІ СЂР°Р·РґРµР»\n\n                  В§aРЎРїРёСЃРѕРє РґРѕСЃС‚СѓРїРЅС‹С… СЂР°Р·РґРµР»РѕРІ\n\n             В§dвЋ№     В§a1.   В§6 Industrial Craft 2     В§dвЋ№ \n             В§dвЋ№     В§a2.   В§2 Thermal Expansion     В§dвЋ№ \n             В§dвЋ№     В§a3.   В§3 EnderIO     В§dвЋ№ \n\nВ§d В§nР§С‚РѕР±С‹ С‚РµР»РµРїРѕСЂС‚РёСЂРѕРІР°С‚СЊСЃСЏ РІРІРµРґРёС‚Рµ С†РёС„СЂСѓ РІ С‡Р°С‚!\n")


--]]


local com = require("component")
local computer = require("computer")
local term = require("term")
local event = require("event")
local fs = require("filesystem")
local io = require("io")

local gpu = com.gpu
local cb = com.chat_box

function Menu_sections()
  cb.say(": РњРµРЅСЋ -> РўРµР»РµРїРѕСЂС‚Р°С†РёСЏ РІ СЂР°Р·РґРµР»\n\n                  В§aРЎРїРёСЃРѕРє РґРѕСЃС‚СѓРїРЅС‹С… СЂР°Р·РґРµР»РѕРІ\n\n                        В§a1   В§6 Industrial Craft 2\n                        В§a2   В§6 Thermal Expansion\n                        В§a3   В§6 Ender IO\n\nВ§d В§nР§С‚РѕР±С‹ С‚РµР»РµРїРѕСЂС‚РёСЂРѕРІР°С‚СЊСЃСЏ РІРІРµРґРёС‚Рµ С†РёС„СЂСѓ РІ С‡Р°С‚!\n")
end

function Menu()
  cb.say(": РњРµРЅСЋ \n\n                        В§a1   В§6 Р Р°Р·РґРµР»С‹ \n\nВ§d В§nР§С‚РѕР±С‹ РІС‹Р±СЂР°С‚СЊ РІРІРµРґРёС‚Рµ С†РёС„СЂСѓ РІ С‡Р°С‚!\n")
  function ReadAction()
    local _, _, Nickname, Message = event.pull(1, "chat_message", nil, "dispeloff") -- msg РїСЂРёРЅРёРјР°РµС‚СЃСЏ С‚РѕР»СЊРєРѕ РѕС‚ РјРµРЅСЏ
    if Message == nil then
    return Message

    elseif Message == "1" then
      Menu_sections()
    return
  end
  ReadAction()
end
end

function Global_Shop()
  print("pizdec")
  --cb.say("Р”РѕР±СЂРѕ РїРѕР¶Р°Р»РѕРІР°С‚СЊ РЅР° /warp inf - dispeloff! \n ")
  Menu()
end

-- event "chat_message" - first start
function ReadChat()
  local _, _, Nickname, Message = event.pull(1, "chat_message", nil, "dispeloff") -- msg РїСЂРёРЅРёРјР°РµС‚СЃСЏ С‚РѕР»СЊРєРѕ РѕС‚ РјРµРЅСЏ
  if Message == nil then
  return Message

  elseif Message == "start" then
    cb.say("В§6Р—Р°РїСѓСЃРє СѓРјРЅРѕРіРѕ РІР°СЂРїР°...")
    Global_Shop()
  return

  elseif Message == "help" then
    cb.say("В§bРЎРїРёСЃРѕРє РґРѕСЃС‚СѓРїРЅС‹С… РєРѕРјР°РЅРґ: \n   В§a help В§6 - РЎРїРёСЃРѕРє РґРѕСЃС‚СѓРїРЅС‹С… РєРѕРјР°РЅРґ \n  В§a start В§6 - Р—Р°РїСѓСЃРє СѓРјРЅРѕРіРѕ РІР°СЂРїР° \n   В§a stop В§6 - РћСЃС‚Р°РЅРѕРІРєР° Р±РѕС‚Р°\n   В§a @dw В§6 - РћР±РЅРѕРІР»РµРЅРёРµ Р±Р°Р·С‹ РґР°РЅРЅС‹С… (GitHub update)")
  return

  elseif Message == "stop" then
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