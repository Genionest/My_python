import pygame
import sys
import math
from typing import List, Tuple, Dict, Any

# 初始化 Pygame
pygame.init()

# 屏幕尺寸
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("卡牌游戏界面")

# 颜色定义
BACKGROUND = (50, 50, 70)
PLAYER_BG = (40, 40, 60, 180)
ANNOUNCEMENT_BG = (30, 30, 50)
CARD_SLOT = (70, 70, 100)
EQUIPMENT_SLOT = (90, 70, 120)
BUFF_SLOT = (80, 100, 130)
AVATAR_BORDER = (180, 160, 220)
TEXT_COLOR = (220, 220, 220)
HIGHLIGHT = (255, 215, 0)

# 字体
font_small = pygame.font.SysFont(None, 20)
font_medium = pygame.font.SysFont(None, 28)
font_large = pygame.font.SysFont(None, 36)

class Background:
    """背景板类"""
    def __init__(self):
        self.image = self.create_background()
        
    def create_background(self) -> pygame.Surface:
        """创建背景图像"""
        bg = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        bg.fill(BACKGROUND)
        
        # 添加装饰性图案
        for i in range(0, SCREEN_WIDTH, 40):
            for j in range(0, SCREEN_HEIGHT, 40):
                if (i // 40 + j // 40) % 2 == 0:
                    pygame.draw.rect(bg, (60, 60, 90), (i, j, 20, 20), 1)
        
        # 添加中心装饰
        center_x, center_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        pygame.draw.circle(bg, (80, 80, 110), (center_x, center_y), 150, 3)
        pygame.draw.circle(bg, (100, 100, 140), (center_x, center_y), 120, 2)
        
        return bg
    
    def draw(self, surface: pygame.Surface) -> None:
        """绘制背景"""
        surface.blit(self.image, (0, 0))


class Avatar:
    """头像类"""
    def __init__(self, x: int, y: int, size: int, player_id: int, is_main: bool = False):
        self.x = x
        self.y = y
        self.size = size
        self.player_id = player_id
        self.is_main = is_main
        self.image = self.create_avatar()
        
    def create_avatar(self) -> pygame.Surface:
        """创建头像图像"""
        avatar = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        
        # 头像背景
        color = (120, 90, 180) if self.is_main else (90, 120, 180)
        pygame.draw.rect(avatar, color, (0, 0, self.size, self.size), border_radius=10)
        
        # 头像边框
        border_width = 4 if self.is_main else 3
        pygame.draw.rect(avatar, AVATAR_BORDER, (0, 0, self.size, self.size), border_width, border_radius=10)
        
        # 头像内容 (使用玩家ID作为占位符)
        text = font_medium.render(f"P{self.player_id}", True, TEXT_COLOR)
        text_rect = text.get_rect(center=(self.size//2, self.size//2))
        avatar.blit(text, text_rect)
        
        # 如果是主角色，添加装饰
        if self.is_main:
            pygame.draw.rect(avatar, HIGHLIGHT, (0, 0, self.size, self.size), 2, border_radius=10)
            pygame.draw.circle(avatar, HIGHLIGHT, (self.size//2, self.size//2), self.size//3, 2)
        
        return avatar
    
    def draw(self, surface: pygame.Surface) -> None:
        """绘制头像"""
        surface.blit(self.image, (self.x, self.y))


class BuffBar:
    """Buff栏类"""
    def __init__(self, x: int, y: int, width: int, height: int, rows: int, cols: int, is_main: bool = False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols
        self.is_main = is_main
        self.buffs = self.create_buffs()
        self.slot_size = min((width - 10) // cols, (height - 10) // rows)
        
    def create_buffs(self) -> List[Dict[str, Any]]:
        """创建Buff列表"""
        buffs = []
        buff_count = 6 if self.is_main else 4
        
        for i in range(buff_count):
            buffs.append({
                'id': i,
                'name': f"Buff{i+1}",
                'duration': 3 + i
            })
        
        return buffs
    
    def draw(self, surface: pygame.Surface) -> None:
        """绘制Buff栏"""
        # 绘制背景
        bg = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        bg.fill((*PLAYER_BG[:3], 200))
        pygame.draw.rect(bg, (80, 80, 120), (0, 0, self.width, self.height), 2, border_radius=8)
        surface.blit(bg, (self.x, self.y))
        
        # 绘制标题
        title = font_small.render("BUFF栏", True, TEXT_COLOR)
        surface.blit(title, (self.x + 10, self.y + 5))
        
        # 绘制Buff槽位
        start_x = self.x + 10
        start_y = self.y + 30
        
        for row in range(self.rows):
            for col in range(self.cols):
                idx = row * self.cols + col
                slot_x = start_x + col * (self.slot_size + 5)
                slot_y = start_y + row * (self.slot_size + 5)
                
                # 绘制槽位
                pygame.draw.rect(surface, BUFF_SLOT, 
                                (slot_x, slot_y, self.slot_size, self.slot_size), 
                                border_radius=5)
                pygame.draw.rect(surface, (120, 120, 160), 
                                (slot_x, slot_y, self.slot_size, self.slot_size), 
                                1, border_radius=5)
                
                # 如果有Buff，绘制Buff
                if idx < len(self.buffs):
                    buff = self.buffs[idx]
                    text = font_small.render(str(buff['duration']), True, HIGHLIGHT)
                    text_rect = text.get_rect(center=(slot_x + self.slot_size//2, 
                                                      slot_y + self.slot_size//2))
                    surface.blit(text, text_rect)


class EquipmentBar:
    """装备栏类"""
    def __init__(self, x: int, y: int, width: int, height: int, slot_count: int, is_main: bool = False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.slot_count = slot_count
        self.is_main = is_main
        self.equipments = self.create_equipments()
        self.slot_width = (width - 20) // slot_count - 5
        
    def create_equipments(self) -> List[Dict[str, Any]]:
        """创建装备列表"""
        equipments = []
        equip_count = 4 if self.is_main else 3
        
        for i in range(equip_count):
            equipments.append({
                'id': i,
                'name': f"装备{i+1}",
                'level': 1 + i
            })
        
        return equipments
    
    def draw(self, surface: pygame.Surface) -> None:
        """绘制装备栏"""
        # 绘制背景
        bg = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        bg.fill((*PLAYER_BG[:3], 200))
        pygame.draw.rect(bg, (80, 80, 120), (0, 0, self.width, self.height), 2, border_radius=8)
        surface.blit(bg, (self.x, self.y))
        
        # 绘制标题
        title = font_small.render("装备栏", True, TEXT_COLOR)
        surface.blit(title, (self.x + 10, self.y + 5))
        
        # 绘制装备槽位
        start_x = self.x + 10
        start_y = self.y + 30
        
        for i in range(self.slot_count):
            slot_x = start_x + i * (self.slot_width + 5)
            slot_y = start_y
            
            # 绘制槽位
            pygame.draw.rect(surface, EQUIPMENT_SLOT, 
                            (slot_x, slot_y, self.slot_width, self.height - 40), 
                            border_radius=5)
            pygame.draw.rect(surface, (120, 120, 160), 
                            (slot_x, slot_y, self.slot_width, self.height - 40), 
                            1, border_radius=5)
            
            # 如果有装备，绘制装备
            if i < len(self.equipments):
                equip = self.equipments[i]
                text = font_small.render(f"E{equip['id']+1}", True, TEXT_COLOR)
                text_rect = text.get_rect(center=(slot_x + self.slot_width//2, 
                                                slot_y + (self.height - 40)//2))
                surface.blit(text, text_rect)


class CardSlot:
    """卡槽类"""
    def __init__(self, x: int, y: int, width: int, height: int, card_count: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.card_count = card_count
        self.cards = self.create_cards()
        self.card_width = (width - 20) // card_count - 5
        
    def create_cards(self) -> List[Dict[str, Any]]:
        """创建卡牌列表"""
        cards = []
        
        for i in range(self.card_count):
            cards.append({
                'id': i,
                'name': f"卡牌{i+1}",
                'cost': i+1,
                'type': '攻击' if i % 3 == 0 else '防御' if i % 3 == 1 else '特殊'
            })
        
        return cards
    
    def draw(self, surface: pygame.Surface) -> None:
        """绘制卡槽"""
        # 绘制背景
        bg = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        bg.fill((*PLAYER_BG[:3], 200))
        pygame.draw.rect(bg, (80, 80, 120), (0, 0, self.width, self.height), 2, border_radius=8)
        surface.blit(bg, (self.x, self.y))
        
        # 绘制标题
        title = font_small.render("卡牌槽", True, TEXT_COLOR)
        surface.blit(title, (self.x + 10, self.y + 5))
        
        # 绘制卡牌
        start_x = self.x + 10
        start_y = self.y + 30
        
        for i in range(self.card_count):
            card_x = start_x + i * (self.card_width + 5)
            card_y = start_y
            
            # 绘制卡牌背景
            card_color = (180, 80, 100) if i % 3 == 0 else (80, 100, 180) if i % 3 == 1 else (100, 180, 100)
            pygame.draw.rect(surface, card_color, 
                           (card_x, card_y, self.card_width, self.height - 40), 
                           border_radius=5)
            pygame.draw.rect(surface, (200, 200, 220), 
                           (card_x, card_y, self.card_width, self.height - 40), 
                           1, border_radius=5)
            
            # 绘制卡牌信息
            card = self.cards[i]
            text = font_small.render(f"C{card['id']+1}", True, TEXT_COLOR)
            text_rect = text.get_rect(center=(card_x + self.card_width//2, 
                                            card_y + (self.height - 40)//2))
            surface.blit(text, text_rect)
            
            # 绘制消耗
            cost_bg = pygame.Surface((20, 20), pygame.SRCALPHA)
            pygame.draw.circle(cost_bg, (220, 180, 60), (10, 10), 10)
            pygame.draw.circle(cost_bg, (150, 120, 30), (10, 10), 10, 1)
            cost_text = font_small.render(str(card['cost']), True, (30, 30, 30))
            cost_rect = cost_text.get_rect(center=(10, 10))
            cost_bg.blit(cost_text, cost_rect)
            surface.blit(cost_bg, (card_x + 5, card_y + 5))


class AnnouncementBoard:
    """公告栏类"""
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.messages = [
            "游戏开始!",
            "玩家1使用了攻击卡牌",
            "玩家2装备了新武器",
            "玩家3获得了BUFF",
            "玩家4的生命值降低",
            "玩家5使用了特殊技能",
            "回合结束",
            "轮到玩家1的回合"
        ]
        
    def draw(self, surface: pygame.Surface) -> None:
        """绘制公告栏"""
        # 绘制背景
        bg = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        bg.fill((*ANNOUNCEMENT_BG[:3], 220))
        pygame.draw.rect(bg, (60, 60, 100), (0, 0, self.width, self.height), 3, border_radius=10)
        surface.blit(bg, (self.x, self.y))
        
        # 绘制标题
        title = font_large.render("游戏公告", True, HIGHLIGHT)
        title_rect = title.get_rect(center=(self.x + self.width//2, self.y + 30))
        surface.blit(title, title_rect)
        
        # 绘制分割线
        pygame.draw.line(surface, (80, 80, 120), 
                        (self.x + 20, self.y + 60), 
                        (self.x + self.width - 20, self.y + 60), 2)
        
        # 绘制消息
        start_y = self.y + 80
        for i, msg in enumerate(self.messages):
            text = font_medium.render(msg, True, TEXT_COLOR)
            surface.blit(text, (self.x + 30, start_y + i * 40))
        
        # 绘制底部装饰
        pygame.draw.rect(surface, (70, 70, 110), 
                       (self.x + 20, self.y + self.height - 40, self.width - 40, 30), 
                       border_radius=5)
        footer = font_small.render("当前回合: 玩家1", True, HIGHLIGHT)
        footer_rect = footer.get_rect(center=(self.x + self.width//2, self.y + self.height - 25))
        surface.blit(footer, footer_rect)


class Player:
    """玩家角色基类"""
    def __init__(self, x: int, y: int, width: int, height: int, player_id: int, is_main: bool = False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.player_id = player_id
        self.is_main = is_main
        
        # 创建组件
        self.avatar = self.create_avatar()
        self.buff_bar = self.create_buff_bar()
        self.equipment_bar = self.create_equipment_bar()
        
    def create_avatar(self) -> Avatar:
        """创建头像"""
        # 主角色在右侧，其他角色在中间
        if self.is_main:
            avatar_x = self.x + self.width - 100
            avatar_y = self.y + self.height - 100
        else:
            avatar_x = self.x + (self.width - 80) // 2
            avatar_y = self.y + 10
            
        return Avatar(avatar_x, avatar_y, 80 if self.is_main else 70, self.player_id, self.is_main)
    
    def create_buff_bar(self) -> BuffBar:
        """创建Buff栏"""
        # 主角色在头像上方，其他角色在头像下方
        if self.is_main:
            buff_x = self.x + self.width - 100
            buff_y = self.y + self.height - 150
            return BuffBar(buff_x, buff_y, 100, 70, 2, 3, self.is_main)
        else:
            buff_x = self.x + (self.width - 90) // 2
            buff_y = self.y + 90
            return BuffBar(buff_x, buff_y, 90, 60, 2, 2)
    
    def create_equipment_bar(self) -> EquipmentBar:
        """创建装备栏"""
        # 主角色在卡槽上方，其他角色在头像左侧
        if self.is_main:
            equip_x = self.x + 10
            equip_y = self.y + 10
            return EquipmentBar(equip_x, equip_y, self.width - 120, 80, 4, self.is_main)
        else:
            equip_x = self.x + 10
            equip_y = self.y + 10
            return EquipmentBar(equip_x, equip_y, 60, 80, 1, self.is_main)
    
    def draw(self, surface: pygame.Surface) -> None:
        """绘制玩家区域"""
        # 绘制玩家背景
        player_bg = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        player_bg.fill(PLAYER_BG)
        pygame.draw.rect(player_bg, (80, 80, 120), (0, 0, self.width, self.height), 2, border_radius=12)
        surface.blit(player_bg, (self.x, self.y))
        
        # 绘制组件
        self.avatar.draw(surface)
        self.buff_bar.draw(surface)
        self.equipment_bar.draw(surface)


class MainPlayer(Player):
    """主角色类"""
    def __init__(self, x: int, y: int, width: int, height: int, player_id: int):
        super().__init__(x, y, width, height, player_id, True)
        self.card_slot = self.create_card_slot()
    
    def create_card_slot(self) -> CardSlot:
        """创建卡槽"""
        # 卡槽在头像左侧
        card_x = self.x + 10
        card_y = self.y + self.height - 110
        return CardSlot(card_x, card_y, self.width - 120, 100, 5)
    
    def draw(self, surface: pygame.Surface) -> None:
        """绘制主角色"""
        super().draw(surface)
        self.card_slot.draw(surface)
        
        # 绘制玩家标签
        label = font_medium.render(f"玩家{self.player_id} (你)", True, HIGHLIGHT)
        label_rect = label.get_rect(center=(self.x + self.width//2, self.y + 25))
        surface.blit(label, label_rect)


class OtherPlayer(Player):
    """其他角色类"""
    def draw(self, surface: pygame.Surface) -> None:
        """绘制其他角色"""
        super().draw(surface)
        
        # 绘制玩家标签
        label = font_medium.render(f"玩家{self.player_id}", True, TEXT_COLOR)
        label_rect = label.get_rect(center=(self.x + self.width//2, self.y + self.height - 20))
        surface.blit(label, label_rect)


class Game:
    """游戏主类"""
    def __init__(self):
        self.background = Background()
        self.announcement_board = AnnouncementBoard(SCREEN_WIDTH - 300, 20, 280, SCREEN_HEIGHT - 40)
        
        # 创建主角色 (在底部)
        self.main_player = MainPlayer(50, SCREEN_HEIGHT - 200, SCREEN_WIDTH - 350, 180, 1)
        
        # 创建其他5个角色 (在上方)
        self.other_players = []
        player_width = (SCREEN_WIDTH - 350) // 5 - 10
        
        for i in range(5):
            player_id = i + 2  # 玩家ID从2到6
            player_x = 50 + i * (player_width + 10)
            player_y = 20
            self.other_players.append(
                OtherPlayer(player_x, player_y, player_width, 160, player_id)
            )
    
    def draw(self, surface: pygame.Surface) -> None:
        """绘制整个游戏界面"""
        # 绘制背景
        self.background.draw(surface)
        
        # 绘制公告栏
        self.announcement_board.draw(surface)
        
        # 绘制主角色
        self.main_player.draw(surface)
        
        # 绘制其他角色
        for player in self.other_players:
            player.draw(surface)
        
        # 绘制游戏标题
        title = font_large.render("卡牌游戏界面", True, HIGHLIGHT)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150))
        surface.blit(title, title_rect)
        
        # 绘制提示文字
        hint = font_medium.render("按ESC退出游戏", True, TEXT_COLOR)
        hint_rect = hint.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))
        surface.blit(hint, hint_rect)
    
    def run(self) -> None:
        """运行游戏主循环"""
        clock = pygame.time.Clock()
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            
            # 绘制游戏
            self.draw(screen)
            
            pygame.display.flip()
            clock.tick(60)
        
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()