import sys
import re
import copy
# Please implement this function according to Section "Read Configuration File"
def load_config_file(filepath):
	# It should return width, height, waters, woods, foods, golds based on the file
	# Complete the test driver of this function in file_loading_test.py
	f = open(filepath,'r')
	#format error
	ln_ls = [x.rstrip('\n') for x in f.readlines()]
	# ln_ls = [x for x in f.readlines()]
	k = True
	if len(ln_ls) !=5:
		k = False
	elif ln_ls[0].startswith("Frame: ") == False:
		k = False
	elif ln_ls[1].startswith("Water: ") == False:
		k = False
	elif ln_ls[2].startswith("Wood: ") == False:
		k = False
	elif ln_ls[3].startswith("Food: ") == False:
		k = False
	elif ln_ls[4].startswith("Gold: ") == False:
		k = False
	if k == False:
		f.close()
		raise SyntaxError('Invalid Configuration File: format error!')
	#frame format error
	frame_value = ln_ls[0].lstrip('Frame: ')
	if len(ln_ls[0]) != 10:
		f.close()
		raise SyntaxError("Invalid Configuration File: frame should be in format widthxheight!")
	find_x = frame_value.find("x")  
	if find_x < 0:
		f.close()
		raise SyntaxError("Invalid Configuration File: frame should be in format widthxheight!")
	frame_format = frame_value.rsplit("x")  
	if len(frame_format) !=2:
		f.close()
		raise SyntaxError("Invalid Configuration File: frame should be in format widthxheight!")
	elif frame_format[0].isnumeric() == False or frame_format[1].isnumeric() == False:
		f.close()
		raise SyntaxError("Invalid Configuration File: frame should be in format widthxheight!")
	#frame out of range error
	if not re.match("[5-7]x[5-7]", frame_value):
		f.close()
		raise ArithmeticError("Invalid Configuration File: width and height should range from 5 to 7!")
	width = frame_value.rsplit("x")[0]
	height = frame_value.rsplit("x")[1]
	all_coordinate_ls = []
	#contains non-integer characters
	for i in range(1,5):
		ln_value = (ln_ls[i].rsplit(": ")[1])
		ln_name = (ln_ls[i].rsplit(": ")[0])
		s = ln_value.split()
		for i in s:
			if not i.isnumeric():
				f.close()
				raise ValueError("Invalid Configuration File: {} contains non integer characters!".format(ln_name))
	#contains odd number of elements  
		if len(s) % 2 !=0:
			f.close()
			raise SyntaxError("Invalid Configuration File: {} contains an odd number of elements!".format(ln_name))
	# contains a position out of map  
		coordinate_ls = [(int(s[i]),int(s[i+1])) for i in range(0,len(s),2)]
		for i in coordinate_ls:
			if int(i[0])>=int(width) or int(i[1])>=int(height):
				f.close()
				raise ArithmeticError("Invalid Configuration File: {} contains a position that is out of map.".format(ln_name))
		coordinate_ls = [(int(s[i]),int(s[i+1])) for i in range(0,len(s),2)]
		for i in coordinate_ls:
			if i == (1,1) or i == (int(width)-2,int(height)-2):
				f.close()
	#position of home base      
				raise ValueError("Invalid Configuration File: The positions of home bases or the positions next to the home bases are occupied!")
			if i == (1,0) or i == (0,1) or i == (1,2) or i == (2,1) or i == (int(width)-1,int(height)-2) or i == (int(width)-2,int(height)-1) or i == (int(width)-3,int(height)-2) or i == (int(width)-2,int(height)-3):
	#position of next to home base
				f.close()
				raise ValueError("Invalid Configuration File: The positions of home bases or the positions next to the home bases are occupied!")
			if coordinate_ls.count(i) > 1:
				f.close()
	#duplicate positions one line
				raise SyntaxError("Invalid Confiuration File: Duplicate positions {}!".format(i))
			all_coordinate_ls.append(i)
	#duplicate positions multi line   
	for i in all_coordinate_ls:
		if all_coordinate_ls.count(i) > 1:
			f.close()
			raise SyntaxError("Invalid Confiuration File: Duplicate positions {}!".format(i))
	water_str_ls = ln_ls[1].rsplit(": ")[1].split()
	wood_str_ls = ln_ls[2].rsplit(": ")[1].split()
	food_str_ls = ln_ls[3].rsplit(": ")[1].split()
	gold_str_ls = ln_ls[4].rsplit(": ")[1].split()
	#load values into the factors
	width = int(width)
	height = int(height)
	waters = [(int(water_str_ls[i]),int(water_str_ls[i+1])) for i in range(0,len(water_str_ls),2)]
	woods = [(int(wood_str_ls[i]),int(wood_str_ls[i+1])) for i in range(0,len(wood_str_ls),2)]
	foods = [(int(food_str_ls[i]),int(food_str_ls[i+1])) for i in range(0,len(food_str_ls),2)]
	golds = [(int(gold_str_ls[i]),int(gold_str_ls[i+1])) for i in range(0,len(gold_str_ls),2)]
	f.close()
	return width, height, waters, woods, foods, golds

recruit_prices = "Recruit Prices:\n  Spearman (S) - 1W, 1F\n  Archer (A) - 1W, 1G\n  Knight (K) - 1F, 1G\n  Scout (T) - 1W, 1F, 1G"	   
class Little_Battle:
	def __init__(self):
		self.board_ls = []
		for i in range(width):
			board = ["  " for i in range(height)]
			self.board_ls.append(board)
		self.res = {
			"Player 1" :[2,2,2], #wood,food,gold
			"Player 2" :[2,2,2]  #wood,food,gold
		}
		self.army = {
			"Player 1" :[['  Spearman:'],['  Archer:'],['  Knight:'],['  Scout:']],
			"Player 2" :[['  Spearman:'],['  Archer:'],['  Knight:'],['  Scout:']]
		}
	pass
	#Print out map
	def print_map(self):
		print("Please check the battlefield, commander.")
		print("  X"+' '.join('%02d'%x for x in range(width))+"X")
		print(" Y+" + "-"*(width*3-1) + "+")
		for y in range(height):
			print('{:02d}'.format(y)+"|", end="")
			for x in range(width):
				print("{}|".format(self.board_ls[x][y]), end = "")
			print()
		print(" Y+" + "-"*(3*width-1) + "+")
		pass
	#Put config data in map	   
	def put_config_in_map(self):
		for w in waters:
			x, y = w[0], w[1]
			self.board_ls[x][y] = '~~'
		for w in woods:
			x, y = w[0], w[1]
			self.board_ls[x][y] = 'WW'
		for f in foods:
			x, y = f[0], f[1]
			self.board_ls[x][y] = 'FF'
		for g in golds:
			x, y = g[0], g[1]
			self.board_ls[x][y] = 'GG'
		self.board_ls[1][1] = 'H1'
		self.board_ls[width-2][height-2] = 'H2'
		print("Configuration file {} was loaded.".format(file_path))
		print("Game Started: Little Battle! (enter QUIT to quit the game)\n")
		game.print_map()
		print("(enter DIS to display the map)\n")
		print(recruit_prices)
		print("(enter PRIS to display the price list)\n")
		pass
	#Player recruit
	def player_recruit(self,player):
		print("-Year {}-\n".format(year))
		print("+++{}'s Stage: Recruit Armies+++\n".format(player))
		print("[Your Asset: Wood - {} Food - {} Gold - {}]".format(self.res[player][0],self.res[player][1],self.res[player][2]))
		#only ask player if resource and space are enough
		enough_resource = True
		enough_space = True
		while enough_resource == True and enough_space == True:
			if (self.res[player][0]==0 and self.res[player][2]==0) or (self.res[player][2]==0 and self.res[player][1]==0) or (self.res[player][1] ==0 and self.res[player][0]==0):
# print("[Your Asset: Wood - {} Food - {} Gold - {}]".format(self.res[player][0],self.res[player][1],self.res[player][2]))
				print("No resources to recruit any armies.")
				enough_resource = False
				break
			elif player == 'Player 1' and (self.board_ls[1][0] != '  ' and self.board_ls[0][1] != '  ' and self.board_ls[1][2] != '  ' and self.board_ls[2][1] != '  '):
				print("No place to recruit new armies.")
				enough_space = False
				break
			elif player == 'Player 2' and (self.board_ls[int(width)-1][int(height)-2] != '  ' and self.board_ls[int(width)-2][int(height)-1] != '  ' and self.board_ls[int(width)-3][int(height)-2] != '  ' and self.board_ls[int(width)-2][int(height)-3] != '  '):
				print("No place to recruit new armies.")
				enough_space = False
				break
#enought resource/space, now recruit input	
			else:
				recruit = input("\nWhich type of army to recruit, (enter) ‘S’, ‘A’, ‘K’, or ‘T’? Enter ‘NO’ to end this stage.\n")
				if recruit not in ['S','A','K','T','NO','QUIT','DIS','PRIS']:
					print("Sorry, invalid input. Try again.")
					continue
				elif recruit == 'S' and (self.res[player][0] <1 or self.res[player][1] <1):
					print("Insufficient resources. Try again.")
					continue
				elif recruit == 'A' and (self.res[player][0] <1 or self.res[player][2] <1):
					print("Insufficient resources. Try again.")
					continue
				elif recruit == 'K' and (self.res[player][2] <1 or self.res[player][1] <1):
					print("Insufficient resources. Try again.")
					continue
				elif recruit == 'T' and (self.res[player][0]<1 or self.res[player][1]<1 or self.res[player][2]<1):
					print("Insufficient resources. Try again.")
					continue
				#edge cases	
				elif recruit == 'NO':
					break 
				elif recruit == 'QUIT':
					exit()
				elif recruit == 'DIS':
					game.print_map()
					continue
				elif recruit == 'PRIS':
					print(recruit_prices)
					continue
				#input looks right, now recruit
				if recruit == 'S':
					recruit_name = 'Spearman'
				elif recruit == 'A':
					recruit_name = 'Archer'
				elif recruit == 'K':
					recruit_name = 'Knight'
				elif recruit == 'T':
					recruit_name = 'Scout'
				while True:
					k = input("\nYou want to recruit a {}. Enter two integers as format ‘x y’ to place your army.\n".format(recruit_name)) 
					if k == 'DIS':
						game.print_map()
						continue
					elif k == 'PRIS':
						print(recruit_prices)
						continue
					elif k == 'QUIT':
						exit()
					# check the entered coordinates valid/invalid	
					try:
						a, b = k.split()
						x, y = int(a), int(b)
					except ValueError:
						print("Sorry, invalid input. Try again.")
						continue
					except TypeError:
						print("Sorry, invalid input. Try again.")
						continue
					except IndexError:
						print("Sorry, invalid input. Try again.")
						continue
					if len(k)>3:
						print("Sorry, invalid input. Try again.")
						continue
					# edge cases	
					elif x>=width or y >=height:
						print("You must place your newly recruited unit in an unoccupied position next to your home base. Try again.")
						continue
					if self.board_ls[int(x)][int(y)] != "  ":
						print("You must place your newly recruited unit in an unoccupied position next to your home base. Try again.")
						continue
					elif player == 'Player 1' and (int(x), int(y)) not in [(1,0),(0,1),(2,1),(1,2)]:
						print("You must place your newly recruited unit in an unoccupied position next to your home base. Try again.")
						continue   
					elif player == 'Player 2' and (int(x), int(y)) not in [(int(width)-1,int(height)-2),(int(width)-2,int(height)-1),(int(width)-3,int(height)-2), (int(width)-2,int(height)-3)]:
						print("You must place your newly recruited unit in an unoccupied position next to your home base. Try again.")
						continue
					else:
						#recruit success, reduce resources and put them in player army object
						if recruit == 'S':
							print("\nYou has recruited a Spearman.\n")
							self.res[player][0], self.res[player][1] = self.res[player][0] -1, self.res[player][1] -1
							self.army[player][0].append((x,y))
						elif recruit == 'A':
							print("\nYou has recruited a Archer.\n")
							self.res[player][0], self.res[player][2] = self.res[player][0] -1, self.res[player][2] -1
							self.army[player][1].append((x,y))
						elif recruit == 'K':
							print("\nYou has recruited a Knight.\n")
							self.res[player][1], self.res[player][2] = self.res[player][1] -1, self.res[player][2] -1 
							self.army[player][2].append((x,y))
						elif recruit == 'T':
							print("\nYou has recruited a Scout.\n")
							self.res[player][0], self.res[player][1], self.res[player][2] = self.res[player][0] -1, self.res[player][1] -1, self.res[player][2] -1  
							self.army[player][3].append((x,y))                 
						print("[Your Asset: Wood - {} Food - {} Gold - {}]".format(self.res[player][0],self.res[player][1],self.res[player][2]))
						break
				self.board_ls[int(x)][int(y)] = recruit+player.lstrip("Player ")
			continue
	# print army from a local list in move_army
	def print_local_army(self,local_army_ls):
		# print()
		print("Armies to Move:")
		for i in range(4):
			if len(local_army_ls[i])>1:
				sub_local_army = [(x,y) for x,y in local_army_ls[i][1:]]
				print(local_army_ls[i][0],', '.join('('+str(x)+', '+str(y)+')' for x,y in sub_local_army))
		print()
		pass
	def move_army(self,player):
		print("\n==={}'s Stage: Move Armies===".format(player))
		#copies the army object into a local list so that we can modify elements within this step without affecting object.
		#local army list will be refreshed every turn by parsing army object
		local_army_ls = copy.deepcopy(self.army[player])
		#check if there's army to move
		while True:
			has_army = False
			for i in range(4):
				if len(local_army_ls[i])>1:
					has_army = True
			if not has_army:
				print()
				print("No Army to Move: next turn.\n")
				break
			else:
				# have army, check input cases
				print()
				game.print_local_army(local_army_ls)
				move = input("Enter four integers as a format ‘x0 y0 x1 y1’ to represent move unit from (x0, y0) to (x1, y1) or ‘NO’ to end this turn.\n")
				if move == 'QUIT':
					exit()
				elif move == 'NO':
					print()
					break
				elif move == 'DIS':
					game.print_map()
					# print()
					continue
				elif move == 'PRIS':
					print(recruit_prices)
					continue	
				# check on input coordinates	
				try:#check input length/type/value
					move_ls = [int(x.strip()) for x in move.split(" ") if x.strip()]
					move_ls_tup = [(move_ls[k],move_ls[k+1]) for k in range(0,len(move_ls),2)]
				except IndexError:
					print("Invalid move. Try again.")
					continue
				except ValueError:
					print("Invalid move. Try again.")
					continue
				if len(move_ls) != 4 or len(move) != 7:
					print("Invalid move. Try again.")
					continue
				#check if start is unmoved army
				local_army_sub_ls = [local_army_ls[i] for i in range(4)]
				in_list = False
				for k in local_army_sub_ls:
					if move_ls_tup[0] in k:
						in_list = True
				if in_list == False:	
					print("Invalid move. Try again.")
					continue
				#check if destination is in map
				elif move_ls[2] not in range(width) or move_ls[3] not in range(height):
					print("Invalid move. Try again.")
					continue
				#check if destination is home base
				elif player == 'Player 1' and move_ls_tup[1] == (1,1):
					print("Invalid move. Try again.")
					continue
				elif player == 'Player 2' and move_ls_tup[1] == (width-2,height-2):
					print("Invalid move. Try again.")
					continue
				#check if destination coordinate in own army
				in_list2 = False
				for k in [self.army[player][i] for i in range(4)]:
					if move_ls_tup[1] in k:
						in_list2 = True
				if in_list2 == True:
					print("Invalid move. Try again.")
					continue
				#check if steps are correct
				one_step_ls = [(move_ls[0]-1,move_ls[1])
								,(move_ls[0]+1,move_ls[1])
								,(move_ls[0],move_ls[1]-1)
								,(move_ls[0],move_ls[1]+1)]
				two_step_ls = [(move_ls[0]-2,move_ls[1])
								,(move_ls[0]+2,move_ls[1])
								,(move_ls[0],move_ls[1]-2)
								,(move_ls[0],move_ls[1]+2)]
				#check if non-scout destination not one step
				if move_ls_tup[0] not in local_army_sub_ls[3] and move_ls_tup[1] not in one_step_ls:
					print("Invalid move. Try again.")
					continue
				#check if scout destination not in one step or two step
				elif move_ls_tup[0] in local_army_sub_ls[3] and move_ls_tup[1] not in (one_step_ls+two_step_ls):
					print("Invalid move. Try again.")
					continue
				else:
					for i in range(4):
						if move_ls_tup[0] in [local_army_ls[i] for i in range(4)][i]:
							print("\nYou have moved {} from {} to {}.".format(local_army_sub_ls[i][0].strip(' :'),move_ls_tup[0],move_ls_tup[1]))
							army_move_from_x, army_move_from_y = move_ls_tup[0][0], move_ls_tup[0][1]
							army_move_to_x, army_move_to_y = move_ls_tup[1][0], move_ls_tup[1][1]
							army_type = local_army_sub_ls[i][0].strip(' :')
							game.move_result(army_move_from_x, army_move_from_y, army_move_to_x, army_move_to_y, army_type)
							[local_army_ls[i] for i in range(4)][i].remove(move_ls_tup[0])
							continue						
		pass
	def move_result(self,army_move_from_x,army_move_from_y,army_move_to_x,army_move_to_y,army_type):
		self.board_ls[army_move_from_x][army_move_from_y] = '  '
		if army_type == 'Spearman':
			game.check_win(army_move_to_x,army_move_to_y,army_type)
			if 'S' in self.board_ls[army_move_to_x][army_move_to_y]:
				print("We destroyed the enemy {} with massive loss!".format(army_type))
				self.board_ls[army_move_to_x][army_move_to_y] = '  '
				game.remove_own_army(army_move_from_x,army_move_from_y)
				game.remove_def_army(army_move_to_x,army_move_to_y)
			elif 'K' in self.board_ls[army_move_to_x][army_move_to_y]:
				print("Great! We defeated the enemy Knight!")
				self.board_ls[army_move_to_x][army_move_to_y] = 'S'+ player.lstrip("Player ")
				game.remove_def_army(army_move_to_x,army_move_to_y) 
				game.remove_own_army(army_move_from_x,army_move_from_y)
				game.update_own_army(army_move_to_x,army_move_to_y,army_type)
			elif 'A' in self.board_ls[army_move_to_x][army_move_to_y] or '~~' in self.board_ls[army_move_to_x][army_move_to_y]:
				print("We lost the army {} due to your command!".format(army_type))
				game.remove_own_army(army_move_from_x,army_move_from_y)
			elif 'T' in self.board_ls[army_move_to_x][army_move_to_y]:
				print("Great! We defeated the enemy Scout!")
				self.board_ls[army_move_to_x][army_move_to_y] = 'S'+ player.lstrip("Player ")
				game.remove_def_army(army_move_to_x,army_move_to_y) 
				game.remove_own_army(army_move_from_x,army_move_from_y)
				game.update_own_army(army_move_to_x,army_move_to_y,army_type)
			elif self.board_ls[army_move_to_x][army_move_to_y] == '  ':
				self.board_ls[army_move_to_x][army_move_to_y] = 'S'+ player.lstrip("Player ")
				game.remove_own_army(army_move_from_x,army_move_from_y)
				game.update_own_army(army_move_to_x,army_move_to_y,army_type)
			else:
				game.collect_resource(army_move_from_x,army_move_from_y,army_move_to_x,army_move_to_y,army_type,'S')
		#archer
		if army_type == 'Archer':
			game.check_win(army_move_to_x,army_move_to_y,army_type)
			if 'A' in self.board_ls[army_move_to_x][army_move_to_y]:
				print("We destroyed the enemy {} with massive loss!".format(army_type))
				self.board_ls[army_move_to_x][army_move_to_y] = '  '
				game.remove_own_army(army_move_from_x,army_move_from_y)
				game.remove_def_army(army_move_to_x,army_move_to_y)
			elif 'S' in self.board_ls[army_move_to_x][army_move_to_y]:
				print("Great! We defeated the enemy Spearman!")
				self.board_ls[army_move_to_x][army_move_to_y] = 'A'+ player.lstrip("Player ")
				game.remove_def_army(army_move_to_x,army_move_to_y) 
				game.remove_own_army(army_move_from_x,army_move_from_y)
				game.update_own_army(army_move_to_x,army_move_to_y,army_type)
			elif 'K' in self.board_ls[army_move_to_x][army_move_to_y] or '~~' in self.board_ls[army_move_to_x][army_move_to_y]:
				print("We lost the army {} due to your command!".format(army_type))
				game.remove_own_army(army_move_from_x,army_move_from_y)
			elif 'T' in self.board_ls[army_move_to_x][army_move_to_y]:
				print("Great! We defeated the enemy Scout!")
				self.board_ls[army_move_to_x][army_move_to_y] = 'A'+ player.lstrip("Player ")
				game.remove_def_army(army_move_to_x,army_move_to_y) 
				game.remove_own_army(army_move_from_x,army_move_from_y)
				game.update_own_army(army_move_to_x,army_move_to_y,army_type)
			elif self.board_ls[army_move_to_x][army_move_to_y] == '  ':
				self.board_ls[army_move_to_x][army_move_to_y] = 'A'+ player.lstrip("Player ")
				game.remove_own_army(army_move_from_x,army_move_from_y)
				game.update_own_army(army_move_to_x,army_move_to_y,army_type)
			game.collect_resource(army_move_from_x,army_move_from_y,army_move_to_x,army_move_to_y,army_type,'A')
		#Knight
		if army_type == 'Knight':
			game.check_win(army_move_to_x,army_move_to_y,army_type)
			if 'K' in self.board_ls[army_move_to_x][army_move_to_y]:
				print("We destroyed the enemy {} with massive loss!".format(army_type))
				self.board_ls[army_move_to_x][army_move_to_y] = '  '
				game.remove_own_army(army_move_from_x,army_move_from_y)
				game.remove_def_army(army_move_to_x,army_move_to_y)
			elif 'A' in self.board_ls[army_move_to_x][army_move_to_y]:
				print("Great! We defeated the enemy Archer!")
				self.board_ls[army_move_to_x][army_move_to_y] = 'K'+ player.lstrip("Player ")
				game.remove_def_army(army_move_to_x,army_move_to_y) 
				game.remove_own_army(army_move_from_x,army_move_from_y)
				game.update_own_army(army_move_to_x,army_move_to_y,army_type) 
			elif 'S' in self.board_ls[army_move_to_x][army_move_to_y] or '~~' in self.board_ls[army_move_to_x][army_move_to_y]:
				print("We lost the army {} due to your command!".format(army_type))
				game.remove_own_army(army_move_from_x,army_move_from_y)
			elif 'T' in self.board_ls[army_move_to_x][army_move_to_y]:
				print("Great! We defeated the enemy Scout!")
				self.board_ls[army_move_to_x][army_move_to_y] = 'K'+ player.lstrip("Player ")
				game.remove_def_army(army_move_to_x,army_move_to_y) 
				game.remove_own_army(army_move_from_x,army_move_from_y)
				game.update_own_army(army_move_to_x,army_move_to_y,army_type)
			elif self.board_ls[army_move_to_x][army_move_to_y] == '  ':
				self.board_ls[army_move_to_x][army_move_to_y] = 'K'+ player.lstrip("Player ")
				game.remove_own_army(army_move_from_x,army_move_from_y)
				game.update_own_army(army_move_to_x,army_move_to_y,army_type)
			game.collect_resource(army_move_from_x,army_move_from_y,army_move_to_x,army_move_to_y,army_type,'K')
		#Scout
		if army_type == 'Scout':
			#if scout moves two steps
			if abs(army_move_to_x-army_move_from_x)>1 or abs(army_move_to_y-army_move_from_y)>1:
				# scout moves two steps on x mid steps
				mid_step_x = int((army_move_to_x+army_move_from_x)/2)
				mid_step_y = int((army_move_to_y+army_move_from_y)/2)
				# if mid step enemy home base: win
				game.check_win(mid_step_x,mid_step_y,army_type)		
				if 'T' in self.board_ls[mid_step_x][mid_step_y] and self.board_ls[mid_step_x][mid_step_y]!='T'+ player.lstrip("Player "):
					print("We destroyed the enemy {} with massive loss!".format(army_type))
					self.board_ls[mid_step_x][mid_step_y] = '  '
					game.remove_own_army(army_move_from_x,army_move_from_y)
					game.remove_def_army(mid_step_x,mid_step_y)
				# if mid step enemy A S K or ~~
				elif (('S' in self.board_ls[mid_step_x][mid_step_y] and self.board_ls[mid_step_x][mid_step_y]!='S'+ player.lstrip("Player "))
					or ('A' in self.board_ls[mid_step_x][mid_step_y] and self.board_ls[mid_step_x][mid_step_y]!='A'+ player.lstrip("Player "))
					or ('K' in self.board_ls[mid_step_x][mid_step_y] and self.board_ls[mid_step_x][mid_step_y]!='K'+ player.lstrip("Player "))
					or ('~~' in self.board_ls[mid_step_x][mid_step_y])):
					print("We lost the army {} due to your command!".format(army_type))
					game.remove_own_army(army_move_from_x,army_move_from_y)
				# if mid step resource
				else:
					game.scout_mid_collect_resource(mid_step_x,mid_step_y)	
					game.check_win(army_move_to_x,army_move_to_y,army_type)
					game.scout_move_check(army_move_from_x, army_move_from_y,army_move_to_x,army_move_to_y,army_type)
					game.collect_resource(army_move_from_x, army_move_from_y,army_move_to_x,army_move_to_y,army_type,'T')
			else:
				game.check_win(army_move_to_x,army_move_to_y,army_type)
				game.scout_move_check(army_move_from_x, army_move_from_y,army_move_to_x,army_move_to_y,army_type)
				game.collect_resource(army_move_from_x, army_move_from_y,army_move_to_x,army_move_to_y,army_type,'T')
		pass
	def remove_def_army(self,x,y):
		if player == 'Player 1':
			for i in range(4):
				if (x,y) in self.army['Player 2'][i]:
					self.army['Player 2'][i].remove((x,y))
		elif player == 'Player 2':
			for i in range(4):
				if (x,y) in self.army['Player 1'][i]:
					self.army['Player 1'][i].remove((x,y))
	pass
	def remove_own_army(self,x,y):
		move_from_tup = (x,y)
		for i in range(4):
			if move_from_tup in [self.army[player][i] for i in range(4)][i]:
				[self.army[player][i] for i in range(4)][i].remove(move_from_tup)
		pass
	def update_own_army(self,x,y,army_type):
		if army_type == 'Spearman':
			self.army[player][0].append((x,y))
		elif army_type == 'Archer':
			self.army[player][1].append((x,y))
		elif army_type == 'Knight':
			self.army[player][2].append((x,y))
		elif army_type == 'Scout':
			self.army[player][3].append((x,y))
		pass 
	def scout_move_check(self,from_x,from_y,to_x,to_y,army_type):
		if 'T' in self.board_ls[to_x][to_y]:
			print("We destroyed the enemy Scout with massive loss!")
			self.board_ls[to_x][to_y] = '  '
			game.remove_own_army(from_x,from_y)
			game.remove_def_army(to_x,to_y)
		elif self.board_ls[to_x][to_y] not in ['  ','WW','FF','GG']:
			print("We lost the army Scout due to your command!")
			game.remove_own_army(from_x,from_y)
		elif self.board_ls[to_x][to_y] == '  ':
			self.board_ls[to_x][to_y] = 'T'+ player.lstrip("Player ")
			game.remove_own_army(from_x,from_y)
			game.update_own_army(to_x,to_y,army_type)
		pass
	def scout_mid_collect_resource(self,x,y):
		if 'WW' in self.board_ls[x][y]:
			print("Good. We collected 2 Wood.")
			self.res[player][0] = self.res[player][0]+2
			self.board_ls[x][y] = '  '
		elif 'FF' in self.board_ls[x][y]:
			print("Good. We collected 2 Food.")
			self.res[player][1] = self.res[player][1]+2
			self.board_ls[x][y] = '  '
		elif 'GG' in self.board_ls[x][y]:
			print("Good. We collected 2 Gold.")
			self.res[player][2] = self.res[player][2]+2
			self.board_ls[x][y] = '  '
		pass
	def collect_resource(self,from_x,from_y,x,y,army_type,army_type_letter):
		if 'WW' in self.board_ls[x][y]:
			print("Good. We collected 2 Wood.")
			self.res[player][0] = self.res[player][0]+2
			self.board_ls[x][y] = army_type_letter+player.lstrip("Player ")
			game.remove_own_army(from_x,from_y)
			game.update_own_army(x,y,army_type)
		elif 'FF' in self.board_ls[x][y]:
			print("Good. We collected 2 Food.")
			self.res[player][1] = self.res[player][1]+2
			self.board_ls[x][y] = army_type_letter+player.lstrip("Player ")
			game.remove_own_army(from_x,from_y)
			game.update_own_army(x,y,army_type)
		elif 'GG' in self.board_ls[x][y]:
			print("Good. We collected 2 Gold.")
			self.res[player][2] = self.res[player][2]+2
			self.board_ls[x][y] = army_type_letter+player.lstrip("Player ")
			game.remove_own_army(from_x,from_y)
			game.update_own_army(x,y,army_type)
		pass
	def check_win(self,x,y,army_type):
		if 'H' in self.board_ls[x][y] and self.board_ls[x][y]!='H'+ player.lstrip("Player "):
			print("The army {} captured the enemy’s capital.\n".format(army_type))
			name = input("What’s your name, commander?\n")
			print("\n***Congratulation! Emperor {} unified the country in {}.***".format(name,year))
			exit()
		pass
if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python3 little_battle.py <filepath>")
		sys.exit()
	file_path = sys.argv[1]
	width, height, waters, woods, foods, golds = load_config_file(file_path)
	game = Little_Battle()
	game.put_config_in_map()
	year = 617
	player = 'Player 1'
	while True:
		game.player_recruit(player)
		game.move_army(player)
		if player == 'Player 1':
			player = 'Player 2'
		else:
			player = 'Player 1'
			year = year + 1

