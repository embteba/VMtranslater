
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
            # 空白行を消す
            filterd_lines = [judged_whitespace_line for judged_whitespace_line in f if judged_whitespace_line.strip()]
            # コメント削除
            self.lines = [judged_commment_line for judged_commment_line in filterd_lines if not judged_commment_line.startswith("//")]
            
        
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
        self.current_command = self.lines[self.current_command_index].strip()
        
    
    
    def command_type(self) -> str:
        # 命令の種類を取得
        if self.current_command.startswith("push"):
            return "C_PUSH"
        elif self.current_command.startswith("pop"):
            return "C_POP"
        elif self.current_command.startswith("add"):
            return "C_ARITHMETIC"
        elif self.current_command.startswith("sub"):
            return "C_ARITHMETIC"
        elif self.current_command.startswith("neg"):
            return "C_ARITHMETIC"
        elif self.current_command.startswith("eq"):
            return "C_ARITHMETIC"
        elif self.current_command.startswith("gt"):
            return "C_ARITHMETIC"
        elif self.current_command.startswith("lt"):
            return "C_ARITHMETIC"
        elif self.current_command.startswith("and"):
            return "C_ARITHMETIC"
        elif self.current_command.startswith("or"):
            return "C_ARITHMETIC"
        elif self.current_command.startswith("not"):
            return "C_ARITHMETIC"
        elif self.current_command.startswith("label"):
            return "C_LABEL"
        elif self.current_command.startswith("goto"):
            return "C_GOTO"
        elif self.current_command.startswith("if-goto"):
            return "C_IF"
        elif self.current_command.startswith("function"):
            return "C_FUNCTION"
        elif self.current_command.startswith("call"):
            return "C_CALL"
        elif self.current_command.startswith("return"): 
            return "C_RETURN"
        else:
            raise ValueError(f"Unknown command: {self.current_command}")
        
        
    # 命令の第一引数を取得    
    # RETURNコマンドの場合はそもそも関数を呼ばない
    def arg1(self) -> str:
        # 算術コマンドの場合はコマンドそのものを返す
        if self.command_type() == "C_ARITHMETIC":
            return self.current_command
        elif self.command_type() == "C_LABEL":
            return self.current_command.split()[1]
        elif self.command_type() == "C_GOTO":
            return self.current_command.split()[1]
        elif self.command_type() == "C_IF":
            return self.current_command.split()[1]
        elif self.command_type() == "C_PUSH":
            return self.current_command.split()[1]
        elif self.command_type() == "C_POP":  
            return self.current_command.split()[1]
        elif self.command_type() == "C_FUNCTION":
            return self.current_command.split()[1]
        elif self.command_type() == "C_CALL":
            return self.current_command.split()[1]
        


