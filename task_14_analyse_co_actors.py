def analyse_co_actors():
	import json
	import pprint
	with open('scrape_movie_cast_details.json','r') as new_file:
		details=json.load(new_file)
	
	list_id=[]
	cast_list=[]
	all_id=[]
	for i in details:
		cast=(i['cast'])
		cast_list.append(cast)
		for j in cast:
			a=j['imdb_id']
			# print(a)
			all_id.append(a)
			if a not in list_id:
				list_id.append(a)
	# print(list_id)
	# print(all_id)

	dict_1={}
	not_repit=[]
	for k_id in list_id:
		# print(k_id)
		not_repit.append(k_id)
		list_sec=[]
		sec_dict={}
		Y=False
		for p_id in all_id:
			# print(p_id)
			if p_id not in not_repit:
				num_movies=0
				dict_frepuent={}
				T=False
				for l in cast_list:
					one_dict_list=[]
					for n in l:
						id_one=n['imdb_id']
						one_dict_list.append(id_one)
						if k_id == id_one:
							name=n['name']
							# print(name)
						if p_id == id_one:
							name_patnar=n['name']
							# print(name_patnar)
					# print(one_dict_list)
					if k_id in one_dict_list:
						if p_id in one_dict_list:
							num_movies=num_movies+1
							T=True
					else:
						break
				# print(num_movies)
				if T == True:
					dict_frepuent={'imdb_id':p_id,'name':name_patnar,'num_movies':num_movies}
					list_sec.append(dict_frepuent)
					Y=True
		if Y == True:
			sec_dict={'name':name,'frequent_co_actors':list_sec}
			pprint.pprint(sec_dict)
			dict_1[k_id]=sec_dict
	# pprint.pprint(dict_1)


analyse_co_actors()








# def analyse_co_actors():
# 	import json
# 	import pprint
# 	with open('scrape_movie_cast_details.json','r') as new_file:
# 		details=json.load(new_file)
	
# 	list_id=[]
# 	cast_list=[]
# 	for i in details:
# 		cast=(i['cast'])
# 		cast_list.append(cast)
# 		for j in cast:
# 			a=j['imdb_id']
# 			# print(a)
# 			if a not in list_id:
# 				list_id.append(a)
# 	# print(list_id)
# 	dict_1={}
# 	not_repit=[]
# 	for k_id in list_id:
# 		# print(k_id)
# 		not_repit.append(k_id)
# 		list_sec=[]
# 		sec_dict={}
# 		Y=False
# 		for p_id in list_id:
# 			# print(p_id)
# 			if p_id not in not_repit:
# 				num_movies=0
# 				if k_id != p_id:
# 					dict_frepuent={}
# 					T=False
# 					for l in cast_list:
# 						one_dict_list=[]
# 						for n in l:
# 							id_one=n['imdb_id']
# 							one_dict_list.append(id_one)
# 							if k_id == id_one:
# 								name=n['name']
# 								# print(name)
# 							if p_id == id_one:
# 								name_patnar=n['name']
# 								# print(name_patnar)
# 						# print(one_dict_list)
# 						if k_id in one_dict_list:
# 							if p_id in one_dict_list:
# 								num_movies=num_movies+1
# 								T=True
# 						else:
# 							break
# 					# print(num_movies)
# 					if T == True:
# 						dict_frepuent={'imdb_id':p_id,'name':name_patnar,'num_movies':num_movies}
# 						list_sec.append(dict_frepuent)
# 						Y=True
# 		if Y == True:
# 			sec_dict={'name':name,'frequent_co_actors':list_sec}
# 			pprint.pprint(sec_dict)
# 			dict_1[k_id]=sec_dict
# 	pprint.pprint(dict_1)


# analyse_co_actors()






