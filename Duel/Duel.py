from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me, command
from .config import Config
import json
from typing import List
from nonebot.adapters.onebot.v11 import MessageEvent, GroupMessageEvent
from .DuelRank import *
from .MakeDuel import *

def get_message_at(data: str) -> list:
    qq_list = []
    data = json.loads(data)
    try:
        for msg in data['message']:
            if msg['type'] == 'at':
                qq_list.append(int(msg['data']['qq']))
        return qq_list
    except Exception:
        return []

async def send_forward_msg(bot: Bot, event: MessageEvent, name: str, uin: str, msgs: List[str]):
    def to_json(msg):
        return {"type": "node", "data": {"name": name, "uin": uin, "content": msg}}

    messages = [to_json(msg) for msg in msgs]
    if isinstance(event, GroupMessageEvent):
        await bot.call_api("send_group_forward_msg", group_id=event.group_id, messages=messages)
    else:
        await bot.call_api("send_private_forward_msg", user_id=event.user_id, messages=messages)

make_duel = on_keyword("发起决斗", rule = to_me() & command("发起决斗"), priority = Config.priority)
getList = on_keyword("查看排名", rule = to_me() & command("查看排名"), priority = Config.priority)
getpool = on_keyword("查看寄能池", rule = to_me() & command("查看寄能池"), priority = Config.priority)

@make_duel.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    ids = event.get_session_id()
    if ids.startswith("group"):
        _, group_id, user_id = event.get_session_id().split('_')
        _at = get_message_at(event.json())
        if group_id in Config.used_in_group and user_id != Config.bot_id and _at:
            _at = _at[0]
            if str(user_id) == str(_at):
                await make_duel.finish("你怎么能和自己决斗捏？(～￣▽￣)～")
            try:
                infos = str(await bot.call_api("get_stranger_info", user_id = user_id)).replace("\'", "\"")
                name_challenger = json.loads(infos)["nickname"]
                infos = str(await bot.call_api("get_stranger_info", user_id = _at)).replace("\'", "\"")
                name_defender = json.loads(infos)["nickname"]
                await send_forward_msg(bot, event, "决斗系统", bot.self_id, duel(name_challenger, name_defender, group_id))
            except:
                await make_duel.finish("决斗启动失败！")

@getList.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    ids = event.get_session_id()
    if ids.startswith("group"):
        _, group_id, user_id = event.get_session_id().split('_')
        if group_id in Config.used_in_group and user_id != Config.bot_id:
            await getList.finish(getRank(group_id))

@getpool.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    ids = event.get_session_id()
    if ids.startswith("group"):
        _, group_id, user_id = event.get_session_id().split('_')
        if group_id in Config.used_in_group and user_id != Config.bot_id:
            list = getSkillsList()
            tmp = str()
            for item in list:
                tmp = tmp + item[0]
                for skill in item[1]:
                    tmp = tmp + "\n\t" + skill
                tmp = tmp + "\n\t" + item[2] + "\n\n"
            await send_forward_msg(bot, event, "决斗系统", bot.self_id, ["当前的寄能池如下：", tmp])

turn_off = on_keyword("关闭决斗功能", rule = to_me() & command("关闭决斗功能"), priority = Config.priority - 2)
@turn_off.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    ids = event.get_session_id()
    if ids.startswith("group"):
        _, group_id, user_id = event.get_session_id().split('_')
        if user_id != Config.bot_id:
            if user_id in Config.super_uid:
                Config.used_in_group.remove(group_id)
                await turn_off.finish("决斗功能已关闭！")
            else:
                await turn_off.finish("对不起，你没有权限做这件事！")

turn_on = on_keyword("打开决斗功能", rule = to_me() & command("打开决斗功能"), priority = Config.priority - 2)
@turn_on.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    ids = event.get_session_id()
    if ids.startswith("group"):
        _, group_id, user_id = event.get_session_id().split('_')
        if user_id != Config.bot_id:
            if user_id in Config.super_uid:
                Config.used_in_group.append(group_id)
                await turn_on.finish("决斗功能已打开！")
            else:
                await turn_on.finish("对不起，你没有权限做这件事！")