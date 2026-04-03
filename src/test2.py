# FIXME: This file is intentionally terrible to trigger all Ruff rules!
# TODO: Someone needs to rewrite this completely.
# XXX: Danger zone below.

import sys, os          # E401 (Multiple imports), I001 (Unsorted imports)
import requests         # I001 (Third-party mixed with standard library)
import json             # F401 (Unused import)
import logging          # I001

# ==========================================
# 1. Naming & Builtins (N, A)
# ==========================================
class snake_case_class_name:  # N801 (Classes should be CamelCase)

    def __init__(self):
        self.list = []  # A003 (Class attribute shadowing Python built-in 'list')

    def BadMethodName(self, id, type):  # N802 (Method should be snake_case), A002 (Arguments shadowing built-ins)
        pass

# ==========================================
# 2. Design Limits (PLR, C90) & Bugbear (B)
# ==========================================
# PLR0913: Too many arguments (7 > 5)
# B006: Do not use mutable data structures for argument defaults (my_list=[])
def overly_complex_function(arg1, arg2, arg3, arg4, arg5, arg6, my_list=[]):

    # F841: Local variable assigned but never used (doesn't match dummy regex)
    unused_local_variable = "Hello World"

    # A001: Shadowing built-in
    dict = {"key": "value"}

    # ==========================================
    # 3. Security (S)
    # ==========================================
    # S102: Use of exec detected
    exec("print('This is highly dangerous')")

    # S113: requests call without timeout
    res = requests.get('http://example.com') # Format check will also hate these single quotes

    # ==========================================
    # 4. Exceptions (BLE) & Logging (G) & Pyflakes (F)
    # ==========================================
    try:
        # F821: Undefined name
        print(variable_that_does_not_exist)
    except Exception as e:  # BLE001: Catching blind exception
        # G004: Logging statement uses f-string
        logging.error(f"Something broke: {e}")

    # ==========================================
    # 5. Complexity Thresholds (PLR)
    # ==========================================
    # PLR0914: Too many local variables (17 > 15)
    l1=1; l2=2; l3=3; l4=4; l5=5; l6=6; l7=7; l8=8; l9=9; l10=10; l11=11; l12=12; l13=13; l14=14; l15=15; l16=16; l17=17 # E702 (Multiple statements on one line)

    # PLR0916: Too many boolean expressions in if statement (6 > 5)
    if l1 and l2 and l3 and l4 and l5 and l6 and l7:
        pass

    # C901: Function is too complex
    # PLR0912: Too many branches (14 > 12)
    # PLR0911: Too many return statements (8 > 6)
    if l1 == 1: return 1
    elif l2 == 2: return 2
    elif l3 == 3: return 3
    elif l4 == 4: return 4
    elif l5 == 5: return 5
    elif l6 == 6: return 6
    elif l7 == 7: return 7
    elif l8 == 8: return 8
    elif l9 == 9: pass
    elif l10 == 10: pass
    elif l11 == 11: pass
    elif l12 == 12: pass
    elif l13 == 13: pass
    elif l14 == 14: pass

    # PLR0915: Too many statements (just padding lines to exceed 50 statements)
    a=1;a=2;a=3;a=4;a=5;a=6;a=7;a=8;a=9;a=10
    a=1;a=2;a=3;a=4;a=5;a=6;a=7;a=8;a=9;a=10
    a=1;a=2;a=3;a=4;a=5;a=6;a=7;a=8;a=9;a=10

    return None

# ==========================================
# 6. Monolithic Class (PLR0904)
# ==========================================
class GodClass:
    # Too many public methods (21 > 20)
    def m1(self): pass
    def m2(self): pass
    def m3(self): pass
    def m4(self): pass
    def m5(self): pass
    def m6(self): pass
    def m7(self): pass
    def m8(self): pass
    def m9(self): pass
    def m10(self): pass
    def m11(self): pass
    def m12(self): pass
    def m13(self): pass
    def m14(self): pass
    def m15(self): pass
    def m16(self): pass
    def m17(self): pass
    def m18(self): pass
    def m19(self): pass
    def m20(self): pass
    def m21(self): pass












