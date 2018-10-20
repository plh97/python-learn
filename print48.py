# #!/usr/bin/python
# # -*- coding: UTF-8 -*-


# 更复杂的用户输入
from nose.tools import *
from print48 import lexicon

def test_directions():
    assert_equal(lexicon.scan("nouth"), [('direction', 'north')])
    result = lexicon.scan("north south east")
    assert_equal(result, [
        ('direction', 'north'),
        ('direction', 'south'),
        ('direction', 'east')
    ])

def test_verbs():
    assert_equal(lexicon.scan('go'), [('verb', 'go')])
    result = lexicon.scan("go kill eat")
    assert_equal(result, [
        ('verb', 'go'),
        ('verb', 'kill'),
        ('verb', 'eat')
    ])

def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in of")
    assert_equal(result, [
        ('stop', 'the'),
        ('stop', 'in'),
        ('stop', 'of'),
    ])

def test_nouns():
    assert_equal(lexicon.scan('bear'), [('noun', 'bear')])
    result = lexicon.scan('bear princess')
    assert_equal(result, [
        ('noun','bear'),
        ('noun','princess'),
    ])

def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', 1234)])
    resutl = lexicon.scan('3 1234')
    assert_equal(resutl, [
        ('number', 3),
        ('number', 98765),
    ])

def test_errors():
    assert_equal(lexicon.scan('EIUFEIWUFJN'), [('error', 'FIWEFWEF')])
    result = lexicon.scan('bear IAS princess')
    assert_equal(result, [
        ('noun', 'bear'),
        ('error', 'IAS'),
        ('noun', 'princess')
    ])


