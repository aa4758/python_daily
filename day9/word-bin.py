import sys

txt = '''
Python was conceived in the late 1980s[34] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC programming language, which was inspired by SETL),[35] capable of exception handling and interfacing with the Amoeba operating system.[8] Its implementation began in December 1989.[36] Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his "permanent vacation" from his responsibilities as Python's Benevolent Dictator For Life, a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker.[37] He now shares his leadership as a member of a five-person steering council.[38][39][40] In January 2019, active Python core developers elected Brett Cannon, Nick Coghlan, Barry Warsaw, Carol Willing and Van Rossum to a five-member "Steering Council" to lead the project.[41] Guido van Rossum has since then withdrawn his nomination for the 2020 Steering council.[42]

Python 2.0 was released on 16 October 2000 with many major new features, including a cycle-detecting garbage collector and support for Unicode.[43]

Python 3.0 was released on 3 December 2008. It was a major revision of the language that is not completely backward-compatible.[44] Many of its major features were backported to Python 2.6.x[45] and 2.7.x version series. Releases of Python 3 include the 2to3 utility, which automates (at least partially) the translation of Python 2 code to Python 3.[46]
'''

args = sys.argv[1]

import re

for i in txt:
    re.findall