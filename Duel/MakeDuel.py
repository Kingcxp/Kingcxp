from random import randint, choice
from .DuelRank import rank_list

legendarySkillsList = 		["恶臭攻击",
							 "哼！讨厌啦！",
							 "莫挨老子",
							 "鸡你太美",
							 "噫！唔！"]
							 
passiveSkillsList = 		["Homo特有的无处不在",
							 "闪避！闪避！闪避！",
							 "看我身法！",
							 "吃得好！",
							 "荆棘",
							 "再生",
							 "破甲"]
							 
rareSkillsList =			["旋风斩",
							 "猪突猛进",
							 "跃浪击",
							 "芜湖！",
							 "雷霆万钧",
							 "天动万象"]
							 
recoverSkillsList = 		["调息",
							 "嗑药",
							 "旺旺碎冰冰"]
							 
specialSkillsList = 		["嘿嘿嘿哈！",
							 "尖啸",
							 "仪式",
							 "你中有我，我中有你"]
							 
strikeBackSkillsList = 		["反击",
							 "你真是逊啦~",
							 "滚！",
							 "忽略！"]
							 
badSkillsList = 			["笨拙冲锋",
							 "你过来啊！",
							 "你干嘛~嗨嗨诶哟"]

def randSkills():
	finalSkillsList = []
	legendaryNum = randint(0, 1)
	passiveNum = randint(0, 2)
	rareNum = randint(0, 2)
	recoverNum = randint(0, 1)
	specialNum = randint(0, 1)
	strikebackNum = randint(0, 1)
	badNum = randint(0, 1)
	
	for i in range(0, legendaryNum):
		skill = choice(legendarySkillsList)
		while skill in finalSkillsList:
			skill = choice(legendarySkillsList)
		finalSkillsList.append(skill)
	
	for i in range(0, passiveNum):
		skill = choice(passiveSkillsList)
		while skill in finalSkillsList:
			skill = choice(passiveSkillsList)
		finalSkillsList.append(skill)
		
	for i in range(0, rareNum):
		skill = choice(rareSkillsList)
		while skill in finalSkillsList:
			skill = choice(rareSkillsList)
		finalSkillsList.append(skill)
	
	for i in range(0, recoverNum):
		skill = choice(recoverSkillsList)
		while skill in finalSkillsList:
			skill = choice(recoverSkillsList)
		finalSkillsList.append(skill)
	
	for i in range(0, specialNum):
		skill = choice(specialSkillsList)
		while skill in finalSkillsList:
			skill = choice(specialSkillsList)
		finalSkillsList.append(skill)
		
	for i in range(0, strikebackNum):
		skill = choice(strikeBackSkillsList)
		while skill in finalSkillsList:
			skill = choice(strikeBackSkillsList)
		finalSkillsList.append(skill)
	
	for i in range(0, badNum):
		skill = choice(badSkillsList)
		while skill in finalSkillsList:
			skill = choice(badSkillsList)
		finalSkillsList.append(skill)
	
	return finalSkillsList

def randStatus():
	atk = randint(150, 200)
	defense = randint(30, 100)
	health = randint(3000, 5000)
	chance = randint(0, 5)
	return [atk, defense, health, chance]
		
def getSkillsList():
	return [("传奇寄能池：", legendarySkillsList, "发动概率为 1%"),
			("被动寄能池：", passiveSkillsList, "发动概率为 100%"),
			("稀有寄能池：", rareSkillsList, "发动概率为 20%，每种寄能分开计算，一回合最多一次寄能"),
			("回复寄能池：", recoverSkillsList, "发动概率为 5%"),
			("特殊寄能池：", specialSkillsList, "发动概率 1%"),
			("反击寄能池：", strikeBackSkillsList, "发动概率 5%"),
			("作死寄能池：", badSkillsList, "发动概率 10%，与稀有寄能冲突，每回合只能一种")]

def passiveSkillEffect(challenger, defender, challengerSkills, challengerStatus, defenderStatus):
	result = []
	
	if "Homo特有的无处不在" in challengerSkills:
		result.append(challenger + " 触发被动寄能：Homo特有的无处不在，每回合行动次数+1")
	if "真正的欧皇" in challengerSkills:
		result.append(challenger + " 触发被动寄能：真正的欧皇，闪避率+80%")
		challengerStatus[3] = challengerStatus[3] + 80
	if "闪避！闪避！闪避！" in challengerSkills:
		result.append(challenger + " 触发被动寄能：闪避！闪避！闪避！前三回合闪避所有攻击")
	if "看我身法！" in challengerSkills:
		result.append(challenger + " 触发被动寄能：看我身法！闪避率+20%")
		challengerStatus[3] = challengerStatus[3] + 20
	if "吃得好！" in challengerSkills:
		result.append(challenger + " 触发被动寄能：吃得好！各项属性提升20%")
		for stat in challengerStatus:
			stat = int(stat * 1.2)
	if "荆棘" in challengerSkills:
		result.append(challenger + " 触发被动寄能：荆棘，反弹受到伤害的20%，反弹伤害无视防御")
	if "再生" in challengerSkills:
		result.append(challenger + " 触发被动寄能：再生，受到伤害时回复10点生命值")
	if "破甲" in challengerSkills:
		result.append(challenger + " 触发被动寄能：破甲，攻击伤害无视防御")
	return result

def showStatus(challenger, challengerStatus, challengerSkills):
	tmp = challenger
	tmp = tmp + "\n" + "血量:    %d"%challengerStatus[2]
	tmp = tmp + "\n" + "攻击力:  %d"%challengerStatus[0]
	tmp = tmp + "\n" + "防御力:  %d"%challengerStatus[1]
	tmp = tmp + "\n" + "闪避率:  %d percent"%challengerStatus[3]
	tmp = tmp + "\n" + "掌握技能："
	for skill in challengerSkills:
		tmp = tmp + "\n\t" + skill
	return tmp

def damage(round, challenger, challengerStatus, challengerSkills, defender, defenderStatus, defenderSkills, dmg, withoutDefense = False):
	if not withoutDefense:
		dmg = dmg - defenderStatus[1]
	if ("闪避！闪避！闪避！" in defenderSkills and round <= 3) or randint(0, 99) < defenderStatus[3]:
		return "闪避！" + defender + " 躲过了这次攻击。"
	defenderStatus[2] -= dmg
	tmp = defender + "受到了%d点伤害！"%dmg
	if "荆棘" in defenderSkills:
		challengerStatus[2] -= int(dmg * 0.2)
		tmp = tmp + "\n" + challenger + " 受到了%d点反弹伤害。"%int(dmg * 0.2)
	if "再生" in defenderSkills:
		defenderStatus[2] += 10
		tmp = tmp + "\n" + defender + " 触发被动寄能：再生，恢复了10点生命值。"
	return tmp

def skillsEffect(round, challenger, challengerStatus, challengerSkills, defender, defenderStatus, defenderSkills, skill):
	tmp = str()
	if skill in legendarySkillsList:
		tmp = tmp + challenger + " 发动寄能：" + skill + "\n" + damage(round, challenger, challengerStatus, challengerSkills, defender, defenderStatus, defenderSkills, 114514, True)
	if skill in rareSkillsList:
		if skill == "旋风斩":
			for i in range(0, randint(2, 5)):
				if i > 0:
					tmp = tmp + '\n'
				tmp = tmp + challenger + " 发动寄能：旋风斩" + "\n" + damage(round, challenger, challengerStatus, challengerSkills, defender, defenderStatus, defenderSkills, challengerStatus[0], "破甲" in challengerSkills)
		if skill == "猪突猛进":
			tmp = tmp + challenger + " 发动寄能：猪突猛进" + "\n" + damage(round, challenger, challengerStatus, challengerSkills, defender, defenderStatus, defenderSkills, challengerStatus[0] * 2, "破甲" in challengerSkills)
		if skill == "跃浪击":
			tmp = tmp + challenger + " 发动寄能：跃浪击" + "\n" + damage(round, challenger, challengerStatus, challengerSkills, defender, defenderStatus, defenderSkills, challengerStatus[0] * 3, "破甲" in challengerSkills)
		if skill == "芜湖！":
			tmp = tmp + challenger + " 发动寄能：芜湖！" + "\n" + damage(round, challenger, challengerStatus, challengerSkills, defender, defenderStatus, defenderSkills, challengerStatus[0] * 3, "破甲" in challengerSkills)
		if skill == "雷霆万钧":
			tmp = tmp + challenger + " 发动寄能：雷霆万钧" + "\n" + damage(round, challenger, challengerStatus, challengerSkills, defender, defenderStatus, defenderSkills, challengerStatus[0] * 5, "破甲" in challengerSkills)
		if skill == "天动万象":
			tmp = tmp + challenger + " 发动寄能：天动万象" + "\n" + damage(round, challenger, challengerStatus, challengerSkills, defender, defenderStatus, defenderSkills, challengerStatus[0] * 5, "破甲" in challengerSkills)
	if skill in badSkillsList:
		if skill == "笨拙冲锋":
			tmp = tmp + challenger + " 发动寄能：笨拙冲锋" + "\n" + damage(round, challenger, challengerStatus, challengerSkills, defender, defenderStatus, defenderSkills, challengerStatus[0] * 2, "破甲" in challengerSkills)
			challengerStatus[2] -= 200
			tmp = tmp + challenger + " 因为太蠢，自己受到了200点伤害！"
		if skill == "你过来啊！":
			defenderStatus[0] += 20
			tmp = tmp + challenger + " 发动寄能：你过来啊！" + "\n" + defender + " 觉得受到了鄙视，非常愤怒！" + "\n" + defender + " 的攻击力上升了20！"
		if skill == "你干嘛~嗨嗨诶哟":
			defenderStatus[1] += 20
			tmp = tmp + challenger + "发动寄能：你干嘛~嗨嗨诶哟" + "\n" + defender + "发现" + challenger + "竟然是小黑子！变得更加小心了" + "\n" + defender + "的防御力上升了20！"
	return tmp

def attack(round, challenger, challengerStatus, challengerSkills, defender, defenderStatus, defenderSkills):
	tmp = str()
	skill_used = False
	for skill in challengerSkills:
		if skill in badSkillsList:
			chance = randint(0, 99)
			if chance < 10:
				skill_used = True
				tmp = tmp + "\n\n" + skillsEffect(round, challenger, challengerStatus, challengerSkills, defender, defenderStatus, defenderSkills, skill)
				break
		if skill in rareSkillsList:
			chance = randint(0, 99)
			if chance < 20:
				skill_used = True
				tmp = tmp + "\n\n" + skillsEffect(round, challenger, challengerStatus, challengerSkills, defender, defenderStatus, defenderSkills, skill)
				break
		if skill in legendarySkillsList:
			chance = randint(0, 99)
			if chance < 1:
				skill_used = True
				tmp = tmp + "\n\n" + skillsEffect(round, challenger, challengerStatus, challengerSkills, defender, defenderStatus, defenderSkills, skill)
				break
	if not skill_used:
		tmp = tmp + "\n\n" + challenger + " 发动普通攻击！\n" + damage(round, challenger, challengerStatus, challengerSkills, defender, defenderStatus, defenderSkills, challengerStatus[0], "破甲" in challengerSkills)
	return tmp
				
def fight_back(round, challenger, challengerStatus, challengerSkills, defender, defenderStatus, defenderSkills):
	tmp = str()
	chance = randint(0, 99)
	if chance > 5:
		return tmp
	if "反击" in challengerSkills:
		tmp = tmp + "\n" + challenger + " 发动寄能：反击" + "\n" + damage(round, challenger, challengerStatus, challengerSkills, defender, defenderStatus, defenderSkills, challengerStatus[0], "破甲" in challengerSkills)
	if "你真是逊啦~" in challengerSkills:
		defenderStatus[0] -= 20
		tmp = tmp + "\n" + challenger + " 发动寄能：你真是逊啦~" + "\n" + defender + "受到了嘲讽！攻击力下降50"
	if "滚！" in challengerSkills:
		tmp = tmp + "\n" + challenger + " 发动寄能：滚！" + "\n" + damage(round, challenger, challengerStatus, challengerSkills, defender, defenderStatus, defenderSkills, challengerStatus[0] * 2, "破甲" in challengerSkills)
	if "忽略！" in challengerSkills:
		challengerStatus[1] += 20
		tmp = tmp + "\n" + challenger + " 发动寄能：忽略！" + "\n" + challenger + "因为这次攻击更加警觉了，防御力上升50"
	return tmp

def recover(round, challenger, challengerSkills, challengerStatus):
	tmp = str()
	chance = randint(0, 99)
	if chance > 5:
		return tmp
	if "调息" in challengerSkills:
		challengerStatus[2] += 100
		tmp = tmp + "\n" + challenger + " 发动寄能：调息\n嗯，好多了，生命值恢复了100点。"
	if "嗑药" in challengerSkills:
		challengerStatus[2] += 200
		tmp = tmp + "\n" + challenger + " 发动寄能：嗑药\n精神百倍！生命值恢复了200点。"
	if "旺旺碎冰冰" in challengerSkills:
		challengerStatus[2] += 500
		tmp + tmp + "\n" + challenger + " 发动寄能：旺旺碎冰冰\n哇！冰凉清爽，你家有吗？生命值恢复了500点。"
	return tmp

def special(round, challenger, challengerSkills, challengerStatus, defender, defenderSkills, defenderStatus):
	tmp = str()
	chance = randint(0, 99)
	if chance > 0:
		return tmp
	if "嘿嘿嘿哈！" in challengerSkills:
		defenderStatus[1] -= 50
		tmp = tmp + "\n" + challenger + " 发动寄能：嘿嘿嘿哈！\n" + defender + " 受到了嘲笑！防御力下降50点。"
	if "尖啸" in challengerSkills:
		defenderStatus[0] -= 20
		tmp = tmp + "\n" + challenger + " 发动寄能：尖啸\n多么刺耳！" + defender + " 攻击力下降了20点。"
	if "仪式" in challengerSkills:
		challengerStatus[0] += 20
		tmp = tmp + "\n" + challenger + " 发动寄能：仪式\n咔咔！" + challenger + " 进行了一种神秘的仪式，攻击力提升了20点。"
	if "你中有我，我中有你" in challengerSkills:
		t = challengerStatus[2]
		challengerStatus[2] = defenderStatus[2]
		defenderStatus[2] = t
		tmp = tmp + "\n" + challenger + " 发动寄能：你中有我，我中有你\n" + challenger + " 和" + defender + " 的血量交换了！"
	return tmp

def getResult(group_id, challenger, challengerStatus, defender, defenderStatus):
	if defenderStatus[2] <= 0:
		try:
			rank_list[group_id][challenger] += 1
		except:
			try:
				rank_list[group_id][challenger] = int(1)
			except:
				rank_list[group_id] = {}
				rank_list[group_id][challenger] = int(1)
		return defender + "输了！\n" + challenger + " 赢得了比赛。"
	if challengerStatus[2] <= 0:
		try:
			rank_list[group_id][defender] += 1
		except:
			try:
				rank_list[group_id][defender] = int(1)
			except:
				rank_list[group_id] = {}
				rank_list[group_id][defender] = int(1)
		return challenger + "输了！\n" + defender + " 赢得了比赛。"
	return "平局！此次成绩不计入排名。"

def duel(challenger, defender, group_id):
	result = []

	challengerStatus = randStatus()
	defenderStatus = randStatus()
	challengerSkills = randSkills()
	defenderSkills = randSkills()
	
	result = result + passiveSkillEffect(challenger, defender, challengerSkills, challengerStatus, defenderStatus)
	result = result + passiveSkillEffect(defender, challenger, defenderSkills, defenderStatus, challengerStatus)

	result.append(showStatus(challenger, challengerStatus, challengerSkills))
	result.append(showStatus(defender, defenderStatus, defenderSkills))

	round = 0
	
	while challengerStatus[2] > 0 and defenderStatus[2] > 0:
		round += 1
		tmp = "第%02d / 30回合"%round
		if round > 30:
			break
		tmp = tmp + attack(round, challenger, challengerStatus, challengerSkills, defender, defenderStatus, defenderSkills)
		if "Homo特有的无处不在" in challengerSkills:
			tmp = tmp + attack(round, challenger, challengerStatus, challengerSkills, defender, defenderStatus, defenderSkills)
		tmp = tmp + fight_back(round, defender, defenderStatus, defenderSkills, challenger, challengerStatus, challengerSkills)
		tmp = tmp + recover(round, challenger, challengerSkills, challengerStatus)
		tmp = tmp + special(round, challenger, challengerSkills, challengerStatus, defender, defenderSkills, defenderStatus)
		if defenderStatus[2] <= 0 or challengerStatus[2] <= 0:
			tmp = tmp + "\n\n" + challenger + " 剩余血量: %d"%challengerStatus[2] + "\n" + defender + " 剩余血量: %d"%defenderStatus[2]
			result.append(tmp)
			break
		tmp = tmp + attack(round, defender, defenderStatus, defenderSkills, challenger, challengerStatus, challengerSkills)
		if "Homo特有的无处不在" in defenderSkills:
			tmp = tmp + attack(round, defender, defenderStatus, defenderSkills, challenger, challengerStatus, challengerSkills)
		tmp = tmp + fight_back(round, challenger, challengerStatus, challengerSkills, defender, defenderStatus, defenderSkills)
		tmp = tmp + recover(round, defender, defenderSkills, defenderStatus)
		tmp = tmp + special(round, challenger, challengerSkills, challengerStatus, defender, defenderSkills, defenderStatus)
		tmp = tmp + "\n\n" + challenger + " 剩余血量: %d"%challengerStatus[2] + "\n" + defender + " 剩余血量: %d"%defenderStatus[2]
		result.append(tmp)
	result.append(getResult(group_id, challenger, challengerStatus, defender, defenderStatus))
	return result