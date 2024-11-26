from bloodandsugar import *

def test01():
    assert pingpong(110,95) == 'Genaral'
def test02():
    assert pingpong(125,110) == 'Risk'
def test03():
    assert pingpong(145,130) == 'High Risk (Blood Level 1, Sugar Level 1)'
def test04():
    assert pingpong(165,160) == 'High Risk (Blood Level 2, Sugar Level 2)'
def test05():
    assert pingpong(185,190) == 'High Risk (Blood Level 3, Sugar Level 3)'
