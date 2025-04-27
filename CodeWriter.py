# VMコマンドをHackアセンブリに変換するクラス
class CodeWriter:
        def __init__(self, filename_or_filepath: str):
            # クラス変数定義
            self.filename: str = ""                      # ファイル名またはファイルパス 今はいったんファイル名だけの想定
            self.output_file = open("out.asm", "w")      # 出力ファイル
            self.stack_pointer: int = 256                # スタックポインタの初期値


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
                self.output_file.write("M=M-1\n")
                self.output_file.write("A=M\n")
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
                self.output_file.write("@EQUAL\n")
                self.output_file.write("D;JEQ\n")
                self.output_file.write("@SP\n")
                self.output_file.write("A=M\n")
                self.output_file.write("M=0\n")
                self.output_file.write("@END_EQ\n")
                self.output_file.write("0;JMP\n")
                self.output_file.write("(EQUAL)\n")
                self.output_file.write("@SP\n")
                self.output_file.write("A=M\n")
                self.output_file.write("M=-1\n")
                self.output_file.write("(END_EQ)\n")
                self.output_file.write("@SP\n")
                self.output_file.write("M=M+1\n")
                self.output_file.write("\n")
        
        
        # 算術コマンドをHackアセンブリに変換する
        # C_ARITHMETICのときにのみコールする
        def write_PushPop(self, command: str, segment: str, index: int) -> None:
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
        
        
        def close_output_file(self) -> None:
            self.output_file.close()
