# -*- coding: utf-8 -*-
class Colorin(object):

    format_switch= {
        "bo": "1",# "bo" [1; -> bold
        "di": "2",# "di" [2; -> dim(fino)
        "it": "3",# "it" [3; -> cursiva
        "un": "4",# "un" [4; -> underline(subrayado)
        "bl": "5",# "bl" [5; -> blink(parpadeo)
        "rv": "7",# "rv" [7; -> reverse(invertido)
        "hi": "8",# "hi" [8; -> hidden
        "cr": "9",# "cr" [9; -> tachado
    }

    len_header= []
    header=[]
    rows=[]
    table_res=''

#
# clase Tabla
#
    def __init__(self, header=[]):
        for s in header:
            self.len_header.append(len(str(s)))
        self.header= header

    def add_row(self, cols):
        if len(cols)<len(self.len_header): # menos ele,mentos que header
            for x in range(len(self.len_header)-len(cols)):
                cols.extend([''])

        for i in range(len(cols)):
            if str(cols[i]).find('\x1b')==0:
                siz= len(cols[i][cols[i].find('m')+1:cols[i].find('\x1b[0;0m')])
            else:
                siz= len(str(cols[i]))
            if self.len_header[i] < siz:
                self.len_header[i] = siz
        self.rows.append(cols)


    def _header(self):
        return self.header
    def _rows(self):
        return self.rows
    def _len_header(self):
        return self.len_header

    def separator(self):
        self.table_res+= '\n+'
        for t in self.len_header:
            self.table_res+= '-'*(t+2)+'+'

    def _printTable(self):

        self.separator()
        self.table_res+= '\n| '
        for r in range(len(self.header)):
            esp= self.len_header[r]-len(str(self.header[r]))
            self.table_res+= self._default(self.header[r], 'bo') +' '*esp+' | '

        self.separator()
        for x in range(len(self.rows)):
            self.table_res+= '\n| '
            for i in range(len(self.rows[x])):
                if str(self.rows[x][i]).find('\x1b')==0:
                    siz= len(self.rows[x][i][self.rows[x][i].find('m')+1:self.rows[x][i].find('\x1b[0;0m')])
                    esp= self.len_header[i]-siz
                    self.table_res+= str(self.rows[x][i]) +' '*(esp)+' | '
                else:
                    esp= self.len_header[i]-len(str(self.rows[x][i]))
                    self.table_res+= str(self.rows[x][i]) +' '*(esp)+' | '

        self.separator()
        return self.table_res

#
# clase Colorin
#
    def set_format(self, esc_format, format= False):
        if (format!=False):
            esc_format= esc_format.replace("[0;", "["+self.format_switch[format]+";")
        return esc_format

    neutral= "\x1b[0;0m"

    black= "\x1b[0;30m"
    red= "\x1b[0;31m"
    green= "\x1b[0;32m"
    yellow= "\x1b[0;33m"
    blue= "\x1b[0;34m"
    magenta= "\x1b[0;35m"
    cyan= "\x1b[0;36m"
    lgray= "\x1b[0;37m"
    default= "\x1b[0;39m"

    dgray= "\x1b[0;90m" #dark
    lred= "\x1b[0;91m" #light
    lgreen= "\x1b[0;92m" #light
    lyellow= "\x1b[0;93m" #light
    lblue= "\x1b[0;94m" #light
    lmagenta= "\x1b[0;95m" #light
    lcyan= "\x1b[0;96m" #light
    white= "\x1b[0;97m"

    #Bold + Red forground + Green background "\e[1;31;42m"
    bdefault= "\x1b[0;49m" #backbround
    bblack= "\x1b[0;40m" #backbround
    bred= "\x1b[0;41m" #backbround
    bgreen= "\x1b[0;42m" #backbround
    byellow= "\x1b[0;43m" #backbround
    bblue= "\x1b[0;44m" #backbround
    bmagenta= "\x1b[0;45m" #backbround
    bcyan= "\x1b[0;46m" #backbround
    blgray= "\x1b[0;47m" #backbround light
    bdgray= "\x1b[0;100m" #backbround dark
    blred= "\x1b[0;101m" #backbround light
    blgreen= "\x1b[0;102m" #backbround light
    blyellow= "\x1b[0;103m" #backbround light
    blblue= "\x1b[0;104m" #backbround light
    blmagenta= "\x1b[0;105m" #backbround light
    blcyan= "\x1b[0;106m" #backbround
    bwhite= "\x1b[0;107m" #backbround

    #black
    def _black (self, text, format=False):
        esc_format= self.set_format(self.black, format)
        return (esc_format+ str(text)+ self.neutral)
    #red
    def _red (self, text, format=False):
        esc_format= self.set_format(self.red, format)
        return (esc_format+ str(text)+ self.neutral)
    #green
    def _green (self, text, format=False):
        esc_format= self.set_format(self.green, format)
        return (esc_format+ str(text)+ self.neutral)
    #yellow
    def _yellow (self, text, format=False):
        esc_format= self.set_format(self.yellow, format)
        return (esc_format+ str(text)+ self.neutral)
    #blue
    def _blue (self, text, format=False):
        esc_format= self.set_format(self.blue, format)
        return (esc_format+ str(text)+ self.neutral)
    #purple
    def _magenta (self, text, format=False):
        esc_format= self.set_format(self.magenta, format)
        return (esc_format+ str(text)+ self.neutral)
    #cyan
    def _cyan (self, text, format=False):
        esc_format= self.set_format(self.cyan, format)
        return (esc_format+ str(text)+ self.neutral)
    #lgray
    def _lgray (self, text, format=False):
        esc_format= self.set_format(self.lgray, format)
        return (esc_format+ str(text)+ self.neutral)
    #default
    def _default (self, text, format=False):
        esc_format= self.set_format(self.default, format)
        return (esc_format+ str(text)+ self.neutral)
    #dgray
    def _dgray (self, text, format=False):
        esc_format= self.set_format(self.dgray, format)
        return (esc_format+ str(text)+ self.neutral)
    #lred
    def _lred (self, text, format=False):
        esc_format= self.set_format(self.lred, format)
        return (esc_format+ str(text)+ self.neutral)
    #lgreen
    def _lgreen (self, text, format=False):
        esc_format= self.set_format(self.lgreen, format)
        return (esc_format+ str(text)+ self.neutral)
    #lyellow
    def _lyellow (self, text, format=False):
        esc_format= self.set_format(self.lyellow, format)
        return (esc_format+ str(text)+ self.neutral)
    #lblue
    def _lblue (self, text, format=False):
        esc_format= self.set_format(self.lblue, format)
        return (esc_format+ str(text)+ self.neutral)
    #lmagenta
    def _lmagenta (self, text, format=False):
        esc_format= self.set_format(self.lmagenta, format)
        return (esc_format+ str(text)+ self.neutral)
    #lcyan
    def _lcyan (self, text, format=False):
        esc_format= self.set_format(self.lcyan, format)
        return (esc_format+ str(text)+ self.neutral)
    #white
    def _white (self, text, format=False):
        esc_format= self.set_format(self.white, format)
        return (esc_format+ str(text)+ self.neutral)
