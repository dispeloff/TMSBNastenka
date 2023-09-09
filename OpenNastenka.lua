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
  local _, _, Nickname, Message = event.pull(1, "chat_message", nil, "dispeloff") -- msg принимается только от меня
  if Message == nil then
  return

  elseif Message == "@help" then
    cb.say("§bСписок доступных команд: \n   §c1.§a help §6 - Список доступных команд \n   §c1.§a stop §6 - Остановка бота\n")
  return

  elseif Message == "@stop" then
    cb.say("§cМоя Остановочка")
    os.exit()
  end
end

-- main loop function
function MainLoop()
  while true do
    ReadChat()
  end
end

cb.say("§6Привет dispeloff!")
os.sleep(0.3)

MainLoop()




--test