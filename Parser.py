
# 各vmファイルのパースを行うクラス
class Parser:
    def __init__(self, filename_or_filepath):
        # クラス変数定義
        self.filename = filename_or_filepath # ファイル名またはファイルパス 今はいったんファイル名だけの想定
        self.lines: list = []                # ファイルの中身
        self.current_command: str = ""       # 現在の命令
        self.current_command_index: int = -1 # 現在の命令のインデックス
         
        # ファイルの読み込み
        with open(filename_or_filepath, 'r') as f:
            self.lines = f.readlines()
            
        
    def has_more_commands(self) -> bool:
        # 次の命令行数目
        next_command_index = self.current_command_index + 1
        
        # 次の命令が存在するかどうか
        if next_command_index >= len(self.lines):
            return False
        else:
            return True
        
    def advance(self) -> None:
        # 次の命令を取得
        self.current_command_index += 1
        self.current_command = self.lines[self.current_command_index]
        


