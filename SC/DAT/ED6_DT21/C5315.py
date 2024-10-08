import sys
sys.path.append(r'C:\nw_profile\IDE\pycharm\pycharmProj\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5315_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5315   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5315.x'
    header.mapIndex       = 1
    header.bgm            = 35
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
        ScenaNpcData(
            name                = '德尔基昂①',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '德尔基昂②',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0xE8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xE8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xE8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xE8
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_F6',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_02_11C)

    def _loc_F6(): pass

    label('loc_F6')

    Return()

# id: 0x0001 offset: 0xF7
@scena.Code('func_01_F7')
def func_01_F7():
    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x450),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_111',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlaySE(235, 0x01, 0x64)

    def _loc_111(): pass

    label('loc_111')

    OP_71(0x0000, 0x0004)
    OP_71(0x0002, 0x0004)

    Return()

# id: 0x0002 offset: 0x11C
@scena.Code('func_02_11C')
def func_02_11C():
    Call(0, 0x0003)
    Call(0, 0x0004)

    Return()

# id: 0x0003 offset: 0x125
@scena.Code('func_03_125')
def func_03_125():
    EventBegin(0x00)
    OP_C0(0x15, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_161',
    )

    Call(0, 0x0008)
    Call(0, 0x0009)
    FormationDelMember(0x01, 0xFF)

    def _loc_161(): pass

    label('loc_161')

    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 0)
    LoadChip('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP', 1)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_1A6'),
        (0x00000005, 'loc_1BD'),
        (0x00000003, 'loc_1D4'),
        (0x00000004, 'loc_1EB'),
        (0x00000006, 'loc_202'),
        (0x00000007, 'loc_219'),
        (0x00000008, 'loc_230'),
        (0x0000000A, 'loc_247'),
        (0x0000000E, 'loc_25E'),
        (0x0000000F, 'loc_275'),
        (-1, 'loc_28C'),
    )

    def _loc_1A6(): pass

    label('loc_1A6')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 2)
    LoadChip('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP', 3)

    Jump('loc_28C')

    def _loc_1BD(): pass

    label('loc_1BD')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 2)
    LoadChip('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP', 3)

    Jump('loc_28C')

    def _loc_1D4(): pass

    label('loc_1D4')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 2)
    LoadChip('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP', 3)

    Jump('loc_28C')

    def _loc_1EB(): pass

    label('loc_1EB')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 2)
    LoadChip('ED6_DT27/CH04211._CH', 'ED6_DT27/CH04211P._CP', 3)

    Jump('loc_28C')

    def _loc_202(): pass

    label('loc_202')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 2)
    LoadChip('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP', 3)

    Jump('loc_28C')

    def _loc_219(): pass

    label('loc_219')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 2)
    LoadChip('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP', 3)

    Jump('loc_28C')

    def _loc_230(): pass

    label('loc_230')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 2)
    LoadChip('ED6_DT27/CH04081._CH', 'ED6_DT27/CH04081P._CP', 3)

    Jump('loc_28C')

    def _loc_247(): pass

    label('loc_247')

    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 2)
    LoadChip('ED6_DT07/CH00311._CH', 'ED6_DT07/CH00311P._CP', 3)

    Jump('loc_28C')

    def _loc_25E(): pass

    label('loc_25E')

    LoadChip('ED6_DT27/CH04580._CH', 'ED6_DT27/CH04580P._CP', 2)
    LoadChip('ED6_DT27/CH04581._CH', 'ED6_DT27/CH04581P._CP', 3)

    Jump('loc_28C')

    def _loc_275(): pass

    label('loc_275')

    LoadChip('ED6_DT27/CH04570._CH', 'ED6_DT27/CH04570P._CP', 2)
    LoadChip('ED6_DT27/CH04571._CH', 'ED6_DT27/CH04571P._CP', 3)

    Jump('loc_28C')

    def _loc_28C(): pass

    label('loc_28C')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_2BD'),
        (0x00000005, 'loc_2D4'),
        (0x00000003, 'loc_2EB'),
        (0x00000004, 'loc_302'),
        (0x00000006, 'loc_319'),
        (0x00000007, 'loc_330'),
        (0x00000008, 'loc_347'),
        (0x0000000A, 'loc_35E'),
        (0x0000000E, 'loc_375'),
        (0x0000000F, 'loc_38C'),
        (-1, 'loc_3A3'),
    )

    def _loc_2BD(): pass

    label('loc_2BD')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 4)
    LoadChip('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP', 5)

    Jump('loc_3A3')

    def _loc_2D4(): pass

    label('loc_2D4')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 4)
    LoadChip('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP', 5)

    Jump('loc_3A3')

    def _loc_2EB(): pass

    label('loc_2EB')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 4)
    LoadChip('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP', 5)

    Jump('loc_3A3')

    def _loc_302(): pass

    label('loc_302')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 4)
    LoadChip('ED6_DT27/CH04211._CH', 'ED6_DT27/CH04211P._CP', 5)

    Jump('loc_3A3')

    def _loc_319(): pass

    label('loc_319')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 4)
    LoadChip('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP', 5)

    Jump('loc_3A3')

    def _loc_330(): pass

    label('loc_330')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 4)
    LoadChip('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP', 5)

    Jump('loc_3A3')

    def _loc_347(): pass

    label('loc_347')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 4)
    LoadChip('ED6_DT27/CH04081._CH', 'ED6_DT27/CH04081P._CP', 5)

    Jump('loc_3A3')

    def _loc_35E(): pass

    label('loc_35E')

    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 4)
    LoadChip('ED6_DT07/CH00311._CH', 'ED6_DT07/CH00311P._CP', 5)

    Jump('loc_3A3')

    def _loc_375(): pass

    label('loc_375')

    LoadChip('ED6_DT27/CH04580._CH', 'ED6_DT27/CH04580P._CP', 4)
    LoadChip('ED6_DT27/CH04581._CH', 'ED6_DT27/CH04581P._CP', 5)

    Jump('loc_3A3')

    def _loc_38C(): pass

    label('loc_38C')

    LoadChip('ED6_DT27/CH04570._CH', 'ED6_DT27/CH04570P._CP', 4)
    LoadChip('ED6_DT27/CH04571._CH', 'ED6_DT27/CH04571P._CP', 5)

    Jump('loc_3A3')

    def _loc_3A3(): pass

    label('loc_3A3')

    OP_12(0x00007530, 0x000493E0, 0x00000000)
    CameraMove(270, 1350, 1450, 0)
    OP_67(0, 12650, -10000, 0)
    CameraSetDistance(4090, 0)
    OP_6C(27000, 0)
    OP_6E(514, 0)
    OP_6F(0x0001, 30)
    OP_70(0x0001, 270)
    ChrSetPos(0x0101, 0, 1350, 1000, 0)
    ChrSetPos(0x00F8, -1000, 1350, -1000, 225)
    ChrSetPos(0x00F9, 1000, 1350, -1000, 135)
    FadeIn(1000, 0)
    OP_12(0x00007530, 0x00027100, 0x00001F40)

    @scena.Lambda('lambda_044A')
    def lambda_044A():
        CameraMove(300, 1350, -10, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_044A)

    @scena.Lambda('lambda_0462')
    def lambda_0462():
        OP_67(0, 7550, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0462)

    @scena.Lambda('lambda_047A')
    def lambda_047A():
        CameraSetDistance(2800, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_047A)

    @scena.Lambda('lambda_048A')
    def lambda_048A():
        OP_6C(45000, 8000)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_048A)

    @scena.Lambda('lambda_049A')
    def lambda_049A():
        OP_6E(320, 8000)

        ExitThread()

    DispatchAsync(0x00F9, 0x0002, lambda_049A)

    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_51D',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420001V#212F想不到这原来是\n',
            '升降梯的传动轴……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090420002V到底会下降到什么地方呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8BC')

    def _loc_51D(): pass

    label('loc_51D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_59F',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420003V#276F没想到竟然是\n',
            '电梯井道啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110420004V……而且还相当深………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8BC')

    def _loc_59F(): pass

    label('loc_59F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_60E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420005V#057F想不到这原来是\n',
            '升降梯的传动轴……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050420006V到底会下降到什么地方呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8BC')

    def _loc_60E(): pass

    label('loc_60E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_67D',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420007V#022F想不到这原来是\n',
            '升降梯的传动轴……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030420008V到底会下降到什么地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8BC')

    def _loc_67D(): pass

    label('loc_67D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6ED',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420009V#1163F想不到这原来是\n',
            '升降梯的传动轴……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060420010V到底会下降到什么地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8BC')

    def _loc_6ED(): pass

    label('loc_6ED')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_75C',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420011V#032F想不到这原来是\n',
            '升降梯的传动轴……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040420012V到底会下降到什么地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8BC')

    def _loc_75C(): pass

    label('loc_75C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7E0',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420013V#178F没想到竟然是\n',
            '电梯井道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100420014V这到底会降到多深呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8BC')

    def _loc_7E0(): pass

    label('loc_7E0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_850',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420015V#1063F想不到这原来是\n',
            '升降梯的传动轴……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180420016V到底会下降到什么地方呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8BC')

    def _loc_850(): pass

    label('loc_850')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8BC',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420017V#072F想不到这原来是\n',
            '升降梯的传动轴……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080420018V到底会下降到什么地方呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8BC(): pass

    label('loc_8BC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_940',
    )

    ChrTalk(
        0x0107,
        (
            '#0070420019V#063F……好像这纵坑的深度\n',
            '比中枢塔的高度还要厉害。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070420020V可能会下降到\n',
            '浮游都市的中心部……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D8B')

    def _loc_940(): pass

    label('loc_940')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9C0',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420021V#072F好像这纵坑的深度\n',
            '比中枢塔的高度还要厉害……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080420022V可能会下降到\n',
            '浮游都市的中心部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D8B')

    def _loc_9C0(): pass

    label('loc_9C0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A41',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420023V#1063F好像这纵坑的深度\n',
            '比中枢塔的高度还要厉害……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180420024V可能会下降到\n',
            '浮游都市的中心部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D8B')

    def _loc_A41(): pass

    label('loc_A41')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AEA',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420025V#178F看起来这似乎是\n',
            '一个比中枢塔还要深得多的竖井……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100420026V按这个趋势，可能会\n',
            '一直降到浮游都市的中心部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D8B')

    def _loc_AEA(): pass

    label('loc_AEA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B6A',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420027V#032F好像这纵坑的深度\n',
            '比中枢塔的高度还要厉害……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040420028V可能会下降到\n',
            '浮游都市的中心部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D8B')

    def _loc_B6A(): pass

    label('loc_B6A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BEB',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420029V#1163F好像这纵坑的深度\n',
            '比中枢塔的高度还要厉害……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060420030V可能会下降到\n',
            '浮游都市的中心部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D8B')

    def _loc_BEB(): pass

    label('loc_BEB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C6B',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420031V#022F好像这纵坑的深度\n',
            '比中枢塔的高度还要厉害……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030420032V可能会下降到\n',
            '浮游都市的中心部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D8B')

    def _loc_C6B(): pass

    label('loc_C6B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CEB',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420033V#057F好像这纵坑的深度\n',
            '比中枢塔的高度还要厉害……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050420034V可能会下降到\n',
            '浮游都市的中心部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D8B')

    def _loc_CEB(): pass

    label('loc_CEB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D8B',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420035V#270F目测这个竖井\n',
            '比中枢塔还要深得多……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110420036V也有可能会\n',
            '降到浮游都市的中心部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D8B(): pass

    label('loc_D8B')

    ChrTalk(
        0x0101,
        (
            '#0010420037V#1003F#5P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0DC6')
    def lambda_0DC6():
        ChrSetDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0DC6)

    Sleep(100)

    ChrSetDirection(0x00F9, 0, 400)
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_113E',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420038V#1162F艾丝蒂尔……没问题的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060420039V你跟约修亚约好\n',
            '要一起走到最后的吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060420040V#1168F那样的话……\n',
            '他一定会恢复原样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010420041V#1025F#5P科洛丝……谢谢你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420042V#1012F是啊……\n',
            '他不是会爽约的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420043V#1019F而且我也不会\n',
            '让那个无视我们的\n',
            '眼镜男为所欲为的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420044V#1005F看我用少女的力量夺回他吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060420045V#1161F嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FC5',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420046V#275F嘿嘿，就是要这种精神！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_113B')

    def _loc_FC5(): pass

    label('loc_FC5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1001',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420047V#071F对，就是要这种精神！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_113B')

    def _loc_1001(): pass

    label('loc_1001')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1042',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420048V#171F呵呵，就是要这种精神！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_113B')

    def _loc_1042(): pass

    label('loc_1042')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1080',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420049V#051F嘿嘿，就是要这种精神！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_113B')

    def _loc_1080(): pass

    label('loc_1080')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10BF',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420050V#1061F哈哈，就是要这种精神！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_113B')

    def _loc_10BF(): pass

    label('loc_10BF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10FD',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420051V#021F呵呵，就是要这种精神！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_113B')

    def _loc_10FD(): pass

    label('loc_10FD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_113B',
    )

    ChrTalk(
        0x0107,
        (
            '#0070420052V#061F嘿嘿……\n',
            '就是要这种精神！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_113B(): pass

    label('loc_113B')

    Jump('loc_23A9')

    def _loc_113E(): pass

    label('loc_113E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1485',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420053V#214F真是的……\n',
            '别一副苦瓜脸啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090420054V约修亚才不会让\n',
            '那种眼镜男恣意操纵呢！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090420055V肯定会恢复原样的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010420056V#1025F#5P乔丝特……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420042V#1012F是啊……\n',
            '他不是会爽约的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420043V#1019F而且我也不会\n',
            '让那个无视我们的\n',
            '眼镜男为所欲为的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420059V#1005F看我用少女的力量夺回他吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090420060V#211F嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_130C',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420046V#275F嘿嘿，就是要这种精神！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1482')

    def _loc_130C(): pass

    label('loc_130C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1348',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420047V#071F对，就是要这种精神！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1482')

    def _loc_1348(): pass

    label('loc_1348')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1389',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420048V#171F呵呵，有这种决心就好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1482')

    def _loc_1389(): pass

    label('loc_1389')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13C7',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420049V#051F嘿嘿，就是要这种精神！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1482')

    def _loc_13C7(): pass

    label('loc_13C7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1406',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420050V#1061F哈哈，就是要这种精神！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1482')

    def _loc_1406(): pass

    label('loc_1406')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1444',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420051V#021F呵呵，就是要这种精神！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1482')

    def _loc_1444(): pass

    label('loc_1444')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1482',
    )

    ChrTalk(
        0x0107,
        (
            '#0070420052V#061F嘿嘿……\n',
            '就是要这种精神！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1482(): pass

    label('loc_1482')

    Jump('loc_23A9')

    def _loc_1485(): pass

    label('loc_1485')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_16BF',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420053V#214F真是的……\n',
            '别一副苦瓜脸啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090420069V约修亚才不会让\n',
            '那种眼镜男恣意操纵呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060420070V#1168F而且你和他约好\n',
            '要一起走到最后的吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060420071V那么说的话……\n',
            '他一定会恢复原样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010420072V#1025F#5P科洛丝、乔丝特……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420042V#1012F是啊……\n',
            '他不是会爽约的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420043V#1019F而且我也不会\n',
            '让那个无视我们的\n',
            '眼镜男为所欲为的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420059V#1005F看我用少女的力量夺回他吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_168A',
    )

    ChrTalk(
        0x0105,
        (
            '#1161F#1K嗯！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x010B,
        (
            '#0090420077V#211F#1K嗯！',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_16B9')

    def _loc_168A(): pass

    label('loc_168A')

    ChrTalk(
        0x0105,
        (
            '#1161F#1K嗯！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x010B,
        (
            '#0090420079V#211F#1K嗯！',
            TxtCtl.Enter,
        ),
    )

    def _loc_16B9(): pass

    label('loc_16B9')

    OP_56(0x01)
    OP_59()

    Jump('loc_23A9')

    def _loc_16BF(): pass

    label('loc_16BF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_183C',
    )

    ChrTalk(
        0x0107,
        (
            '#0070420080V#062F姐姐……你别担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070420081V你不是和哥哥约好\n',
            '要一起走到最后的吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070420082V#560F那就没问题的……\n',
            '他一定会复原的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010420083V#1025F#5P提妲……谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420042V#1012F是啊……\n',
            '他可是个言出必行的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420085V#1019F而且我也不会\n',
            '让那个无视我们的\n',
            '眼镜男为所欲为的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420086V#1005F看我用少女的力量夺回他吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21F2')

    def _loc_183C(): pass

    label('loc_183C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_19BC',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420087V#026F艾丝蒂尔……\n',
            '别那么担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030420088V#027F你和那孩子约好\n',
            '要一起走到最后的吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030420089V那就没问题了……\n',
            '他一定会复原的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010420090V#1025F#5P雪拉姐……谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420042V#1012F是啊……\n',
            '他不是会爽约的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420085V#1019F而且我也不会\n',
            '让那个无视我们的\n',
            '眼镜男为所欲为的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420086V#1005F看我用少女的力量夺回他吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21F2')

    def _loc_19BC(): pass

    label('loc_19BC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B3C',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420094V#1065F艾丝蒂尔……\n',
            '不用那么担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180420095V#1060F你和约修亚约好\n',
            '要一起走到最后的吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180420096V那就不要紧了。\n',
            '他会恢复原样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010420097V#1025F#5P凯文……谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420042V#1012F是啊……\n',
            '他不是会爽约的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420085V#1019F而且我也不会\n',
            '让那个无视我们的\n',
            '眼镜男为所欲为的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420086V#1005F看我用少女的力量夺回他吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21F2')

    def _loc_1B3C(): pass

    label('loc_1B3C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1CBE',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420101V#053F艾丝蒂尔……\n',
            '别摆出那副表情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050420102V#556F你和那家伙约好\n',
            '要一起走到最后的吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050420103V那就别担心了。\n',
            '他肯定会复原的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010420104V#1025F#5P阿加特……谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420042V#1012F是啊……\n',
            '他不是会爽约的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420085V#1019F而且我也不会\n',
            '让那个无视我们的\n',
            '眼镜男为所欲为的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420086V#1005F看我用少女的力量夺回他吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21F2')

    def _loc_1CBE(): pass

    label('loc_1CBE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1EA0',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420108V#176F艾丝蒂尔……\n',
            '他也曾在\n',
            '卡西乌斯准将的麾下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100420109V#170F他不是那种\n',
            '会违背约定的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100420110V他一定会回来的。\n',
            '……相信这一点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010420111V#1025F尤莉亚……谢谢你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420112V#1012F是啊……\n',
            '他不是会爽约的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420085V#1019F而且我也不会\n',
            '让那个无视我们的\n',
            '眼镜男为所欲为的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420086V#1005F看我用少女的力量夺回他吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21F2')

    def _loc_1EA0(): pass

    label('loc_1EA0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2019',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420115V#074F艾丝蒂尔……别担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080420116V#070F你和约修亚约好\n',
            '要一起走到最后的吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080420117V那就不要紧了。\n',
            '那家伙一定会复原的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010420118V#1025F#5P金……谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420042V#1012F是啊……\n',
            '他不是会爽约的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420085V#1019F而且我也不会\n',
            '让那个无视我们的\n',
            '眼镜男为所欲为的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420086V#1005F看我用少女的力量夺回他吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21F2')

    def _loc_2019(): pass

    label('loc_2019')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_21F2',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420122V#272F……没必要露出那样的表情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110420123V#277F你和他已经一起\n',
            '度过了无数次危机，不是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110420124V既然如此，现在就要向前看，继续走下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010420125V#1025F穆拉……\n',
            '……谢谢你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420042V#1012F是啊……\n',
            '他不是会爽约的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420085V#1019F而且我也不会\n',
            '让那个无视我们的\n',
            '眼镜男为所欲为的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420086V#1005F看我用少女的力量夺回他吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21F2(): pass

    label('loc_21F2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2233',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420046V#275F嘿嘿，就是要这种精神！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23A9')

    def _loc_2233(): pass

    label('loc_2233')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_226F',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420130V#071F对，就是要这种精神！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23A9')

    def _loc_226F(): pass

    label('loc_226F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_22B0',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420048V#171F呵呵，就是要这种精神！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23A9')

    def _loc_22B0(): pass

    label('loc_22B0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_22EE',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420049V#051F嘿嘿，就是要这种精神！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23A9')

    def _loc_22EE(): pass

    label('loc_22EE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_232D',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420050V#1061F哈哈，就是要这种精神！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23A9')

    def _loc_232D(): pass

    label('loc_232D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_236B',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420051V#021F呵呵，就是要这种精神！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23A9')

    def _loc_236B(): pass

    label('loc_236B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_23A9',
    )

    ChrTalk(
        0x0107,
        (
            '#0070420052V#061F嘿嘿……\n',
            '就是要这种精神！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23A9(): pass

    label('loc_23A9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2451',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420136V#031F呵呵，万一不行的话\n',
            '就交给我吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040420137V我一定会用满溢的爱\n',
            '让约修亚复原的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420138V#1016F#5P知道啦知道啦，拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2451(): pass

    label('loc_2451')

    PlaySE(344, 0x01, 0x64)

    @scena.Lambda('lambda_245C')
    def lambda_245C():
        OP_7C(10, 10, 1000, 1000)
        Yield()

        Jump('lambda_245C')

    DispatchAsync2(0x0101, 0x0002, lambda_245C)

    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24AF',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)

    Jump('loc_24E3')

    def _loc_24AF(): pass

    label('loc_24AF')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24D1',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)

    Jump('loc_24E3')

    def _loc_24D1(): pass

    label('loc_24D1')

    OP_62(0x00F8, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)

    def _loc_24E3(): pass

    label('loc_24E3')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_250A',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)

    Jump('loc_253E')

    def _loc_250A(): pass

    label('loc_250A')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_252C',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)

    Jump('loc_253E')

    def _loc_252C(): pass

    label('loc_252C')

    OP_62(0x00F9, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)

    def _loc_253E(): pass

    label('loc_253E')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010420139V#1020F#5P这、这是什么声音……',
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
        'loc_25A4',
    )

    ChrTalk(
        0x0107,
        (
            '#0070420140V#065F……莫非。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_274F')

    def _loc_25A4(): pass

    label('loc_25A4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_25D7',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420141V#1163F莫非……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_274F')

    def _loc_25D7(): pass

    label('loc_25D7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_260D',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420142V#216F莫、莫非……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_274F')

    def _loc_260D(): pass

    label('loc_260D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_263F',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420143V#023F莫非……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_274F')

    def _loc_263F(): pass

    label('loc_263F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2672',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420144V#1063F莫非……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_274F')

    def _loc_2672(): pass

    label('loc_2672')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_26AD',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420145V#273F莫非……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_274F')

    def _loc_26AD(): pass

    label('loc_26AD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_26EE',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420146V#178F可恶，莫非……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_274F')

    def _loc_26EE(): pass

    label('loc_26EE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2720',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420147V#032F……莫非。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_274F')

    def _loc_2720(): pass

    label('loc_2720')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_274F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420148V#052F莫非……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_274F(): pass

    label('loc_274F')

    OP_DB()
    Sleep(200)

    Fade(1000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapClearFlags(0x00000010)
    CameraMove(270, 1350, 1450, 0)
    OP_67(0, 12650, -10000, 0)
    CameraSetDistance(4090, 0)
    OP_6C(27000, 0)
    OP_6E(514, 0)
    OP_6F(0x0001, 30)
    OP_70(0x0001, 270)

    @scena.Lambda('lambda_27B9')
    def lambda_27B9():
        CameraMove(-650, 6000, 5500, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_27B9)

    @scena.Lambda('lambda_27D1')
    def lambda_27D1():
        OP_67(0, 4600, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_27D1)

    @scena.Lambda('lambda_27E9')
    def lambda_27E9():
        CameraSetDistance(3880, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_27E9)

    @scena.Lambda('lambda_27F9')
    def lambda_27F9():
        OP_6C(27000, 10000)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_27F9)

    @scena.Lambda('lambda_2809')
    def lambda_2809():
        OP_6E(449, 10000)

        ExitThread()

    DispatchAsync(0x00F8, 0x0002, lambda_2809)

    OP_A1(0x0008, 0x0000)
    ChrSetPos(0x0008, 0, 30000, 15980, 180)
    ChrClearFlags(0x0008, 0x0100)
    OP_D1(0x0008, 0, -45000, 0, 100)
    OP_72(0x0000, 0x0004)
    OP_71(0x0000, 0x0020)
    OP_B0(0x0000, 0x0F)
    OP_6F(0x0000, 320)
    OP_70(0x0000, 340)

    @scena.Lambda('lambda_2863')
    def lambda_2863():
        ChrMoveTo(0x00FE, 0, 1000, 15980, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2863)

    @scena.Lambda('lambda_287E')
    def lambda_287E():
        OP_D1(0x00FE, 0, 180000, 0, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_287E)

    @scena.Lambda('lambda_2898')
    def lambda_2898():
        OP_97(0x00FE, -90, 280, 730000, 25000, 0x0001)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_2898)

    PlaySE(213, 0x00, 0x64)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 0)
    Sleep(150)

    ChrSetSubChip(0x00F8, 0)
    ChrSetChipByIndex(0x00F8, 2)
    Sleep(100)

    ChrSetSubChip(0x00F9, 0)
    ChrSetChipByIndex(0x00F9, 4)

    @scena.Lambda('lambda_28E1')
    def lambda_28E1():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_28E1')

    DispatchAsync2(0x0101, 0x0000, lambda_28E1)

    @scena.Lambda('lambda_28F2')
    def lambda_28F2():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_28F2')

    DispatchAsync2(0x00F8, 0x0000, lambda_28F2)

    @scena.Lambda('lambda_2903')
    def lambda_2903():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_2903')

    DispatchAsync2(0x00F9, 0x0000, lambda_2903)

    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0008, 0x0002)
    WaitForThreadExit(0x0008, 0x0003)

    @scena.Lambda('lambda_2923')
    def lambda_2923():
        ChrMoveTo(0x00FE, -230, 2000, 6090, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2923)

    @scena.Lambda('lambda_293E')
    def lambda_293E():
        ChrSetDirection(0x00FE, 180, 50)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_293E)

    OP_D8(0x00, 0x012C)
    OP_B0(0x0000, 0x0F)
    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 25)
    OP_70(0x0000, 35)
    OP_73(0x0000)
    OP_D8(0x00, 0x012C)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 1)
    OP_70(0x0000, 20)
    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0008, 0x0002)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(1000)

    Fade(500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x00000010)
    CameraMove(1320, 2560, 4050, 0)
    OP_67(0, 2000, -10000, 0)
    CameraSetDistance(3170, 0)
    OP_6C(33000, 0)
    OP_6E(423, 0)
    OP_A1(0x0009, 0x0002)
    ChrSetPos(0x0009, -230, 2000, 6090, 0)
    ChrClearFlags(0x0009, 0x0100)
    OP_72(0x0002, 0x0004)
    OP_72(0x0002, 0x0020)
    OP_B0(0x0002, 0x0F)
    OP_6F(0x0002, 300)
    OP_71(0x0000, 0x0004)
    ChrSetDirection(0x0009, 180, 0)

    @scena.Lambda('lambda_2A21')
    def lambda_2A21():
        ChrMoveTo(0x00FE, -270, 1350, 5960, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2A21)

    OP_6F(0x0002, 300)
    OP_70(0x0002, 310)
    CreateThread(0x00F9, 0x00, 0x00, func_07_3515)
    Sleep(30)

    CreateThread(0x00F8, 0x00, 0x00, func_06_34F1)
    Sleep(50)

    CreateThread(0x0101, 0x00, 0x00, func_05_34CD)
    WaitForThreadExit(0x0009, 0x0001)
    OP_23(0x0158)
    PlaySE(236, 0x00, 0x64)
    OP_7C(0, 400, 3000, 1000)
    TerminateThread(0x0101, 0x02)
    OP_73(0x0002)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 20)
    Sleep(1000)

    OP_DC()

    ChrTalk(
        0x0101,
        (
            '#0010420149V#1020F#6P竟、竟然还有一架……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420150V#1002F这……\n',
            '看来只有正面应战了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B43',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420151V#076F#6P嗯……\n',
            '拿出斗志来上吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D6E')

    def _loc_2B43(): pass

    label('loc_2B43')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B83',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420152V#054F#6P嗯……\n',
            '拿出斗志上吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D6E')

    def _loc_2B83(): pass

    label('loc_2B83')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2BC3',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420153V#035F#6P呼……\n',
            '拿出斗志上吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D6E')

    def _loc_2BC3(): pass

    label('loc_2BC3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2C13',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420154V#177F呵呵……\n',
            '拿出斗志上吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D6E')

    def _loc_2C13(): pass

    label('loc_2C13')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2C67',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420155V#277F嗯……\n',
            '只有拿出斗志上了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D6E')

    def _loc_2C67(): pass

    label('loc_2C67')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2CAC',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420156V#1069F#6P嗯……\n',
            '只有拿出斗志上了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D6E')

    def _loc_2CAC(): pass

    label('loc_2CAC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2CEE',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420157V#024F#6P嗯……\n',
            '拿出斗志上吧！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D6E')

    def _loc_2CEE(): pass

    label('loc_2CEE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D2E',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420158V#214F#6P嗯……\n',
            '拿出斗志上吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D6E')

    def _loc_2D2E(): pass

    label('loc_2D2E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D6E',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420159V#1162F#6P嗯……\n',
            '拿出斗志来上了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D6E(): pass

    label('loc_2D6E')

    PlaySE(243, 0x00, 0x64)
    OP_72(0x0002, 0x0020)
    OP_6F(0x0002, 320)
    OP_70(0x0002, 340)
    OP_73(0x0002)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 340)
    OP_70(0x0002, 350)

    @scena.Lambda('lambda_2DA2')
    def lambda_2DA2():
        CameraMove(810, 1350, 5810, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2DA2)

    @scena.Lambda('lambda_2DBA')
    def lambda_2DBA():
        OP_67(0, 4710, -10000, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2DBA)

    @scena.Lambda('lambda_2DD2')
    def lambda_2DD2():
        CameraSetDistance(2440, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2DD2)

    @scena.Lambda('lambda_2DE2')
    def lambda_2DE2():
        ChrMoveTo(0x00FE, -260, 1350, 2350, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2DE2)

    @scena.Lambda('lambda_2DFD')
    def lambda_2DFD():
        ChrMoveTo(0x00FE, -1830, 1350, 1440, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0000, lambda_2DFD)

    @scena.Lambda('lambda_2E18')
    def lambda_2E18():
        ChrMoveTo(0x00FE, 560, 1350, 1290, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_2E18)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x00F8, 0xFF)
    TerminateThread(0x00F9, 0xFF)
    OP_23(0x01C3)
    OP_23(0x00EB)
    OP_23(0x0079)
    OP_23(0x0158)

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0x191),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00000450, 0x00000000, 0x00, 0x0080, 0xFF)

    Return()

# id: 0x0004 offset: 0x2E6B
@scena.Code('func_04_2E6B')
def func_04_2E6B():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x00F8, 0x00)
    TerminateThread(0x00F9, 0x00)
    OP_DB()
    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 0)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_2EBF'),
        (0x00000005, 'loc_2ECC'),
        (0x00000003, 'loc_2ED9'),
        (0x00000004, 'loc_2EE6'),
        (0x00000006, 'loc_2EF3'),
        (0x00000007, 'loc_2F00'),
        (0x00000008, 'loc_2F0D'),
        (0x0000000A, 'loc_2F1A'),
        (0x0000000E, 'loc_2F27'),
        (0x0000000F, 'loc_2F34'),
        (-1, 'loc_2F41'),
    )

    def _loc_2EBF(): pass

    label('loc_2EBF')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 2)

    Jump('loc_2F41')

    def _loc_2ECC(): pass

    label('loc_2ECC')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 2)

    Jump('loc_2F41')

    def _loc_2ED9(): pass

    label('loc_2ED9')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 2)

    Jump('loc_2F41')

    def _loc_2EE6(): pass

    label('loc_2EE6')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 2)

    Jump('loc_2F41')

    def _loc_2EF3(): pass

    label('loc_2EF3')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 2)

    Jump('loc_2F41')

    def _loc_2F00(): pass

    label('loc_2F00')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 2)

    Jump('loc_2F41')

    def _loc_2F0D(): pass

    label('loc_2F0D')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 2)

    Jump('loc_2F41')

    def _loc_2F1A(): pass

    label('loc_2F1A')

    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 2)

    Jump('loc_2F41')

    def _loc_2F27(): pass

    label('loc_2F27')

    LoadChip('ED6_DT27/CH04580._CH', 'ED6_DT27/CH04580P._CP', 2)

    Jump('loc_2F41')

    def _loc_2F34(): pass

    label('loc_2F34')

    LoadChip('ED6_DT27/CH04570._CH', 'ED6_DT27/CH04570P._CP', 2)

    Jump('loc_2F41')

    def _loc_2F41(): pass

    label('loc_2F41')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_2F72'),
        (0x00000005, 'loc_2F7F'),
        (0x00000003, 'loc_2F8C'),
        (0x00000004, 'loc_2F99'),
        (0x00000006, 'loc_2FA6'),
        (0x00000007, 'loc_2FB3'),
        (0x00000008, 'loc_2FC0'),
        (0x0000000A, 'loc_2FCD'),
        (0x0000000E, 'loc_2FDA'),
        (0x0000000F, 'loc_2FE7'),
        (-1, 'loc_2FF4'),
    )

    def _loc_2F72(): pass

    label('loc_2F72')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 4)

    Jump('loc_2FF4')

    def _loc_2F7F(): pass

    label('loc_2F7F')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 4)

    Jump('loc_2FF4')

    def _loc_2F8C(): pass

    label('loc_2F8C')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 4)

    Jump('loc_2FF4')

    def _loc_2F99(): pass

    label('loc_2F99')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 4)

    Jump('loc_2FF4')

    def _loc_2FA6(): pass

    label('loc_2FA6')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 4)

    Jump('loc_2FF4')

    def _loc_2FB3(): pass

    label('loc_2FB3')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 4)

    Jump('loc_2FF4')

    def _loc_2FC0(): pass

    label('loc_2FC0')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 4)

    Jump('loc_2FF4')

    def _loc_2FCD(): pass

    label('loc_2FCD')

    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 4)

    Jump('loc_2FF4')

    def _loc_2FDA(): pass

    label('loc_2FDA')

    LoadChip('ED6_DT27/CH04580._CH', 'ED6_DT27/CH04580P._CP', 4)

    Jump('loc_2FF4')

    def _loc_2FE7(): pass

    label('loc_2FE7')

    LoadChip('ED6_DT27/CH04570._CH', 'ED6_DT27/CH04570P._CP', 4)

    Jump('loc_2FF4')

    def _loc_2FF4(): pass

    label('loc_2FF4')

    OP_A1(0x0008, 0x0000)
    ChrSetPos(0x0008, 0, 1350, 2430, 0)
    ChrSetDirection(0x0008, 180, 0)
    ChrClearFlags(0x0008, 0x0100)
    OP_72(0x0000, 0x0004)
    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 260)
    OP_70(0x0000, 260)
    OP_71(0x0002, 0x0004)
    ChrSetChipByIndex(0x0101, 0)
    ChrSetChipByIndex(0x00F8, 2)
    ChrSetChipByIndex(0x00F9, 4)
    ChrSetSubChip(0x0000, 0)
    ChrSetSubChip(0x0001, 0)
    ChrSetSubChip(0x0002, 0)
    ChrSetPos(0x0101, 0, 1350, -2880, 0)
    ChrSetPos(0x00F8, -820, 1350, -4370, 0)
    ChrSetPos(0x00F9, 820, 1350, -4370, 0)
    LoadEffect(0x01, 'battle\\\\btbomb00.eff')
    LoadEffect(0x02, 'monster\\\\ms30109a.eff')
    LoadEffect(0x03, 'monster\\\\ms30109b.eff')
    CameraMove(-170, 3000, 3490, 0)
    OP_67(0, 2590, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(0, 0)
    OP_6E(308, 0)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapClearFlags(0x00000010)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_3125')
    def lambda_3125():
        CameraMove(-170, 4019, 12490, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3125)

    @scena.Lambda('lambda_313D')
    def lambda_313D():
        CameraSetDistance(4300, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_313D)

    OP_B0(0x0000, 0x0A)
    OP_6F(0x0000, 260)
    OP_70(0x0000, 310)
    PlayEffect(0x02, 0x00, 0x0008, 180, 3800, 500, 0, 0, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0xFF, 0x00FF, 180, 2560, 1060, 0, 0, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0x00, 0x0008, 180, 2300, 1400, 0, 0, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    PlayEffect(0x01, 0xFF, 0x00FF, 460, 3000, 2560, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0x01, 0x0008, 1000, 3500, 2500, 0, 0, 0, 1200, 1200, 1200, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    PlayEffect(0x02, 0x00, 0x0008, 300, 3500, 3000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x02, 0x00, 0x0008, 400, 1600, 4000, 0, 0, 0, 1300, 1067869798, 1300, 0x00FF, 0, 0, 0, 0)
    Sleep(400)

    PlayEffect(0x01, 0xFF, 0x00FF, -750, 3000, 4150, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0x01, 0x0008, -1000, 3000, 5000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_3355')
    def lambda_3355():
        CameraMove(-60, 1350, 12530, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3355)

    @scena.Lambda('lambda_336D')
    def lambda_336D():
        OP_67(0, 22350, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_336D)

    @scena.Lambda('lambda_3385')
    def lambda_3385():
        CameraSetDistance(500, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3385)

    @scena.Lambda('lambda_3395')
    def lambda_3395():
        OP_6E(513, 3000)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_3395)

    Sleep(900)

    PlayEffect(0x01, 0xFF, 0x00FF, 840, 4500, 8400, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    Fade(1000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x00000010)
    OP_B0(0x0000, 0x05)
    PlayEffect(0x01, 0xFF, 0x00FF, -900, 2560, 10090, 0, 0, 0, 1100, 1100, 1100, 0x00FF, 0, 0, 0, 0)
    WaitForThreadExit(0x0101, 0x0000)
    ChrSetPos(0x0101, 0, 1350, 1000, 0)
    ChrSetPos(0x00F8, -1000, 1350, -1000, 0)
    ChrSetPos(0x00F9, 1000, 1350, -1000, 0)

    @scena.Lambda('lambda_3468')
    def lambda_3468():
        ChrMoveToRelativeAsync(0x00FE, 0, -100000, 10000, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_3468)

    @scena.Lambda('lambda_3483')
    def lambda_3483():
        OP_67(0, 23350, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3483)

    @scena.Lambda('lambda_349B')
    def lambda_349B():
        CameraSetDistance(2600, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_349B)

    Sleep(4000)

    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(2000)

    MapSetFlags(0x00100000)
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5314._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x34CD
@scena.Code('func_05_34CD')
def func_05_34CD():
    ChrSetDirection(0x00FE, 0, 0)
    ChrJumpTo(0x00FE, -330, 1350, -3260, 500, 5000)
    PlaySE(164, 0x00, 0x64)

    Return()

# id: 0x0006 offset: 0x34F1
@scena.Code('func_06_34F1')
def func_06_34F1():
    ChrSetDirection(0x00FE, 0, 0)
    ChrJumpTo(0x00FE, -1780, 1350, -4930, 500, 5000)
    PlaySE(164, 0x00, 0x64)

    Return()

# id: 0x0007 offset: 0x3515
@scena.Code('func_07_3515')
def func_07_3515():
    ChrSetDirection(0x00FE, 0, 0)
    ChrJumpTo(0x00FE, 230, 1350, -5210, 500, 5000)
    PlaySE(164, 0x00, 0x64)

    Return()

# id: 0x0008 offset: 0x3539
@scena.Code('func_08_3539')
def func_08_3539():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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

    OP_5F(0x0000)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_35B3'),
        (0x00000001, 'loc_35B9'),
        (-1, 'loc_35BF'),
    )

    def _loc_35B3(): pass

    label('loc_35B3')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_35BF')

    def _loc_35B9(): pass

    label('loc_35B9')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_35BF')

    def _loc_35BF(): pass

    label('loc_35BF')

    Return()

# id: 0x0009 offset: 0x35C0
@scena.Code('func_09_35C0')
def func_09_35C0():
    FadeOut(0, 0, -1)
    CameraMove(-211220, -20490, -48190, 0)
    OP_67(0, 9000, -10000, 0)
    CameraSetDistance(5000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['科洛丝'],
            ChrTable['奥利维尔'],
            ChrTable['提妲'],
            ChrTable['金'],
            ChrTable['凯文神父'],
            ChrTable['乔丝特'],
            ChrTable['尤莉亚上尉'],
            ChrTable['穆拉'],
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
