import os
import glob


def main():
#print(os.getcwd())
	ct = 0
	ct1 = 0
	print("1)Rename all files in same pattern\n2)Rename specific files")
	choice = int(input())

	if choice==1:
		print("List of files before renaming are ")
		for filename in os.listdir(os.getcwd()):
			print(filename)
		print("Choose the type of rename style")
		print("Some standard patterns are : \n1)filename00,filename01,...\n2)filename_01,filename_02,...")
		ch = int(input())
		if ch==1:
			print("Enter the filename you want")
			name = input()
			for file in glob.glob('*.txt'):
				ct+=1
				os.rename(file,name+str(ct)+'.txt')
				int(ct)
		else:
			print("Enter the file name ")
			name1 = input()
			for file1 in glob.glob('*.txt'):
				ct1+=1
				os.rename(file1,name1+'_'+str(ct1)+'.txt')
				int(ct1)
		
		
		print("Files after renaming are")
		for file2 in glob.glob('*.txt'):
			print(file2)
		


if __name__ == '__main__':
	main()