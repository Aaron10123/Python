class Player:
    def __init__(self, name, health, attack, defense):
        """初始化玩家, name: 名稱, health: 血量, attack: 攻擊, defense: 防禦"""
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        """受到傷害"""
        if damage>self.defense:
            self.health -= damage - self.defense
        return f"{self.name} 受到了 {damage}點傷害!"
    
class Mage(Player):
    def __init__(self, name, health, attack, defense, magic_power):
        """初始化法師, name: 名稱, health: 血量, attack: 攻擊, defense: 防禦, magic_power: 魔力 """
        super().__init__(name, health, attack, defense)
        self.magic_power = magic_power

    def cast_spell(self):
        """施放魔法"""
        self.magic_power -= 10
        return self.attack + self.magic_power
    
class Warrior(Player):
    def __init__(self, name, health, attack, defense, armor):
        """初始化戰士, name: 名稱, health: 血量, attack: 攻擊, defense: 防禦, armor: 護甲 """
        super().__init__(name, health, attack, defense)
        self.armor = armor

    def use_armor(self):
        """裝甲回復"""
        self.health += self.armor
        
# player1 = Player("666", 100, 2, 9)
# print(f"玩家名稱: {player1.name}")
# print(f"玩家血量: {player1.health}")
# print(f"玩家攻擊: {player1.attack}")
# print(f"玩家防禦: {player1.defense}")

# player2 = Player("007", 50, 10, 5)
# print(f"玩家名稱: {player2.name}")
# print(f"玩家血量: {player2.health}")
# print(f"玩家攻擊: {player2.attack}")
# print(f"玩家防禦: {player2.defense}")

# print(player2.take_damage(player1.attack))
# print(f"玩家2血量剩餘: {player2.health}")

player1 = Warrior("666", 100, 15, 10, 5)
player2 = Mage("007", 80, 10, 5, 20)


print(f"{player1.name}血量剩餘: {player1.health}")
player1.use_armor()
print(f"{player1.name}血量剩餘: {player1.health}")

print(f"{player2.name}血量剩餘: {player2.magic_power}")
player1.take_damage(player2.cast_spell())
print(f"{player2.name}對 {player1.name}釋放魔法攻擊!")
print(f"{player2.name}目前魔力: {player2.magic_power}")
print(f"{player1.name}血量剩餘: {player2.health}")
