import sys
sys.path.append(r'C:\nw_profile\IDE\pycharm\pycharmProj\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5318_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5318   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5318.x'
    header.mapIndex       = 1
    header.bgm            = 56
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
            name                = '怀斯曼教授',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '格里德',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '核心用目标角色',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01E4,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x108
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x108
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x108
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x108
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_116',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_02_147)

    def _loc_116(): pass

    label('loc_116')

    Return()

# id: 0x0001 offset: 0x117
@scena.Code('func_01_117')
def func_01_117():
    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x451),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12C',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x38),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_12C(): pass

    label('loc_12C')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x452),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_141',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x39),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_141(): pass

    label('loc_141')

    OP_71(0x0002, 0x0004)

    Return()

# id: 0x0002 offset: 0x147
@scena.Code('func_02_147')
def func_02_147():
    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0x103),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_C4(0x00, 0x00000010)
    OP_C0(0x16, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    OP_C4(0x01, 0x00000010)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    Call(0, 0x0003)
    Call(0, 0x0004)
    Call(0, 0x0005)

    Return()

# id: 0x0003 offset: 0x191
@scena.Code('func_03_191')
def func_03_191():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1A8',
    )

    Call(0, 0x0009)
    Call(0, 0x000A)

    def _loc_1A8(): pass

    label('loc_1A8')

    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 0)
    LoadChip('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP', 1)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_1ED'),
        (0x00000005, 'loc_1FA'),
        (0x00000003, 'loc_207'),
        (0x00000004, 'loc_214'),
        (0x00000006, 'loc_221'),
        (0x00000007, 'loc_22E'),
        (0x00000008, 'loc_23B'),
        (0x0000000A, 'loc_248'),
        (0x0000000E, 'loc_255'),
        (0x0000000F, 'loc_262'),
        (-1, 'loc_26F'),
    )

    def _loc_1ED(): pass

    label('loc_1ED')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 2)

    Jump('loc_26F')

    def _loc_1FA(): pass

    label('loc_1FA')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 2)

    Jump('loc_26F')

    def _loc_207(): pass

    label('loc_207')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 2)

    Jump('loc_26F')

    def _loc_214(): pass

    label('loc_214')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 2)

    Jump('loc_26F')

    def _loc_221(): pass

    label('loc_221')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 2)

    Jump('loc_26F')

    def _loc_22E(): pass

    label('loc_22E')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 2)

    Jump('loc_26F')

    def _loc_23B(): pass

    label('loc_23B')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 2)

    Jump('loc_26F')

    def _loc_248(): pass

    label('loc_248')

    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 2)

    Jump('loc_26F')

    def _loc_255(): pass

    label('loc_255')

    LoadChip('ED6_DT27/CH04580._CH', 'ED6_DT27/CH04580P._CP', 2)

    Jump('loc_26F')

    def _loc_262(): pass

    label('loc_262')

    LoadChip('ED6_DT27/CH04570._CH', 'ED6_DT27/CH04570P._CP', 2)

    Jump('loc_26F')

    def _loc_26F(): pass

    label('loc_26F')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_2A0'),
        (0x00000005, 'loc_2AD'),
        (0x00000003, 'loc_2BA'),
        (0x00000004, 'loc_2C7'),
        (0x00000006, 'loc_2D4'),
        (0x00000007, 'loc_2E1'),
        (0x00000008, 'loc_2EE'),
        (0x0000000A, 'loc_2FB'),
        (0x0000000E, 'loc_308'),
        (0x0000000F, 'loc_315'),
        (-1, 'loc_322'),
    )

    def _loc_2A0(): pass

    label('loc_2A0')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 3)

    Jump('loc_322')

    def _loc_2AD(): pass

    label('loc_2AD')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 3)

    Jump('loc_322')

    def _loc_2BA(): pass

    label('loc_2BA')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 3)

    Jump('loc_322')

    def _loc_2C7(): pass

    label('loc_2C7')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 3)

    Jump('loc_322')

    def _loc_2D4(): pass

    label('loc_2D4')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 3)

    Jump('loc_322')

    def _loc_2E1(): pass

    label('loc_2E1')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 3)

    Jump('loc_322')

    def _loc_2EE(): pass

    label('loc_2EE')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 3)

    Jump('loc_322')

    def _loc_2FB(): pass

    label('loc_2FB')

    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 3)

    Jump('loc_322')

    def _loc_308(): pass

    label('loc_308')

    LoadChip('ED6_DT27/CH04580._CH', 'ED6_DT27/CH04580P._CP', 3)

    Jump('loc_322')

    def _loc_315(): pass

    label('loc_315')

    LoadChip('ED6_DT27/CH04570._CH', 'ED6_DT27/CH04570P._CP', 3)

    Jump('loc_322')

    def _loc_322(): pass

    label('loc_322')

    ChrClearFlags(0x0000, 0x0008)
    ChrClearFlags(0x0001, 0x0008)
    ChrClearFlags(0x0002, 0x0008)
    ChrClearFlags(0x0003, 0x0008)
    ChrSetPos(0x0101, -1200, 0, -500, 0)
    ChrSetPos(0x0102, 600, 0, -500, 0)
    ChrSetPos(0x00F8, -900, 0, -1500, 0)
    ChrSetPos(0x00F9, 1000, 0, -1500, 0)
    ChrSetChipByIndex(0x0101, 0)
    ChrSetChipByIndex(0x0102, 1)
    ChrSetChipByIndex(0x00F8, 2)
    ChrSetChipByIndex(0x00F9, 3)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, 0, 0, 9500, 180)
    OP_A1(0x0008, 0x0002)
    OP_72(0x0002, 0x0004)
    OP_71(0x0000, 0x0004)
    OP_6F(0x0002, 11)
    OP_70(0x0002, 50)
    CameraMove(-730, 2890, 2610, 0)
    OP_67(0, 2230, -10000, 0)
    CameraSetDistance(2300, 0)
    OP_6C(25000, 0)
    OP_6E(583, 0)
    OP_E8(0xDC, 0x05, 0x00, 0x00)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeIn(2000, 0)
    CameraSetDistance(1800, 3000)
    OP_0D()
    SetMessageWindowPos(100, 190, -1, -1)
    TalkSetChrName('怀斯曼的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150420757V竟然能纠缠到这种地步……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420758V但终究……\n',
            '也只是徒劳的挣扎而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420759V在隐藏了无限力量的『环』面前──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(100)

    Fade(500)
    CameraMove(0, 0, 18610, 0)
    OP_67(0, 3380, -10000, 0)
    CameraSetDistance(3900, 0)
    OP_6C(0, 0)
    OP_6E(410, 0)
    OP_0D()

    @scena.Lambda('lambda_0512')
    def lambda_0512():
        CameraSetDistance(3450, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0512)

    OP_72(0x0002, 0x0020)
    OP_6F(0x0002, 51)
    OP_70(0x0002, 90)
    PlaySE(328, 0x00, 0x64)
    OP_73(0x0002)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 11)
    OP_70(0x0002, 50)
    WaitForThreadExit(0x0101, 0x0000)
    SetMessageWindowPos(190, 270, -1, -1)
    TalkSetChrName('怀斯曼的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150420760V怎、怎么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420761V『环』……\n',
            '……我体内的『环』……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_DB()
    LoadEffect(0x00, 'monster\\ms31000.eff')
    LoadEffect(0x01, 'map\\mp103_00.eff')
    LoadEffect(0x02, 'monster\\ms30900f.eff')
    Fade(500)
    OP_72(0x0002, 0x0020)
    OP_6F(0x0002, 211)
    OP_70(0x0002, 250)
    PlaySE(143, 0x00, 0x64)
    OP_73(0x0002)
    Play3DEffect(0x00, 0x00, 0x02, 'Frame95__ball', 0x00000000, 0x00000000, 0x00000000, 0x0000, 0x0000, 0x0000, 0x000005DC, 0x000005DC, 0x000005DC, 0x00000000)
    PlaySE(215, 0x00, 0x64)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 251)
    OP_70(0x0002, 290)
    Sleep(2000)

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
    CameraMove(0, 0, -690, 0)
    OP_67(0, 80810, -10000, 0)
    CameraSetDistance(500, 0)
    OP_6C(1000, 0)
    OP_6E(858, 0)
    ChrSetPos(0x0101, -550, 0, -500, 0)
    ChrSetPos(0x0102, 600, 0, -500, 0)
    ChrSetPos(0x00F8, -1250, 0, -1500, 0)
    ChrSetPos(0x00F9, 1200, 0, -1500, 0)
    OP_0D()
    Sleep(1000)

    @scena.Lambda('lambda_0709')
    def lambda_0709():
        CameraSetDistance(0, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0709)

    Sleep(400)

    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0101, 0x03)
    Fade(500)
    CameraMove(0, -30000, -500, 0)
    OP_67(0, 2510, -10000, 0)
    CameraSetDistance(230, 0)
    OP_6C(0, 0)
    OP_6E(600, 0)
    PlaySE(133, 0x00, 0x64)
    OP_0D()
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetPos(0x0009, 0, -50000, 9500, 180)
    OP_A1(0x0009, 0x0001)
    OP_72(0x0001, 0x0004)
    OP_B0(0x0001, 0x14)
    OP_6F(0x0001, 291)
    OP_70(0x0001, 330)
    PlaySE(342, 0x00, 0x64)
    ChrMoveToRelativeAsync(0x0009, 0, 20000, 0, 4000, 0x00)
    Sleep(1000)

    @scena.Lambda('lambda_07CB')
    def lambda_07CB():
        CameraSetDistance(1500, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_07CB)

    @scena.Lambda('lambda_07DB')
    def lambda_07DB():
        OP_6E(644, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_07DB)

    WaitForThreadExit(0x0101, 0x0000)
    OP_B0(0x0001, 0x1E)

    @scena.Lambda('lambda_07F4')
    def lambda_07F4():
        ChrMoveTo(0x00FE, 0, 30000, 9500, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_07F4)

    Sleep(500)

    @scena.Lambda('lambda_0814')
    def lambda_0814():
        ChrMoveTo(0x00FE, 0, 30000, 9500, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_0814)

    Sleep(400)

    @scena.Lambda('lambda_0834')
    def lambda_0834():
        ChrMoveTo(0x00FE, 0, 30000, 9500, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_0834)

    Sleep(300)

    @scena.Lambda('lambda_0854')
    def lambda_0854():
        ChrMoveTo(0x00FE, 0, 30000, 9500, 13000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_0854)

    Sleep(200)

    @scena.Lambda('lambda_0874')
    def lambda_0874():
        ChrMoveTo(0x00FE, 0, 30000, 9500, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_0874)

    Sleep(100)

    @scena.Lambda('lambda_0894')
    def lambda_0894():
        ChrMoveTo(0x00FE, 0, 30000, 9500, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_0894)

    WaitForThreadExit(0x0009, 0x0000)
    Fade(500)
    CameraMove(0, -60400, 12450, 0)
    OP_67(0, 40270, -10000, 0)
    CameraSetDistance(590, 0)
    OP_6C(0, 0)
    OP_6E(733, 0)
    ChrSetPos(0x0009, 0, -100000, 7500, 180)
    OP_B0(0x0001, 0x28)

    @scena.Lambda('lambda_090B')
    def lambda_090B():
        CameraSetDistance(0, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_090B)

    ChrMoveToRelativeAsync(0x0009, 0, 100000, 10000, 20000, 0x00)
    OP_71(0x0001, 0x0004)
    StopEffect(0x00, 0x00)
    OP_71(0x0002, 0x0004)
    OP_72(0x0000, 0x0004)
    ChrSetPos(0x0008, 0, 3000, 9500, 180)
    OP_A1(0x0008, 0x0000)
    OP_6F(0x0000, 11)
    OP_70(0x0000, 50)
    Play3DEffect(0x00, 0x01, 0x00, 'Frame294__ball', 0x00000000, 0x00000000, 0x00000000, 0x0000, 0x0000, 0x0000, 0x000005DC, 0x000005DC, 0x000005DC, 0x00000000)
    Fade(500)
    CameraMove(0, 0, 9700, 0)
    OP_67(0, 9620, -10000, 0)
    CameraSetDistance(1910, 0)
    OP_6C(0, 0)
    OP_6E(659, 0)

    @scena.Lambda('lambda_09DC')
    def lambda_09DC():
        OP_67(0, 7490, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_09DC)

    @scena.Lambda('lambda_09F4')
    def lambda_09F4():
        CameraSetDistance(1650, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_09F4)

    @scena.Lambda('lambda_0A04')
    def lambda_0A04():
        OP_6E(579, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0A04)

    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 50)
    OP_70(0x0000, 90)
    Sleep(1200)

    OP_23(0x0085)
    OP_23(0x0156)
    PlaySE(343, 0x00, 0x64)
    OP_73(0x0000)
    WaitForThreadExit(0x0101, 0x0000)

    @scena.Lambda('lambda_0A3F')
    def lambda_0A3F():
        CameraMove(0, 5170, 7290, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0A3F)

    @scena.Lambda('lambda_0A57')
    def lambda_0A57():
        OP_67(0, 5870, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0A57)

    OP_20(0x00001388)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 91)
    OP_70(0x0000, 130)
    PlaySE(328, 0x00, 0x64)
    SetMessageWindowPos(170, 280, -1, -1)
    TalkSetChrName('怀斯曼的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#40W#3S呜……\n',
            '……啊啊啊啊啊啊啊啊……！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    WaitForThreadExit(0x0101, 0x0000)
    OP_56(0x00)
    Sleep(100)

    Fade(500)
    CameraMove(0, 5170, 9100, 0)
    OP_67(0, 5850, -10000, 0)
    CameraSetDistance(840, 0)
    OP_6C(0, 0)
    OP_6E(746, 0)
    OP_0D()
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x00F8, 0x0080)
    ChrSetFlags(0x00F9, 0x0080)
    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 170)
    OP_70(0x0000, 210)
    PlaySE(333, 0x00, 0x64)
    OP_73(0x0000)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 251)
    OP_70(0x0000, 290)
    Sleep(1000)

    @scena.Lambda('lambda_0B67')
    def lambda_0B67():
        CameraMove(0, 7000, 12410, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0B67)

    @scena.Lambda('lambda_0B7F')
    def lambda_0B7F():
        OP_67(0, -3830, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B7F)

    @scena.Lambda('lambda_0B97')
    def lambda_0B97():
        CameraSetDistance(1800, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0B97)

    @scena.Lambda('lambda_0BA7')
    def lambda_0BA7():
        OP_6E(900, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0BA7)

    Sleep(1000)

    PlayEffect(0x01, 0x02, 0x0008, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(327, 0x00, 0x64)
    PlayBGM(57)
    WaitForThreadExit(0x0101, 0x0000)
    FadeOut(2000, 16777215, -1)
    OP_0D()
    Sleep(2500)

    StopEffect(0x01, 0x00)
    StopEffect(0x02, 0x00)

    Return()

# id: 0x0004 offset: 0xC0E
@scena.Code('func_04_C0E')
def func_04_C0E():
    OP_6F(0x0000, 371)
    OP_70(0x0000, 410)
    Play3DEffect(0x02, 0xFF, 0x00, 'Frame43_hiface', 0x00000000, 0x00000000, 0xFFFFFC18, 0x0000, 0x0000, 0xFF97, 0x000003E8, 0x000003E8, 0x000003E8, 0x00000000)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0102, 0x0080)
    ChrClearFlags(0x0002, 0x0080)
    ChrClearFlags(0x0003, 0x0080)
    CameraMove(110, 5040, 12390, 0)
    OP_67(0, 1920, -10000, 0)
    CameraSetDistance(1800, 0)
    OP_6C(181000, 0)
    OP_6E(804, 0)
    FadeIn(2000, 16777215)
    OP_0D()
    Sleep(1000)

    FadeOut(1000, 16777215, -1)
    OP_0D()
    CameraMove(-50, 5320, 7830, 0)
    OP_67(0, 1360, -10000, 0)
    CameraSetDistance(1580, 0)
    OP_6C(0, 0)
    OP_6E(539, 0)

    @scena.Lambda('lambda_0CFF')
    def lambda_0CFF():
        CameraMove(0, 4000, 1090, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0CFF)

    @scena.Lambda('lambda_0D17')
    def lambda_0D17():
        OP_67(0, 1330, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0D17)

    @scena.Lambda('lambda_0D2F')
    def lambda_0D2F():
        CameraSetDistance(1580, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0D2F)

    @scena.Lambda('lambda_0D3F')
    def lambda_0D3F():
        OP_6E(733, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0D3F)

    FadeIn(1000, 16777215)
    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 331)
    OP_70(0x0000, 370)
    PlaySE(328, 0x00, 0x64)
    OP_73(0x0000)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 371)
    OP_70(0x0000, 410)
    WaitForThreadExit(0x0101, 0x0000)

    @scena.Lambda('lambda_0D8B')
    def lambda_0D8B():
        CameraSetDistance(1680, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0D8B)

    OP_DC()
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DD4',
    )

    ChrTalk(
        0x0107,
        (
            '#0070420762V#065F#5P哎呀呀呀……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E16')

    def _loc_DD4(): pass

    label('loc_DD4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E16',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420763V#273F……这、这是…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E16(): pass

    label('loc_E16')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E52',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420764V#1163F#5P天、天使……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EC5')

    def _loc_E52(): pass

    label('loc_E52')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E8D',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420765V#173F#5P天、天使……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EC5')

    def _loc_E8D(): pass

    label('loc_E8D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EC5',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420766V#216F#5P天、天使……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EC5(): pass

    label('loc_EC5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F09',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420767V#039F#5P唔……\n',
            '好强大的灵压啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FD3')

    def _loc_F09(): pass

    label('loc_F09')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F4B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420768V#077F#5P唔……\n',
            '好强的灵压啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FD3')

    def _loc_F4B(): pass

    label('loc_F4B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F90',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420769V#523F#5P唔……这是什么灵压啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FD3')

    def _loc_F90(): pass

    label('loc_F90')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FD3',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420770V#1070F#5P唔……好惊人的灵压啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FD3(): pass

    label('loc_FD3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_100D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420771V#054F#5P嘿……这样才对！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_100D(): pass

    label('loc_100D')

    ChrTalk(
        0x0101,
        (
            '#0010420772V#1002F#5P看来这是最后的\n',
            '捶死挣扎了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420773V#1005F赶快打倒它，\n',
            '然后回到莱维身边！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420774V#1046F#5P嗯……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    Battle(0x00000452, 0x00300017, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0000, 0x0008)
    ChrSetFlags(0x0001, 0x0008)
    ChrSetFlags(0x0002, 0x0008)
    ChrSetFlags(0x0003, 0x0008)
    OP_C0(0x15, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)

    Return()

# id: 0x0005 offset: 0x10E3
@scena.Code('func_05_10E3')
def func_05_10E3():
    SetScenaFlags(ScenaFlag(0x0456, 4, 0x22B4))
    EventBegin(0x00)
    FadeOut(0, 16777215, -1)
    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 0)
    LoadChip('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP', 1)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_112F'),
        (0x00000005, 'loc_113C'),
        (0x00000003, 'loc_1149'),
        (0x00000004, 'loc_1156'),
        (0x00000006, 'loc_1163'),
        (0x00000007, 'loc_1170'),
        (0x00000008, 'loc_117D'),
        (0x0000000A, 'loc_118A'),
        (-1, 'loc_1197'),
    )

    def _loc_112F(): pass

    label('loc_112F')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 2)

    Jump('loc_1197')

    def _loc_113C(): pass

    label('loc_113C')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 2)

    Jump('loc_1197')

    def _loc_1149(): pass

    label('loc_1149')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 2)

    Jump('loc_1197')

    def _loc_1156(): pass

    label('loc_1156')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 2)

    Jump('loc_1197')

    def _loc_1163(): pass

    label('loc_1163')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 2)

    Jump('loc_1197')

    def _loc_1170(): pass

    label('loc_1170')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 2)

    Jump('loc_1197')

    def _loc_117D(): pass

    label('loc_117D')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 2)

    Jump('loc_1197')

    def _loc_118A(): pass

    label('loc_118A')

    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 2)

    Jump('loc_1197')

    def _loc_1197(): pass

    label('loc_1197')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_11C0'),
        (0x00000005, 'loc_11CD'),
        (0x00000003, 'loc_11DA'),
        (0x00000004, 'loc_11E7'),
        (0x00000006, 'loc_11F4'),
        (0x00000007, 'loc_1201'),
        (0x00000008, 'loc_120E'),
        (0x0000000A, 'loc_121B'),
        (-1, 'loc_1228'),
    )

    def _loc_11C0(): pass

    label('loc_11C0')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 3)

    Jump('loc_1228')

    def _loc_11CD(): pass

    label('loc_11CD')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 3)

    Jump('loc_1228')

    def _loc_11DA(): pass

    label('loc_11DA')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 3)

    Jump('loc_1228')

    def _loc_11E7(): pass

    label('loc_11E7')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 3)

    Jump('loc_1228')

    def _loc_11F4(): pass

    label('loc_11F4')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 3)

    Jump('loc_1228')

    def _loc_1201(): pass

    label('loc_1201')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 3)

    Jump('loc_1228')

    def _loc_120E(): pass

    label('loc_120E')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 3)

    Jump('loc_1228')

    def _loc_121B(): pass

    label('loc_121B')

    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 3)

    Jump('loc_1228')

    def _loc_1228(): pass

    label('loc_1228')

    ChrSetPos(0x0101, -550, 0, -500, 0)
    ChrSetPos(0x0102, 600, 0, -500, 0)
    ChrSetPos(0x00F8, -1250, 0, -1500, 0)
    ChrSetPos(0x00F9, 1200, 0, -1500, 0)
    ChrSetChipByIndex(0x0101, 0)
    ChrSetChipByIndex(0x0102, 1)
    ChrSetChipByIndex(0x00F8, 2)
    ChrSetChipByIndex(0x00F9, 3)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_72(0x0003, 0x0004)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, 0, 3000, 9500, 180)
    OP_A1(0x0008, 0x0003)
    OP_72(0x0003, 0x0020)
    CreateThread(0x0008, 0x03, 0x00, func_07_178A)
    CreateThread(0x0102, 0x03, 0x00, func_08_17AC)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetPos(0x0009, 0, 3000, 9500, 180)
    OP_A1(0x0009, 0x0004)
    OP_71(0x0004, 0x0004)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetPos(0x000A, 0, 5300, 7700, 180)
    OP_A1(0x000A, 0x0005)
    OP_71(0x0005, 0x0004)
    LoadEffect(0x00, 'monster\\ms31000.eff')
    LoadEffect(0x01, 'monster\\ms31003a.eff')
    LoadEffect(0x02, 'monster\\ms30900f.eff')
    Play3DEffect(0x00, 0x00, 0x03, 'Frame147_chest', 0x000005DC, 0x00000000, 0x00000000, 0x0000, 0x005A, 0x00B4, 0x00000708, 0x00000708, 0x00000708, 0x00000000)

    @scena.Lambda('lambda_1390')
    def lambda_1390():
        OP_7C(100, 100, 3000, 100)
        Yield()

        Jump('lambda_1390')

    DispatchAsync2(0x0008, 0x0000, lambda_1390)

    CameraMove(0, 3000, -4850, 0)
    OP_67(0, 190, -10000, 0)
    CameraSetDistance(1400, 0)
    OP_6C(0, 0)
    OP_6E(660, 0)
    PlaySE(133, 0x00, 0x64)
    FadeIn(2000, 16777215)

    @scena.Lambda('lambda_13F6')
    def lambda_13F6():
        CameraMove(0, 4890, 9640, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_13F6)

    @scena.Lambda('lambda_140E')
    def lambda_140E():
        OP_67(0, 540, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_140E)

    @scena.Lambda('lambda_1426')
    def lambda_1426():
        CameraSetDistance(1400, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1426)

    @scena.Lambda('lambda_1436')
    def lambda_1436():
        OP_6E(733, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1436)

    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1000)

    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x00F8, 0x0080)
    ChrSetFlags(0x00F9, 0x0080)
    Fade(500)
    CameraSetDistance(1200, 0)
    TerminateThread(0x0008, 0x03)
    TerminateThread(0x0102, 0x03)
    OP_71(0x0003, 0x0004)
    OP_72(0x0004, 0x0004)
    OP_72(0x0005, 0x0004)
    OP_72(0x0004, 0x0020)
    OP_6F(0x0004, 10)
    OP_70(0x0004, 10)
    OP_6F(0x0005, 0)
    OP_70(0x0005, 20)
    StopEffect(0x00, 0x02)
    PlaySE(335, 0x00, 0x64)
    PlayEffect(0x00, 0x01, 0x000A, 0, 0, 0, 0, 0, 0, 2300, 2300, 2300, 0x00FF, 0, 0, 0, 0)
    Sleep(2000)

    @scena.Lambda('lambda_14EC')
    def lambda_14EC():
        CameraMove(0, 1750, 3200, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_14EC)

    @scena.Lambda('lambda_1504')
    def lambda_1504():
        OP_67(0, -15110, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1504)

    @scena.Lambda('lambda_151C')
    def lambda_151C():
        CameraSetDistance(240, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_151C)

    @scena.Lambda('lambda_152C')
    def lambda_152C():
        OP_6E(700, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_152C)

    PlayEffect(0x00, 0x02, 0x000A, 0, -300, 0, 0, 0, 0, 2300, 2300, 2300, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_1571')
    def lambda_1571():
        ChrMoveTo(0x00FE, 0, 8500, 7700, 250, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_1571)

    Sleep(500)

    @scena.Lambda('lambda_1591')
    def lambda_1591():
        ChrMoveTo(0x00FE, 0, 8500, 7700, 500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_1591)

    Sleep(400)

    @scena.Lambda('lambda_15B1')
    def lambda_15B1():
        ChrMoveTo(0x00FE, 0, 8500, 7700, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_15B1)

    Sleep(300)

    @scena.Lambda('lambda_15D1')
    def lambda_15D1():
        ChrMoveTo(0x00FE, 0, 8500, 7700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_15D1)

    Sleep(900)

    @scena.Lambda('lambda_15F1')
    def lambda_15F1():
        ChrMoveTo(0x00FE, 0, 8500, 7700, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_15F1)

    Sleep(700)

    @scena.Lambda('lambda_1611')
    def lambda_1611():
        ChrMoveTo(0x00FE, 0, 8500, 7700, 500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_1611)

    Sleep(500)

    @scena.Lambda('lambda_1631')
    def lambda_1631():
        ChrMoveTo(0x00FE, 0, 8500, 7700, 250, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_1631)

    WaitForThreadExit(0x000A, 0x0000)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1000)

    @scena.Lambda('lambda_165B')
    def lambda_165B():
        CameraSetDistance(1400, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_165B)

    @scena.Lambda('lambda_166B')
    def lambda_166B():
        OP_67(0, -10110, -10000, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_166B)

    PlayEffect(0x01, 0x03, 0x000A, 0, -100, 0, 0, 45, 0, 1800, 1800, 1800, 0x00FF, 0, 0, 0, 0)
    PlaySE(336, 0x00, 0x64)

    @scena.Lambda('lambda_16BD')
    def lambda_16BD():
        OP_7C(300, 300, 3000, 100)
        Yield()

        Jump('lambda_16BD')

    DispatchAsync2(0x0008, 0x0000, lambda_16BD)

    Sleep(4000)

    OP_71(0x0005, 0x0004)
    FadeOut(1000, 16777215, -1)
    OP_0D()
    OP_C4(0x00, 0x00000010)
    Sleep(4000)

    PlaySE(327, 0x00, 0x64)
    CreateThread(0x0008, 0x03, 0x00, func_06_171B)
    OP_20(0x00000BB8)
    FadeIn(3000, 16777215)
    OP_0D()
    OP_21()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5317._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x171B
@scena.Code('func_06_171B')
def func_06_171B():
    OP_24(0x0085, 0x5A)
    OP_24(0x0147, 0x5A)
    Sleep(400)

    OP_24(0x0085, 0x50)
    OP_24(0x0147, 0x50)
    Sleep(400)

    OP_24(0x0085, 0x46)
    OP_24(0x0147, 0x46)
    Sleep(400)

    OP_24(0x0085, 0x3C)
    OP_24(0x0147, 0x3C)
    Sleep(400)

    OP_24(0x0085, 0x32)
    OP_24(0x0147, 0x32)
    Sleep(400)

    OP_24(0x0085, 0x28)
    OP_24(0x0147, 0x28)
    Sleep(400)

    OP_24(0x0085, 0x1E)
    OP_24(0x0147, 0x1E)
    Sleep(400)

    OP_24(0x0085, 0x14)
    OP_24(0x0147, 0x14)
    Sleep(400)

    OP_23(0x0085)
    OP_23(0x0147)

    Return()

# id: 0x0007 offset: 0x178A
@scena.Code('func_07_178A')
def func_07_178A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_17AB',
    )

    OP_6F(0x0003, 350)
    OP_70(0x0003, 380)
    OP_73(0x0003)
    OP_D8(0x03, 0x01F4)

    Jump('func_07_178A')

    def _loc_17AB(): pass

    label('loc_17AB')

    Return()

# id: 0x0008 offset: 0x17AC
@scena.Code('func_08_17AC')
def func_08_17AC():
    PlaySE(328, 0x00, 0x46)
    Sleep(4000)

    PlaySE(328, 0x00, 0x46)

    Return()

# id: 0x0009 offset: 0x17BC
@scena.Code('func_09_17BC')
def func_09_17BC():
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
        (0x00000000, 'loc_1836'),
        (0x00000001, 'loc_183C'),
        (-1, 'loc_1842'),
    )

    def _loc_1836(): pass

    label('loc_1836')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_1842')

    def _loc_183C(): pass

    label('loc_183C')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_1842')

    def _loc_1842(): pass

    label('loc_1842')

    Return()

# id: 0x000A offset: 0x1843
@scena.Code('func_0A_1843')
def func_0A_1843():
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
