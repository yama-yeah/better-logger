# BetterLog Test
import pytest
from better_logger import BetterLog, BetterLogArgs,Color
from traceback import StackSummary,FrameSummary
import copy
fake_project_root='/home/user/fake_project'
fake_frames=[FrameSummary(filename=fake_project_root+'/src/better_logger/__init__.py',lineno=10,name='test_BetterLog'),FrameSummary(filename=fake_project_root+'/tests/better_log.py',lineno=10,name='test_BetterLog')]
fake_tb=StackSummary(fake_frames)
args=BetterLogArgs(messages=('test',),color=Color.RED,project_root=fake_project_root,width=50,emoji='🚀',header_text='header',tb=fake_tb)
# from_argsが正しく動作しているか
def test_better_log_from_args():
    _args=copy.deepcopy(args)
    better_log_from_args=BetterLog.from_args(_args)
    better_log=BetterLog(('test',),Color.RED,fake_project_root,50,'🚀','header',fake_tb)
    assert better_log_from_args.color==better_log.color
    _args.header_text=None
    better_log_from_args=BetterLog.from_args(_args)
    better_log.header_text=None
    assert better_log_from_args.header_text==better_log.header_text
    _args.tb=None
    better_log_from_args=BetterLog.from_args(_args)
    better_log.tb=None
    assert better_log_from_args.tb==better_log.tb

# おおよそ正しい出力がされるか
def test_better_log_output():
    _args=copy.deepcopy(args)
    better_log=BetterLog.from_args(_args)
    correct_output="\x1b[31m┌────────────────────────────────────────────────┐\n│                     header                     │\n├────────────────────────────────────────────────┤\n│ #1    test_BetterLogsrc/better_logger/__init__.py:10 │\n│ #2    test_BetterLog    tests/better_log.py:10 │\n├────────────────────────────────────────────────┤\n│ 🚀 'test'                                      │\n└────────────────────────────────────────────────┘\x1b[0m\n"
    output=better_log.output()
    assert output==correct_output
# ログが長すぎて使い物にならないためコメントアウト
# @pytest.mark.parametrize('head_text,correct_output',[
#     (None,"\x1b[31m┌────────────────────────────────────────────────┐\n│ #1    test_BetterLogsrc/better_logger/__init__.py:10 │\n│ #2    test_BetterLog    tests/better_log.py:10 │\n├────────────────────────────────────────────────┤\n│ 🚀 'test'                                      │\n└────────────────────────────────────────────────┘\x1b[0m\n"),
#     (Exception('test exception'),"\x1b[31m┌────────────────────────────────────────────────┐\n│                 test exception                 │\n├────────────────────────────────────────────────┤\n│ #1    test_BetterLogsrc/better_logger/__init__.py:10 │\n│ #2    test_BetterLog    tests/better_log.py:10 │\n├────────────────────────────────────────────────┤\n│ 🚀 'test'                                      │\n└────────────────────────────────────────────────┘\x1b[0m\n")
#     ])
def test_better_log_output_header():
    _args=copy.deepcopy(args)
    # Noneの場合
    _args.header_text=None
    better_log=BetterLog.from_args(_args)
    output=better_log.output()
    correct_output="\x1b[31m┌────────────────────────────────────────────────┐\n│ #1    test_BetterLogsrc/better_logger/__init__.py:10 │\n│ #2    test_BetterLog    tests/better_log.py:10 │\n├────────────────────────────────────────────────┤\n│ 🚀 'test'                                      │\n└────────────────────────────────────────────────┘\x1b[0m\n"
    assert output==correct_output

    # str以外のobjectが入力された場合
    _args.header_text=Exception('test exception')
    better_log=BetterLog.from_args(_args)
    output=better_log.output()
    correct_output="\x1b[31m┌────────────────────────────────────────────────┐\n│                 test exception                 │\n├────────────────────────────────────────────────┤\n│ #1    test_BetterLogsrc/better_logger/__init__.py:10 │\n│ #2    test_BetterLog    tests/better_log.py:10 │\n├────────────────────────────────────────────────┤\n│ 🚀 'test'                                      │\n└────────────────────────────────────────────────┘\x1b[0m\n"
    assert output==correct_output
    
def test_better_log_output_tb():
    # tracebackがNoneの場合
    _args=copy.deepcopy(args)
    _args.tb=None
    better_log=BetterLog.from_args(_args)
    output=better_log.output()
    correct_output="\x1b[31m┌────────────────────────────────────────────────┐\n│                     header                     │\n├────────────────────────────────────────────────┤\n│ 🚀 'test'                                      │\n└────────────────────────────────────────────────┘\x1b[0m\n"
    assert output==correct_output

def test_better_log_output_messages():
    # messagesが複数の場合
    _args=copy.deepcopy(args)
    _args.messages=('test1','test2',)
    better_log=BetterLog.from_args(_args)
    output=better_log.output()
    correct_output="\x1b[31m┌────────────────────────────────────────────────┐\n│                     header                     │\n├────────────────────────────────────────────────┤\n│ #1    test_BetterLogsrc/better_logger/__init__.py:10 │\n│ #2    test_BetterLog    tests/better_log.py:10 │\n├────────────────────────────────────────────────┤\n│ 🚀 'test1'                                     │\n│ 🚀 'test2'                                     │\n└────────────────────────────────────────────────┘\x1b[0m\n"
    assert output==correct_output

# widthが極端に短くてもエラーにならないか
def test_better_log_output_width():
    _args=copy.deepcopy(args)
    _args.width=100
    better_log=BetterLog.from_args(_args)
    correct_output="\x1b[31m┌──────────────────────────────────────────────────────────────────────────────────────────────────┐\n│                                              header                                              │\n├──────────────────────────────────────────────────────────────────────────────────────────────────┤\n│ #1    test_BetterLog                                            src/better_logger/__init__.py:10 │\n│ #2    test_BetterLog                                                      tests/better_log.py:10 │\n├──────────────────────────────────────────────────────────────────────────────────────────────────┤\n│ 🚀 'test'                                                                                        │\n└──────────────────────────────────────────────────────────────────────────────────────────────────┘\x1b[0m\n"
    output=better_log.output()
    assert output==correct_output
    _args.width=2
    better_log=BetterLog.from_args(_args)
    output2=better_log.output()
    correct_output="\x1b[31m┌─┐\n│h│\n│e│\n│a│\n│d│\n│e│\n│r│\n├─┤\n│ #1    test_BetterLogsrc/better_logger/__init__.py:10 │\n│ #2    test_BetterLogtests/better_log.py:10 │\n├─┤\n│ 🚀 \n'test'\n│\n└─┘\x1b[0m\n"
    _args.width=3
    better_log=BetterLog.from_args(_args)
    output3=better_log.output()
    assert output3==correct_output and output2==correct_output

def test_better_log_make_top():
    _args=copy.deepcopy(args)
    better_log=BetterLog.from_args(_args)
    output=better_log._top()
    correct_output='┌────────────────────────────────────────────────┐\n'
    assert output==correct_output
@pytest.mark.parametrize('width,correct_output',[
    (50,'                       test                       '),
    (2,'test'),
    (7,' test  ')
    ])
def test_better_log_make_center_text(width,correct_output):
    _args=copy.deepcopy(args)
    better_log=BetterLog.from_args(_args)
    output=better_log._text_center('test',width)
    assert output==correct_output

def test_better_log_make_traceback_area():
    _args=copy.deepcopy(args)
    better_log=BetterLog.from_args(_args)
    output=better_log._traceback()
    correct_output='│ #1    test_BetterLogsrc/better_logger/__init__.py:10 │\n│ #2    test_BetterLog    tests/better_log.py:10 │\n├────────────────────────────────────────────────┤\n'
    assert output==correct_output
    _args.tb=None
    better_log=BetterLog.from_args(_args)
    output=better_log._traceback()
    correct_output=''
    assert output==correct_output
def test_better_log_make_footer():
    _args=copy.deepcopy(args)
    better_log=BetterLog.from_args(_args)
    output=better_log._footer()
    correct_output='└────────────────────────────────────────────────┘'
    assert output==correct_output
def test_better_log_make_relative_path():
    _args=copy.deepcopy(args)
    better_log=BetterLog.from_args(_args)
    output=better_log._cut_file_path(fake_frames[0].filename)
    correct_output='src/better_logger/__init__.py'
    assert output==correct_output
def test_better_log_make_left_text():
    _args=copy.deepcopy(args)
    better_log=BetterLog.from_args(_args)
    output=better_log._left('test message','🚀',30)
    correct_output=' 🚀 test message              '
    assert output==correct_output
