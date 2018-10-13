from numpy import abs
from random import (randrange, choice)
import tkinter as tk



class Drawing_World_Method:
    def add_background(self, rect_left, rect_top):
        if self.instance == 1:
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.ground_grass_image_source)
        if self.instance == 2:
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.ground_muddy_grass_image_source)
        if self.instance == 3:
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.weird_red_ground_image_source)
        if self.instance == 4:
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.ground_block_a_image_source)
    def draw_world_frame(self, i_row, f_col, rect_left, rect_top):
        if self.grid_list[i_row][f_col] == 40: 
            if self.instance == 1:
                self.add_background(rect_left, rect_top)
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.world_border_image_source)
            if self.instance == 2:
                self.add_background(rect_left, rect_top)
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.border_weird_image_source)
            if self.instance == 3:
                self.add_background(rect_left, rect_top)
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.border_space_image_source)
            if self.instance == 4:
                self.add_background(rect_left, rect_top)
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.wall_block_b_image_source)
        if self.grid_list[i_row][f_col] == 0: 
            self.add_background(rect_left, rect_top)
        if self.grid_list[i_row][f_col] == 11: 
            self.add_background(rect_left, rect_top)
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.staff_ground_image_source)
        if self.grid_list[i_row][f_col] == 101: 
            self.add_background(rect_left, rect_top)
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.portal_a_image_source)
        if self.grid_list[i_row][f_col] == 102: 
            self.add_background(rect_left, rect_top)
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.portal_b_image_source)
        if self.grid_list[i_row][f_col] == 103: 
            self.add_background(rect_left, rect_top)
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.portal_c_image_source)
        if self.grid_list[i_row][f_col] == 104:
            self.add_background(rect_left, rect_top)
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.portal_d_image_source)
        if self.grid_list[i_row][f_col] == 105: 
            self.add_background(rect_left, rect_top)
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.portal_e_image_source)
        if self.grid_list[i_row][f_col] == 106: 
            self.add_background(rect_left, rect_top)
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.portal_f_image_source)
        if self.grid_list[i_row][f_col] == 80: 
            self.add_background(rect_left, rect_top)
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.portal_lock_image_source)
        if self.grid_list[i_row][f_col] == 30: 
            self.add_background(rect_left, rect_top)
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.portal_key_image_source)
        if self.grid_list[i_row][f_col] == 31: 
            self.add_background(rect_left, rect_top)
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.tesseract_key_image_source)
        if self.grid_list[i_row][f_col] == 41: 
            if self.instance == 1:
                self.add_background(rect_left, rect_top)
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.bush_wall_image_source)
            if self.instance == 2:
                self.add_background(rect_left, rect_top)
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.wall_block_image_source)
            if self.instance == 3:
                self.add_background(rect_left, rect_top)
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.weird_wall_block_image_source)
            if self.instance == 4:
                self.add_background(rect_left, rect_top)
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.wall_block_a_image_source)
        if self.grid_list[i_row][f_col] == 81: 
            self.add_background(rect_left, rect_top)
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.tesseract_off_image_source)
        if self.grid_list[i_row][f_col] == 82:
            self.add_background(rect_left, rect_top)
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.tesseract_on_image_source) 
        if self.grid_list[i_row][f_col] == 1337: 
            self.add_background(rect_left, rect_top)
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.monitor_a_image_source)
        if self.grid_list[i_row][f_col] == 1336: 
            self.add_background(rect_left, rect_top)
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.monitor_b_image_source)
        if self.grid_list[i_row][f_col] == 20: 
            self.add_background(rect_left, rect_top)
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.mana_block_image_source)
class Drawing_Method:
    def write_board(self):
        self.grid_list = []
        for row in range(self.board_size): 
            self.grid_list += [[0] * self.board_size] 
        for row in range(self.board_size-1): 
            self.grid_list[0][row] = 40
            self.grid_list[self.board_size-1][row] = 40  
        for col in range(self.board_size):
            self.grid_list[col][0] = 40
            self.grid_list[col][self.board_size-1] = 40 
    def draw_frame(self):
        for i_row in range(self.board_size):
            for f_col in range(self.board_size): 
                rect_left = 5 + f_col * self.object_size+ 12
                rect_right = rect_left + self.object_size + 12
                rect_top = 5 + i_row * self.object_size + 110
                rect_bottom = rect_top + self.object_size + 110
                if self.grid_list[i_row][f_col] == 1:
                    self.add_background(rect_left, rect_top)
                    self.draw_player_frame(rect_left, rect_top)
                    self.draw_player_stat()
                if self.grid_list[i_row][f_col] == 97:
                    self.add_background(rect_left, rect_top)
                    self.draw_npc_frame(rect_left, rect_top)
                    self.draw_npc_stat()
                if self.grid_list[i_row][f_col] == 96:
                    self.add_background(rect_left, rect_top)
                    self.draw_npc_b_frame(rect_left, rect_top)
                    self.draw_npc_b_stat()
                if self.grid_list[i_row][f_col] == 95:
                    self.add_background(rect_left, rect_top)
                    self.draw_npc_d_frame(rect_left, rect_top)
                    self.draw_npc_d_stat()
                if self.grid_list[i_row][f_col] == 94:
                    self.add_background(rect_left, rect_top)
                    self.draw_npc_c_frame(rect_left, rect_top)
                    self.draw_npc_c_stat()
                if self.grid_list[i_row][f_col] == 100:
                    self.add_background(rect_left, rect_top)
                    self.draw_fire_ability(rect_left, rect_top)
                self.draw_world_frame(i_row, f_col, rect_left, rect_top)

class Animation_Method:
    def timer_clock(self): 
        if self.instance == 1:
            self.tk_frame.delete(tk.ALL) 
            self.game_clock += 1
            if self.game_clock >= 10:
                self.game_clock = 0
            if self.plasma == 1:
                self.move_plasma_projectile()
            if self.npc_hp >= 1:
                self.move_npc()
            self.draw_frame()
        if self.instance == 2:
            self.tk_frame.delete(tk.ALL) 
            self.game_clock += 1
            if self.game_clock >= 10:
                self.game_clock = 0
            if self.plasma == 1:
                self.move_plasma_projectile()
            if self.npc_d_hp > 0 and self.world_tesseract_beacon == 1:
                self.move_npc_d()
            self.draw_frame()
        if self.instance == 3:
            self.tk_frame.delete(tk.ALL) 
            self.game_clock += 1
            if self.game_clock >= 10:
                self.game_clock = 0
            if self.plasma == 1:
                self.move_plasma_projectile()
            if self.npc_b_hp >= 1:
                self.move_npc_b()
            self.draw_frame()    
        if self.instance == 4:
            self.game_clock += 1
            self.tk_frame.delete(tk.ALL) 
            if self.game_clock >= 10:
                self.game_clock = 0
            if self.plasma == 1:
                self.move_plasma_projectile()
            if self.npc_c_hp >= 1:
                self.move_npc_c()
            self.draw_frame()    
        self.tk_frame.after(self.game_delay, self.timer_clock)
    def key_pressed(self, tk_command):
        self.tk_frame = tk_command.widget.tk_frame
        if (tk_command.char == "p") and (self.instance == 0):
            self.write_first_instance() 
            self.timer_clock()
            self.move_player(0,0)
        if (tk_command.char == "f") and (self.player_staff == 1) and (self.player_mp >= 10) and (self.plasma != 1):
            self.launch_plasma_projectile()
            self.player_mp -= 10
        if tk_command.keysym == "1" and (self.player_staff == 1): 
            self.player_staff = 0
            self.player_inventory_staff = 1
        if tk_command.keysym == "2" and (self.player_inventory_staff == 1): 
            self.player_inventory_staff = 0
            self.player_staff = 1
        if tk_command.keysym == "c" and (self.instance != 0): 
            self.start_new_game()
        if tk_command.keysym == "x": 
            self.npc_hp = 0
        if tk_command.keysym == "i": 
            self.world_tesseract_beacon = 1
        if tk_command.keysym == "b": 
            self.npc_b_hp = 0
        if tk_command.keysym == "g": 
            self.npc_d_hp = 0
        if tk_command.keysym == "Up":
            if (self.instance == 1 or self.instance == 2 or self.instance == 3 or self.instance == 4): 
                self.move_player(-1, 0) 
        if tk_command.keysym == "Down":
            if (self.instance == 1 or self.instance == 2 or self.instance == 3 or self.instance == 4):
                self.move_player(+1, 0) 
        if tk_command.keysym == "Left":
            if (self.instance == 1 or self.instance == 2 or self.instance == 3 or self.instance == 4):
                self.move_player(0,-1) 
        if tk_command.keysym == "Right":
            if (self.instance == 1 or self.instance == 2 or self.instance == 3 or self.instance == 4):
                self.move_player(0,+1)

class Instance_Planner:
    def write_first_instance(self):
        self.write_board() 
        if self.instance == 0:
            self.player_hp = 100 
            self.player_mp = 100
            self.npc_hp = 100
            self.grid_list[4][6] = 11 
            self.player_row_pos = 13
            self.player_col_pos = 2
        if self.instance == 2:        
            self.player_row_pos = 1
            self.player_col_pos = 1 
            self.grid_list[0][1] = 101
        for i in range(2): 
            self.grid_list[9][i+7] = 41
        for i in range(3):
            self.grid_list[i+1][9] = 41 
        self.move_player(0,0)       
        if self.npc_hp >= 1:             
            self.npc_row_pos = 7
            self.npc_col_pos = 7
            self.grid_list[7][7] = 97 
            self.move_npc()
        self.grid_list[10][2] = 80
        self.instance = 1 
        self.draw_frame() 
    def write_second_instance(self):
        self.write_board()
        self.grid_list[14][15] = 102 
        self.grid_list[0][1] = 103 
        if self.instance == 1: 
            self.player_row_pos = 14
            self.player_col_pos = 14
        if self.instance == 3: 
            self.player_row_pos = 1
            self.player_col_pos = 1
        if self.instance == 4: 
            self.player_row_pos = 14
            self.player_col_pos = 6
            self.grid_list[15][6] = 105
        if self.world_tesseract_beacon == 1:
            self.grid_list[0][13] = 1337
            if self.npc_d_hp >= 1 and self.world_tesseract_beacon == 1:              
                self.npc_d_row_pos = 7
                self.npc_d_col_pos = 7
                self.grid_list[7][7] = 95 
        self.move_player(0,0) 
        for i in range(6): 
            self.grid_list[9][i+1] = 41
        for i in range(5):
            self.grid_list[i+1][9] = 41 
        self.grid_list[3][3] = 20 
        self.grid_list[10][3] = 20 
        self.grid_list[6][8] = 20 
        self.instance = 2
        self.draw_frame()
    def write_third_instance(self):
        self.write_board()
        self.grid_list[14][15] = 104 
        if self.instance == 2:
            self.player_row_pos = 14
            self.player_col_pos = 14
        self.move_player(0,0) 
        if self.npc_b_hp >= 1:              
            self.npc_b_row_pos = 7
            self.npc_b_col_pos = 7
            self.grid_list[7][7] = 96
            self.move_npc_b()
        for i in range(3): 
            self.grid_list[7][i+1] = 41
        for i in range(3): 
            self.grid_list[3][i+1] = 41
        for i in range(2):
            self.grid_list[i+1][3] = 41 
        for i in range(6):
            self.grid_list[i+1][7] = 41 
        self.grid_list[3][2] = 81
        self.grid_list[1][2] = 20
        self.grid_list[1][1] = 20   
        self.grid_list[2][1] = 20  
        self.grid_list[2][2] = 20  
        self.grid_list[2][3] = 20  
        if self.world_tesseract_beacon == 1:
            self.grid_list[3][2] = 82
        self.instance = 3
        self.draw_frame()
    def write_fourth_instance(self):
        self.write_board()
        self.grid_list[0][6] = 106
        if self.instance == 2:
            self.player_row_pos = 2
            self.player_col_pos = 6
        self.move_player(0,0) 
        if self.npc_c_hp >= 1:             
            self.npc_c_row_pos = 7
            self.npc_c_col_pos = 7
            self.grid_list[7][7] = 96
            self.move_npc_c()
        for i in range(3): 
            self.grid_list[2][i+1] = 41
        for i in range(3): 
            self.grid_list[12][i+1] = 41
        for i in range(3):
            self.grid_list[i+1][2] = 41 
        for i in range(3):
            self.grid_list[i+1][12] = 41 
        self.instance = 4
        self.draw_frame()
    def write_ui_instance(self): 
        self.instance = 0
        self.tk_frame.create_image(self.frame_width/2, (self.frame_height/2) + 200, image=self.game_ui_image_source)
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2) - 250, 
                                  text='Towers of Atlantis v6.1', fill="black")
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2) - 200, 
                                  text='Press P to play', fill="black")
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2) - 150, 
                                  text='Press F to fire, when staff equipped', fill="black")
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2) - 100, 
                                  text='Press 2 to equip staff if owned', fill="black")
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2) - 50, 
                                  text='Press 1 to remove weapon from hand, and interact with object', fill="black")
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2), 
                                  text='Press C to restart game at any time (except now)', fill="black")
    def write_game_won_instance(self): 
        self.instance = 1001
        self.tk_frame.delete(tk.ALL)
        self.tk_frame.create_image(self.frame_width/2, (self.frame_height/2) + 200, image=self.game_won_image_source)
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2) - 250, 
                                  text='Congratulations, well played!', fill="black")
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2) - 200, 
                                  text='Press C if you want to play again', fill="black")    
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2) - 150, 
                                  text='Stay tuned for more content!', fill="black")
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2) - 100, 
                                  text='Dont forget to leave a like and/or comment!', fill="black")
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2) - 50, 
                                  text='If you feel like it of course, not forcing you.', fill="black")
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2), 
                                  text='Any feedback is highly appreciated...', fill="black")
    def write_game_lost_instance(self): 
        self.instance = -1
        self.tk_frame.delete(tk.ALL)
        self.tk_frame.create_image(self.frame_width/2, (self.frame_height/2) + 200, image=self.game_lost_image_source)
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2) - 250, 
                                  text='You lost. (Press C if you want to play again)', fill="black")
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2) - 200, 
                                  text='Gameplay reminder:', fill="black")
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2) - 150, 
                                  text='Press F to fire, when staff equipped', fill="black")
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2) - 100, 
                                  text='Press 2 to equip staff if owned', fill="black")
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2) - 50, 
                                  text='Press 1 to remove weapon from hand', fill="black")
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2), 
                                  text='Interacting with locks requires unarmed', fill="black")
    def start_new_game(self):
        self.player_inventory_staff = 0 
        self.player_tesseract_key = 0
        self.world_tesseract_beacon = 0
        self.player_portal_a_key = 0
        self.player_staff = 0
        self.plasma = 0
        self.player_hp = 100 
        self.player_mp = 100
        self.npc_hp = 100
        self.npc_b_hp = 100
        self.npc_d_hp = 100
        self.npc_c_hp = 100
        self.grid_list[self.player_row_pos][self.player_col_pos] = 0 
        self.player_row_pos = 13
        self.player_col_pos = 2
        self.grid_list[self.player_row_pos][self.player_col_pos] = 1
        self.write_first_instance() 
        self.grid_list[7][7] = 97 
        self.grid_list[4][6] = 11

class Game_Images:
    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    def pull_images(self):
        self.player_up_image_source = tk.PhotoImage(file=self.resource_path("img/human_fa_up.gif"))
        self.player_down_image_source = tk.PhotoImage(file=self.resource_path("img/human_fa_down.gif"))
        self.player_left_image_source = tk.PhotoImage(file=self.resource_path("img/human_fa_left.gif"))
        self.player_right_image_source = tk.PhotoImage(file=self.resource_path("img/human_fa_right.gif"))
        self.staff_ground_image_source = tk.PhotoImage(file=self.resource_path("img/staff_ground.gif"))
        self.staff_up_image_source = tk.PhotoImage(file=self.resource_path("img/staff_up.gif"))
        self.staff_down_image_source = tk.PhotoImage(file=self.resource_path("img/staff_down.gif"))
        self.staff_left_image_source = tk.PhotoImage(file=self.resource_path("img/staff_left.gif"))
        self.staff_right_image_source = tk.PhotoImage(file=self.resource_path("img/staff_right.gif"))
        self.aggro_spiderbot_up_image_source = tk.PhotoImage(file=self.resource_path("img/aggro_spiderbot_up.gif"))
        self.aggro_spiderbot_down_image_source = tk.PhotoImage(file=self.resource_path("img/aggro_spiderbot.gif"))
        self.aggro_spiderbot_left_image_source = tk.PhotoImage(file=self.resource_path("img/aggro_spiderbot_left.gif"))
        self.aggro_spiderbot_right_image_source = tk.PhotoImage(file=self.resource_path("img/aggro_spiderbot_right.gif"))
        self.spiderbot_up_image_source = tk.PhotoImage(file=self.resource_path("img/spiderbot_up.gif"))
        self.spiderbot_down_image_source = tk.PhotoImage(file=self.resource_path("img/spiderbot.gif"))
        self.spiderbot_left_image_source = tk.PhotoImage(file=self.resource_path("img/spiderbot_left.gif"))
        self.spiderbot_right_image_source = tk.PhotoImage(file=self.resource_path("img/spiderbot_right.gif"))
        self.aggro_shroom_bot_up_image_source = tk.PhotoImage(file=self.resource_path("img/shroom_bot_up.gif"))
        self.aggro_shroom_bot_down_image_source = tk.PhotoImage(file=self.resource_path("img/aggro_shroom_bot_down.gif"))
        self.aggro_shroom_bot_left_image_source = tk.PhotoImage(file=self.resource_path("img/aggro_shroom_bot_left.gif"))
        self.aggro_shroom_bot_right_image_source = tk.PhotoImage(file=self.resource_path("img/aggro_shroom_bot_right.gif")) 
        self.shroom_bot_up_image_source = tk.PhotoImage(file=self.resource_path("img/shroom_bot_up.gif"))
        self.shroom_bot_down_image_source = tk.PhotoImage(file=self.resource_path("img/shroom_bot_down.gif"))
        self.shroom_bot_left_image_source = tk.PhotoImage(file=self.resource_path("img/shroom_bot_left.gif"))
        self.shroom_bot_right_image_source = tk.PhotoImage(file=self.resource_path("img/shroom_bot_right.gif"))
        self.aggro_npc_b_down_image_source = tk.PhotoImage(file=self.resource_path("img/aggro_npc_b_down.gif"))
        self.aggro_npc_b_left_image_source = tk.PhotoImage(file=self.resource_path("img/aggro_npc_b_left.gif"))
        self.aggro_npc_b_right_image_source = tk.PhotoImage(file=self.resource_path("img/aggro_npc_b_right.gif"))
        self.npc_b_up_image_source = tk.PhotoImage(file=self.resource_path("img/npc_b.gif"))
        self.npc_b_down_image_source = tk.PhotoImage(file=self.resource_path("img/npc_b_down.gif"))
        self.npc_b_left_image_source = tk.PhotoImage(file=self.resource_path("img/npc_b_left.gif"))
        self.npc_b_right_image_source = tk.PhotoImage(file=self.resource_path("img/npc_b_right.gif"))
        self.aggro_npc_d_up_image_source = tk.PhotoImage(file=self.resource_path("img/aggro_npc_d_up.gif"))
        self.aggro_npc_d_down_image_source = tk.PhotoImage(file=self.resource_path("img/aggro_npc_d_down.gif"))
        self.aggro_npc_d_left_image_source = tk.PhotoImage(file=self.resource_path("img/aggro_npc_d_left.gif"))
        self.aggro_npc_d_right_image_source = tk.PhotoImage(file=self.resource_path("img/aggro_npc_d_right.gif"))
        self.npc_d_up_image_source = tk.PhotoImage(file=self.resource_path("img/npc_d_up.gif"))
        self.npc_d_down_image_source = tk.PhotoImage(file=self.resource_path("img/npc_d_down.gif"))
        self.npc_d_left_image_source = tk.PhotoImage(file=self.resource_path("img/npc_d_left.gif"))
        self.npc_d_right_image_source = tk.PhotoImage(file=self.resource_path("img/npc_d_right.gif"))
        self.fire_up_image_source = tk.PhotoImage(file=self.resource_path("img/fire_up.gif"))
        self.fire_down_image_source = tk.PhotoImage(file=self.resource_path("img/fire_down.gif"))
        self.fire_right_image_source = tk.PhotoImage(file=self.resource_path("img/fire_left.gif"))
        self.fire_left_image_source = tk.PhotoImage(file=self.resource_path("img/fire_right.gif"))
        self.world_border_image_source = tk.PhotoImage(file=self.resource_path("img/border_stone_grass.gif"))
        self.ground_grass_image_source = tk.PhotoImage(file=self.resource_path("img/ground_grass.gif"))
        self.ground_block_a_image_source = tk.PhotoImage(file=self.resource_path("img/ground_block_a.gif")) 
        self.ground_muddy_grass_image_source = tk.PhotoImage(file=self.resource_path("img/ground_muddy_grass.gif"))
        self.weird_red_ground_image_source = tk.PhotoImage(file=self.resource_path("img/weird_red_ground.gif"))
        self.mana_bar_image_source = tk.PhotoImage(file=self.resource_path("img/mana_bar.gif"))
        self.life_bar_image_source = tk.PhotoImage(file=self.resource_path("img/life_bar.gif"))
        self.energy_icon_image_source = tk.PhotoImage(file=self.resource_path("img/mana_icon.gif"))
        self.life_icon_image_source = tk.PhotoImage(file=self.resource_path("img/life_icon.gif"))
        self.life_bar_icon_image_source = tk.PhotoImage(file=self.resource_path("img/life_bar_icon.gif"))
        self.portal_lock_image_source = tk.PhotoImage(file=self.resource_path("img/portal_lock.gif"))
        self.portal_a_image_source = tk.PhotoImage(file=self.resource_path("img/portal_a.gif"))
        self.portal_b_image_source = tk.PhotoImage(file=self.resource_path("img/portal_b.gif"))
        self.portal_c_image_source = tk.PhotoImage(file=self.resource_path("img/portal_c.gif"))
        self.portal_d_image_source = tk.PhotoImage(file=self.resource_path("img/portal_d.gif"))
        self.portal_e_image_source = tk.PhotoImage(file=self.resource_path("img/portal_e.gif"))
        self.portal_f_image_source = tk.PhotoImage(file=self.resource_path("img/portal_f.gif"))
        self.portal_key_image_source = tk.PhotoImage(file=self.resource_path("img/portal_key.gif"))
        self.wall_block_image_source = tk.PhotoImage(file=self.resource_path("img/wall_block.gif"))
        self.weird_wall_block_image_source = tk.PhotoImage(file=self.resource_path("img/weird_wall_block.gif"))
        self.bush_wall_image_source = tk.PhotoImage(file=self.resource_path("img/bush_wall.gif"))
        self.wall_block_a_image_source = tk.PhotoImage(file=self.resource_path("img/wall_block_a.gif"))
        self.wall_block_b_image_source = tk.PhotoImage(file=self.resource_path("img/wall_block_b.gif"))
        self.border_space_image_source = tk.PhotoImage(file=self.resource_path("img/border_space.gif"))
        self.border_weird_image_source = tk.PhotoImage(file=self.resource_path("img/border_weird.gif")) 
        self.monitor_a_image_source = tk.PhotoImage(file=self.resource_path("img/monitor_a.gif"))
        self.monitor_b_image_source = tk.PhotoImage(file=self.resource_path("img/monitor_b.gif"))
        self.tesseract_on_image_source = tk.PhotoImage(file=self.resource_path("img/tesseract_beacon.gif"))
        self.tesseract_off_image_source = tk.PhotoImage(file=self.resource_path("img/tesseract_beacon_off.gif"))
        self.tesseract_key_image_source = tk.PhotoImage(file=self.resource_path("img/tesseract_key.gif"))
        self.mana_block_image_source = tk.PhotoImage(file=self.resource_path("img/mana_block.gif"))
        self.game_won_image_source = tk.PhotoImage(file=self.resource_path("img/game_won.gif"))
        self.game_lost_image_source = tk.PhotoImage(file=self.resource_path("img/game_lost.gif"))
        self.game_ui_image_source = tk.PhotoImage(file=self.resource_path("img/game_ui.gif"))
        self.aggro_sign_image_source = tk.PhotoImage(file=self.resource_path("img/aggro_sign.gif"))

class Drawing_Player_Method:
    def draw_player_stat(self):
        self.tk_frame.create_rectangle(10,5,640,100,fill='green',width=0) 
        for i in range(int(self.player_hp/10)):
            self.tk_frame.create_image(60+30*i, 70, image=self.life_bar_image_source)
        self.tk_frame.create_image(30, 70, image=self.life_icon_image_source)
        for i in range(int(self.player_mp/10)):
            self.tk_frame.create_image(60+30*i, 40, image=self.mana_bar_image_source)
        self.tk_frame.create_image(30, 40, image=self.energy_icon_image_source)
        if self.player_inventory_staff == 1 and self.player_staff == 0: 
            self.tk_frame.create_rectangle(400, 40, 450, 90, fill='grey')
            self.tk_frame.create_image(428, 66, image=self.staff_ground_image_source)
            self.tk_frame.create_rectangle(500, 40, 550, 90, fill='green')
        if self.player_inventory_staff == 0 and self.player_staff == 1: 
            self.tk_frame.create_rectangle(400, 40, 450, 90, fill='green')
            self.tk_frame.create_image(428, 66, image=self.staff_ground_image_source)
            self.tk_frame.create_rectangle(500, 40, 550, 90, fill='grey')
        if self.player_inventory_staff == 0 and self.player_staff == 0: 
            self.tk_frame.create_rectangle(500, 40,550,90, fill='green')
        if self.npc_status == 'chasing' or self.npc_b_status == 'chasing' or self.npc_c_status == 'chasing' or self.npc_d_status == 'chasing':
            self.tk_frame.create_image(528, 66, image=self.aggro_sign_image_source)
    def draw_player_frame(self, rect_left, rect_top):
        if self.player_staff == 1:
            if self.player_row_vec == -1 and self.player_col_vec == 0:
                self.tk_frame.create_image(rect_left+10, rect_top+20, image=self.staff_up_image_source)
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.player_up_image_source)
            elif self.player_row_vec == 1 and self.player_col_vec == 0:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.player_down_image_source)
                self.tk_frame.create_image(rect_left+10, rect_top+20, image=self.staff_down_image_source)
            elif self.player_row_vec == 0 and self.player_col_vec == -1:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.player_left_image_source)
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.staff_left_image_source)
            elif self.player_row_vec == 0 and self.player_col_vec == 1:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.staff_right_image_source)
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.player_right_image_source)
            else:
                self.tk_frame.create_image(rect_left+10, rect_top+15, image=self.player_down_image_source)
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.staff_down_image_source)
        if self.player_staff == 0:
            if self.player_row_vec == -1 and self.player_col_vec == 0:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.player_up_image_source)
            elif self.player_row_vec == 1 and self.player_col_vec == 0:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.player_down_image_source)
            elif self.player_row_vec == 0 and self.player_col_vec == -1:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.player_left_image_source)
            elif self.player_row_vec == 0 and self.player_col_vec == 1:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.player_right_image_source)
            else:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.player_down_image_source)                
class Ability_Player_Method:
    def launch_plasma_projectile(self):
        self.plasma = 1
        if self.grid_list[self.player_row_pos + self.player_row_vec][self.player_col_pos + self.player_col_vec] == 0:
            self.plasma_rpos = self.player_row_pos
            self.plasma_cpos = self.player_col_pos
            self.grid_list[self.plasma_rpos][self.plasma_cpos] = 100
            self.plasma_row_vec = self.player_row_vec 
            self.plasma_col_vec = self.player_col_vec
        else:
            self.plasma = 0
    def move_plasma_projectile(self):
        if self.grid_list[self.plasma_rpos + self.plasma_row_vec][self.plasma_cpos + self.plasma_col_vec] == 0:
            self.grid_list[self.plasma_rpos][self.plasma_cpos] = 0
            self.plasma_rpos = self.plasma_rpos + self.plasma_row_vec
            self.plasma_cpos = self.plasma_cpos + self.plasma_col_vec
            self.grid_list[self.plasma_rpos][self.plasma_cpos] = 100
            self.plasma = 1
            self.grid_list[self.player_row_pos][self.player_col_pos] = 1
        elif self.grid_list[self.plasma_rpos + self.plasma_row_vec][self.plasma_cpos + self.plasma_col_vec] == 97:
            self.npc_hp -= randrange(0,100)
            self.plasma = 0
            self.grid_list[self.plasma_rpos][self.plasma_cpos] = 0
            if self.npc_hp <= 0:
                self.grid_list[self.npc_row_pos][self.npc_col_pos] = 30
                self.npc_row_pos = -1000
                self.npc_col_pos = -1000
        elif self.grid_list[self.plasma_rpos + self.plasma_row_vec][self.plasma_cpos + self.plasma_col_vec] == 96:
            self.npc_b_hp -= randrange(0,100)
            self.plasma = 0
            self.grid_list[self.plasma_rpos][self.plasma_cpos] = 0
            if self.npc_b_hp <= 0:
                self.grid_list[self.npc_b_row_pos][self.npc_b_col_pos] = 31
                self.npc_b_row_pos = -1000
                self.npc_b_col_pos = -1000
        elif self.grid_list[self.plasma_rpos + self.plasma_row_vec][self.plasma_cpos + self.plasma_col_vec] == 95:
            self.npc_d_hp -= randrange(0,100)
            self.plasma = 0
            self.grid_list[self.plasma_rpos][self.plasma_cpos] = 0
            if self.npc_d_hp <= 0:
                self.grid_list[self.npc_d_row_pos][self.npc_d_col_pos] = 0
                self.npc_d_row_pos = -1000
                self.npc_d_col_pos = -1000
        elif self.grid_list[self.plasma_rpos + self.plasma_row_vec][self.plasma_cpos + self.plasma_col_vec] == 94:
            self.npc_c_hp -= randrange(0,100)
            self.plasma = 0
            self.grid_list[self.plasma_rpos][self.plasma_cpos] = 0
            if self.npc_c_hp <= 0:
                self.grid_list[self.npc_c_row_pos][self.npc_c_col_pos] = 0
                self.npc_c_row_pos = -1000
                self.npc_c_col_pos = -1000
                self.grid_list[14][13] = 1336
        else:
            self.grid_list[self.plasma_rpos][self.plasma_cpos] = 0
            self.plasma = 0
    def draw_fire_ability(self, rect_left, rect_top):
        if self.plasma_row_vec == -1 and self.plasma_col_vec == 0:
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.fire_up_image_source)
        elif self.plasma_row_vec == 1 and self.plasma_col_vec == 0:
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.fire_down_image_source)
        elif self.plasma_row_vec == 0 and self.plasma_col_vec == -1:
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.fire_left_image_source)
        elif self.plasma_row_vec == 0 and self.plasma_col_vec == 1:
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.fire_right_image_source)
class Player_Method:
    plasma = 0
    player_staff = 0
    player_inventory_staff = 0
    player_portal_a_key = 0
    player_tesseract_key = 0
    world_tesseract_beacon = 0
    player_hp = 100
    player_mp = 100
    def move_player(self, dist_row, dist_col):
        self.player_row_vec = dist_row
        self.player_col_vec = dist_col
        if self.grid_list[self.player_row_pos + dist_row][self.player_col_pos + dist_col] == 0: 
            self.grid_list[self.player_row_pos][self.player_col_pos] = 0
            self.player_row_pos = self.player_row_pos + dist_row
            self.player_col_pos = self.player_col_pos + dist_col
            self.grid_list[self.player_row_pos][self.player_col_pos] = 1
        if self.grid_list[self.player_row_pos + dist_row][self.player_col_pos + dist_col] == 11: 
            self.grid_list[self.player_row_pos][self.player_col_pos] = 0
            self.player_row_pos = self.player_row_pos + dist_row
            self.player_col_pos = self.player_col_pos + dist_col
            self.grid_list[self.player_row_pos][self.player_col_pos] = 1
            self.player_staff = 1
        if self.grid_list[self.player_row_pos + dist_row][self.player_col_pos + dist_col] == 30: 
            self.grid_list[self.player_row_pos][self.player_col_pos] = 0
            self.player_row_pos = self.player_row_pos + dist_row
            self.player_col_pos = self.player_col_pos + dist_col
            self.grid_list[self.player_row_pos][self.player_col_pos] = 1
            self.player_portal_a_key = 1
        if self.grid_list[self.player_row_pos + dist_row][self.player_col_pos + dist_col] == 31: 
            self.grid_list[self.player_row_pos][self.player_col_pos] = 0
            self.player_row_pos = self.player_row_pos + dist_row
            self.player_col_pos = self.player_col_pos + dist_col
            self.grid_list[self.player_row_pos][self.player_col_pos] = 1
            self.player_tesseract_key = 1
        if self.grid_list[self.player_row_pos + dist_row][self.player_col_pos + dist_col] == 20: 
            self.grid_list[self.player_row_pos][self.player_col_pos] = 0
            self.player_row_pos = self.player_row_pos + dist_row
            self.player_col_pos = self.player_col_pos + dist_col
            self.grid_list[self.player_row_pos][self.player_col_pos] = 1
            if self.player_mp <= 90:
                self.player_mp += 10
        if self.grid_list[self.player_row_pos + dist_row][self.player_col_pos + dist_col] == 80:
            if self.player_portal_a_key == 1 and self.player_staff == 0:
                self.grid_list[self.player_row_pos][self.player_col_pos] = 1
                self.grid_list[0][1] = 101 
        if self.grid_list[self.player_row_pos + dist_row][self.player_col_pos + dist_col] == 81:
            if self.player_tesseract_key == 1 and self.player_staff == 0:
                self.grid_list[self.player_row_pos][self.player_col_pos] = 1
                self.grid_list[3][2] = 82
                self.world_tesseract_beacon = 1
        if self.grid_list[self.player_row_pos + dist_row][self.player_col_pos + dist_col] == 101:
            self.grid_list[self.player_row_pos][self.player_col_pos] = 0
            self.write_second_instance()
        if self.grid_list[self.player_row_pos + dist_row][self.player_col_pos + dist_col] == 102:
            self.grid_list[self.player_row_pos][self.player_col_pos] = 0
            self.write_first_instance()
        if self.grid_list[self.player_row_pos + dist_row][self.player_col_pos + dist_col] == 103:
            self.grid_list[self.player_row_pos][self.player_col_pos] = 0
            self.write_third_instance()
        if self.grid_list[self.player_row_pos + dist_row][self.player_col_pos + dist_col] == 104:
            self.grid_list[self.player_row_pos][self.player_col_pos] = 0
            self.write_second_instance()
        if self.grid_list[self.player_row_pos + dist_row][self.player_col_pos + dist_col] == 105:
            self.grid_list[self.player_row_pos][self.player_col_pos] = 0
            self.write_fourth_instance()
        if self.grid_list[self.player_row_pos + dist_row][self.player_col_pos + dist_col] == 106:
            self.grid_list[self.player_row_pos][self.player_col_pos] = 0
            self.write_second_instance()
        if self.grid_list[self.player_row_pos + dist_row][self.player_col_pos + dist_col] == 1337:
            if self.npc_d_hp <= 0 and self.player_staff == 0:
                self.grid_list[15][6] = 105
        if self.grid_list[self.player_row_pos + dist_row][self.player_col_pos + dist_col] == 1336:
            if self.npc_c_hp <= 0 and self.player_staff == 0:
                self.write_game_won_instance()
        if self.grid_list[self.player_row_pos + dist_row][self.player_col_pos + dist_col] == 97: 
            self.grid_list[self.player_row_pos][self.player_col_pos] = 1
            self.player_hp -= randrange(0,100)
            if self.player_hp <= 0:
                self.write_game_lost_instance()
        if self.grid_list[self.player_row_pos + dist_row][self.player_col_pos + dist_col] == 96: 
            self.grid_list[self.player_row_pos][self.player_col_pos] = 1
            self.player_hp -= randrange(0,100)
            if self.player_hp <= 0:
                self.write_game_lost_instance()
        if self.grid_list[self.player_row_pos + dist_row][self.player_col_pos + dist_col] == 95: 
            self.grid_list[self.player_row_pos][self.player_col_pos] = 1
            self.player_hp -= randrange(0,100)
            if self.player_hp <= 0:
                self.write_game_lost_instance()

class Drawing_NPC_Method:
    def draw_npc_frame(self, rect_left, rect_top):
        if self.npc_status == 'roaming':
            if self.npc_a_row_dx == -1 and self.npc_a_col_dy == 0:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.spiderbot_up_image_source)
            elif self.npc_a_row_dx == 1 and self.npc_a_col_dy == 0:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.spiderbot_down_image_source)
            elif self.npc_a_row_dx == 0 and self.npc_a_col_dy == -1:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.spiderbot_left_image_source)
            elif self.npc_a_row_dx == 0 and self.npc_a_col_dy == 1:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.spiderbot_right_image_source)
            else:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.spiderbot_down_image_source)
        if self.npc_status == 'chasing':
            if self.npc_a_row_dx == -1 and self.npc_a_col_dy == 0:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.aggro_spiderbot_up_image_source)
            elif self.npc_a_row_dx == 1 and self.npc_a_col_dy == 0:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.aggro_spiderbot_down_image_source)
            elif self.npc_a_row_dx == 0 and self.npc_a_col_dy == -1:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.aggro_spiderbot_left_image_source)
            elif self.npc_a_row_dx == 0 and self.npc_a_col_dy == 1:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.aggro_spiderbot_right_image_source)
            else:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.aggro_spiderbot_down_image_source)
    def draw_npc_stat(self):
        if self.npc_hp >= 1:
            for i in range(int(self.npc_hp/10)):
                self.tk_frame.create_image(40*self.npc_col_pos+i*5, 60+(40*self.npc_row_pos),
                                           image=self.life_bar_icon_image_source)
class NPC_Method:
    npc_hp = 100
    npc_row_pos = 7
    npc_col_pos = 7
    npc_row_dist = 0
    npc_col_dist = 0
    dx_step = 0
    dy_step = 0
    n_row = 6
    n_col = 6
    npc_a_row_dx = 0
    npc_a_col_dy = 0
    npc_status = 'idle'
    def move_npc(self):
        if self.npc_hp >= 1:
            self.npc_row_dist = self.player_row_pos - self.npc_row_pos
            self.npc_col_dist = self.player_col_pos - self.npc_col_pos
            if self.npc_col_dist <= 4 and self.npc_row_dist <= 4 and  self.npc_row_dist != 0 and self.game_clock == 2:
                self.dx_step = int(self.npc_row_dist/abs(self.npc_row_dist))
                self.chase_player()
            if self.npc_col_dist <= 4 and self.npc_row_dist <= 4 and self.npc_col_dist != 0 and  self.game_clock == 7:
                self.dy_step = int(self.npc_col_dist/abs(self.npc_col_dist))
                self.chase_player()
            elif self.game_clock == 3:
                self.roam_random()
            else:
                pass
        else:
            if self.grid_list[self.npc_row_pos][self.npc_col_pos] == 2:
                self.grid_list[self.npc_row_pos][self.npc_col_pos] = 0
    def roam_random(self):
        self.npc_status = 'roaming'
        (dx, dy) = choice([(0,1),(0,-1),(1,0),(-1,0)])
        self.npc_a_row_dx = dx
        self.npc_a_col_dy = dy
        self.n_row = self.npc_row_pos + dx
        self.n_col = self.npc_col_pos + dy
        if self.grid_list[self.n_row][self.n_col] == 0 and self.npc_hp > 0:
            self.grid_list[self.npc_row_pos][self.npc_col_pos] = 0
            self.npc_row_pos = self.n_row
            self.npc_col_pos = self.n_col
            self.grid_list[self.npc_row_pos][self.npc_col_pos] = 97
        if self.grid_list[self.n_row][self.n_col] == 100:
            self.grid_list[self.npc_row_pos][self.npc_col_pos] = 0
            self.npc_row_pos = self.n_row
            self.npc_col_pos = self.n_col
            self.grid_list[self.npc_row_pos][self.npc_col_pos] = 97
            self.npc_hp += randrange(0,50)
        if self.grid_list[self.n_row][self.n_col] == 1:
            self.grid_list[self.npc_row_pos][self.npc_col_pos] = 97
            self.player_hp -= randrange(0,50)
            self.npc_hp += randrange(0,50)
            if self.player_hp <= 0:
                self.write_game_lost_instance()
    def chase_player(self):
        self.npc_status = 'chasing'
        self.n_row = self.npc_row_pos + self.dx_step
        self.n_col = self.npc_col_pos + self.dy_step
        self.npc_a_row_dx = self.dx_step
        self.npc_a_col_dy = self.dy_step
        if self.grid_list[self.n_row][self.n_col] == 0:
            self.grid_list[self.npc_row_pos][self.npc_col_pos] = 0
            self.npc_row_pos = self.n_row
            self.npc_col_pos = self.n_col
            self.grid_list[self.npc_row_pos][self.npc_col_pos] = 97
        if self.grid_list[self.n_row][self.n_col] == 100:
            self.grid_list[self.npc_row_pos][self.npc_col_pos] = 0
            self.npc_row_pos = self.n_row
            self.npc_col_pos = self.n_col
            self.grid_list[self.npc_row_pos][self.npc_col_pos] = 97
            self.npc_hp += randrange(0,50)
        if self.grid_list[self.n_row][self.n_col] == 1:
            self.grid_list[self.npc_row_pos][self.npc_col_pos] = 97
            self.player_hp -= randrange(0,50)
            self.npc_hp += randrange(0,50)
            if self.player_hp <= 0:
                self.write_game_lost_instance()


class Drawing_NPC_B_Method:
    def draw_npc_b_frame(self, rect_left, rect_top):
        if self.npc_b_status == 'roaming':
            if self.npc_b_row_dx == -1 and self.npc_b_col_dy == 0:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.npc_b_up_image_source)
            elif self.npc_b_row_dx == 1 and self.npc_b_col_dy == 0:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.npc_b_down_image_source)
            elif self.npc_b_row_dx == 0 and self.npc_b_col_dy == -1:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.npc_b_left_image_source)
            elif self.npc_b_row_dx == 0 and self.npc_b_col_dy == 1:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.npc_b_right_image_source)
            else:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.npc_b_down_image_source)
        if self.npc_b_status == 'chasing':
            if self.npc_b_row_dx == -1 and self.npc_b_col_dy == 0:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.aggro_npc_b_up_image_source)
            elif self.npc_b_row_dx == 1 and self.npc_b_col_dy == 0:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.aggro_npc_b_down_image_source)
            elif self.npc_b_row_dx == 0 and self.npc_b_col_dy == -1:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.aggro_npc_b_left_image_source)
            elif self.npc_b_row_dx == 0 and self.npc_b_col_dy == 1:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.aggro_npc_b_right_image_source)
            else:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.aggro_npc_b_down_image_source)
    def draw_npc_b_stat(self):
        if self.npc_b_hp >= 1:
            for i in range(int(self.npc_b_hp/10)):
                self.tk_frame.create_image(40*self.npc_b_col_pos+i*5, 60+(40*self.npc_b_row_pos),
                                           image=self.life_bar_icon_image_source)
class NPC_B_Method:
    npc_b_hp = 100
    npc_b_row_pos = 7
    npc_b_col_pos = 7
    npc_b_row_dist = 0
    npc_b_col_dist = 0
    b_dx_step = 0
    b_dy_step = 0
    b_n_row = 6
    b_n_col = 6
    npc_b_row_dx = 0
    npc_b_col_dy = 0
    npc_b_status = 'idle'
    def move_npc_b(self):
        if self.npc_b_hp >= 1:
            self.npc_b_row_dist = self.player_row_pos - self.npc_b_row_pos
            self.npc_b_col_dist = self.player_col_pos - self.npc_b_col_pos
            if self.npc_b_col_dist <= 4 and self.npc_b_row_dist <= 4 and  self.npc_b_row_dist != 0 and self.game_clock == 2:
                self.b_dx_step = int(self.npc_b_row_dist/abs(self.npc_b_row_dist))
                self.b_chase_player()
            if self.npc_b_col_dist <= 4 and self.npc_b_row_dist <= 4 and self.npc_b_col_dist != 0 and  self.game_clock == 7:
                self.b_dy_step = int(self.npc_b_col_dist/abs(self.npc_b_col_dist))
                self.b_chase_player()
            elif self.game_clock == 3:
                self.b_roam_random()
            else:
                pass
        else:
            if self.grid_list[self.npc_b_row_pos][self.npc_b_col_pos] == 2:
                self.grid_list[self.npc_b_row_pos][self.npc_b_col_pos] = 0
    def b_roam_random(self):
        self.npc_b_status = 'roaming'
        (b_dx, b_dy) = choice([(0,1),(0,-1),(1,0),(-1,0)])
        self.npc_b_row_dx = b_dx
        self.npc_b_col_dy = b_dy
        self.b_n_row = self.npc_b_row_pos + b_dx
        self.b_n_col = self.npc_b_col_pos + b_dy
        if self.grid_list[self.b_n_row][self.b_n_col] == 0:
            self.grid_list[self.npc_b_row_pos][self.npc_b_col_pos] = 0
            self.npc_b_row_pos = self.b_n_row
            self.npc_b_col_pos = self.b_n_col
            self.grid_list[self.npc_b_row_pos][self.npc_b_col_pos] = 96
        if self.grid_list[self.b_n_row][self.b_n_col] == 100:
            self.grid_list[self.npc_b_row_pos][self.npc_b_col_pos] = 0
            self.npc_b_row_pos = self.b_n_row
            self.npc_b_col_pos = self.b_n_col
            self.grid_list[self.npc_b_row_pos][self.npc_b_col_pos] = 96
            self.npc_b_hp += randrange(0,50)
        if self.grid_list[self.b_n_row][self.b_n_col] == 1:
            self.grid_list[self.npc_b_row_pos][self.npc_b_col_pos] = 96
            self.player_hp -= randrange(0,50)
            self.npc_b_hp += randrange(0,50)
            if self.player_hp <= 0:
                self.write_game_lost_instance()
    def b_chase_player(self):
        self.npc_b_status = 'chasing'
        self.b_n_row = self.npc_b_row_pos + self.b_dx_step
        self.b_n_col = self.npc_b_col_pos + self.b_dy_step
        self.npc_b_row_dx = self.b_dx_step
        self.npc_b_col_dy = self.b_dy_step
        if self.grid_list[self.b_n_row][self.b_n_col] == 0:
            self.grid_list[self.npc_b_row_pos][self.npc_b_col_pos] = 0
            self.npc_b_row_pos = self.b_n_row
            self.npc_b_col_pos = self.b_n_col
            self.grid_list[self.npc_b_row_pos][self.npc_b_col_pos] = 96 
        if self.grid_list[self.b_n_row][self.b_n_col] == 100:
            self.grid_list[self.npc_b_row_pos][self.npc_b_col_pos] = 0
            self.npc_b_row_pos = self.b_n_row
            self.npc_b_col_pos = self.b_n_col
            self.grid_list[self.npc_b_row_pos][self.npc_b_col_pos] = 96
            self.npc_b_hp += randrange(0,50)
        if self.grid_list[self.b_n_row][self.b_n_col] == 1:
            self.grid_list[self.npc_b_row_pos][self.npc_b_col_pos] = 96
            self.player_hp -= randrange(0,50)
            self.npc_b_hp += randrange(0,50)
            if self.player_hp <= 0:
                self.write_game_lost_instance()


class Drawing_NPC_C_Method:
    def draw_npc_c_frame(self, rect_left, rect_top):
        if self.npc_c_status == 'roaming':
            if self.npc_c_row_dx == -1 and self.npc_c_col_dy == 0:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.shroom_bot_up_image_source)
            elif self.npc_c_row_dx == 1 and self.npc_c_col_dy == 0:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.shroom_bot_down_image_source)
            elif self.npc_c_row_dx == 0 and self.npc_c_col_dy == -1:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.shroom_bot_left_image_source)
            elif self.npc_c_row_dx == 0 and self.npc_c_col_dy == 1:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.shroom_bot_right_image_source)
            else:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.shroom_bot_down_image_source)
        if self.npc_c_status == 'chasing':
            if self.npc_c_row_dx == -1 and self.npc_c_col_dy == 0:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.shroom_bot_up_image_source)
            elif self.npc_c_row_dx == 1 and self.npc_c_col_dy == 0:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.aggro_shroom_bot_down_image_source)
            elif self.npc_c_row_dx == 0 and self.npc_c_col_dy == -1:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.aggro_shroom_bot_left_image_source)
            elif self.npc_c_row_dx == 0 and self.npc_c_col_dy == 1:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.aggro_shroom_bot_right_image_source)
            else:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.aggro_shroom_bot_down_image_source)
    def draw_npc_c_stat(self):
        if self.npc_c_hp >= 1:
            for i in range(int(self.npc_c_hp/10)):
                self.tk_frame.create_image(40*self.npc_c_col_pos+i*5, 60+(40*self.npc_c_row_pos),
                                           image=self.life_bar_icon_image_source)
class NPC_C_Method:
    npc_c_hp = 100
    npc_c_row_pos = 7
    npc_c_col_pos = 7
    npc_c_row_dist = 0
    npc_c_col_dist = 0
    c_dx_step = 0
    c_dy_step = 0
    c_n_row = 6
    c_n_col = 6
    npc_c_row_dx = 0
    npc_c_col_dy = 0
    npc_c_status = 'idle'
    def move_npc_c(self):
        if self.npc_c_hp >= 1:
            self.npc_c_row_dist = self.player_row_pos - self.npc_c_row_pos
            self.npc_c_col_dist = self.player_col_pos - self.npc_c_col_pos
            if self.npc_c_col_dist <= 4 and self.npc_c_row_dist <= 4 and  self.npc_c_row_dist != 0 and self.game_clock == 2:
                self.c_dx_step = int(self.npc_c_row_dist/abs(self.npc_c_row_dist))
                self.c_chase_player()
            if self.npc_c_col_dist <= 4 and self.npc_c_row_dist <= 4 and self.npc_c_col_dist != 0 and  self.game_clock == 7:
                self.c_dy_step = int(self.npc_c_col_dist/abs(self.npc_c_col_dist))
                self.c_chase_player()
            elif self.game_clock == 3:
                self.c_roam_random()
            else:
                pass
        else:
            if self.grid_list[self.npc_c_row_pos][self.npc_c_col_pos] == 2:
                self.grid_list[self.npc_c_row_pos][self.npc_c_col_pos] = 0
    def c_roam_random(self):
        self.npc_c_status = 'roaming'
        (c_dx, c_dy) = choice([(0,1),(0,-1),(1,0),(-1,0)])
        self.npc_c_row_dx = c_dx
        self.npc_c_col_dy = c_dy
        self.c_n_row = self.npc_c_row_pos + c_dx
        self.c_n_col = self.npc_c_col_pos + c_dy
        if self.grid_list[self.c_n_row][self.c_n_col] == 0:
            self.grid_list[self.npc_c_row_pos][self.npc_c_col_pos] = 0
            self.npc_c_row_pos = self.c_n_row
            self.npc_c_col_pos = self.c_n_col
            self.grid_list[self.npc_c_row_pos][self.npc_c_col_pos] = 94
        if self.grid_list[self.c_n_row][self.c_n_col] == 100:
            self.grid_list[self.npc_c_row_pos][self.npc_c_col_pos] = 0
            self.npc_c_row_pos = self.c_n_row
            self.npc_c_col_pos = self.c_n_col
            self.grid_list[self.npc_c_row_pos][self.npc_c_col_pos] = 94
            self.npc_c_hp += randrange(0,50)
        if self.grid_list[self.c_n_row][self.c_n_col] == 1:
            self.grid_list[self.npc_c_row_pos][self.npc_c_col_pos] = 94
            self.player_hp -= randrange(0,50)
            self.npc_c_hp += randrange(0,50)
            if self.player_hp <= 0:
                self.write_game_lost_instance()
    def c_chase_player(self):
        self.npc_c_status = 'chasing'
        self.c_n_row = self.npc_c_row_pos + self.c_dx_step
        self.c_n_col = self.npc_c_col_pos + self.c_dy_step
        self.npc_c_row_dx = self.c_dx_step
        self.npc_c_col_dy = self.c_dy_step
        if self.grid_list[self.c_n_row][self.c_n_col] == 0:
            self.grid_list[self.npc_c_row_pos][self.npc_c_col_pos] = 0
            self.npc_c_row_pos = self.c_n_row
            self.npc_c_col_pos = self.c_n_col
            self.grid_list[self.npc_c_row_pos][self.npc_c_col_pos] = 94 
        if self.grid_list[self.c_n_row][self.c_n_col] == 100:
            self.grid_list[self.npc_c_row_pos][self.npc_c_col_pos] = 0
            self.npc_c_row_pos = self.c_n_row
            self.npc_c_col_pos = self.c_n_col
            self.grid_list[self.npc_c_row_pos][self.npc_c_col_pos] = 94
            self.npc_c_hp += randrange(0,50)
        if self.grid_list[self.c_n_row][self.c_n_col] == 1:
            self.grid_list[self.npc_c_row_pos][self.npc_c_col_pos] = 94
            self.player_hp -= randrange(0,50)
            self.npc_c_hp += randrange(0,50)
            if self.player_hp <= 0:
                self.write_game_lost_instance()


class Drawing_NPC_D_Method:
    def draw_npc_d_frame(self, rect_left, rect_top):
        if self.npc_d_status == 'roaming':
            if self.npc_d_row_dx == -1 and self.npc_d_col_dy == 0:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.npc_d_up_image_source)
            elif self.npc_d_row_dx == 1 and self.npc_d_col_dy == 0:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.npc_d_down_image_source)
            elif self.npc_d_row_dx == 0 and self.npc_d_col_dy == -1:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.npc_d_left_image_source)
            elif self.npc_d_row_dx == 0 and self.npc_d_col_dy == 1:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.npc_d_right_image_source)
            else:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.npc_d_down_image_source)
        if self.npc_d_status == 'chasing':
            if self.npc_d_row_dx == -1 and self.npc_d_col_dy == 0:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.aggro_npc_d_up_image_source)
            elif self.npc_d_row_dx == 1 and self.npc_d_col_dy == 0:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.aggro_npc_d_down_image_source)
            elif self.npc_d_row_dx == 0 and self.npc_d_col_dy == -1:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.aggro_npc_d_left_image_source)
            elif self.npc_d_row_dx == 0 and self.npc_d_col_dy == 1:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.aggro_npc_d_right_image_source)
            else:
                self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.aggro_npc_d_down_image_source)
    def draw_npc_d_stat(self):
        if self.npc_d_hp >= 1:
            for i in range(int(self.npc_d_hp/10)):
                self.tk_frame.create_image(40*self.npc_d_col_pos+i*5, 60+(40*self.npc_d_row_pos),
                                           image=self.life_bar_icon_image_source)
class NPC_D_Method():
    npc_d_hp = 100
    npc_d_row_pos = 7
    npc_d_col_pos = 7
    npc_d_row_dist = 0
    npc_d_col_dist = 0
    d_dx_step = 0
    d_dy_step = 0
    d_n_row = 6
    d_n_col = 6
    npc_d_row_dx = 0
    npc_d_col_dy = 0
    npc_d_status = 'idle'
    def move_npc_d(self):
        if self.npc_d_hp >= 1:
            self.npc_d_row_dist = self.player_row_pos - self.npc_d_row_pos
            self.npc_d_col_dist = self.player_col_pos - self.npc_d_col_pos
            if self.npc_d_col_dist <= 4 and self.npc_d_row_dist <= 4 and  self.npc_d_row_dist != 0 and self.game_clock == 2:
                self.d_dx_step = int(self.npc_d_row_dist/abs(self.npc_d_row_dist))
                self.d_chase_player()
            if self.npc_d_col_dist <= 4 and self.npc_d_row_dist <= 4 and self.npc_d_col_dist != 0 and  self.game_clock == 7:
                self.d_dy_step = int(self.npc_d_col_dist/abs(self.npc_d_col_dist))
                self.d_chase_player()
            elif self.game_clock == 3:
                self.d_roam_random()
            else:
                pass
        else:
            if self.grid_list[self.npc_d_row_pos][self.npc_d_col_pos] == 2:
                self.grid_list[self.npc_d_row_pos][self.npc_d_col_pos] = 0
    def d_roam_random(self):
        self.npc_d_status = 'roaming'
        (d_dx, d_dy) = choice([(0,1),(0,-1),(1,0),(-1,0)])
        self.npc_d_row_dx = d_dx
        self.npc_d_col_dy = d_dy
        self.d_n_row = self.npc_d_row_pos + d_dx
        self.d_n_col = self.npc_d_col_pos + d_dy
        if self.grid_list[self.d_n_row][self.d_n_col] == 0:
            self.grid_list[self.npc_d_row_pos][self.npc_d_col_pos] = 0
            self.npc_d_row_pos = self.d_n_row
            self.npc_d_col_pos = self.d_n_col
            self.grid_list[self.npc_d_row_pos][self.npc_d_col_pos] = 95
        if self.grid_list[self.d_n_row][self.d_n_col] == 100:
            self.grid_list[self.npc_d_row_pos][self.npc_d_col_pos] = 0
            self.npc_d_row_pos = self.d_n_row
            self.npc_d_col_pos = self.d_n_col
            self.grid_list[self.npc_d_row_pos][self.npc_d_col_pos] = 95
            self.npc_d_hp -= randrange(0,50)
        if self.grid_list[self.d_n_row][self.d_n_col] == 1:
            self.grid_list[self.npc_d_row_pos][self.npc_d_col_pos] = 95
            self.player_hp -= randrange(0,50)
            self.npc_d_hp += randrange(0,50)
            if self.player_hp <= 0:
                self.write_game_lost_instance()
    def d_chase_player(self):
        self.npc_d_status = 'chasing'
        self.d_n_row = self.npc_d_row_pos + self.d_dx_step
        self.d_n_col = self.npc_d_col_pos + self.d_dy_step
        self.npc_d_row_dx = self.d_dx_step
        self.npc_d_col_dy = self.d_dy_step
        if self.grid_list[self.d_n_row][self.d_n_col] == 0:
            self.grid_list[self.npc_d_row_pos][self.npc_d_col_pos] = 0
            self.npc_d_row_pos = self.d_n_row
            self.npc_d_col_pos = self.d_n_col
            self.grid_list[self.npc_d_row_pos][self.npc_d_col_pos] = 95
        if self.grid_list[self.d_n_row][self.d_n_col] == 100:
            self.grid_list[self.npc_d_row_pos][self.npc_d_col_pos] = 0
            self.npc_d_row_pos = self.d_n_row
            self.npc_d_col_pos = self.d_n_col
            self.grid_list[self.npc_d_row_pos][self.npc_d_col_pos] = 95
            self.npc_d_hp -= randrange(0,50)
        if self.grid_list[self.d_n_row][self.d_n_col] == 1:
            self.grid_list[self.npc_d_row_pos][self.npc_d_col_pos] = 95
            self.player_hp -= randrange(0,50)
            self.npc_d_hp += randrange(0,50)
            if self.player_hp <= 0:
                self.write_game_lost_instance()

class Game_Init(tk.Tk, Instance_Planner, Drawing_NPC_Method, Drawing_NPC_B_Method, 
                Drawing_NPC_D_Method, Drawing_Player_Method, Ability_Player_Method, 
                NPC_Method, NPC_B_Method, NPC_D_Method, Player_Method, Animation_Method, 
                Drawing_World_Method, Drawing_Method, Game_Images, Drawing_NPC_C_Method, NPC_C_Method):
    game_delay = 71 
    game_clock = 0 
    object_size = 40
    board_size = 16
    message_log_size = 100
    frame_width = 2*5 + board_size * object_size 
    frame_height = 2*5 + board_size * object_size + message_log_size
    def __init__(self):
        super().__init__()
        self.bind("<Key>", self.key_pressed) 
        self.tk_frame = tk.Canvas(self, width=self.frame_width, height=self.frame_height) 
        self.tk_frame.pack()
        self.pull_images()
        self.write_ui_instance()
        self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_id()))
init_grid = Game_Init()
init_grid.mainloop() # APACHE Licenced Ruf's Towers of Atlantis game 1111 lines, Saturday 12:00 AM October/13th/2018