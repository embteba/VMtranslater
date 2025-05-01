import Parser
import CodeWriter

# 変換対象ファイルの定義
VM_FILE = "StackTest.vm"
# VM_FILE = "debug.vm"

# Parserクラスのインスタンスを作成
parser = Parser.Parser(VM_FILE)

# CodeWriterクラスのインスタンスを作成
codewriter = CodeWriter.CodeWriter(VM_FILE)

# 1行ずつ読み込んで翻訳する
while parser.has_more_commands():    
    #次の行に進む 
    parser.advance()
    # コマンドの種類を取得
    command_type = parser.command_type()
    
    # ローカル変数の初期化
    arg1: str = ""
    arg2: int = -1 
    
    # コマンドの第一引数を取得
    if command_type == "C_RETURN":
       pass
    else:    
        arg1 = parser.arg1()
        
    # コマンドの第二引数を取得
    if(    command_type == "C_PUSH" 
        or command_type == "C_POP" 
        or command_type == "C_FUNCTION" 
        or command_type == "C_CALL"):
        arg2 = parser.arg2()
    
    # コマンドをアセンブリに変換する
    if command_type == "C_ARITHMETIC":
        codewriter.write_Arithmetic(arg1)
    elif command_type == "C_PUSH" or command_type == "C_POP":
        codewriter.write_PushPop(command_type, arg1, arg2)
        
        
# 出力ファイルを閉じる
codewriter.close_output_file()
