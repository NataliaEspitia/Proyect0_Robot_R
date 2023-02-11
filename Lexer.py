from ply.lex import lexer 

def read(file):
    X = open(file)
    filestring= (X.read()).lower
    return filestring


tokens = {
    "robot_r": "robot_r",
    "vars": "vars",
    "procs" : "procs",
    "[": "[",
    "]": "]",
    ";" : ";",
    "|" : "|",
    #commands
    "assignto": "assignto",
    "goto": "goto",
    "move": "move",
    "turn": "turn",
    "face": "face",
    "put" : "put",
    "pick" :"pick",
    "movetothe" :"movetothe",
    "moveindir": "moveindir",
    "jumptothe":"jumptothe",
    "jumpindir":"jumpindir",
    "nop":"nop",
    #conditional
    "if" : "if",  
    "while" : "while",
    "repeat" : "repeat"
}


def lexer(strx):
    





















































































































