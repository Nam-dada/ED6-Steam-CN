import sys
sys.path.append(r'C:\nw_profile\IDE\pycharm\pycharmProj\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2120_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2120_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0403.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10001 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('Init')
def Init():
    Call(1, 0x0001)

    Return()

# id: 0x0001 offset: 0xAD
@scena.Code('func_01_AD')
def func_01_AD():
    TalkBegin(0x0009)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 3, 0x20E3)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_FF',
    )

    Call(6, 0x0003)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EB',
    )

    OP_0D()

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_E3',
    )

    OP_A9(0x77)

    Jump('loc_E5')

    def _loc_E3(): pass

    label('loc_E3')

    OP_A9(0x64)

    def _loc_E5(): pass

    label('loc_E5')

    OP_56(0x00)
    TalkEnd(0x0009)

    Return()

    def _loc_EB(): pass

    label('loc_EB')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FC',
    )

    TalkEnd(0x0009)

    Return()

    def _loc_FC(): pass

    label('loc_FC')

    Jump('loc_B25')

    def _loc_FF(): pass

    label('loc_FF')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B25',
    )

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, -29500, 0, 2800, 0)
    ChrSetPos(0x0102, -30300, 0, 2600, 0)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_166',
    )

    ChrSetPos(0x00F9, -29900, 0, 1600, 0)
    ChrSetPos(0x00F8, -30800, 0, 1400, 0)

    Jump('loc_188')

    def _loc_166(): pass

    label('loc_166')

    ChrSetPos(0x00F8, -29900, 0, 1600, 0)
    ChrSetPos(0x00F9, -30800, 0, 1400, 0)

    def _loc_188(): pass

    label('loc_188')

    ChrSetDirection(0x0009, 180, 0)
    CameraMove(-30100, 0, 3960, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '不好意思工房现在停业了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '因为导力驱动的工具\n',
            '全都不能动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '明明看起来都是好的……\n',
            '到底是怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 2, 0x20E2)),
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 3, 0x20E3)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 4, 0x20E4)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 5, 0x20E5)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 6, 0x20E6)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_279',
    )

    ChrTalk(
        0x0101,
        (
            '#1018F#4P啊，那个不用担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们带了好东西来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '噢，是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6CB')

    def _loc_279(): pass

    label('loc_279')

    ChrTalk(
        0x0101,
        (
            '#1026F#4P啊，是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F嗯……不过真伤脑筋啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '结晶回路的合成和结晶孔的强化\n',
            '都完全不能进行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_328',
    )

    ChrTalk(
        0x0103,
        (
            '#025F嗯嗯，难得有了这的发生器，\n',
            '真是太可惜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C3')

    def _loc_328(): pass

    label('loc_328')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_36B',
    )

    ChrTalk(
        0x0108,
        (
            '#072F唔，难得有了这的发生器，\n',
            '真是太可惜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C3')

    def _loc_36B(): pass

    label('loc_36B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3C3',
    )

    ChrTalk(
        0x0106,
        (
            '#552F啊啊，难得有了这的发生器，\n',
            '恢复导力魔法了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这真是太可惜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C3(): pass

    label('loc_3C3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_418',
    )

    ChrTalk(
        0x0107,
        (
            '#064F啊，不过姐姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '如果只是一小会儿，\n',
            '那我或许有点办法喔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_466')

    def _loc_418(): pass

    label('loc_418')

    ChrTalk(
        0x0102,
        (
            '#1043F#1P确实如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1040F不过，如果只是一小会儿\n',
            '那我或许有点办法喔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_466(): pass

    label('loc_466')

    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4E3',
    )

    @scena.Lambda('lambda_0496')
    def lambda_0496():
        ChrTurnDirection(0x0000, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0496)

    Sleep(120)

    @scena.Lambda('lambda_04A9')
    def lambda_04A9():
        ChrTurnDirection(0x0001, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_04A9)

    @scena.Lambda('lambda_04B7')
    def lambda_04B7():
        ChrTurnDirection(0x0002, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_04B7)

    Sleep(120)

    @scena.Lambda('lambda_04CA')
    def lambda_04CA():
        ChrTurnDirection(0x0003, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_04CA)

    @scena.Lambda('lambda_04D8')
    def lambda_04D8():
        ChrTurnDirection(0x0009, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_04D8)

    Jump('loc_4EA')

    def _loc_4E3(): pass

    label('loc_4E3')

    ChrTurnDirection(0x0101, 0x0102, 400)

    def _loc_4EA(): pass

    label('loc_4EA')

    WaitForThreadExit(0x0000, 0x0001)
    WaitForThreadExit(0x0001, 0x0001)
    WaitForThreadExit(0x0002, 0x0001)
    WaitForThreadExit(0x0003, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#1004F#4P啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_547',
    )

    ChrTalk(
        0x0106,
        (
            '#052F能让工房运作起来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5A2')

    def _loc_547(): pass

    label('loc_547')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_575',
    )

    ChrTalk(
        0x0103,
        (
            '#023F能让工房运作起来？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5A2')

    def _loc_575(): pass

    label('loc_575')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5A2',
    )

    ChrTalk(
        0x0108,
        (
            '#073F能让工房运作起来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5A2(): pass

    label('loc_5A2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5E4',
    )

    ChrTalk(
        0x0107,
        (
            '#060F是，是，大概……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '用那个发生器的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_62C')

    def _loc_5E4(): pass

    label('loc_5E4')

    ChrTalk(
        0x0102,
        (
            '#1040F#1P是，我想……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '如果使用那个发生器，\n',
            '应该能在短时间内复原。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_62C(): pass

    label('loc_62C')

    ChrTalk(
        0x0101,
        (
            '#1018F#4P啊，原来如此！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '喂喂，你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那到底是怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_067B')
    def lambda_067B():
        ChrTurnDirection(0x0000, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_067B)

    Sleep(120)

    @scena.Lambda('lambda_068E')
    def lambda_068E():
        ChrTurnDirection(0x0001, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_068E)

    @scena.Lambda('lambda_069C')
    def lambda_069C():
        ChrTurnDirection(0x0002, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_069C)

    Sleep(120)

    @scena.Lambda('lambda_06AF')
    def lambda_06AF():
        ChrTurnDirection(0x0003, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_06AF)

    WaitForThreadExit(0x0000, 0x0001)
    WaitForThreadExit(0x0001, 0x0001)
    WaitForThreadExit(0x0002, 0x0001)
    WaitForThreadExit(0x0003, 0x0001)

    def _loc_6CB(): pass

    label('loc_6CB')

    ChrTalk(
        0x0102,
        (
            '#1040F#1P那个，是这样的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '说明了使用『零力场发生器』\n',
            '可暂时恢复工房机能的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    ChrTurnDirection(0x0009, 0x0102, 400)

    ChrTalk(
        0x0009,
        (
            '咦，真厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '工具的话这里有，\n',
            '试试看吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F#4P嗯，这就照办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7C9',
    )

    ChrTalk(
        0x0107,
        (
            '#560F那么～\n',
            '请稍等。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7F9')

    def _loc_7C9(): pass

    label('loc_7C9')

    ChrTalk(
        0x0102,
        (
            '#1040F#1P那么，稍等片刻。\n',
            '借用一下机械了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7F9(): pass

    label('loc_7F9')

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    PlaySE(157, 0x00, 0x64)
    ChrSetDirection(0x0009, 315, 0)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '使用『零力场发生器』将工房机能恢复了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '喔喔，看起来很不错呢。\n',
            '导力能源又回到机械里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 2, 0x20E2)),
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 3, 0x20E3)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 4, 0x20E4)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 5, 0x20E5)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 6, 0x20E6)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_8DC',
    )

    ChrTurnDirection(0x0009, 0x0000, 400)

    ChrTalk(
        0x0009,
        (
            '虽然只是做了应急维修，\n',
            '要调整就趁现在了!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9FE')

    def _loc_8DC(): pass

    label('loc_8DC')

    ChrTalk(
        0x0101,
        (
            '#1000F#4P太好了……看来是成功了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_95B',
    )

    ChrTalk(
        0x0107,
        (
            '#063F嗯，不过这\n',
            '只是暂时能动……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#561F马上又会回到不动的状态的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9A9')

    def _loc_95B(): pass

    label('loc_95B')

    ChrTalk(
        0x0102,
        (
            '#1040F#1P嗯，确实很顺利……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '但并不是真的修好了。\n',
            '过一段时间又会停止的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9A9(): pass

    label('loc_9A9')

    ChrTurnDirection(0x0009, 0x0000, 400)

    ChrTalk(
        0x0009,
        (
            '是吗……\n',
            '仅仅是应急维修而已吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '呼，不管怎么说，\n',
            '要调整就趁现在了!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()

    def _loc_9FE(): pass

    label('loc_9FE')

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0x77)
    OP_56(0x00)
    OP_0D()
    Sleep(30)

    ChrTalk(
        0x0009,
        (
            '话虽如此……\n',
            '真是个厉害的装置啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '可以的话，\n',
            '能留下一个吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F#4P嗯～可以的话\n',
            '是想这么做……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F#1P但是不好意思。\n',
            '重要的任务还要使用它呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '呼，果然不行吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '嗯，来这里的时候\n',
            '就带着那个好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那样就可以像刚才一样\n',
            '使用工房了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x041C, 3, 0x20E3))
    EventEnd(0x00)
    TalkEnd(0x0009)

    Return()

    def _loc_B25(): pass

    label('loc_B25')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_BC5',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0066, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_B79',
    )

    ChrTalk(
        0x0009,
        (
            '唔～游击士\n',
            '照相的技术也不错嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '有什么特别的训练吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BC2')

    def _loc_B79(): pass

    label('loc_B79')

    ChrTalk(
        0x0009,
        (
            '去哪里摄影了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '因为兴趣而开始使用相机的人\n',
            '最近增加了不少呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BC2(): pass

    label('loc_BC2')

    Jump('loc_1119')

    def _loc_BC5(): pass

    label('loc_BC5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_CBD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C76',
    )

    ChrTalk(
        0x0009,
        (
            '城里的导力器\n',
            '还是不能动啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '只要大桥动不了，\n',
            '这状态就会持续啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '但是，使用导力的机械\n',
            '居然全部不能动了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '真是的，利贝尔\n',
            '以后会怎样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_CBA')

    def _loc_C76(): pass

    label('loc_C76')

    ChrTalk(
        0x0009,
        (
            '城里的导力器\n',
            '还是不能动啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '真是的，利贝尔\n',
            '以后会怎样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CBA(): pass

    label('loc_CBA')

    Jump('loc_1119')

    def _loc_CBD(): pass

    label('loc_CBD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_D32',
    )

    ChrTalk(
        0x0009,
        (
            '只要有那个装置\n',
            '就能再开始营业啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '也好，\n',
            '不能强人所难嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '只好老老实实等待\n',
            '这灾难过去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1119')

    def _loc_D32(): pass

    label('loc_D32')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_E51',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_DCC',
    )

    ChrTalk(
        0x0009,
        (
            '诺曼先生说得对，\n',
            '旅游业确实有前途。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '但是，卢安这里和王都\n',
            '都是连接海路的要地嘛。\n',
            '港口设施也不能疏忽哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '呼，该给谁投票呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E4E')

    def _loc_DCC(): pass

    label('loc_DCC')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '诺曼先生说得对，\n',
            '旅游业确实有前途。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '但是，卢安这里和王都\n',
            '都是连接海路的要地嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '整备港口设施\n',
            '感觉还是很重要呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E4E(): pass

    label('loc_E4E')

    Jump('loc_1119')

    def _loc_E51(): pass

    label('loc_E51')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_F4B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_EB6',
    )

    ChrTalk(
        0x0009,
        (
            '因为戴尔蒙市长的事\n',
            '使得城市的形象变坏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '要是再引起骚动\n',
            '真的是受不了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F48')

    def _loc_EB6(): pass

    label('loc_EB6')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '真是头痛啊。\n',
            '竟然发生那样的骚动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '本来就因为戴尔蒙市长的事\n',
            '使得城市的形象变坏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '如果再发生什么，\n',
            '在别人心中坏印象就改变不了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F48(): pass

    label('loc_F48')

    Jump('loc_1119')

    def _loc_F4B(): pass

    label('loc_F4B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Return,
        ),
        'loc_F76',
    )

    ChrTalk(
        0x0009,
        (
            '哟，怎么了？\n',
            '感觉很着急啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1119')

    def _loc_F76(): pass

    label('loc_F76')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1043',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_FEF',
    )

    ChrTalk(
        0x0009,
        (
            '最近有很多旅游的客人\n',
            '拜托我冲洗感光结晶回路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '因为导力照相机普及，\n',
            '拍摄照片的人也增多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1040')

    def _loc_FEF(): pass

    label('loc_FEF')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '该支持哪位候选人，\n',
            '其实还没决定呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我们和游客、港口之间\n',
            '都有交易。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1040(): pass

    label('loc_1040')

    Jump('loc_1119')

    def _loc_1043(): pass

    label('loc_1043')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_1119',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_10B8',
    )

    ChrTalk(
        0x0009,
        (
            '新型导力器的普及活动\n',
            '由爱普斯泰恩财团在推进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '像我们这样个人经营的工房，\n',
            '也要配合这活动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1119')

    def _loc_10B8(): pass

    label('loc_10B8')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '哟，新型导力器\n',
            '使用感觉怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '为了更好掌握其性能，结晶孔\n',
            '还是积极地强化了比较好哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1119(): pass

    label('loc_1119')

    TalkEnd(0x0009)

    Return()

# id: 0x0002 offset: 0x111D
@scena.Code('func_02_111D')
def func_02_111D():
    Call(1, 0x0003)

    Return()

# id: 0x0003 offset: 0x1122
@scena.Code('func_03_1122')
def func_03_1122():
    TalkBegin(0x000A)
    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1150',
    )

    OP_0D()

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1148',
    )

    OP_A9(0x76)

    Jump('loc_114A')

    def _loc_1148(): pass

    label('loc_1148')

    OP_A9(0x65)

    def _loc_114A(): pass

    label('loc_114A')

    OP_56(0x00)
    TalkEnd(0x000A)

    Return()

    def _loc_1150(): pass

    label('loc_1150')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1161',
    )

    TalkEnd(0x000A)

    Return()

    def _loc_1161(): pass

    label('loc_1161')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_2F2F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0408, 0, 0x2040)),
            Expr.Ez,
            (Expr.PushValueByIndex, 0xCB),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_12C9',
    )

    ChrTalk(
        0x000A,
        (
            '哎呀，游击士们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我听说了哦，学院的事件\n',
            '好像平安解决了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，总算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '因为有卡露娜前辈他们\n',
            '的帮助啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '呵呵，我的收藏\n',
            '好像也稍微派上点用场呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F收藏……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F对了，卡露娜是\n',
            '使用枪的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0102, 400)

    ChrTalk(
        0x000A,
        (
            '嗯嗯，火药式枪械\n',
            '的使用是非常难的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过，卡露娜\n',
            '是没问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    SetScenaFlags(ScenaFlag(0x0416, 3, 0x20B3))
    SetScenaFlags(ScenaFlag(0x0408, 0, 0x2040))

    Jump('loc_2F2C')

    def _loc_12C9(): pass

    label('loc_12C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0408, 0, 0x2040)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E2E',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_166F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0416, 3, 0x20B3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1562',
    )

    ChrTalk(
        0x000A,
        (
            '哎呀，游击士们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我听说了哦，学院的事件\n',
            '好像平安解决了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，总算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '因为有卡露娜前辈他们\n',
            '的帮助啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '呵呵，我的收藏\n',
            '好像也稍微派上点用场呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F收藏……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F对了，卡露娜是\n',
            '使用枪的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0102, 400)

    ChrTalk(
        0x000A,
        (
            '嗯嗯，火药式枪械\n',
            '的使用是非常难的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过，卡露娜\n',
            '是没问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '话说回来，最让我吃惊的，\n',
            '还是那位和卡露娜一起\n',
            '开枪射击的女孩子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F啊，你是说提妲啊。。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '对，就是那个提妲。。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '但是，好像现在\n',
            '不在一起呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1044F你有什么想要\n',
            '传达的事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '呵呵……有一点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    SetScenaFlags(ScenaFlag(0x0416, 3, 0x20B3))

    Jump('loc_166C')

    def _loc_1562(): pass

    label('loc_1562')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_15BA',
    )

    ChrTalk(
        0x000A,
        (
            '我妹妹妮吉塔\n',
            '也在王立学院上学。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '事件平安解决了，\n',
            '我也衷心表示感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_166C')

    def _loc_15BA(): pass

    label('loc_15BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_163B',
    )

    ChrTalk(
        0x000A,
        (
            '王立学院的事件\n',
            '好像平安解决了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我妹妹妮吉塔\n',
            '也在那学院上学。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '事件平安解决了，\n',
            '我也衷心表示感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_166C')

    def _loc_163B(): pass

    label('loc_163B')

    ChrTalk(
        0x000A,
        (
            '事件解决真是谢谢你们了。\n',
            '让我衷心表示感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_166C(): pass

    label('loc_166C')

    Jump('loc_2E2B')

    def _loc_166F(): pass

    label('loc_166F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0416, 3, 0x20B3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A10',
    )

    ChrTalk(
        0x000A,
        (
            '#4110361261V哎呀，游击士们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4110361262V我听说了哦，学院的事件\n',
            '好像平安解决了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010361263V#1006F嗯，总算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010361264V因为有卡露娜前辈他们\n',
            '的帮助啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#4110361265V呵呵，我的收藏\n',
            '好像也稍微派上点用场呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010361266V#1011F收藏……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361267V#1040F对了，卡露娜是\n',
            '使用枪的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0102, 400)

    ChrTalk(
        0x000A,
        (
            '#4110361268V嗯嗯，火药式枪械\n',
            '的使用是非常难的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4110361269V不过，卡露娜\n',
            '是没问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4110361270V话说回来，最让我吃惊的，\n',
            '还是那位和卡露娜一起\n',
            '开枪射击的女孩子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x000A, 0x0107, 400)

    ChrTalk(
        0x000A,
        (
            '#4110361271V莫非……\n',
            '你就是我说的那位提妲？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070361272V#064F咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010361273V#1015F嗯，是没错啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361274V#1044F提妲她\n',
            '怎么了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4110361275V嗯，我有点事情\n',
            '想要找她……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4110361276V只要一下子就好，\n',
            '能占用你一点时间吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BBB')

    def _loc_1A10(): pass

    label('loc_1A10')

    ChrTalk(
        0x000A,
        (
            '#4110361277V哎呀，游击士们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x000A, 0x0107, 400)

    ChrTalk(
        0x000A,
        (
            '#4110361278V难道……\n',
            '你是提妲吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070361272V#064F诶……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361280V#1040F说起来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020361281V你有什么话\n',
            '想转达给提妲吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4110361282V是的，我是想\n',
            '传达一些事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4110361283V总之，能不能让我\n',
            '稍微占用一点时间呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BBB(): pass

    label('loc_1BBB')

    FadeOut(1500, 0, -1)
    OP_0D()
    EventBegin(0x00)
    Sleep(500)

    ChrSetDirection(0x000A, 180, 0)
    CameraMove(1130, 400, 3310, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2550, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0101, 2050, 0, 1930, 0)
    ChrSetPos(0x0102, 620, 0, 1630, 0)
    ChrSetPos(0x00F8, 1220, 0, 2670, 0)
    ChrSetPos(0x00F9, 1320, 0, 710, 0)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1C84',
    )

    ChrSetPos(0x00F9, 1220, 0, 2670, 0)
    ChrSetPos(0x00F8, 1320, 0, 710, 0)

    def _loc_1C84(): pass

    label('loc_1C84')

    FadeIn(1500, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070361284V#560F那、那个……\n',
            '到底是什么事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4110361285V嗯，关于这个嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4110361286V可以先让我看看\n',
            '你所使用的\n',
            '火药式机关炮吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070361287V#064F啊、好的。\n',
            '没有问题……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '提妲拿出了\n',
            '常用的格林炮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    Sleep(500)

    OP_62(0x000A, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x000A)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#4110361288V原来如此啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4110361289V呵呵，\n',
            '我果然没弄错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070361290V#064F诶……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4110361291V提妲你知道\n',
            '那是什么型号的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070361292V#560F啊、是的，是俗称\n',
            'ＣＺ系列的型号。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070361293V这把在该系列中也是属于初期型产品，\n',
            '是全世界仅有数把的珍贵品，\n',
            '爷爷是这么说的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4110361294V嗯，没错。\n',
            '还有呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070361295V#561F呃、那个……\n',
            '武器之类的\n',
            '我并不是很清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070361296V#060F只是，这个初期型号的\n',
            '基本构造似乎有些问题\n',
            '所以无法发挥出设计上的性能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070361297V因为这样子，所以虽然能强化火力，\n',
            '却难以调整炮击范围。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070361298V不过这点听说在几代前的型号\n',
            '就已经获得改善了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_21B0',
    )

    ChrTalk(
        0x0101,
        (
            '#0010361299V#1016F（我、我觉得她已经\n',
            '  知道得很清楚了耶……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050361300V#551F（嗯嗯，没错。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_222D')

    def _loc_21B0(): pass

    label('loc_21B0')

    ChrTalk(
        0x0101,
        (
            '#0010361299V#1016F（我、我觉得她已经\n',
            '  知道得很清楚了耶……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361302V#1054F（哈哈，说的没错。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_222D(): pass

    label('loc_222D')

    ChrTalk(
        0x000A,
        (
            '#4110361303V原来如此，既然你都这么清楚了，\n',
            '那么话就好说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4110361304V所以说，提妲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4110361305V你听说过莱恩福尔特公司\n',
            '推出的Ｆ零件吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070361306V#560F有，是指为了弥补\n',
            ' ＣＺ系列缺陷的Ｆｉｎａｌ零件吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070361307V不过我听说那只能支援\n',
            '比较新的型号……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4110361308V其实，世上存在着能支援\n',
            '那把初期型的Ｆ零件',
            TxtCtl.Enter,
            '\n',
            '――我这么说你会相信吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070361309V#064F咦……这是真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4110361310V嗯，是真的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4110361311V因为需求量不大，\n',
            '所以流通的数量并不多，\n',
            '不过是真的有这种零件噢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4110361312V接下来，我们就进入正题吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070361313V#062F咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4110361314V其实，本店正巧\n',
            '有那种零件噢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070361315V#560F真、真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4110361316V嗯，我要说的不是别的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4110361317V就是希望你务必收下\n',
            '那个Ｆ零件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070361318V#064F真、真的……\n',
            '真的可以吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4110361319V呵呵，当然咯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4110361320V毕竟你们都拯救了\n',
            '我那位在王立学院\n',
            '上学的妹妹……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4110361321V再说，要是就这样\n',
            '让零件放着生灰尘\n',
            '也实在太可惜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070361322V#561F可、可是，\n',
            '总觉得很不好意思耶……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_28C6',
    )

    OP_62(0x0106, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x0106)
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050361323V#053F嗯，我说啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050361324V#051F这里就老老实实收下\n',
            '不就好了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050361325V如果你还是很在意的话\n',
            '就用别的方式\n',
            '报答不就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070361326V#064F阿加特……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29E6')

    def _loc_28C6(): pass

    label('loc_28C6')

    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x0101)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010361327V#1011F欸、提妲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010361328V店长都这么说了，\n',
            '我觉得你还是\n',
            '老实收下比较好哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010361329V如果你还是很在意的话\n',
            '就用别的方式\n',
            '来报答就好了呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070361330V#064F姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29E6(): pass

    label('loc_29E6')

    OP_62(0x0107, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x0107)
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070361331V#563F……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070361332V#067F……请问，我真的\n',
            '可以收下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4110361333V呵呵，当然咯。\n',
            '我一开始就是这么想的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4110361334V知道零件怎么安装吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070361335V#061F是的，大概知道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070361336V#560F呃，方便的话\n',
            '可以向您借用这里吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070361337V我马上就会安装好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4110361338V呵呵，没问题哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    PlaySE(183, 0x00, 0x64)
    Sleep(2500)

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '提妲学会了新Ｓ战技\n',
            (TxtCtl.SetColor, 0x2),
            '『炮射冲击Ｆ』',
            (TxtCtl.SetColor, 0x5),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(542, 0x00, 0x64)
    SetMessageWindowPos(-1, 38, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '要将『炮射冲击Ｆ』登记为Ｓ战技吗？',
            0x18,
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2C7A(): pass

    label('loc_2C7A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D2C',
    )

    Menu(
        1,
        -1,
        250,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    OP_5F(0x0001)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2CBC'),
        (-1, 'loc_2CF6'),
    )

    def _loc_2CBC(): pass

    label('loc_2CBC')

    AddCraft(ChrTable['提妲'], CraftTable['炮射冲击Ⅱ'])
    OP_BB(0x06, 0x06, 0x00000107)
    OP_C0(0x18, 0x00000001, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2D29')

    def _loc_2CF6(): pass

    label('loc_2CF6')

    AddCraft(ChrTable['提妲'], CraftTable['炮射冲击Ⅱ'])
    OP_C0(0x18, 0x00000001, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2D29')

    def _loc_2D29(): pass

    label('loc_2D29')

    Jump('loc_2C7A')

    def _loc_2D2C(): pass

    label('loc_2D2C')

    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#4110361339V呵呵，看来\n',
            '改造得很成功呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4110361340V性能和以往相较下\n',
            '肯定不可同日而语。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070361341V#560F是的，我马上就去试试。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070361342V#061F真的非常感谢您。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0408, 0, 0x2040))
    EventEnd(0x00)

    def _loc_2E2B(): pass

    label('loc_2E2B')

    Jump('loc_2F2C')

    def _loc_2E2E(): pass

    label('loc_2E2E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2EE2',
    )

    ChrTalk(
        0x000A,
        (
            '谢谢你们顺利解决了\n',
            '王立学院的事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我妹妹妮吉塔\n',
            '也是王立学院的学生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我打从心底\n',
            '感谢各位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_2F2C')

    def _loc_2EE2(): pass

    label('loc_2EE2')

    ChrTalk(
        0x000A,
        (
            '谢谢你们顺利解决了事件。\n',
            '我打从心底感谢各位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F2C(): pass

    label('loc_2F2C')

    Jump('loc_3644')

    def _loc_2F2F(): pass

    label('loc_2F2F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_309B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_300E',
    )

    ChrTalk(
        0x000A,
        (
            '看来使用导力的\n',
            '武器都无法运作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过，普通的武器还是可以用的，\n',
            '只要有武术的基础就没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '呵呵，关键时刻\n',
            '果然还是基本功最重要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_3098')

    def _loc_300E(): pass

    label('loc_300E')

    ChrTalk(
        0x000A,
        (
            '看来使用导力的\n',
            '武器都无法运作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过，普通的武器还是可以用的，\n',
            '只要有武术的基础就没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3098(): pass

    label('loc_3098')

    Jump('loc_3644')

    def _loc_309B(): pass

    label('loc_309B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_31AE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_3122',
    )

    ChrTalk(
        0x000A,
        (
            '我会去投票\n',
            '但对选举没什么兴趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '嗯，我打算看人品\n',
            '来决定投给谁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31AB')

    def _loc_3122(): pass

    label('loc_3122')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x000A,
        (
            '虽然我会去投票，\n',
            '但说实话，兴趣不大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '那些工作会受到影响的人们\n',
            '似乎在热心地参与活动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_31AB(): pass

    label('loc_31AB')

    Jump('loc_3644')

    def _loc_31AE(): pass

    label('loc_31AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_324A',
    )

    ChrTalk(
        0x000A,
        (
            '卢安是个水手之城\n',
            '所以本来就有很多性格刚烈的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '如果没有那样的毅力\n',
            '是无法忍受长时间航海的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3644')

    def _loc_324A(): pass

    label('loc_324A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Return,
        ),
        'loc_32AD',
    )

    ChrTalk(
        0x000A,
        (
            '刚才有位客人\n',
            '突然冲出店里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '发生了什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3644')

    def _loc_32AD(): pass

    label('loc_32AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_35C7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_3338',
    )

    ChrTalk(
        0x000A,
        (
            '游击士的工作需要到处奔波\n',
            '真是不容易啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '至少在你们待在卢安的时候\n',
            '好好休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35C4')

    def _loc_3338(): pass

    label('loc_3338')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_349E',
    )

    ChrTalk(
        0x000A,
        (
            '欢迎光临，游击士们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '你们的工作到处奔波\n',
            '确实很辛苦吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '没有时间安定下来\n',
            '遇见合适对象的机会也会减少……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '看来男性们成家的年龄\n',
            '也往往会比较晚呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#1028F哎～原来如此啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#552F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '喂，干嘛看着我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35C4')

    def _loc_349E(): pass

    label('loc_349E')

    ChrTalk(
        0x000A,
        (
            '欢迎光临，游击士们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '你们的工作需要到处奔波\n',
            '确实很辛苦吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '没有时间安定下来\n',
            '遇见合适对象的机会也会减少……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '看来也有很多女性\n',
            '因此完全错过了结婚的时机呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#023F（……………………）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '呵呵，开个小玩笑啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_35C4(): pass

    label('loc_35C4')

    Jump('loc_3644')

    def _loc_35C7(): pass

    label('loc_35C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_3644',
    )

    ChrTalk(
        0x000A,
        (
            '啊，欢迎光临。\n',
            '游击士们都到齐了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '现在卡露娜也不在，\n',
            '所以拜托你们多多费心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3644(): pass

    label('loc_3644')

    TalkEnd(0x000A)

    Return()

# id: 0x0004 offset: 0x3648
@scena.Code('func_04_3648')
def func_04_3648():
    Call(1, 0x0005)

    Return()

# id: 0x0005 offset: 0x364D
@scena.Code('func_05_364D')
def func_05_364D():
    TalkBegin(0x000B)
    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_367B',
    )

    OP_0D()

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3673',
    )

    OP_A9(0x6D)

    Jump('loc_3675')

    def _loc_3673(): pass

    label('loc_3673')

    OP_A9(0x66)

    def _loc_3675(): pass

    label('loc_3675')

    OP_56(0x00)
    TalkEnd(0x000B)

    Return()

    def _loc_367B(): pass

    label('loc_367B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_368C',
    )

    TalkEnd(0x000B)

    Return()

    def _loc_368C(): pass

    label('loc_368C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_37C6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_375E',
    )

    ChrTalk(
        0x000B,
        (
            '灯油和食品\n',
            '还有一些库存……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '如果这样的状态长久持续下去，\n',
            '恐怕很快也会见底吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '中央工房制的新型眼镜\n',
            '也陆续上市了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '特别是在灯灭了的地方使用，\n',
            '非常方便。\n',
            '来买几个好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_37C3')

    def _loc_375E(): pass

    label('loc_375E')

    ChrTalk(
        0x000B,
        (
            '中央工房制的新型眼镜\n',
            '也陆续上市了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '特别是在灯灭了的地方使用，\n',
            '非常方便。\n',
            '来买几个好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_37C3(): pass

    label('loc_37C3')

    Jump('loc_4011')

    def _loc_37C6(): pass

    label('loc_37C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3927',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_38B3',
    )

    ChrTalk(
        0x000B,
        (
            '唔，导力器停止\n',
            '真是不得了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这样的现象就连我\n',
            '也从来没见过啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '对了，\n',
            '说到前所未见……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '中央工房出产的\n',
            '新型眼镜上市了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '特别是在灯灭了的地方使用，\n',
            '非常方便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '如果没有，\n',
            '来买几个好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_3924')

    def _loc_38B3(): pass

    label('loc_38B3')

    ChrTalk(
        0x000B,
        (
            '中央工房出产的\n',
            '新型眼镜上市了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '特别是在灯灭了的地方使用，\n',
            '非常方便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '如果没有，\n',
            '来买几个好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3924(): pass

    label('loc_3924')

    Jump('loc_4011')

    def _loc_3927(): pass

    label('loc_3927')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_3A49',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_39A6',
    )

    ChrTalk(
        0x000B,
        (
            '仅靠港口收入支撑城市的开销\n',
            '是完全不行的，这是不争的事实。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '重视旅游也可以理解，\n',
            '不过感觉真有点寂寞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A46')

    def _loc_39A6(): pass

    label('loc_39A6')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x000B,
        (
            '身为前船员还是希望\n',
            '能想办法维持港口啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '仅靠港口收入支撑城市的开销\n',
            '是完全不行的，这是不争的事实。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '重视旅游也可以理解，\n',
            '不过感觉真有点寂寞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3A46(): pass

    label('loc_3A46')

    Jump('loc_4011')

    def _loc_3A49(): pass

    label('loc_3A49')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_3C24',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3A7F',
    )

    ChrTalk(
        0x000B,
        (
            '怎么，想听更多\n',
            '我的冒险故事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C21')

    def _loc_3A7F(): pass

    label('loc_3A7F')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x000B,
        (
            '好像发生了什么骚乱,\n',
            '呼…没什么大不了的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我年轻的时候参加过的\n',
            '某民族的选举，\n',
            '要过激得多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '那些家伙的选举很单纯。\n',
            '大家打群架，最后\n',
            '谁站着谁就是新的代表。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '当然我也被卷进去了。\n',
            '但是话虽如此，我也是\n',
            '身经百战的船长·欧尼尔啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '缓过神来的时候\n',
            '才发现只有我一个人站着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '哎呀，差点被\n',
            '他们选作新酋长，\n',
            '拼尽全力才逃到船上跑回来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '如果就那样当了酋长,\n',
            '应该也会过得很开心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '哇哈哈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C21(): pass

    label('loc_3C21')

    Jump('loc_4011')

    def _loc_3C24(): pass

    label('loc_3C24')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Return,
        ),
        'loc_3C6E',
    )

    ChrTalk(
        0x000B,
        (
            '唔～好像\n',
            '桥那边很吵闹啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '又～是年轻人\n',
            '在胡闹了吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4011')

    def _loc_3C6E(): pass

    label('loc_3C6E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_3E47',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3CF6',
    )

    ChrTalk(
        0x000B,
        (
            '要说没有选举的国家\n',
            '就是埃雷波尼亚帝国吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '以地方民主制度和王室\n',
            '分担职能的利贝尔\n',
            '可以说具有贤明的制度啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E44')

    def _loc_3CF6(): pass

    label('loc_3CF6')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x000B,
        (
            '没有选举的代表国家\n',
            '那就是埃雷波尼亚帝国吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '虽然在边境的自治区还有选举，\n',
            '但帝国中枢是严格的等级社会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '不过这样的制度\n',
            '运转顺利的时候还是挺好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '如果身份高贵的人中优秀的人很多，\n',
            '这个制度就会好得令人吃惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '当然反之\n',
            '就会惨不忍睹了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '嗯，这样看来将王权和选举\n',
            '完美分开使用的利贝尔\n',
            '可以说具有贤明的制度啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E44(): pass

    label('loc_3E44')

    Jump('loc_4011')

    def _loc_3E47(): pass

    label('loc_3E47')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_4011',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3ECA',
    )

    ChrTalk(
        0x000B,
        (
            '选举的做法也根据国家各自\n',
            '价值观的不同而大相径庭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '和我们相反选出『讨厌的人』\n',
            '然后赶出去的国家也存在哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4011')

    def _loc_3ECA(): pass

    label('loc_3ECA')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x000B,
        (
            '城市由于选举而热闹起来，\n',
            '虽说是选举，但各国制度各不一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '譬如利贝尔的市长选举制度\n',
            '是以共和国为范本的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '那个国家民族众多，\n',
            '因此需要公平的方法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '话说回来世界上和我们制度相反，\n',
            '选『讨厌的人』的国家也存在哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '在那里得票最多的不受欢迎者\n',
            '会从会议上被赶走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这个制度\n',
            '说不定很有道理哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '哇哈哈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4011(): pass

    label('loc_4011')

    TalkEnd(0x000B)

    Return()

# id: 0x0006 offset: 0x4015
@scena.Code('func_06_4015')
def func_06_4015():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_4026',
    )

    OP_2A(0x00B9, 0x00BA, 0xFFFF)

    Jump('loc_40A7')

    def _loc_4026(): pass

    label('loc_4026')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_4043',
    )

    OP_2A(0x0065, 0x0066, 0x00A1, 0x00A3, 0x0067, 0x0068, 0x00A2, 0x00A4, 0xFFFF)

    Jump('loc_40A7')

    def _loc_4043(): pass

    label('loc_4043')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_405E',
    )

    OP_2A(0x0065, 0x0066, 0x00A1, 0x00A3, 0x0067, 0x00A2, 0x00A4, 0xFFFF)

    Jump('loc_40A7')

    def _loc_405E(): pass

    label('loc_405E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_4073',
    )

    OP_2A(0x0065, 0x0066, 0x00A1, 0x00A3, 0xFFFF)

    Jump('loc_40A7')

    def _loc_4073(): pass

    label('loc_4073')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '没发出什么委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_40A7(): pass

    label('loc_40A7')

    TalkEnd(0x00FF)

    Return()

# id: 0x0007 offset: 0x40AB
@scena.Code('func_07_40AB')
def func_07_40AB():
    EventBegin(0x00)
    CameraMove(-32970, 0, 5800, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ChrClearFlags(0x0015, 0x0080)
    ChrSetPos(0x0009, -33640, 0, 6750, 0)
    ChrSetPos(0x0015, -29550, 0, 3100, 0)
    ChrSetPos(0x0101, -30640, 0, 3100, 0)
    ChrSetPos(0x00F7, -29970, 0, 1750, 0)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['朵洛希'])"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_4151',
    )

    ChrSetPos(0x0127, -31340, 0, 1210, 0)

    def _loc_4151(): pass

    label('loc_4151')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_416F',
    )

    ChrSetPos(0x0104, -31640, 0, 2480, 0)

    def _loc_416F(): pass

    label('loc_416F')

    OP_4A(0x0009, 255)

    @scena.Lambda('lambda_4179')
    def lambda_4179():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_4179')

    DispatchAsync2(0x0000, 0x0001, lambda_4179)

    @scena.Lambda('lambda_418A')
    def lambda_418A():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_418A')

    DispatchAsync2(0x0001, 0x0001, lambda_418A)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['朵洛希'])"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_41C4',
    )

    @scena.Lambda('lambda_41A8')
    def lambda_41A8():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_41A8')

    DispatchAsync2(0x0002, 0x0001, lambda_41A8)

    @scena.Lambda('lambda_41B9')
    def lambda_41B9():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_41B9')

    DispatchAsync2(0x0003, 0x0001, lambda_41B9)

    def _loc_41C4(): pass

    label('loc_41C4')

    @scena.Lambda('lambda_41CA')
    def lambda_41CA():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_41CA')

    DispatchAsync2(0x0015, 0x0001, lambda_41CA)

    FadeIn(2000, 0)
    OP_0D()
    Sleep(1000)

    @scena.Lambda('lambda_41EA')
    def lambda_41EA():
        CameraMove(-29850, 0, 3090, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_41EA)

    ChrWalkTo(0x0009, -30590, 0, 6050, 2000, 0x00)
    ChrWalkTo(0x0009, -30000, 0, 4910, 2000, 0x00)
    ChrSetDirection(0x0009, 180, 400)
    Sleep(400)

    WaitForThreadExit(0x0000, 0x0002)
    TerminateThread(0x0015, 0xFF)
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['朵洛希'])"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_4256',
    )

    TerminateThread(0x0002, 0xFF)
    TerminateThread(0x0003, 0xFF)

    def _loc_4256(): pass

    label('loc_4256')

    ChrTalk(
        0x0009,
        (
            '#1750430428V好，完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#2930430429V……嗯，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_429A')
    def lambda_429A():
        ChrTurnDirection(0x00FE, 0x0015, 400)
        Yield()

        Jump('lambda_429A')

    DispatchAsync2(0x0000, 0x0001, lambda_429A)

    @scena.Lambda('lambda_42AB')
    def lambda_42AB():
        ChrTurnDirection(0x00FE, 0x0015, 400)
        Yield()

        Jump('lambda_42AB')

    DispatchAsync2(0x0001, 0x0001, lambda_42AB)

    @scena.Lambda('lambda_42BC')
    def lambda_42BC():
        ChrTurnDirection(0x00FE, 0x0015, 400)
        Yield()

        Jump('lambda_42BC')

    DispatchAsync2(0x0002, 0x0001, lambda_42BC)

    @scena.Lambda('lambda_42CD')
    def lambda_42CD():
        ChrTurnDirection(0x00FE, 0x0015, 400)
        Yield()

        Jump('lambda_42CD')

    DispatchAsync2(0x0003, 0x0001, lambda_42CD)

    ChrTalk(
        0x0015,
        (
            '#2930430430V好～了，看看照得怎样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    OP_62(0x0015, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(3000)

    OP_63(0x0015)
    Sleep(1000)

    ChrTurnDirection(0x0015, 0x0101, 400)
    Sleep(400)

    If(
        (
            (Expr.Eval, "OP_29(0x0066, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_473E',
    )

    ChrTalk(
        0x0015,
        (
            '#2930430431V……啊，真令人惊讶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#2930430432V专业人士看了都会惊讶的……不，\n',
            '说白了就是超越专业人士的水准了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430433V#1004F那，那么厉害吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#2930430434V看，请看呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    FadeOut(300, 0, 100)
    OP_C5(0x00, 0, 0, 600, 300, 20, 90, 640, 300, 0, 0, 600, 300, 0x00FFFFFF, 0x00, 'C_VIS198._CH')
    OP_C6(0x00, 0x03, -1, 500, 0)
    Sleep(2000)

    SetMessageWindowPos(50, 50, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010430435V#1011F哎呀～确实漂亮啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(360, 340, -1, -1)
    TalkSetChrName('森特')

    Talk(
        (
            '#2930430436V嗯，十分难得的是\n',
            '焦点也对得非常准确……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(360, 340, -1, -1)
    TalkSetChrName('森特')

    Talk(
        (
            '#2930430437V不～不管怎么说\n',
            '这光线的处理实在是绝妙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(360, 340, -1, -1)
    TalkSetChrName('森特')

    Talk(
        (
            '#2930430438V『装置』的漫长历史\n',
            '光是在照片里看就能感受到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(360, 340, -1, -1)
    TalkSetChrName('森特')

    Talk(
        (
            '#2930430439V这照片\n',
            '足够作为研究资料了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(360, 340, -1, -1)
    TalkSetChrName('森特')

    Talk(
        (
            '#2930430440V这照片作为保留资料\n',
            '真是太可惜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(50, 50, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010310379V#1004F是、是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430442V#1016F啊、哈～好深奥啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(50, 250, -1, -1)
    TalkSetChrName('朵洛希')

    Talk(
        (
            '#0280430443V#151F嘿嘿～了不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x00, 0x03, 16777215, 500, 0)
    FadeIn(300, 0)
    OP_0D()
    OP_C6(0x00, 0x06, 0, 0, 0)
    Sleep(1500)

    OP_C7(0x01, 0xFF, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_46F1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430444V#051F……那，这样就算完成工作了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_472B')

    def _loc_46F1(): pass

    label('loc_46F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_472B',
    )

    ChrTalk(
        0x0103,
        (
            '#0030430445V#020F那么，这样就算完成工作了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_472B(): pass

    label('loc_472B')

    OP_2B(0x0066, 0x0002)
    OP_2C(0x0066, 0x03E8)
    OP_28(0x0066, 0x01, 0x0010)

    Jump('loc_4BEA')

    def _loc_473E(): pass

    label('loc_473E')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Neg,
            Expr.Lss,
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Gtr,
            Expr.Or,
            Expr.Return,
        ),
        'loc_47AF',
    )

    ChrTalk(
        0x0015,
        (
            '#2930430446V……嗯……马马虎虎吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#2930430447V作为资料来说还算能用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0066, 0x01, 0x0080)

    Jump('loc_485E')

    def _loc_47AF(): pass

    label('loc_47AF')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4801',
    )

    ChrTalk(
        0x0015,
        (
            '#2930430448V……嗯，做得好哦。\n',
            '完全没有问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x0066, 0x0001)
    OP_2C(0x0066, 0x03E8)
    OP_28(0x0066, 0x01, 0x0020)

    Jump('loc_485E')

    def _loc_4801(): pass

    label('loc_4801')

    ChrTalk(
        0x0015,
        (
            '#2930430449V……嗯……马马虎虎吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#2930430450V作为资料来说还算能用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2C(0x0066, 0x01F4)
    OP_28(0x0066, 0x01, 0x0040)

    def _loc_485E(): pass

    label('loc_485E')

    ChrTalk(
        0x0015,
        (
            '#2930430451V要看看吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430452V#1018F嗯，看啊看啊⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    FadeOut(300, 0, 100)
    Call(1, 0x0008)
    OP_C5(0x01, 0, 0, 400, 300, 120, 90, 640, 300, 0, 0, 400, 300, 0x00FFFFFF, 0x00, 'C_VIS199._CH')
    OP_C6(0x01, 0x03, -1, 500, 0)
    OP_C6(0x00, 0x03, -1, 500, 0)
    Sleep(2000)

    SetMessageWindowPos(50, 50, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010430453V#1001F啊，太好了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430454V比想象的\n',
            '拍得还漂亮嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_49A7',
    )

    SetMessageWindowPos(250, 50, -1, -1)
    TalkSetChrName('奥利维尔')

    Talk(
        (
            '#2930430455V#031F光线掌握得很好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_49A7(): pass

    label('loc_49A7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['朵洛希'])"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_49EC',
    )

    SetMessageWindowPos(50, 300, -1, -1)
    TalkSetChrName('朵洛希')

    Talk(
        (
            '#2930430456V#150F嗯，拍得很棒嘛⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_49EC(): pass

    label('loc_49EC')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Neg,
            Expr.Lss,
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Gtr,
            Expr.Or,
            Expr.Return,
        ),
        'loc_4AF2',
    )

    SetMessageWindowPos(360, 340, -1, -1)
    TalkSetChrName('森特')

    Talk(
        (
            '#2930430457V很遗憾啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(360, 340, -1, -1)
    TalkSetChrName('森特')

    Talk(
        (
            '#2930430458V因为是资料照片，可以的话\n',
            '最好从正面拍摄哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(50, 50, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010430459V#1008F呜，也对啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430460V不，不知不觉就得意忘形的\n',
            '从奇怪的角度拍摄了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_4B30')

    def _loc_4AF2(): pass

    label('loc_4AF2')

    SetMessageWindowPos(360, 340, -1, -1)
    TalkSetChrName('森特')

    Talk(
        (
            '#2930430461V嗯，这样的话\n',
            '我也能够认可哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_4B30(): pass

    label('loc_4B30')

    OP_C6(0x00, 0x03, 16777215, 500, 0)
    OP_C6(0x01, 0x03, 16777215, 500, 0)
    FadeIn(300, 0)
    OP_0D()
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    Sleep(1500)

    OP_C7(0x01, 0xFF, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4BB6',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430462V#050F这样就算完成工作了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4BEA')

    def _loc_4BB6(): pass

    label('loc_4BB6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_4BEA',
    )

    ChrTalk(
        0x0103,
        (
            '#0030430463V#020F这样就算完成工作了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4BEA(): pass

    label('loc_4BEA')

    ChrTurnDirection(0x0015, 0x00F7, 400)

    ChrTalk(
        0x0015,
        (
            '#2930430464V是，没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#2930430465V呀～各位，\n',
            '真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#2930430466V特意麻烦你们\n',
            '去绀碧之塔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430467V#1015F嗯，确实挺辛苦的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430468V#1006F不过，这也是工作嘛。\n',
            '请别介意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#2930430469V啊哈哈，这么说\n',
            '我就感觉轻松多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#2930430470V对了。\n',
            '虽说也算不上什么谢礼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#2930430471V……请收下这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['月亮眼镜']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['月亮眼镜'], 1)
    Sleep(500)

    ChrTalk(
        0x0015,
        (
            '#2930430472V这是为了此次调查，\n',
            '用研究费购买的物品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#2930430473V去危险的地方时\n',
            '我想一定能帮上忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430474V#1001F嘿嘿，谢谢⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430475V难得你一番好意，\n',
            '就不客气地接受喽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4E8E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430476V#051F不好意思呢。\n',
            '让你破费了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4EC5')

    def _loc_4E8E(): pass

    label('loc_4E8E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_4EC5',
    )

    ChrTalk(
        0x0103,
        (
            '#0030430477V#020F不好意思啊。\n',
            '让你破费了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4EC5(): pass

    label('loc_4EC5')

    ChrTalk(
        0x0015,
        (
            '#2930430478V哪里哪里。\n',
            '也不是什么大不了的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#2930430479V……那么，差不多了，\n',
            '我先告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#2930430480V今天非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430481V#1000F你也要加油\n',
            '继续努力对『装置』的调查哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430482V许多地方都挺令人好奇的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0015, 0x0101, 400)
    OP_62(0x0015, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0015,
        (
            '#2930430483V啊，啊哈哈……\n',
            '那也是辛苦的工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#2930430484V不过，为了不负期待，\n',
            '我们也会尽最大努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#2930430485V……那么，我就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430486V#1006F嗯，那再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrSetDirection(0x0015, 180, 400)

    @scena.Lambda('lambda_50A4')
    def lambda_50A4():
        ChrMoveToRelativeAsync(0x00FE, -400, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0002, lambda_50A4)

    ChrWalkTo(0x0015, -29550, 0, -1000, 2000, 0x01)
    ChrSetRGBAMask(0x0015, 255, 255, 255, 255, 0)

    @scena.Lambda('lambda_50DE')
    def lambda_50DE():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x0015, 0x0002, lambda_50DE)

    ChrWalkTo(0x0015, -29550, -518, -2700, 2000, 0x00)
    WaitForThreadExit(0x0015, 0x0002)
    ChrSetFlags(0x0015, 0x0080)
    Sleep(1500)

    TerminateThread(0x0000, 0x01)
    TerminateThread(0x0001, 0x01)
    TerminateThread(0x0002, 0x01)
    TerminateThread(0x0003, 0x01)
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【『绀碧之塔』的照片拍摄】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x0066, 0x01, 0x0100)
    OP_28(0x0066, 0x04, 0x10)
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_4B(0x0009, 255)
    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0x5197
@scena.Code('func_08_5197')
def func_08_5197():
    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_51D2',
    )

    OP_C5(0x00, 0, 0, 400, 300, 120, 90, 640, 300, 120, 0, 520, 300, 0x00FFFFFF, 0x00, 'C_VIS195._CH')

    Jump('loc_5510')

    def _loc_51D2(): pass

    label('loc_51D2')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_520E',
    )

    OP_C5(0x00, 0, 0, 400, 300, 120, 90, 640, 300, 100, 0, 500, 300, 0x00FFFFFF, 0x00, 'C_VIS195._CH')

    Jump('loc_5510')

    def _loc_520E(): pass

    label('loc_520E')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5249',
    )

    OP_C5(0x00, 0, 0, 400, 300, 120, 90, 640, 300, 140, 0, 540, 300, 0x00FFFFFF, 0x00, 'C_VIS195._CH')

    Jump('loc_5510')

    def _loc_5249(): pass

    label('loc_5249')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5285',
    )

    OP_C5(0x00, 0, 0, 400, 300, 120, 90, 640, 300, 80, 0, 480, 300, 0x00FFFFFF, 0x00, 'C_VIS195._CH')

    Jump('loc_5510')

    def _loc_5285(): pass

    label('loc_5285')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_52C0',
    )

    OP_C5(0x00, 0, 0, 400, 300, 120, 90, 640, 300, 160, 0, 560, 300, 0x00FFFFFF, 0x00, 'C_VIS195._CH')

    Jump('loc_5510')

    def _loc_52C0(): pass

    label('loc_52C0')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_52FC',
    )

    OP_C5(0x00, 0, 0, 400, 300, 120, 90, 640, 300, 60, 0, 460, 300, 0x00FFFFFF, 0x00, 'C_VIS195._CH')

    Jump('loc_5510')

    def _loc_52FC(): pass

    label('loc_52FC')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5337',
    )

    OP_C5(0x00, 0, 0, 400, 300, 120, 90, 640, 300, 180, 0, 580, 300, 0x00FFFFFF, 0x00, 'C_VIS195._CH')

    Jump('loc_5510')

    def _loc_5337(): pass

    label('loc_5337')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5373',
    )

    OP_C5(0x00, 0, 0, 400, 300, 120, 90, 640, 300, 20, 0, 420, 300, 0x00FFFFFF, 0x00, 'C_VIS195._CH')

    Jump('loc_5510')

    def _loc_5373(): pass

    label('loc_5373')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_53AE',
    )

    OP_C5(0x00, 0, 0, 400, 300, 120, 90, 640, 300, 220, 0, 620, 300, 0x00FFFFFF, 0x00, 'C_VIS195._CH')

    Jump('loc_5510')

    def _loc_53AE(): pass

    label('loc_53AE')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_53EA',
    )

    OP_C5(0x00, 0, 0, 400, 300, 120, 90, 640, 300, 60, 0, 460, 300, 0x00FFFFFF, 0x00, 'C_VIS196._CH')

    Jump('loc_5510')

    def _loc_53EA(): pass

    label('loc_53EA')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5426',
    )

    OP_C5(0x00, 0, 0, 400, 300, 120, 90, 640, 300, 120, 0, 520, 300, 0x00FFFFFF, 0x00, 'C_VIS196._CH')

    Jump('loc_5510')

    def _loc_5426(): pass

    label('loc_5426')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5462',
    )

    OP_C5(0x00, 0, 0, 400, 300, 120, 90, 640, 300, 220, 0, 620, 300, 0x00FFFFFF, 0x00, 'C_VIS196._CH')

    Jump('loc_5510')

    def _loc_5462(): pass

    label('loc_5462')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_549D',
    )

    OP_C5(0x00, 0, 0, 400, 300, 120, 90, 640, 300, 180, 0, 580, 300, 0x00FFFFFF, 0x00, 'C_VIS197._CH')

    Jump('loc_5510')

    def _loc_549D(): pass

    label('loc_549D')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_54D8',
    )

    OP_C5(0x00, 0, 0, 400, 300, 120, 90, 640, 300, 60, 0, 460, 300, 0x00FFFFFF, 0x00, 'C_VIS197._CH')

    Jump('loc_5510')

    def _loc_54D8(): pass

    label('loc_54D8')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5510',
    )

    OP_C5(0x00, 0, 0, 400, 300, 120, 90, 640, 300, 20, 0, 420, 300, 0x00FFFFFF, 0x00, 'C_VIS197._CH')

    def _loc_5510(): pass

    label('loc_5510')

    Return()

# id: 0x0009 offset: 0x5511
@scena.Code('func_09_5511')
def func_09_5511():
    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0151, 0x01)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5532',
    )

    RemoveItem(ItemTable['零力场发生器'], 1)

    Jump('loc_5A4A')

    def _loc_5532(): pass

    label('loc_5532')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFF),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5A4A',
    )

    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '请选择取下零力场发生器的成员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_CC(0x00, 0x00, 0x000A, 0x000A, 0x00)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x0, 0x1F),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            (Expr.GetChrWork, 0x0, 0x20),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_559B',
    )

    Call(1, 0x000A)

    Jump('loc_559F')

    def _loc_559B(): pass

    label('loc_559B')

    Call(1, 0x000B)

    def _loc_559F(): pass

    label('loc_559F')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushValueByIndex, 0xB),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x1, 0x1F),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            (Expr.GetChrWork, 0x1, 0x20),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_55C6',
    )

    Call(1, 0x000A)

    Jump('loc_55CA')

    def _loc_55C6(): pass

    label('loc_55C6')

    Call(1, 0x000B)

    def _loc_55CA(): pass

    label('loc_55CA')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushValueByIndex, 0xC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x2, 0x1F),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            (Expr.GetChrWork, 0x2, 0x20),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_55F1',
    )

    Call(1, 0x000A)

    Jump('loc_55F5')

    def _loc_55F1(): pass

    label('loc_55F1')

    Call(1, 0x000B)

    def _loc_55F5(): pass

    label('loc_55F5')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushValueByIndex, 0xD),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x3, 0x1F),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            (Expr.GetChrWork, 0x3, 0x20),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_561C',
    )

    Call(1, 0x000A)

    Jump('loc_5620')

    def _loc_561C(): pass

    label('loc_561C')

    Call(1, 0x000B)

    def _loc_5620(): pass

    label('loc_5620')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_CC(0x02, 0x00)
    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMessageWindowPos(72, 320, 56, 3)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_5667'),
        (0x00000001, 'loc_56AD'),
        (0x00000002, 'loc_56F3'),
        (0x00000003, 'loc_5739'),
        (-1, 'loc_577F'),
    )

    def _loc_5667(): pass

    label('loc_5667')

    If(
        (
            (Expr.GetChrWork, 0x0, 0x1F),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_568A',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x1F,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_56AA')

    def _loc_568A(): pass

    label('loc_568A')

    If(
        (
            (Expr.GetChrWork, 0x0, 0x20),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_56AA',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x20,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_56AA(): pass

    label('loc_56AA')

    Jump('loc_577F')

    def _loc_56AD(): pass

    label('loc_56AD')

    If(
        (
            (Expr.GetChrWork, 0x1, 0x1F),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_56D0',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushValueByIndex, 0xB),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x1F,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_56F0')

    def _loc_56D0(): pass

    label('loc_56D0')

    If(
        (
            (Expr.GetChrWork, 0x1, 0x20),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_56F0',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushValueByIndex, 0xB),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x20,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_56F0(): pass

    label('loc_56F0')

    Jump('loc_577F')

    def _loc_56F3(): pass

    label('loc_56F3')

    If(
        (
            (Expr.GetChrWork, 0x2, 0x1F),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5716',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushValueByIndex, 0xC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x1F,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5736')

    def _loc_5716(): pass

    label('loc_5716')

    If(
        (
            (Expr.GetChrWork, 0x2, 0x20),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5736',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushValueByIndex, 0xC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x20,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_5736(): pass

    label('loc_5736')

    Jump('loc_577F')

    def _loc_5739(): pass

    label('loc_5739')

    If(
        (
            (Expr.GetChrWork, 0x3, 0x1F),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_575C',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushValueByIndex, 0xD),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0003,
        0x1F,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_577C')

    def _loc_575C(): pass

    label('loc_575C')

    If(
        (
            (Expr.GetChrWork, 0x3, 0x20),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_577C',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushValueByIndex, 0xD),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0003,
        0x20,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_577C(): pass

    label('loc_577C')

    Jump('loc_577F')

    def _loc_577F(): pass

    label('loc_577F')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFF),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_57A8',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '未装备零力场发生器。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_5A3B')

    def _loc_57A8(): pass

    label('loc_57A8')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_57F0',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔已取下零力场发生器，\n',
            '所以暂时无法使用魔法。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_5A3B')

    def _loc_57F0(): pass

    label('loc_57F0')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5836',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚已取下零力场发生器，\n',
            '所以暂时无法使用魔法。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_5A3B')

    def _loc_5836(): pass

    label('loc_5836')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_587E',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '雪拉扎德已取下零力场发生器，\n',
            '所以暂时无法使用魔法。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_5A3B')

    def _loc_587E(): pass

    label('loc_587E')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_58C6',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '奥利维尔已取下零力场发生器，\n',
            '所以暂时无法使用魔法。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_5A3B')

    def _loc_58C6(): pass

    label('loc_58C6')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_590C',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '科洛丝已取下零力场发生器，\n',
            '所以暂时无法使用魔法。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_5A3B')

    def _loc_590C(): pass

    label('loc_590C')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5952',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '阿加特已取下零力场发生器，\n',
            '所以暂时无法使用魔法。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_5A3B')

    def _loc_5952(): pass

    label('loc_5952')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_59BC',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '提妲已取下零力场发生器，\n',
            '无法使用魔法，战技，普通攻击。\n',
            '但S战技『炮射冲击』仍可使用。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_5A3B')

    def _loc_59BC(): pass

    label('loc_59BC')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_59FC',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '金已取下零力场发生器\n',
            '所以暂时无法使用魔法。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_5A3B')

    def _loc_59FC(): pass

    label('loc_59FC')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5A3B',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '凯文已取下零力场发生器\n',
            '所以暂时无法使用魔法。',
            TxtCtl.Enter,
        ),
    )

    def _loc_5A3B(): pass

    label('loc_5A3B')

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    Jump('loc_5532')

    def _loc_5A4A(): pass

    label('loc_5A4A')

    Return()

# id: 0x000A offset: 0x5A4B
@scena.Code('func_0A_5A4B')
def func_0A_5A4B():
    Switch(
        (
            (Expr.PushReg, 0x2),
            Expr.Return,
        ),
        (0x00000000, 'loc_5A78'),
        (0x00000001, 'loc_5A93'),
        (0x00000002, 'loc_5AAC'),
        (0x00000003, 'loc_5AC7'),
        (0x00000004, 'loc_5AE2'),
        (0x00000005, 'loc_5AFB'),
        (0x00000006, 'loc_5B14'),
        (0x00000007, 'loc_5B2B'),
        (0x00000008, 'loc_5B40'),
        (-1, 'loc_5B57'),
    )

    def _loc_5A78(): pass

    label('loc_5A78')

    OP_CC(0x01, 0x00, '【艾丝蒂尔　装备中】')

    Jump('loc_5B57')

    def _loc_5A93(): pass

    label('loc_5A93')

    OP_CC(0x01, 0x00, '【约修亚　装备中】')

    Jump('loc_5B57')

    def _loc_5AAC(): pass

    label('loc_5AAC')

    OP_CC(0x01, 0x00, '【雪拉扎德　装备中】')

    Jump('loc_5B57')

    def _loc_5AC7(): pass

    label('loc_5AC7')

    OP_CC(0x01, 0x00, '【奥利维尔　装备中】')

    Jump('loc_5B57')

    def _loc_5AE2(): pass

    label('loc_5AE2')

    OP_CC(0x01, 0x00, '【科洛丝　装备中】')

    Jump('loc_5B57')

    def _loc_5AFB(): pass

    label('loc_5AFB')

    OP_CC(0x01, 0x00, '【阿加特　装备中】')

    Jump('loc_5B57')

    def _loc_5B14(): pass

    label('loc_5B14')

    OP_CC(0x01, 0x00, '【提妲　装备中】')

    Jump('loc_5B57')

    def _loc_5B2B(): pass

    label('loc_5B2B')

    OP_CC(0x01, 0x00, '【金　装备中】')

    Jump('loc_5B57')

    def _loc_5B40(): pass

    label('loc_5B40')

    OP_CC(0x01, 0x00, '【凯文　装备中】')

    Jump('loc_5B57')

    def _loc_5B57(): pass

    label('loc_5B57')

    Return()

# id: 0x000B offset: 0x5B58
@scena.Code('func_0B_5B58')
def func_0B_5B58():
    Switch(
        (
            (Expr.PushReg, 0x2),
            Expr.Return,
        ),
        (0x00000000, 'loc_5B85'),
        (0x00000001, 'loc_5BA0'),
        (0x00000002, 'loc_5BB9'),
        (0x00000003, 'loc_5BD4'),
        (0x00000004, 'loc_5BEF'),
        (0x00000005, 'loc_5C08'),
        (0x00000006, 'loc_5C21'),
        (0x00000007, 'loc_5C38'),
        (0x00000008, 'loc_5C4D'),
        (-1, 'loc_5C64'),
    )

    def _loc_5B85(): pass

    label('loc_5B85')

    OP_CC(0x01, 0x00, '【艾丝蒂尔　未装备】')

    Jump('loc_5C64')

    def _loc_5BA0(): pass

    label('loc_5BA0')

    OP_CC(0x01, 0x00, '【约修亚　未装备】')

    Jump('loc_5C64')

    def _loc_5BB9(): pass

    label('loc_5BB9')

    OP_CC(0x01, 0x00, '【雪拉扎德　未装备】')

    Jump('loc_5C64')

    def _loc_5BD4(): pass

    label('loc_5BD4')

    OP_CC(0x01, 0x00, '【奥利维尔　未装备】')

    Jump('loc_5C64')

    def _loc_5BEF(): pass

    label('loc_5BEF')

    OP_CC(0x01, 0x00, '【科洛丝　未装备】')

    Jump('loc_5C64')

    def _loc_5C08(): pass

    label('loc_5C08')

    OP_CC(0x01, 0x00, '【阿加特　未装备】')

    Jump('loc_5C64')

    def _loc_5C21(): pass

    label('loc_5C21')

    OP_CC(0x01, 0x00, '【提妲　未装备】')

    Jump('loc_5C64')

    def _loc_5C38(): pass

    label('loc_5C38')

    OP_CC(0x01, 0x00, '【金　未装备】')

    Jump('loc_5C64')

    def _loc_5C4D(): pass

    label('loc_5C4D')

    OP_CC(0x01, 0x00, '【凯文　未装备】')

    Jump('loc_5C64')

    def _loc_5C64(): pass

    label('loc_5C64')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
