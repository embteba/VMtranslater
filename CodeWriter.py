import sys

# VMコマンドをHackアセンブリに変換するクラス
class CodeWriter:
        def __init__(self, filename_or_filepath: str):
            # クラス変数定義
            self.filename: str = ""                      # ファイル名またはファイルパス 今はいったんファイル名だけの想定
            self.output_file = open("out.asm", "w")      # 出力ファイル
            self.eqcounter: int = 0                      # eqコマンドのカウンタ
            self.gtcounter: int = 0                      # eqコマンドのカウンタ
            self.ltcounter: int = 0                      # eqコマンドのカウンタ


        # CodeWriterモジュールに新規VMファイルの変換が開始したことを通知する
        def set_file_name(self, new_trans_filename: str) -> None:
            self.filename = new_trans_filename
        
            
        # 算術コマンドをHackアセンブリに変換する
        # C_ARITHMETICのときにのみコールする
        def write_Arithmetic(self, trans_target_vmcommand: str) -> None:
            if trans_target_vmcommand == "add":
                self.output_file.write("// add\n")
                self.output_file.write("@SP\n")
                self.output_file.write("M=M-1\n")
                self.output_file.write("D=M\n")
                self.output_file.write("A=D\n")
                self.output_file.write("D=M\n")
                self.output_file.write("A=A-1\n")
                self.output_file.write("M=D+M\n")
                self.output_file.write("\n")
                
            if trans_target_vmcommand == "sub":
                self.output_file.write("// add\n")
                self.output_file.write("@SP\n")
                self.output_file.write("M=M-1\n")
                self.output_file.write("D=M\n")
                self.output_file.write("A=D\n")
                self.output_file.write("D=M\n")
                self.output_file.write("A=A-1\n")
                self.output_file.write("M=M-D\n")
                self.output_file.write("\n")
                
            if trans_target_vmcommand == "neg":
                self.output_file.write("// neg\n")
                self.output_file.write("@SP\n")
                self.output_file.write("A=M-1\n")
                self.output_file.write("M=-M\n")
                self.output_file.write("\n")
                
            if trans_target_vmcommand == "eq":
                self.output_file.write("// eq\n")
                self.output_file.write("@SP\n")
                self.output_file.write("M=M-1\n")
                self.output_file.write("A=M\n")
                self.output_file.write("D=M\n")
                self.output_file.write("@SP\n")
                self.output_file.write("M=M-1\n")
                self.output_file.write("A=M\n")
                self.output_file.write("D=M-D\n")
                self.output_file.write(f"@EQUAL{self.eqcounter}\n")
                self.output_file.write("D;JEQ\n")
                self.output_file.write("@SP\n")
                self.output_file.write("A=M\n")
                self.output_file.write("M=0\n")
                self.output_file.write(f"@END_EQ{self.eqcounter}\n")
                self.output_file.write("0;JMP\n")
                self.output_file.write(f"(EQUAL{self.eqcounter})\n")
                self.output_file.write("@SP\n")
                self.output_file.write("A=M\n")
                self.output_file.write("M=-1\n")
                self.output_file.write(f"(END_EQ{self.eqcounter})\n")
                self.output_file.write("@SP\n")
                self.output_file.write("M=M+1\n")
                self.output_file.write("\n")
                self.eqcounter += 1
                
            if trans_target_vmcommand == "gt":
                self.output_file.write("// gt\n")
                self.output_file.write("@SP\n")
                self.output_file.write("M=M-1\n")
                self.output_file.write("A=M\n")
                self.output_file.write("D=M\n")
                self.output_file.write("@SP\n")
                self.output_file.write("M=M-1\n")
                self.output_file.write("A=M\n")
                self.output_file.write("D=M-D\n")
                self.output_file.write(f"@GREATER{self.gtcounter}\n")
                self.output_file.write("D;JGT\n")
                self.output_file.write("@SP\n")
                self.output_file.write("A=M\n")
                self.output_file.write("M=0\n")
                self.output_file.write(f"@END_GT{self.gtcounter}\n")
                self.output_file.write("0;JMP\n")
                self.output_file.write(f"(GREATER{self.gtcounter})\n")
                self.output_file.write("@SP\n")
                self.output_file.write("A=M\n")
                self.output_file.write("M=-1\n")
                self.output_file.write(f"(END_GT{self.gtcounter})\n")
                self.output_file.write("@SP\n")
                self.output_file.write("M=M+1\n")
                self.output_file.write("\n")
                self.gtcounter += 1
                
            if trans_target_vmcommand == "lt":
                self.output_file.write("// lt\n")
                self.output_file.write("@SP\n")
                self.output_file.write("M=M-1\n")  
                self.output_file.write("A=M\n")
                self.output_file.write("D=M\n")
                self.output_file.write("@SP\n")
                self.output_file.write("M=M-1\n")  
                self.output_file.write("A=M\n")
                self.output_file.write("D=M-D\n")  
                self.output_file.write(f"@LESS{self.ltcounter}\n")
                self.output_file.write("D;JLT\n")  
                self.output_file.write("@SP\n")
                self.output_file.write("A=M\n")
                self.output_file.write("M=0\n")  
                self.output_file.write(f"@END_LT{self.ltcounter}\n")
                self.output_file.write("0;JMP\n")
                self.output_file.write(f"(LESS{self.ltcounter})\n")
                self.output_file.write("@SP\n")
                self.output_file.write("A=M\n")
                self.output_file.write("M=-1\n")  
                self.output_file.write(f"(END_LT{self.ltcounter})\n")
                self.output_file.write("@SP\n")
                self.output_file.write("M=M+1\n")  
                self.output_file.write("\n")
                self.ltcounter += 1
                
            if trans_target_vmcommand == "and":
                self.output_file.write("// and\n")
                self.output_file.write("@SP\n")
                self.output_file.write("M=M-1\n")
                self.output_file.write("A=M\n")
                self.output_file.write("D=M\n")
                self.output_file.write("A=A-1\n")
                self.output_file.write("D=D&M\n")
                self.output_file.write("M=D\n")
                self.output_file.write("\n")
            
            if trans_target_vmcommand == "or":
                self.output_file.write("// and\n")
                self.output_file.write("@SP\n")
                self.output_file.write("M=M-1\n")
                self.output_file.write("A=M\n")
                self.output_file.write("D=M\n")
                self.output_file.write("A=A-1\n")
                self.output_file.write("M=D|M\n")
                self.output_file.write("\n")
                
            if trans_target_vmcommand == "not":
                self.output_file.write("// and\n")
                self.output_file.write("@SP\n")
                self.output_file.write("M=M-1\n")
                self.output_file.write("A=M\n")
                self.output_file.write("M=!M\n")
                self.output_file.write("\n")
        
       
        # 算術コマンドをHackアセンブリに変換する
        # C_ARITHMETICのときにのみコールする
        def write_PushPop(self, command: str, segment: str, index: int) -> None:
                # PUSHコマンドの変換
                if command == "C_PUSH":
                    if segment == "constant":
                        self.output_file.write(f"// push constant {index}\n")
                        self.output_file.write(f"@{index}\n")
                        self.output_file.write("D=A\n")
                        self.output_file.write("@SP\n")
                        self.output_file.write("A=M\n")
                        self.output_file.write("M=D\n")
                        self.output_file.write("@SP\n")
                        self.output_file.write("M=M+1\n")
                        self.output_file.write("\n")
                        
                # POPコマンドの変換
                elif command == "C_POP":
                    if segment == "temp":
                        if index >= 8: # tempセグメントは0-7まで
                            raise ValueError(print_error("tempセグメントは0-7までのインデックスを指定してください。"))
                        else:                           
                            self.output_file.write(f"// pop temp {index}\n")
                            self.output_file.write("@SP\n")
                            self.output_file.write("M=M-1\n")
                            self.output_file.write("A=M\n")
                            self.output_file.write("D=M\n")
                            self.output_file.write(f"@{index + 5}\n")  
                            self.output_file.write("M=D\n")
                            self.output_file.write("\n")
                    
                    if segment == "local":
                        if index != 0: # localセグメントは0のみ
                            raise ValueError(print_error("localセグメントは0のインデックスを指定してください。"))
                        else:
                            self.output_file.write(f"// pop local {index}\n")
                            self.output_file.write("@SP\n")
                            self.output_file.write("M=M-1\n")
                            self.output_file.write("A=M\n")
                            self.output_file.write("D=M\n")
                            self.output_file.write("@1\n")
                            self.output_file.write("A=M\n")  
                            self.output_file.write("M=D\n")
                            self.output_file.write("\n")    
        
        
        
        
        
        # ファイルクローズメソッド
        def close_output_file(self) -> None:
            self.output_file.close()

        
# エラーメッセージを赤色で表示するメソッド
def print_error(message):
    RED = "\033[91m"
    RESET = "\033[0m"
    sys.stderr.write(f"{RED}{message}{RESET}\n")
            
    
