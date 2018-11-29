# import os
# root_path = os.getcwd()
# offset = len(root_path.split("\\"))
# for root,dirs,files in os.walk(root_path):
# 	current_dir=root
# 	path_list = current_dir.split("\\")
# 	indent_level = len(path_list) - offset
# 	#print("\t"*indent_level,"\\"+path_list[-1])
# 	#print(files)
# 	#os.path.splittext
# 	for f in files:
# 	# 	#print(os.path.splittext(f))
# 		file_name=os.path.splitext(f)[0]
# 		file_path=os.path.join(root,f)
# 		#file_path = root+"\\"+file_name
# 		print(root)
# 		print(root+"\\"+file_name)
# 		print("\t"*(indent_level+1),file_name)
file_path = r'D:\root\dir1\cp3_data_size.c' #源生字符串
# print(file_path)

def line_count(file_path):
 	code_line,blank_line = 0,0
 	with open(file_path,'r') as fp:
 		while True:
 			line = fp.readline()
 			if not line:
 				break
 		
 			code_line += 1
 	print(code_line,"lines")
line_count(file_path)
