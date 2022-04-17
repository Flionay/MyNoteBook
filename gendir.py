from pathlib import Path
import os


class GenerateDir:
    def __init__(self):
        pass

    def gen_sidebar(self):
        '''
            为每个子目录 生成sidebar 写到 sidebar.md 里
        '''

        start_path = os.path.realpath(__file__)
        start_path = Path(start_path).parent
        print(self.get_filelist(start_path))
 



        # 获取当前目录下的所有目录
        # folder_lev1 = os.listdir(start_path)


        # for folder in folder_lev1:
        #     if os.path.isdir(folder) and not folder.startswith(('.','草稿','static')): # 一级目录
        #         print(folder)
                
        #         # for category in os.path.join(start_path,folder):
        #             # 二级目录  先写标题,然后写md文件
        #         cate = os.path.join(start_path,folder)

        #         for md in os.listdir(cate):
        #             if os.path.isdir(folder) and not md.startswith(('.DS','README.md')):
        #                 string = f"[{md[:-3]}]({folder}/{md})"
        #                 print(string)

        #         # break
        #         print("================================")

    def get_filelist(self,dir):
 
        Filelist = []
    
        for home, dirs, files in os.walk(dir):
            # 先循环目录
            print(home)
            # for dir in dirs:
            #     if os.path.isdir(folder) and not folder.startswith(('.','草稿','static')):
            
            # for filename in files:
            #     if filename.endswith('.md') and 'README' not in filename and "sidebar" not in filename:
    
            #     # 文件名列表，包含完整路径
            #         Filelist.append(filename)
        return Filelist



if __name__ == '__main__':
    gen = GenerateDir()
    gen.gen_sidebar()