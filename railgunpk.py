# -*- coding: UTF-8 -*- 
import random 

class Skill(): 
    def __init__(self, name, power, cd, mzl): 
        self.name = name 
        self.power = power 
        self.cd = cd 
        self.MAXcd = cd 
        self.mzl = mzl 
    def checkCD(self): 
        if self.cd > 0: 
            self.cd -= 1
  
  
class renwu(): 
    def __init__(self, name, skills, hp): 
        self.name = name 
        self.skills = skills 
        self.hp = hp 
  
    def attack(self,target): 
        use_skills = [] 
        for skill in self.skills: 
            skill.checkCD() 
            if skill.cd == 0: 
                use_skills.append(skill) 
                break
  
        if use_skills: 
            if random.randint(1,100) < use_skills[0].mzl: 
                target.hp -= use_skills[0].power 
                use_skills[0].cd = use_skills[0].MAXcd 
                print u"%s使用%s技能攻击%s，造成%d点伤害, %s还有%d点血量" %(self.name, use_skills[0].name, target.name, use_skills[0].power, target.name, target.hp) 
            else: 
                print u"%s使用%s技能攻击%s，但是没有打中！"%(self.name, use_skills[0].name, target.name)
  
  
class pk(): 
    def __init__(self, renwu1,renwu2): 
        self.renwu1 = renwu1 
        self.renwu2 = renwu2 
  
    def start(self): 
        pking = True
        while pking: 
            self.renwu1.attack(renwu2) 
            pking = self.pknotend() 
            self.renwu2.attack(renwu1) 
            pking = self.pknotend() 
        self.winner() 
  
    def pknotend(self): 
        if self.renwu1.hp <= 0 or self.renwu2.hp <= 0: 
            return False
        else: 
            return True
  
    def winner(self): 
        if self.renwu1.hp > self.renwu2.hp: 
            print u"%s 获胜" %self.renwu1.name 
        else: 
            print u"%s 获胜" %self.renwu2.name 
  
  
  
if __name__== "__main__": 
    skill1 = Skill(u"超电磁炮",100,3,55)
    skill2 = Skill(u"电击",15,1,80) 
    renwu1 = renwu(u"炮姐",[skill1,skill2],100) 
    skill3 = Skill(u"原子崩坏",70,3,65) 
    skill4 = Skill(u"闪耀",10,1,80) 
    renwu2 = renwu(u"麦姐",[skill3,skill4],85) 
    liapk = pk(renwu1,renwu2) 
    liapk.start()
    