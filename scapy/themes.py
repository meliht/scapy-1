from config import conf

##################
## Color themes ##
##################

class Color:
    normal = "\033[0m"
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    purple = "\033[35m"
    cyan = "\033[36m"
    grey = "\033[37m"

    bold = "\033[1m"
    uline = "\033[4m"
    blink = "\033[5m"
    invert = "\033[7m"
        

class ColorTheme:
    def __repr__(self):
        return "<%s>" % self.__class__.__name__
    def __getattr__(self, attr):
        return lambda x:x
        

class NoTheme(ColorTheme):
    pass


class AnsiColorTheme(ColorTheme):
    def __getattr__(self, attr):
        if attr.startswith("__"):
            raise AttributeError(attr)
        s = "style_%s" % attr 
        if s in self.__class__.__dict__:
            before = getattr(self, s)
            after = self.style_normal
        else:
            before = after = ""

        def do_style(val, fmt=None, before=before, after=after):
            if fmt is None:
                if type(val) is not str:
                    val = str(val)
            else:
                val = fmt % val
            return before+val+after
        return do_style
        
        
    style_normal = ""
    style_prompt = ""
    style_punct = ""
    style_id = ""
    style_not_printable = ""
    style_layer_name = ""
    style_field_name = ""
    style_field_value = ""
    style_emph_field_name = ""
    style_emph_field_value = ""
    style_packetlist_name = ""
    style_packetlist_proto = ""
    style_packetlist_value = ""
    style_fail = ""
    style_success = ""
    style_odd = ""
    style_even = ""
    style_opening = ""
    style_active = ""
    style_closed = ""
    style_left = ""
    style_right = ""

class BlackAndWhite(AnsiColorTheme):
    pass

class DefaultTheme(AnsiColorTheme):
    style_normal = Color.normal
    style_prompt = Color.blue+Color.bold
    style_punct = Color.normal
    style_id = Color.blue+Color.bold
    style_not_printable = Color.grey
    style_layer_name = Color.red+Color.bold
    style_field_name = Color.blue
    style_field_value = Color.purple
    style_emph_field_name = Color.blue+Color.uline+Color.bold
    style_emph_field_value = Color.purple+Color.uline+Color.bold
    style_packetlist_name = Color.red+Color.bold
    style_packetlist_proto = Color.blue
    style_packetlist_value = Color.purple
    style_fail = Color.red+Color.bold
    style_success = Color.blue+Color.bold
    style_even = Color.black+Color.bold
    style_odd = Color.black
    style_opening = Color.yellow
    style_active = Color.black
    style_closed = Color.grey
    style_left = Color.blue+Color.invert
    style_right = Color.red+Color.invert
    
class BrightTheme(AnsiColorTheme):
    style_normal = Color.normal
    style_punct = Color.normal
    style_id = Color.yellow+Color.bold
    style_layer_name = Color.red+Color.bold
    style_field_name = Color.yellow+Color.bold
    style_field_value = Color.purple+Color.bold
    style_emph_field_name = Color.yellow+Color.bold
    style_emph_field_value = Color.green+Color.bold
    style_packetlist_name = Color.red+Color.bold
    style_packetlist_proto = Color.yellow+Color.bold
    style_packetlist_value = Color.purple+Color.bold
    style_fail = Color.red+Color.bold
    style_success = Color.blue+Color.bold
    style_even = Color.black+Color.bold
    style_odd = Color.black
    style_left = Color.cyan+Color.invert
    style_right = Color.purple+Color.invert


class RastaTheme(AnsiColorTheme):
    style_normal = Color.normal+Color.green+Color.bold
    style_prompt = Color.yellow+Color.bold
    style_punct = Color.red
    style_id = Color.green+Color.bold
    style_not_printable = Color.green
    style_layer_name = Color.red+Color.bold
    style_field_name = Color.yellow+Color.bold
    style_field_value = Color.green+Color.bold
    style_emph_field_name = Color.green
    style_emph_field_value = Color.green
    style_packetlist_name = Color.red+Color.bold
    style_packetlist_proto = Color.yellow+Color.bold
    style_packetlist_value = Color.green+Color.bold
    style_fail = Color.red
    style_success = Color.red+Color.bold
    style_even = Color.yellow
    style_odd = Color.green
    style_left = Color.yellow+Color.invert
    style_right = Color.red+Color.invert


class FormatTheme(ColorTheme):
    def __getattr__(self, attr):
        if attr.startswith("__"):
            raise AttributeError(attr)
        col = self.__class__.__dict__.get("style_%s" % attr, "%s")
        def do_style(val, fmt=None, col=col):
            if fmt is None:
                if type(val) is not str:
                    val = str(val)
            else:
                val = fmt % val
            return col % val
        return do_style
        

class LatexTheme(FormatTheme):
    style_prompt = r"\textcolor{blue}{%s}"
    style_not_printable = r"\textcolor{gray}{%s}"
    style_layer_name = r"\textcolor{red}{\bf %s}"
    style_field_name = r"\textcolor{blue}{%s}"
    style_field_value = r"\textcolor{purple}{%s}"
    style_emph_field_name = r"\textcolor{blue}{\underline{%s}}" #ul
    style_emph_field_value = r"\textcolor{purple}{\underline{%s}}" #ul
    style_packetlist_name = r"\textcolor{red}{\bf %s}"
    style_packetlist_proto = r"\textcolor{blue}{%s}"
    style_packetlist_value = r"\textcolor{purple}{%s}"
    style_fail = r"\textcolor{red}{\bf %s}"
    style_success = r"\textcolor{blue}{\bf %s}"
    style_left = r"\textcolor{blue}{%s}"
    style_right = r"\textcolor{red}{%s}"
#    style_even = r"}{\bf "
#    style_odd = ""

class LatexTheme2(FormatTheme):
    style_prompt = r"@`@textcolor@[@blue@]@@[@%s@]@"
    style_not_printable = r"@`@textcolor@[@gray@]@@[@%s@]@"
    style_layer_name = r"@`@textcolor@[@red@]@@[@@`@bfseries@[@@]@%s@]@"
    style_field_name = r"@`@textcolor@[@blue@]@@[@%s@]@"
    style_field_value = r"@`@textcolor@[@purple@]@@[@%s@]@"
    style_emph_field_name = r"@`@textcolor@[@blue@]@@[@@`@underline@[@%s@]@@]@" 
    style_emph_field_value = r"@`@textcolor@[@purple@]@@[@@`@underline@[@%s@]@@]@" 
    style_packetlist_name = r"@`@textcolor@[@red@]@@[@@`@bfseries@[@@]@%s@]@"
    style_packetlist_proto = r"@`@textcolor@[@blue@]@@[@%s@]@"
    style_packetlist_value = r"@`@textcolor@[@purple@]@@[@%s@]@"
    style_fail = r"@`@textcolor@[@red@]@@[@@`@bfseries@[@@]@%s@]@"
    style_success = r"@`@textcolor@[@blue@]@@[@@`@bfserices@[@@]@%s@]@"
    style_even = r"@`@textcolor@[@gray@]@@[@@`@bfseries@[@@]@%s@]@"
#    style_odd = r"@`@textcolor@[@black@]@@[@@`@bfseries@[@@]@%s@]@"
    style_left = r"@`@textcolor@[@blue@]@@[@%s@]@"
    style_right = r"@`@textcolor@[@red@]@@[@%s@]@"

class HTMLTheme(FormatTheme):
    style_prompt = "<span class=prompt>%s</span>"
    style_not_printable = "<span class=not_printable>%s</span>"
    style_layer_name = "<span class=layer_name>%s</span>"
    style_field_name = "<span class=field_name>%s</span>"
    style_field_value = "<span class=field_value>%s</span>"
    style_emph_field_name = "<span class=emph_field_name>%s</span>"
    style_emph_field_value = "<span class=emph_field_value>%s</span>"
    style_packetlist_name = "<span class=packetlist_name>%s</span>"
    style_packetlist_proto = "<span class=packetlist_proto>%s</span>"
    style_packetlist_value = "<span class=packetlist_value>%s</span>"
    style_fail = "<span class=fail>%s</span>"
    style_success = "<span class=success>%s</span>"
    style_even = "<span class=even>%s</span>"
    style_odd = "<span class=odd>%s</span>"
    style_left = "<span class=left>%s</span>"
    style_right = "<span class=right>%s</span>"

class HTMLTheme2(HTMLTheme):
    style_prompt = "#[#span class=prompt#]#%s#[#/span#]#"
    style_not_printable = "#[#span class=not_printable#]#%s#[#/span#]#"
    style_layer_name = "#[#span class=layer_name#]#%s#[#/span#]#"
    style_field_name = "#[#span class=field_name#]#%s#[#/span#]#"
    style_field_value = "#[#span class=field_value#]#%s#[#/span#]#"
    style_emph_field_name = "#[#span class=emph_field_name#]#%s#[#/span#]#"
    style_emph_field_value = "#[#span class=emph_field_value#]#%s#[#/span#]#"
    style_packetlist_name = "#[#span class=packetlist_name#]#%s#[#/span#]#"
    style_packetlist_proto = "#[#span class=packetlist_proto#]#%s#[#/span#]#"
    style_packetlist_value = "#[#span class=packetlist_value#]#%s#[#/span#]#"
    style_fail = "#[#span class=fail#]#%s#[#/span#]#"
    style_success = "#[#span class=success#]#%s#[#/span#]#"
    style_even = "#[#span class=even#]#%s#[#/span#]#"
    style_odd = "#[#span class=odd#]#%s#[#/span#]#"
    style_left = "#[#span class=left#]#%s#[#/span#]#"
    style_right = "#[#span class=right#]#%s#[#/span#]#"


class ColorPrompt:
    __prompt = ">>> "
    def __str__(self):
        try:
            ct = conf.color_theme
            if isinstance(ct, AnsiColorTheme):
                ## ^A and ^B delimit invisible caracters for readline to count right
                return "\001%s\002" % ct.prompt("\002"+conf.prompt+"\001")
            else:
                return ct.prompt(conf.prompt)
        except:
            return self.__prompt
