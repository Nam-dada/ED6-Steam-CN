import sys
sys.path.append(r'C:\nw_profile\IDE\pycharm\pycharmProj\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5317_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5317   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5317.x'
    header.mapIndex       = 1
    header.bgm            = 0
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/C5317._SN', 'ED6_DT21/C5317_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
            name                = '剑帝莱维',
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
            name                = '穆拉少校',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '尤莉亚上尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '拉赛尔博士',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '多伦',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '吉尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '艾丝蒂尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '约修亚',
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
            name                = '非队伍成员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '非队伍成员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '非队伍成员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '非队伍成员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '非队伍成员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '非队伍成员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '科洛丝',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '雪拉扎德',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '战术壳',
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
            name                = '战术壳',
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
            name                = '战术壳',
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
            name                = '战术壳',
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
            name                = '残像',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '目标',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '目标',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '德尔基昂',
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

# id: 0x10002 offset: 0x3C8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x3C8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x3C8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x3C8
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_3E2',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(1, 0x0002)

    Jump('loc_3EF')

    def _loc_3E2(): pass

    label('loc_3E2')

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x41),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_06_1202)

    def _loc_3EF(): pass

    label('loc_3EF')

    Return()

# id: 0x0001 offset: 0x3F0
@scena.Code('func_01_3F0')
def func_01_3F0():
    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x2714),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_405',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x70),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_405(): pass

    label('loc_405')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x459),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_41D',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x045B, 2, 0x22DA))

    def _loc_41D(): pass

    label('loc_41D')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x465),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_435',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x70),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x045B, 2, 0x22DA))

    def _loc_435(): pass

    label('loc_435')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x451),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_44D',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x38),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x045B, 3, 0x22DB))

    def _loc_44D(): pass

    label('loc_44D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_45D',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x70),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_45D(): pass

    label('loc_45D')

    OP_72(0x0001, 0x0020)
    OP_72(0x0001, 0x0008)
    OP_6F(0x0001, 0)

    Return()

# id: 0x0002 offset: 0x46F
@scena.Code('func_02_46F')
def func_02_46F():
    LoadChip('ED6_DT27/CH04012._CH', 'ED6_DT27/CH04012P._CP', 0)
    LoadChip('ED6_DT27/CH04012._CH', 'ED6_DT27/CH04012P._CP', 1)
    LoadChip('ED6_DT27/CH04544._CH', 'ED6_DT27/CH04544P._CP', 2)
    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 3)
    LoadChip('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP', 4)
    LoadChip('ED6_DT27/CH04004._CH', 'ED6_DT27/CH04004P._CP', 5)
    LoadChip('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP', 6)
    LoadChip('ED6_DT27/CH04011._CH', 'ED6_DT27/CH04011P._CP', 7)
    LoadChip('ED6_DT27/CH04012._CH', 'ED6_DT27/CH04012P._CP', 8)
    LoadChip('ED6_DT27/CH04014._CH', 'ED6_DT27/CH04014P._CP', 9)
    LoadChip('ED6_DT27/CH04019._CH', 'ED6_DT27/CH04019P._CP', 10)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_50E'),
        (0x00000005, 'loc_525'),
        (0x00000003, 'loc_53C'),
        (0x00000004, 'loc_553'),
        (0x00000006, 'loc_56A'),
        (0x00000007, 'loc_581'),
        (0x00000008, 'loc_598'),
        (0x0000000A, 'loc_5AF'),
        (0x0000000E, 'loc_5C6'),
        (0x0000000F, 'loc_5DD'),
        (-1, 'loc_5F4'),
    )

    def _loc_50E(): pass

    label('loc_50E')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 11)
    LoadChip('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP', 12)

    Jump('loc_5F4')

    def _loc_525(): pass

    label('loc_525')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 11)
    LoadChip('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP', 12)

    Jump('loc_5F4')

    def _loc_53C(): pass

    label('loc_53C')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 11)
    LoadChip('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP', 12)

    Jump('loc_5F4')

    def _loc_553(): pass

    label('loc_553')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 11)
    LoadChip('ED6_DT27/CH04211._CH', 'ED6_DT27/CH04211P._CP', 12)

    Jump('loc_5F4')

    def _loc_56A(): pass

    label('loc_56A')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 11)
    LoadChip('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP', 12)

    Jump('loc_5F4')

    def _loc_581(): pass

    label('loc_581')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 11)
    LoadChip('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP', 12)

    Jump('loc_5F4')

    def _loc_598(): pass

    label('loc_598')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 11)
    LoadChip('ED6_DT27/CH04081._CH', 'ED6_DT27/CH04081P._CP', 12)

    Jump('loc_5F4')

    def _loc_5AF(): pass

    label('loc_5AF')

    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 11)
    LoadChip('ED6_DT07/CH00311._CH', 'ED6_DT07/CH00311P._CP', 12)

    Jump('loc_5F4')

    def _loc_5C6(): pass

    label('loc_5C6')

    LoadChip('ED6_DT27/CH04580._CH', 'ED6_DT27/CH04580P._CP', 11)
    LoadChip('ED6_DT27/CH04581._CH', 'ED6_DT27/CH04581P._CP', 12)

    Jump('loc_5F4')

    def _loc_5DD(): pass

    label('loc_5DD')

    LoadChip('ED6_DT27/CH04570._CH', 'ED6_DT27/CH04570P._CP', 11)
    LoadChip('ED6_DT27/CH04571._CH', 'ED6_DT27/CH04571P._CP', 12)

    Jump('loc_5F4')

    def _loc_5F4(): pass

    label('loc_5F4')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_625'),
        (0x00000005, 'loc_63C'),
        (0x00000003, 'loc_653'),
        (0x00000004, 'loc_66A'),
        (0x00000006, 'loc_681'),
        (0x00000007, 'loc_698'),
        (0x00000008, 'loc_6AF'),
        (0x0000000A, 'loc_6C6'),
        (0x0000000E, 'loc_6DD'),
        (0x0000000F, 'loc_6EA'),
        (-1, 'loc_6F7'),
    )

    def _loc_625(): pass

    label('loc_625')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 13)
    LoadChip('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP', 14)

    Jump('loc_6F7')

    def _loc_63C(): pass

    label('loc_63C')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 13)
    LoadChip('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP', 14)

    Jump('loc_6F7')

    def _loc_653(): pass

    label('loc_653')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 13)
    LoadChip('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP', 14)

    Jump('loc_6F7')

    def _loc_66A(): pass

    label('loc_66A')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 13)
    LoadChip('ED6_DT27/CH04211._CH', 'ED6_DT27/CH04211P._CP', 14)

    Jump('loc_6F7')

    def _loc_681(): pass

    label('loc_681')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 13)
    LoadChip('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP', 14)

    Jump('loc_6F7')

    def _loc_698(): pass

    label('loc_698')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 13)
    LoadChip('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP', 14)

    Jump('loc_6F7')

    def _loc_6AF(): pass

    label('loc_6AF')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 13)
    LoadChip('ED6_DT27/CH04081._CH', 'ED6_DT27/CH04081P._CP', 14)

    Jump('loc_6F7')

    def _loc_6C6(): pass

    label('loc_6C6')

    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 13)
    LoadChip('ED6_DT07/CH00311._CH', 'ED6_DT07/CH00311P._CP', 14)

    Jump('loc_6F7')

    def _loc_6DD(): pass

    label('loc_6DD')

    LoadChip('ED6_DT27/CH04580._CH', 'ED6_DT27/CH04580P._CP', 13)

    Jump('loc_6F7')

    def _loc_6EA(): pass

    label('loc_6EA')

    LoadChip('ED6_DT27/CH04570._CH', 'ED6_DT27/CH04570P._CP', 13)

    Jump('loc_6F7')

    def _loc_6F7(): pass

    label('loc_6F7')

    LoadChip('ED6_DT27/CH04550._CH', 'ED6_DT27/CH04550P._CP', 15)
    LoadChip('ED6_DT27/CH04551._CH', 'ED6_DT27/CH04551P._CP', 16)
    LoadChip('ED6_DT27/CH04552._CH', 'ED6_DT27/CH04552P._CP', 17)
    LoadChip('ED6_DT27/CH04555._CH', 'ED6_DT27/CH04555P._CP', 18)
    LoadChip('ED6_DT27/CH04558._CH', 'ED6_DT27/CH04558P._CP', 19)
    LoadChip('ED6_DT29/CH12540._CH', 'ED6_DT29/CH12540P._CP', 20)
    LoadChip('ED6_DT26/CH20497._CH', 'ED6_DT26/CH20497P._CP', 21)
    LoadChip('ED6_DT26/CH20488._CH', 'ED6_DT26/CH20488P._CP', 22)
    LoadChip('ED6_DT27/CH04542._CH', 'ED6_DT27/CH04542P._CP', 23)

    Return()

# id: 0x0003 offset: 0x752
@scena.Code('func_03_752')
def func_03_752():
    OP_C0(0x10, 0x00000006, 0x000000FF, 0x00000007, 0x00000008, 0x0000000A, 0x000000FF, 0x0000000B, 0x0000000C)
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0xFF)
    LoadChip('ED6_DT27/CH04012._CH', 'ED6_DT27/CH04012P._CP', 0)
    LoadChip('ED6_DT26/CH20478._CH', 'ED6_DT26/CH20478P._CP', 1)
    LoadChip('ED6_DT27/CH04544._CH', 'ED6_DT27/CH04544P._CP', 2)
    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 3)
    LoadChip('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP', 4)
    LoadChip('ED6_DT27/CH04004._CH', 'ED6_DT27/CH04004P._CP', 5)
    LoadChip('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP', 6)
    LoadChip('ED6_DT27/CH04011._CH', 'ED6_DT27/CH04011P._CP', 7)
    LoadChip('ED6_DT27/CH04012._CH', 'ED6_DT27/CH04012P._CP', 8)
    LoadChip('ED6_DT27/CH04014._CH', 'ED6_DT27/CH04014P._CP', 9)
    LoadChip('ED6_DT27/CH04019._CH', 'ED6_DT27/CH04019P._CP', 10)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_817'),
        (0x00000005, 'loc_82E'),
        (0x00000003, 'loc_845'),
        (0x00000004, 'loc_85C'),
        (0x00000006, 'loc_873'),
        (0x00000007, 'loc_88A'),
        (0x00000008, 'loc_8A1'),
        (0x0000000A, 'loc_8B8'),
        (0x0000000E, 'loc_8CF'),
        (0x0000000F, 'loc_8E6'),
        (-1, 'loc_8FD'),
    )

    def _loc_817(): pass

    label('loc_817')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 11)
    LoadChip('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP', 12)

    Jump('loc_8FD')

    def _loc_82E(): pass

    label('loc_82E')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 11)
    LoadChip('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP', 12)

    Jump('loc_8FD')

    def _loc_845(): pass

    label('loc_845')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 11)
    LoadChip('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP', 12)

    Jump('loc_8FD')

    def _loc_85C(): pass

    label('loc_85C')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 11)
    LoadChip('ED6_DT27/CH04211._CH', 'ED6_DT27/CH04211P._CP', 12)

    Jump('loc_8FD')

    def _loc_873(): pass

    label('loc_873')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 11)
    LoadChip('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP', 12)

    Jump('loc_8FD')

    def _loc_88A(): pass

    label('loc_88A')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 11)
    LoadChip('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP', 12)

    Jump('loc_8FD')

    def _loc_8A1(): pass

    label('loc_8A1')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 11)
    LoadChip('ED6_DT27/CH04081._CH', 'ED6_DT27/CH04081P._CP', 12)

    Jump('loc_8FD')

    def _loc_8B8(): pass

    label('loc_8B8')

    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 11)
    LoadChip('ED6_DT07/CH00311._CH', 'ED6_DT07/CH00311P._CP', 12)

    Jump('loc_8FD')

    def _loc_8CF(): pass

    label('loc_8CF')

    LoadChip('ED6_DT27/CH04580._CH', 'ED6_DT27/CH04580P._CP', 11)
    LoadChip('ED6_DT27/CH04581._CH', 'ED6_DT27/CH04581P._CP', 12)

    Jump('loc_8FD')

    def _loc_8E6(): pass

    label('loc_8E6')

    LoadChip('ED6_DT27/CH04570._CH', 'ED6_DT27/CH04570P._CP', 11)
    LoadChip('ED6_DT27/CH04571._CH', 'ED6_DT27/CH04571P._CP', 12)

    Jump('loc_8FD')

    def _loc_8FD(): pass

    label('loc_8FD')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_92E'),
        (0x00000005, 'loc_945'),
        (0x00000003, 'loc_95C'),
        (0x00000004, 'loc_973'),
        (0x00000006, 'loc_98A'),
        (0x00000007, 'loc_9A1'),
        (0x00000008, 'loc_9B8'),
        (0x0000000A, 'loc_9CF'),
        (0x0000000E, 'loc_9E6'),
        (0x0000000F, 'loc_9FD'),
        (-1, 'loc_A14'),
    )

    def _loc_92E(): pass

    label('loc_92E')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 13)
    LoadChip('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP', 14)

    Jump('loc_A14')

    def _loc_945(): pass

    label('loc_945')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 13)
    LoadChip('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP', 14)

    Jump('loc_A14')

    def _loc_95C(): pass

    label('loc_95C')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 13)
    LoadChip('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP', 14)

    Jump('loc_A14')

    def _loc_973(): pass

    label('loc_973')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 13)
    LoadChip('ED6_DT27/CH04211._CH', 'ED6_DT27/CH04211P._CP', 14)

    Jump('loc_A14')

    def _loc_98A(): pass

    label('loc_98A')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 13)
    LoadChip('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP', 14)

    Jump('loc_A14')

    def _loc_9A1(): pass

    label('loc_9A1')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 13)
    LoadChip('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP', 14)

    Jump('loc_A14')

    def _loc_9B8(): pass

    label('loc_9B8')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 13)
    LoadChip('ED6_DT27/CH04081._CH', 'ED6_DT27/CH04081P._CP', 14)

    Jump('loc_A14')

    def _loc_9CF(): pass

    label('loc_9CF')

    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 13)
    LoadChip('ED6_DT07/CH00311._CH', 'ED6_DT07/CH00311P._CP', 14)

    Jump('loc_A14')

    def _loc_9E6(): pass

    label('loc_9E6')

    LoadChip('ED6_DT27/CH04580._CH', 'ED6_DT27/CH04580P._CP', 13)
    LoadChip('ED6_DT27/CH04581._CH', 'ED6_DT27/CH04581P._CP', 14)

    Jump('loc_A14')

    def _loc_9FD(): pass

    label('loc_9FD')

    LoadChip('ED6_DT27/CH04570._CH', 'ED6_DT27/CH04570P._CP', 13)
    LoadChip('ED6_DT27/CH04571._CH', 'ED6_DT27/CH04571P._CP', 14)

    Jump('loc_A14')

    def _loc_A14(): pass

    label('loc_A14')

    LoadChip('ED6_DT27/CH04550._CH', 'ED6_DT27/CH04550P._CP', 15)
    LoadChip('ED6_DT27/CH04551._CH', 'ED6_DT27/CH04551P._CP', 16)
    LoadChip('ED6_DT27/CH04552._CH', 'ED6_DT27/CH04552P._CP', 17)
    LoadChip('ED6_DT27/CH04555._CH', 'ED6_DT27/CH04555P._CP', 18)
    LoadChip('ED6_DT27/CH04558._CH', 'ED6_DT27/CH04558P._CP', 19)
    LoadChip('ED6_DT29/CH12540._CH', 'ED6_DT29/CH12540P._CP', 20)
    LoadChip('ED6_DT29/CH12541._CH', 'ED6_DT29/CH12541P._CP', 21)
    LoadChip('ED6_DT27/CH04200._CH', 'ED6_DT27/CH04200P._CP', 22)
    LoadChip('ED6_DT27/CH04201._CH', 'ED6_DT27/CH04201P._CP', 23)
    LoadChip('ED6_DT27/CH04202._CH', 'ED6_DT27/CH04202P._CP', 24)
    LoadChip('ED6_DT29/CH12544._CH', 'ED6_DT29/CH12544P._CP', 25)
    LoadEffect(0x00, 'monster\\msc0647.eff')
    LoadEffect(0x01, 'craft\\cr163_01.eff')

    Return()

# id: 0x0004 offset: 0xAAE
@scena.Code('func_04_AAE')
def func_04_AAE():
    LoadChip('ED6_DT27/CH04012._CH', 'ED6_DT27/CH04012P._CP', 0)
    LoadChip('ED6_DT27/CH04012._CH', 'ED6_DT27/CH04012P._CP', 1)
    LoadChip('ED6_DT27/CH04544._CH', 'ED6_DT27/CH04544P._CP', 2)
    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 3)
    LoadChip('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP', 4)
    LoadChip('ED6_DT27/CH04004._CH', 'ED6_DT27/CH04004P._CP', 5)
    LoadChip('ED6_DT27/CH04200._CH', 'ED6_DT27/CH04200P._CP', 6)
    LoadChip('ED6_DT27/CH04201._CH', 'ED6_DT27/CH04201P._CP', 7)
    LoadChip('ED6_DT27/CH04202._CH', 'ED6_DT27/CH04202P._CP', 8)
    LoadChip('ED6_DT27/CH04204._CH', 'ED6_DT27/CH04204P._CP', 9)
    LoadChip('ED6_DT27/CH04209._CH', 'ED6_DT27/CH04209P._CP', 10)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_B4D'),
        (0x00000005, 'loc_B64'),
        (0x00000003, 'loc_B7B'),
        (0x00000004, 'loc_B92'),
        (0x00000006, 'loc_BA9'),
        (0x00000007, 'loc_BC0'),
        (0x00000008, 'loc_BD7'),
        (0x0000000A, 'loc_BEE'),
        (0x0000000E, 'loc_C05'),
        (0x0000000F, 'loc_C1C'),
        (-1, 'loc_C33'),
    )

    def _loc_B4D(): pass

    label('loc_B4D')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 11)
    LoadChip('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP', 12)

    Jump('loc_C33')

    def _loc_B64(): pass

    label('loc_B64')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 11)
    LoadChip('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP', 12)

    Jump('loc_C33')

    def _loc_B7B(): pass

    label('loc_B7B')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 11)
    LoadChip('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP', 12)

    Jump('loc_C33')

    def _loc_B92(): pass

    label('loc_B92')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 11)
    LoadChip('ED6_DT27/CH04211._CH', 'ED6_DT27/CH04211P._CP', 12)

    Jump('loc_C33')

    def _loc_BA9(): pass

    label('loc_BA9')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 11)
    LoadChip('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP', 12)

    Jump('loc_C33')

    def _loc_BC0(): pass

    label('loc_BC0')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 11)
    LoadChip('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP', 12)

    Jump('loc_C33')

    def _loc_BD7(): pass

    label('loc_BD7')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 11)
    LoadChip('ED6_DT27/CH04081._CH', 'ED6_DT27/CH04081P._CP', 12)

    Jump('loc_C33')

    def _loc_BEE(): pass

    label('loc_BEE')

    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 11)
    LoadChip('ED6_DT07/CH00311._CH', 'ED6_DT07/CH00311P._CP', 12)

    Jump('loc_C33')

    def _loc_C05(): pass

    label('loc_C05')

    LoadChip('ED6_DT27/CH04580._CH', 'ED6_DT27/CH04580P._CP', 11)
    LoadChip('ED6_DT27/CH04581._CH', 'ED6_DT27/CH04581P._CP', 12)

    Jump('loc_C33')

    def _loc_C1C(): pass

    label('loc_C1C')

    LoadChip('ED6_DT27/CH04570._CH', 'ED6_DT27/CH04570P._CP', 11)
    LoadChip('ED6_DT27/CH04571._CH', 'ED6_DT27/CH04571P._CP', 12)

    Jump('loc_C33')

    def _loc_C33(): pass

    label('loc_C33')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_C64'),
        (0x00000005, 'loc_C7B'),
        (0x00000003, 'loc_C92'),
        (0x00000004, 'loc_CA9'),
        (0x00000006, 'loc_CC0'),
        (0x00000007, 'loc_CD7'),
        (0x00000008, 'loc_CEE'),
        (0x0000000A, 'loc_D05'),
        (0x0000000E, 'loc_D1C'),
        (0x0000000F, 'loc_D33'),
        (-1, 'loc_D4A'),
    )

    def _loc_C64(): pass

    label('loc_C64')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 13)
    LoadChip('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP', 14)

    Jump('loc_D4A')

    def _loc_C7B(): pass

    label('loc_C7B')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 13)
    LoadChip('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP', 14)

    Jump('loc_D4A')

    def _loc_C92(): pass

    label('loc_C92')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 13)
    LoadChip('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP', 14)

    Jump('loc_D4A')

    def _loc_CA9(): pass

    label('loc_CA9')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 13)
    LoadChip('ED6_DT27/CH04211._CH', 'ED6_DT27/CH04211P._CP', 14)

    Jump('loc_D4A')

    def _loc_CC0(): pass

    label('loc_CC0')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 13)
    LoadChip('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP', 14)

    Jump('loc_D4A')

    def _loc_CD7(): pass

    label('loc_CD7')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 13)
    LoadChip('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP', 14)

    Jump('loc_D4A')

    def _loc_CEE(): pass

    label('loc_CEE')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 13)
    LoadChip('ED6_DT27/CH04081._CH', 'ED6_DT27/CH04081P._CP', 14)

    Jump('loc_D4A')

    def _loc_D05(): pass

    label('loc_D05')

    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 13)
    LoadChip('ED6_DT07/CH00311._CH', 'ED6_DT07/CH00311P._CP', 14)

    Jump('loc_D4A')

    def _loc_D1C(): pass

    label('loc_D1C')

    LoadChip('ED6_DT27/CH04580._CH', 'ED6_DT27/CH04580P._CP', 13)
    LoadChip('ED6_DT27/CH04581._CH', 'ED6_DT27/CH04581P._CP', 14)

    Jump('loc_D4A')

    def _loc_D33(): pass

    label('loc_D33')

    LoadChip('ED6_DT27/CH04570._CH', 'ED6_DT27/CH04570P._CP', 13)
    LoadChip('ED6_DT27/CH04571._CH', 'ED6_DT27/CH04571P._CP', 14)

    Jump('loc_D4A')

    def _loc_D4A(): pass

    label('loc_D4A')

    LoadChip('ED6_DT27/CH04550._CH', 'ED6_DT27/CH04550P._CP', 15)
    LoadChip('ED6_DT27/CH04551._CH', 'ED6_DT27/CH04551P._CP', 16)
    LoadChip('ED6_DT27/CH04552._CH', 'ED6_DT27/CH04552P._CP', 17)
    LoadChip('ED6_DT26/CH20482._CH', 'ED6_DT26/CH20482P._CP', 18)
    LoadChip('ED6_DT27/CH04558._CH', 'ED6_DT27/CH04558P._CP', 19)
    LoadChip('ED6_DT29/CH12540._CH', 'ED6_DT29/CH12540P._CP', 20)
    LoadChip('ED6_DT07/CH02040._CH', 'ED6_DT07/CH02040P._CP', 21)
    LoadChip('ED6_DT27/CH04540._CH', 'ED6_DT27/CH04540P._CP', 22)
    LoadChip('ED6_DT27/CH04542._CH', 'ED6_DT27/CH04542P._CP', 23)
    LoadChip('ED6_DT27/CH04543._CH', 'ED6_DT27/CH04543P._CP', 24)

    Return()

# id: 0x0005 offset: 0xDAF
@scena.Code('func_05_DAF')
def func_05_DAF():
    LoadChip('ED6_DT26/CH20343._CH', 'ED6_DT26/CH20343P._CP', 0)
    LoadChip('ED6_DT26/CH20475._CH', 'ED6_DT26/CH20475P._CP', 1)
    LoadChip('ED6_DT26/CH20479._CH', 'ED6_DT26/CH20479P._CP', 2)
    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 3)
    LoadChip('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP', 4)
    LoadChip('ED6_DT27/CH04004._CH', 'ED6_DT27/CH04004P._CP', 5)
    LoadChip('ED6_DT27/CH04200._CH', 'ED6_DT27/CH04200P._CP', 6)
    LoadChip('ED6_DT27/CH04201._CH', 'ED6_DT27/CH04201P._CP', 7)
    LoadChip('ED6_DT27/CH04202._CH', 'ED6_DT27/CH04202P._CP', 8)
    LoadChip('ED6_DT27/CH04204._CH', 'ED6_DT27/CH04204P._CP', 9)
    LoadChip('ED6_DT27/CH04209._CH', 'ED6_DT27/CH04209P._CP', 10)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_E4E'),
        (0x00000005, 'loc_E65'),
        (0x00000003, 'loc_E7C'),
        (0x00000004, 'loc_E93'),
        (0x00000006, 'loc_EAA'),
        (0x00000007, 'loc_EC1'),
        (0x00000008, 'loc_ED8'),
        (0x0000000A, 'loc_EEF'),
        (0x0000000E, 'loc_F06'),
        (0x0000000F, 'loc_F1D'),
        (-1, 'loc_F34'),
    )

    def _loc_E4E(): pass

    label('loc_E4E')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 11)
    LoadChip('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP', 12)

    Jump('loc_F34')

    def _loc_E65(): pass

    label('loc_E65')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 11)
    LoadChip('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP', 12)

    Jump('loc_F34')

    def _loc_E7C(): pass

    label('loc_E7C')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 11)
    LoadChip('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP', 12)

    Jump('loc_F34')

    def _loc_E93(): pass

    label('loc_E93')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 11)
    LoadChip('ED6_DT27/CH04211._CH', 'ED6_DT27/CH04211P._CP', 12)

    Jump('loc_F34')

    def _loc_EAA(): pass

    label('loc_EAA')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 11)
    LoadChip('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP', 12)

    Jump('loc_F34')

    def _loc_EC1(): pass

    label('loc_EC1')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 11)
    LoadChip('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP', 12)

    Jump('loc_F34')

    def _loc_ED8(): pass

    label('loc_ED8')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 11)
    LoadChip('ED6_DT27/CH04081._CH', 'ED6_DT27/CH04081P._CP', 12)

    Jump('loc_F34')

    def _loc_EEF(): pass

    label('loc_EEF')

    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 11)
    LoadChip('ED6_DT07/CH00311._CH', 'ED6_DT07/CH00311P._CP', 12)

    Jump('loc_F34')

    def _loc_F06(): pass

    label('loc_F06')

    LoadChip('ED6_DT27/CH04580._CH', 'ED6_DT27/CH04580P._CP', 11)
    LoadChip('ED6_DT27/CH04581._CH', 'ED6_DT27/CH04581P._CP', 12)

    Jump('loc_F34')

    def _loc_F1D(): pass

    label('loc_F1D')

    LoadChip('ED6_DT27/CH04570._CH', 'ED6_DT27/CH04570P._CP', 11)
    LoadChip('ED6_DT27/CH04571._CH', 'ED6_DT27/CH04571P._CP', 12)

    Jump('loc_F34')

    def _loc_F34(): pass

    label('loc_F34')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_F65'),
        (0x00000005, 'loc_F7C'),
        (0x00000003, 'loc_F93'),
        (0x00000004, 'loc_FAA'),
        (0x00000006, 'loc_FC1'),
        (0x00000007, 'loc_FD8'),
        (0x00000008, 'loc_FEF'),
        (0x0000000A, 'loc_1006'),
        (0x0000000E, 'loc_101D'),
        (0x0000000F, 'loc_1034'),
        (-1, 'loc_104B'),
    )

    def _loc_F65(): pass

    label('loc_F65')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 13)
    LoadChip('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP', 14)

    Jump('loc_104B')

    def _loc_F7C(): pass

    label('loc_F7C')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 13)
    LoadChip('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP', 14)

    Jump('loc_104B')

    def _loc_F93(): pass

    label('loc_F93')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 13)
    LoadChip('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP', 14)

    Jump('loc_104B')

    def _loc_FAA(): pass

    label('loc_FAA')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 13)
    LoadChip('ED6_DT27/CH04211._CH', 'ED6_DT27/CH04211P._CP', 14)

    Jump('loc_104B')

    def _loc_FC1(): pass

    label('loc_FC1')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 13)
    LoadChip('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP', 14)

    Jump('loc_104B')

    def _loc_FD8(): pass

    label('loc_FD8')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 13)
    LoadChip('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP', 14)

    Jump('loc_104B')

    def _loc_FEF(): pass

    label('loc_FEF')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 13)
    LoadChip('ED6_DT27/CH04081._CH', 'ED6_DT27/CH04081P._CP', 14)

    Jump('loc_104B')

    def _loc_1006(): pass

    label('loc_1006')

    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 13)
    LoadChip('ED6_DT07/CH00311._CH', 'ED6_DT07/CH00311P._CP', 14)

    Jump('loc_104B')

    def _loc_101D(): pass

    label('loc_101D')

    LoadChip('ED6_DT27/CH04580._CH', 'ED6_DT27/CH04580P._CP', 13)
    LoadChip('ED6_DT27/CH04581._CH', 'ED6_DT27/CH04581P._CP', 14)

    Jump('loc_104B')

    def _loc_1034(): pass

    label('loc_1034')

    LoadChip('ED6_DT27/CH04570._CH', 'ED6_DT27/CH04570P._CP', 13)
    LoadChip('ED6_DT27/CH04571._CH', 'ED6_DT27/CH04571P._CP', 14)

    Jump('loc_104B')

    def _loc_104B(): pass

    label('loc_104B')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_107C'),
        (0x00000005, 'loc_1089'),
        (0x00000003, 'loc_1096'),
        (0x00000004, 'loc_10A3'),
        (0x00000006, 'loc_10B0'),
        (0x00000007, 'loc_10BD'),
        (0x00000008, 'loc_10CA'),
        (0x0000000A, 'loc_10D7'),
        (0x0000000E, 'loc_10E4'),
        (0x0000000F, 'loc_10F1'),
        (-1, 'loc_10FE'),
    )

    def _loc_107C(): pass

    label('loc_107C')

    LoadChip('ED6_DT07/CH00124._CH', 'ED6_DT07/CH00124P._CP', 15)

    Jump('loc_10FE')

    def _loc_1089(): pass

    label('loc_1089')

    LoadChip('ED6_DT07/CH00154._CH', 'ED6_DT07/CH00154P._CP', 15)

    Jump('loc_10FE')

    def _loc_1096(): pass

    label('loc_1096')

    LoadChip('ED6_DT07/CH00134._CH', 'ED6_DT07/CH00134P._CP', 15)

    Jump('loc_10FE')

    def _loc_10A3(): pass

    label('loc_10A3')

    LoadChip('ED6_DT27/CH04214._CH', 'ED6_DT27/CH04214P._CP', 15)

    Jump('loc_10FE')

    def _loc_10B0(): pass

    label('loc_10B0')

    LoadChip('ED6_DT07/CH00164._CH', 'ED6_DT07/CH00164P._CP', 15)

    Jump('loc_10FE')

    def _loc_10BD(): pass

    label('loc_10BD')

    LoadChip('ED6_DT07/CH00174._CH', 'ED6_DT07/CH00174P._CP', 15)

    Jump('loc_10FE')

    def _loc_10CA(): pass

    label('loc_10CA')

    LoadChip('ED6_DT27/CH04084._CH', 'ED6_DT27/CH04084P._CP', 15)

    Jump('loc_10FE')

    def _loc_10D7(): pass

    label('loc_10D7')

    LoadChip('ED6_DT07/CH00314._CH', 'ED6_DT07/CH00314P._CP', 15)

    Jump('loc_10FE')

    def _loc_10E4(): pass

    label('loc_10E4')

    LoadChip('ED6_DT27/CH04584._CH', 'ED6_DT27/CH04584P._CP', 15)

    Jump('loc_10FE')

    def _loc_10F1(): pass

    label('loc_10F1')

    LoadChip('ED6_DT27/CH04574._CH', 'ED6_DT27/CH04574P._CP', 15)

    Jump('loc_10FE')

    def _loc_10FE(): pass

    label('loc_10FE')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
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
        (0x0000000E, 'loc_1197'),
        (0x0000000F, 'loc_11A4'),
        (-1, 'loc_11B1'),
    )

    def _loc_112F(): pass

    label('loc_112F')

    LoadChip('ED6_DT07/CH00124._CH', 'ED6_DT07/CH00124P._CP', 16)

    Jump('loc_11B1')

    def _loc_113C(): pass

    label('loc_113C')

    LoadChip('ED6_DT07/CH00154._CH', 'ED6_DT07/CH00154P._CP', 16)

    Jump('loc_11B1')

    def _loc_1149(): pass

    label('loc_1149')

    LoadChip('ED6_DT07/CH00134._CH', 'ED6_DT07/CH00134P._CP', 16)

    Jump('loc_11B1')

    def _loc_1156(): pass

    label('loc_1156')

    LoadChip('ED6_DT27/CH04214._CH', 'ED6_DT27/CH04214P._CP', 16)

    Jump('loc_11B1')

    def _loc_1163(): pass

    label('loc_1163')

    LoadChip('ED6_DT07/CH00164._CH', 'ED6_DT07/CH00164P._CP', 16)

    Jump('loc_11B1')

    def _loc_1170(): pass

    label('loc_1170')

    LoadChip('ED6_DT07/CH00174._CH', 'ED6_DT07/CH00174P._CP', 16)

    Jump('loc_11B1')

    def _loc_117D(): pass

    label('loc_117D')

    LoadChip('ED6_DT27/CH04084._CH', 'ED6_DT27/CH04084P._CP', 16)

    Jump('loc_11B1')

    def _loc_118A(): pass

    label('loc_118A')

    LoadChip('ED6_DT07/CH00314._CH', 'ED6_DT07/CH00314P._CP', 16)

    Jump('loc_11B1')

    def _loc_1197(): pass

    label('loc_1197')

    LoadChip('ED6_DT27/CH04584._CH', 'ED6_DT27/CH04584P._CP', 16)

    Jump('loc_11B1')

    def _loc_11A4(): pass

    label('loc_11A4')

    LoadChip('ED6_DT27/CH04574._CH', 'ED6_DT27/CH04574P._CP', 16)

    Jump('loc_11B1')

    def _loc_11B1(): pass

    label('loc_11B1')

    LoadChip('ED6_DT26/CH20495._CH', 'ED6_DT26/CH20495P._CP', 17)
    LoadChip('ED6_DT27/CH04544._CH', 'ED6_DT27/CH04544P._CP', 18)
    LoadChip('ED6_DT27/CH04546._CH', 'ED6_DT27/CH04546P._CP', 19)
    LoadChip('ED6_DT26/CH20363._CH', 'ED6_DT26/CH20363P._CP', 20)
    LoadChip('ED6_DT07/CH02040._CH', 'ED6_DT07/CH02040P._CP', 21)
    LoadChip('ED6_DT27/CH04540._CH', 'ED6_DT27/CH04540P._CP', 22)
    LoadChip('ED6_DT27/CH04542._CH', 'ED6_DT27/CH04542P._CP', 23)
    LoadChip('ED6_DT27/CH04543._CH', 'ED6_DT27/CH04543P._CP', 24)

    Return()

# id: 0x0006 offset: 0x1202
@scena.Code('func_06_1202')
def func_06_1202():
    Call(0, 0x0007)
    Call(0, 0x0008)
    Call(0, 0x0009)
    Call(0, 0x000A)
    Call(0, 0x000B)

    Return()

# id: 0x0007 offset: 0x1217
@scena.Code('func_07_1217')
def func_07_1217():
    EventBegin(0x00)
    MapClearFlags(0x02000000)
    MapClearFlags(0x00100000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_123B',
    )

    Call(0, 0x0021)
    Call(0, 0x0022)
    FormationDelMember(0x01, 0xFF)

    def _loc_123B(): pass

    label('loc_123B')

    FormationAddMember(ChrTable['约修亚'], 0xF7, 0xFF)
    Call(0, 0x0002)
    CameraMove(-46590, 100, 300, 0)
    OP_67(0, 8250, -10000, 0)
    CameraSetDistance(2280, 0)
    OP_6C(45000, 0)
    OP_6E(369, 0)
    OP_E5(0x08, 0x00, 0x00)
    ChrSetChipByIndex(0x0008, 15)
    ChrSetPos(0x0008, -1440, 3200, 70, 270)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0102, -2100, 3200, -950, 270)
    ChrSetChipByIndex(0x0102, 22)
    ChrSetPos(0x0101, -48040, 100, -320, 90)
    ChrSetPos(0x00F9, -49300, 100, 560, 90)
    ChrSetPos(0x00F8, -49640, 100, -940, 90)

    @scena.Lambda('lambda_12EE')
    def lambda_12EE():
        ChrWalkTo(0x00FE, -45040, 100, -320, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_12EE)

    @scena.Lambda('lambda_1309')
    def lambda_1309():
        ChrWalkTo(0x00FE, -46300, 100, 560, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_1309)

    @scena.Lambda('lambda_1324')
    def lambda_1324():
        ChrWalkTo(0x00FE, -46640, 100, -940, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_1324)

    FadeIn(1000, 0)
    CameraMove(-44950, 100, -470, 2000)
    WaitForThreadExit(0x0101, 0x0001)
    OP_20(0x000003E8)

    ChrTalk(
        0x0008,
        (
            '#0150420204V欢迎……\n',
            '欢迎各位来到神圣的根源之地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13D7',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_1415')

    def _loc_13D7(): pass

    label('loc_13D7')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13FE',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_1415')

    def _loc_13FE(): pass

    label('loc_13FE')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_1415(): pass

    label('loc_1415')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1441',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_147F')

    def _loc_1441(): pass

    label('loc_1441')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1468',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_147F')

    def _loc_1468(): pass

    label('loc_1468')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_147F(): pass

    label('loc_147F')

    Sleep(500)

    OP_21()
    PlayBGM(112)
    Sleep(500)

    Sleep(100)

    Fade(1000)
    OP_E8(0xD0, 0x07, 0x00, 0x00)
    CameraMove(-27410, 100, -350, 0)
    OP_67(0, 3070, -10000, 0)
    CameraSetDistance(6840, 0)
    OP_6C(78000, 0)
    OP_6E(500, 0)

    @scena.Lambda('lambda_14DE')
    def lambda_14DE():
        CameraMove(3190, 2700, 60, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_14DE)

    @scena.Lambda('lambda_14F6')
    def lambda_14F6():
        OP_67(0, 2140, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_14F6)

    @scena.Lambda('lambda_150E')
    def lambda_150E():
        CameraSetDistance(5000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_150E)

    @scena.Lambda('lambda_151E')
    def lambda_151E():
        OP_6C(90000, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_151E)

    Sleep(1000)

    @scena.Lambda('lambda_1533')
    def lambda_1533():
        ChrWalkTo(0x00FE, -17000, 200, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1533)

    Sleep(100)

    @scena.Lambda('lambda_1553')
    def lambda_1553():
        ChrWalkTo(0x00FE, -18650, 200, 1000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_1553)

    Sleep(50)

    @scena.Lambda('lambda_1573')
    def lambda_1573():
        ChrWalkTo(0x00FE, -18500, 200, -1000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_1573)

    WaitForThreadExit(0x0101, 0x0000)
    Fade(1000)
    CameraMove(900, 2760, 250, 0)
    OP_67(0, 4220, -10000, 0)
    CameraSetDistance(2040, 0)
    OP_6C(91000, 0)
    OP_6E(524, 0)
    OP_E8(0xE8, 0x03, 0x00, 0x00)
    OP_0D()
    ChrSetPos(0x0101, -10000, 200, 0, 90)
    ChrSetPos(0x00F9, -11650, 200, 1000, 90)
    ChrSetPos(0x00F8, -11500, 200, -1000, 90)
    OP_E5(0x08, 0x00, 0x01)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010420205V#1020F#5P约修亚……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420206V#1058F#5P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420207V#1151F#5P呵呵呵，看来你们连\n',
            '最后一道试炼也顺利通过了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420208V那就表示你们有资格\n',
            '亲身见证『辉之环』的复活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420209V#1022F#5P我们对那种东西没兴趣！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420210V我们所希望的\n',
            '只是平息这次的异变！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420211V#1005F还有……\n',
            '把约修亚还给我们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420212V#1154F#5P哈哈哈……\n',
            '真遗憾，那可不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420213V#1020F#5P#3S！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420214V#1150F#5P无论你们如何努力，\n',
            '也无法否定约修亚的心被我\n',
            '改造过的事实。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420215V他肩上的『圣痕』就是明证……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420216V#1151F这是他属于『噬身之蛇』──\n',
            '身为我私人物品的最好证据。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420217V#1005F#5P……你……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420218V#1151F#5P呵呵，其实要让约修亚\n',
            '靠自己的意志来消去『圣痕』，\n',
            '获得真正的解放也并不是不可能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420219V但遗憾的是他好像\n',
            '并没能做到呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420220V既然如此，那他就只能继续当\n',
            '我试验用的素材人偶了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420221V#1002F#5P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A14',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420222V#216F#5P你…你这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A14(): pass

    label('loc_1A14')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A4F',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420223V#1162F#5P……好可恨的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A4F(): pass

    label('loc_1A4F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A88',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420224V#523F#5P这个……恶魔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B37')

    def _loc_1A88(): pass

    label('loc_1A88')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1AC1',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420225V#077F#5P……这个恶棍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B37')

    def _loc_1AC1(): pass

    label('loc_1AC1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1AF9',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420226V#1063F#5P邪魔歪道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B37')

    def _loc_1AF9(): pass

    label('loc_1AF9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B37',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420227V#175F真是卑鄙至极……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B37(): pass

    label('loc_1B37')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B6B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420228V#057F#5P混帐东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B6B(): pass

    label('loc_1B6B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BB1',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420229V#272F真是个胡闹的家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BB1(): pass

    label('loc_1BB1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BE9',
    )

    ChrTalk(
        0x0107,
        (
            '#0070420230V#065F#5P太、太过分了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BE9(): pass

    label('loc_1BE9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C27',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420231V#034F#5P……简直是心理变态啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C27(): pass

    label('loc_1C27')

    ChrTalk(
        0x0008,
        (
            '#0150420232V#1154F#5P哎呀呀，别这么说嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420233V#1150F约修亚大概早就清楚\n',
            '自己肩膀上『圣痕』\n',
            '的意义了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420234V想必也曾因它而烦恼得\n',
            '不知所措吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420235V#1020F#5P#3S！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420236V#1154F#5P但即使如此，他似乎却\n',
            '从没向你们提到过这件事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420237V而你们也从来没察觉到\n',
            '他的烦恼和痛苦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420238V#1151F呵呵……你们所谓的羁绊、友情，\n',
            '其实也不过如此吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420239V#1003F#5P…………呜…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E23',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420240V#1169F#5P……………啊…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E23(): pass

    label('loc_1E23')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E65',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420241V#215F#5P……………呜…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E65(): pass

    label('loc_1E65')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1EA7',
    )

    ChrTalk(
        0x0107,
        (
            '#0070420242V#561F#5P…………啊呜…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EA7(): pass

    label('loc_1EA7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1EE7',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420243V#523F#5P…………这…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EE7(): pass

    label('loc_1EE7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F2D',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420244V#176F…………唔…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F2D(): pass

    label('loc_1F2D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F6F',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420245V#072F#5P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F6F(): pass

    label('loc_1F6F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1FAF',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420246V#552F#5P…………哼…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FAF(): pass

    label('loc_1FAF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1FF1',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420247V#032F#5P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FF1(): pass

    label('loc_1FF1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2033',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420248V#276F#5P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2033(): pass

    label('loc_2033')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2076',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420249V#1063F#5P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2076(): pass

    label('loc_2076')

    ChrTalk(
        0x0008,
        (
            '#0150420250V#1154F#5P好了，你们也不必太悲观，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420251V#1150F既然你们能来到这里，\n',
            '我就给你们个机会，接下来就',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420252V看你们能不能做出正确的选择了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420253V#1026F#5P……机会……选择……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420254V那……是什么意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420255V#1150F#5P呵呵呵，那我先问一句，\n',
            '你们究竟了解多少呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_21B3')
    def lambda_21B3():
        CameraMove(5920, 8840, 70, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_21B3)

    @scena.Lambda('lambda_21CB')
    def lambda_21CB():
        OP_67(0, 3770, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_21CB)

    CameraSetDistance(2850, 3000)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0150420256V#1151F#5P──关于这『辉之环』，\n',
            '还有1200年前发生的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420257V#1020F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_22A0',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420258V#1063F#5P果然，那就是『辉之环』吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24D7')

    def _loc_22A0(): pass

    label('loc_22A0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_22E4',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420259V#1162F#5P那果然就是『辉之环』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24D7')

    def _loc_22E4(): pass

    label('loc_22E4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2329',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420260V#032F#5P那果然就是『辉之环』吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24D7')

    def _loc_2329(): pass

    label('loc_2329')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2374',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420261V#178F果然那就是『辉之环』吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24D7')

    def _loc_2374(): pass

    label('loc_2374')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_23B7',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420262V#022F#5P那果然就是『辉之环』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24D7')

    def _loc_23B7(): pass

    label('loc_23B7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_23FC',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420263V#072F#5P那果然就是『辉之环』吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24D7')

    def _loc_23FC(): pass

    label('loc_23FC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_244C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420264V#057F#5P果然那就是『辉之环』吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24D7')

    def _loc_244C(): pass

    label('loc_244C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_248F',
    )

    ChrTalk(
        0x0107,
        (
            '#0070420265V#065F#5P果、果然是『辉之环』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24D7')

    def _loc_248F(): pass

    label('loc_248F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24D7',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420266V#270F果然那就是『辉之环』吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24D7(): pass

    label('loc_24D7')

    ChrTalk(
        0x0008,
        (
            '#0150420267V#1154F#5P不错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420268V#1152F蕴藏着无限的力量，\n',
            '可以创造出无数奇迹的\n',
            '究极古代遗物之一！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420269V但古代人却在1200年前\n',
            '将如此伟大的至宝封印！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420270V你们知道这是为什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_270C',
    )

    FadeOut(300, 0, 100)

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
            TXT(0x00, '【◇查看过全部解析出的情报】\n'),
            TXT(0x01, '【◇查看过一半以上解析出的情报】\n'),
            TXT(0x02, '【◇查看过的解析情报在一定量以下】\n'),
            TXT(0x03, '【◇什么也没有变更】\n'),
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
        (0x00000000, 'loc_2665'),
        (0x00000001, 'loc_2698'),
        (0x00000002, 'loc_26CB'),
        (-1, 'loc_26FE'),
    )

    def _loc_2665(): pass

    label('loc_2665')

    SetScenaFlags(ScenaFlag(0x0450, 0, 0x2280))
    SetScenaFlags(ScenaFlag(0x0450, 1, 0x2281))
    SetScenaFlags(ScenaFlag(0x0450, 2, 0x2282))
    SetScenaFlags(ScenaFlag(0x0450, 3, 0x2283))
    SetScenaFlags(ScenaFlag(0x0450, 4, 0x2284))
    SetScenaFlags(ScenaFlag(0x0450, 5, 0x2285))
    SetScenaFlags(ScenaFlag(0x0450, 6, 0x2286))
    SetScenaFlags(ScenaFlag(0x0450, 7, 0x2287))
    SetScenaFlags(ScenaFlag(0x0451, 0, 0x2288))
    SetScenaFlags(ScenaFlag(0x0451, 1, 0x2289))
    SetScenaFlags(ScenaFlag(0x0451, 2, 0x228A))
    SetScenaFlags(ScenaFlag(0x0451, 3, 0x228B))
    SetScenaFlags(ScenaFlag(0x044E, 6, 0x2276))
    SetScenaFlags(ScenaFlag(0x044E, 7, 0x2277))
    SetScenaFlags(ScenaFlag(0x044F, 0, 0x2278))
    SetScenaFlags(ScenaFlag(0x044F, 1, 0x2279))

    Jump('loc_26FE')

    def _loc_2698(): pass

    label('loc_2698')

    SetScenaFlags(ScenaFlag(0x0450, 0, 0x2280))
    SetScenaFlags(ScenaFlag(0x0450, 1, 0x2281))
    SetScenaFlags(ScenaFlag(0x0450, 2, 0x2282))
    SetScenaFlags(ScenaFlag(0x0450, 3, 0x2283))
    SetScenaFlags(ScenaFlag(0x0450, 4, 0x2284))
    SetScenaFlags(ScenaFlag(0x0450, 5, 0x2285))
    SetScenaFlags(ScenaFlag(0x0450, 6, 0x2286))
    SetScenaFlags(ScenaFlag(0x0450, 7, 0x2287))
    ClearScenaFlags(ScenaFlag(0x0451, 0, 0x2288))
    ClearScenaFlags(ScenaFlag(0x0451, 1, 0x2289))
    ClearScenaFlags(ScenaFlag(0x0451, 2, 0x228A))
    ClearScenaFlags(ScenaFlag(0x0451, 3, 0x228B))
    ClearScenaFlags(ScenaFlag(0x044E, 6, 0x2276))
    ClearScenaFlags(ScenaFlag(0x044E, 7, 0x2277))
    ClearScenaFlags(ScenaFlag(0x044F, 0, 0x2278))
    ClearScenaFlags(ScenaFlag(0x044F, 1, 0x2279))

    Jump('loc_26FE')

    def _loc_26CB(): pass

    label('loc_26CB')

    ClearScenaFlags(ScenaFlag(0x0450, 0, 0x2280))
    ClearScenaFlags(ScenaFlag(0x0450, 1, 0x2281))
    ClearScenaFlags(ScenaFlag(0x0450, 2, 0x2282))
    ClearScenaFlags(ScenaFlag(0x0450, 3, 0x2283))
    ClearScenaFlags(ScenaFlag(0x0450, 4, 0x2284))
    ClearScenaFlags(ScenaFlag(0x0450, 5, 0x2285))
    ClearScenaFlags(ScenaFlag(0x0450, 6, 0x2286))
    ClearScenaFlags(ScenaFlag(0x0450, 7, 0x2287))
    ClearScenaFlags(ScenaFlag(0x0451, 0, 0x2288))
    ClearScenaFlags(ScenaFlag(0x0451, 1, 0x2289))
    ClearScenaFlags(ScenaFlag(0x0451, 2, 0x228A))
    ClearScenaFlags(ScenaFlag(0x0451, 3, 0x228B))
    ClearScenaFlags(ScenaFlag(0x044E, 6, 0x2276))
    ClearScenaFlags(ScenaFlag(0x044E, 7, 0x2277))
    ClearScenaFlags(ScenaFlag(0x044F, 0, 0x2278))
    ClearScenaFlags(ScenaFlag(0x044F, 1, 0x2279))

    Jump('loc_26FE')

    def _loc_26FE(): pass

    label('loc_26FE')

    FadeIn(300, 0)
    Sleep(500)

    def _loc_270C(): pass

    label('loc_270C')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0450, 0, 0x2280)),
            Expr.Return,
        ),
        'loc_2727',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_2727(): pass

    label('loc_2727')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0450, 1, 0x2281)),
            Expr.Return,
        ),
        'loc_2738',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_2738(): pass

    label('loc_2738')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0450, 2, 0x2282)),
            Expr.Return,
        ),
        'loc_2749',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_2749(): pass

    label('loc_2749')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0450, 3, 0x2283)),
            Expr.Return,
        ),
        'loc_275A',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_275A(): pass

    label('loc_275A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0450, 4, 0x2284)),
            Expr.Return,
        ),
        'loc_276B',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_276B(): pass

    label('loc_276B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0450, 5, 0x2285)),
            Expr.Return,
        ),
        'loc_277C',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_277C(): pass

    label('loc_277C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0450, 6, 0x2286)),
            Expr.Return,
        ),
        'loc_278D',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_278D(): pass

    label('loc_278D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0450, 7, 0x2287)),
            Expr.Return,
        ),
        'loc_279E',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_279E(): pass

    label('loc_279E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0451, 0, 0x2288)),
            Expr.Return,
        ),
        'loc_27AF',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_27AF(): pass

    label('loc_27AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0451, 1, 0x2289)),
            Expr.Return,
        ),
        'loc_27C0',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_27C0(): pass

    label('loc_27C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0451, 2, 0x228A)),
            Expr.Return,
        ),
        'loc_27D1',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_27D1(): pass

    label('loc_27D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0451, 3, 0x228B)),
            Expr.Return,
        ),
        'loc_27E2',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_27E2(): pass

    label('loc_27E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x044E, 6, 0x2276)),
            Expr.Return,
        ),
        'loc_27F3',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_27F3(): pass

    label('loc_27F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x044E, 7, 0x2277)),
            Expr.Return,
        ),
        'loc_2804',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_2804(): pass

    label('loc_2804')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x044F, 0, 0x2278)),
            Expr.Return,
        ),
        'loc_2815',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_2815(): pass

    label('loc_2815')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x044F, 1, 0x2279)),
            Expr.Return,
        ),
        'loc_2826',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_2826(): pass

    label('loc_2826')

    Sleep(100)

    Fade(500)
    CameraMove(-16640, 200, 780, 0)
    OP_67(0, 5640, -10000, 0)
    CameraSetDistance(2320, 0)
    OP_6C(45000, 0)
    OP_6E(415, 0)
    ChrSetPos(0x0101, -17120, 200, -110, 90)
    ChrSetPos(0x00F9, -18040, 200, 590, 90)
    ChrSetPos(0x00F8, -18430, 200, -1130, 90)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0xC),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_29D5',
    )

    ChrTalk(
        0x0101,
        (
            '#0010420271V#1003F#6P这…虽然不了解详细情况…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420272V#1002F但在里塔中留存的记录上来看，\n',
            '似乎是人类和社会因为辉之环的影响\n',
            '而开始向坏的方向发展了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420273V#1153F#6P喔～原来你们已经把那个解析出来了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420274V#1150F呵呵呵……那我就马上\n',
            '把全部的真相告诉你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A90')

    def _loc_29D5(): pass

    label('loc_29D5')

    ChrTalk(
        0x0101,
        (
            '#0010420275V#1003F#6P……那、那是…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420276V#1154F#6P呵呵呵，看来\n',
            '你们只顾着应付眼前的事情而\n',
            '疏于收集情报啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420277V#1150F真是没办法，\n',
            '把全部的真相告诉你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A90(): pass

    label('loc_2A90')

    Sleep(200)

    Fade(1000)
    OP_E8(0xD0, 0x07, 0x00, 0x00)
    CameraMove(0, 3120, 1690, 0)
    OP_67(0, 3940, -10000, 0)
    CameraSetDistance(1960, 0)
    OP_6C(45000, 0)
    OP_6E(524, 0)

    @scena.Lambda('lambda_2AE2')
    def lambda_2AE2():
        CameraMove(1490, 2940, 3620, 20000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2AE2)

    @scena.Lambda('lambda_2AFA')
    def lambda_2AFA():
        OP_67(0, 8210, -10000, 20000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2AFA)

    @scena.Lambda('lambda_2B12')
    def lambda_2B12():
        CameraSetDistance(2780, 20000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2B12)

    @scena.Lambda('lambda_2B22')
    def lambda_2B22():
        OP_6C(303000, 20000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2B22)

    @scena.Lambda('lambda_2B32')
    def lambda_2B32():
        OP_6E(583, 20000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2B32)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(1000)

    SetMessageWindowPos(-1, 320, 40, 3)
    TalkSetChrName('怀斯曼教授')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0150420278V#1154F──数千年前。\n',
            '女神将『七至宝』授予人类。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420279V它们各擅其能，\n',
            '利用方式也是迥然不同，\n',
            '人类依靠它们，可以创造出各种奇迹。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420280V#1150F而之后，依靠七至宝\n',
            '的古代人类也渐渐分成了七派，\n',
            '各自追求着自己的『理想』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420281V而当时的成果之一，\n',
            '就是以『辉之环』为核心\n',
            '建造了这座实验都市『利贝尔·方舟』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420282V#1154F『辉之环』通过『福音』这个终端\n',
            '让人类实现了无数从前不敢想象的愿望，\n',
            '为人类建造了这座完美的空中乐园……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420283V住在这里的人们从此就过着与世无争\n',
            '的幸福生活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0150420284V#1152F但人类在通过『福音』不劳而获地\n',
            '获得幸福的同时，自己的灵魂也逐渐\n',
            '开始空虚、堕落。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420285V物质上的享乐自不必说，在欲望的驱使下，\n',
            '他们还发现了可以满足精神需求的东西——\n',
            '那就是『环』所创造出的虚幻梦境。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420286V……之后人类开始彻底堕落，\n',
            '像吸毒一样彻底依赖着奇迹的存在，\n',
            '开始走上了灭亡的道路。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420287V#1154F他们丧失了伦理和上进心，\n',
            '精神上也开始出现了各种问题……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420288V不但出生率逐年降低，\n',
            '而且自杀率和犯罪也飞速增长，\n',
            '整个社会进入了慢性死亡的状态。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420289V#1152F但『环』却并不理会这些，\n',
            '只是继续将无数奇迹赐给人类。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420290V就这样，原本美好的空中花园，\n',
            '最终却变成了肮脏和腐烂的孵化所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0101, 0x03)
    TerminateThread(0x0102, 0x01)
    Sleep(100)

    Fade(500)
    OP_E8(0xE8, 0x03, 0x00, 0x00)
    CameraMove(900, 2760, 250, 0)
    OP_67(0, 4220, -10000, 0)
    CameraSetDistance(2040, 0)
    OP_6C(91000, 0)
    OP_6E(524, 0)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetPos(0x0101, -10000, 200, 0, 90)
    ChrSetPos(0x00F9, -11650, 200, 1000, 90)
    ChrSetPos(0x00F8, -11500, 200, -1000, 90)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0150420291V#1150F#5P在这种情况下，\n',
            '利贝尔王室的祖先们在万般无奈之下\n',
            '只得策划起了封印『辉之环』的计划。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420292V他们在『环』之『守护者』\n',
            '的妨碍下，经过无数努力，\n',
            '建造了封印区域和四轮之塔，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420293V#1154F最后终于将『环』和浮游都市\n',
            '一起封印在了异次元空间中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420294V#1020F#5P那就是……\n',
            '1200年前发生的真相……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3226',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420295V#1163F#5P竟然……\n',
            '有那样的事情吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_334C')

    def _loc_3226(): pass

    label('loc_3226')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3270',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420296V#032F#5P原来如此……\n',
            '竟然有那种事啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_334C')

    def _loc_3270(): pass

    label('loc_3270')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_32C6',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420297V#175F不、不会吧……\n',
            '竟然发生了那样的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_334C')

    def _loc_32C6(): pass

    label('loc_32C6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3305',
    )

    ChrTalk(
        0x0107,
        (
            '#0070420298V#065F#5P竟…竟有那样的事吗…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_334C')

    def _loc_3305(): pass

    label('loc_3305')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_334C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420299V#074F#5P原来如此……\n',
            '是这么一回事啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_334C(): pass

    label('loc_334C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_338D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420300V#552F#5P……真是惊人的真相啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3455')

    def _loc_338D(): pass

    label('loc_338D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_33CE',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420301V#522F#5P……真是惊人的真相呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3455')

    def _loc_33CE(): pass

    label('loc_33CE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3413',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420302V#413F#5P真、真是让人大吃一惊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3455')

    def _loc_3413(): pass

    label('loc_3413')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3455',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420303V#272F真是荒唐透顶……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3455(): pass

    label('loc_3455')

    ChrTalk(
        0x0008,
        (
            '#0150420304V#1154F#5P确实，从某种意义上说\n',
            '王室的祖先们做得很好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420305V#1152F──但你们仔细想想。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420306V那次行为的代价\n',
            '就是让人类重新回到了混沌的大地，\n',
            '一切都要重新开始。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420307V而且现在的世界也进入\n',
            '了无休止的霸权斗争。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420308V重新审视一下的话，\n',
            '他们当时的决定真的就是正确吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420309V#1026F#5P………这……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420310V#1152F#5P另一方面，人类\n',
            '在掌握了导力技术之后\n',
            '再次开始享受着富足安乐的生活。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420311V但继续这样下去的话\n',
            '结果也只有两个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420312V#1154F要么便是不断追求\n',
            '永无止境的欲望，最终\n',
            '让世界再次走向灭亡……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420313V要么就和古代人一样，\n',
            '把一切都交付给科技系统来管理，\n',
            '让自己如同家畜一般苟延残喘……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420314V#1151F总之，无论是物质上的毁灭，还是精神\n',
            '上的毁灭，都是同样可悲的结局。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420315V#1026F#5P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420316V#1152F#5P为了防止那种情况再次重现，\n',
            '唯一的办法就是让自己走上进化的道路！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420317V#1154F──要拥有无论面对任何诱惑和逆境\n',
            '也毫不动摇的绝对理性！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420318V还有不会因感情而迷惑，\n',
            '专心追求真理的究极才智！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420319V只有具备了这两种完美的品性，\n',
            '才能引导人类走向正确的道路。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420320V#1151F这就是\n',
            '『福音计划』的最终目的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3919',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420321V#1063F#5P你难道……是认真的吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3919(): pass

    label('loc_3919')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_395C',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420322V#178F竟、竟然会做出那种事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3992')

    def _loc_395C(): pass

    label('loc_395C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3992',
    )

    ChrTalk(
        0x0107,
        (
            '#0070420323V#065F#5P那、那种事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3992(): pass

    label('loc_3992')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_39D7',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420324V#572F#5P……那种虚无缥缈的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A59')

    def _loc_39D7(): pass

    label('loc_39D7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3A1A',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420325V#034F#5P又是一个妄想症患者啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A59')

    def _loc_3A1A(): pass

    label('loc_3A1A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3A59',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420326V#1169F#5P……那种荒诞的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3A59(): pass

    label('loc_3A59')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3AA2',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420327V#276F哼，真是不可理喻……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B5C')

    def _loc_3AA2(): pass

    label('loc_3AA2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3AE1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420328V#552F#5P……简直是做梦啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B5C')

    def _loc_3AE1(): pass

    label('loc_3AE1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3B1E',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420329V#522F#5P太、太乱来了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B5C')

    def _loc_3B1E(): pass

    label('loc_3B1E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3B5C',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420330V#215F#5P太、太不切实际了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B5C(): pass

    label('loc_3B5C')

    ChrTalk(
        0x0008,
        (
            '#0150420331V#1151F#5P哼哼哼……\n',
            '不要以为我是那种盲目自大\n',
            '的妄想狂。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420332V#1150F人这种生物，在面对着超乎想象\n',
            '的新事物时，在畏惧的同时\n',
            '也会努力进行变革和尝试。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420333V从这一点来看，『辉之环』这东西\n',
            '实在是件绝好的至宝。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420334V#1154F我会利用它将人类\n',
            '指引至正确的进化之道，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420335V#1155F身为『使徒』，\n',
            '那也正是『盟主』交付给我们的使命！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420336V#1007F#5P唉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420337V#1019F你说的倒是很动听，可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0150420338V#1153F#5P……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    StopEffect(0x81, 0x00)
    StopEffect(0x80, 0x00)
    Fade(500)
    CameraMove(-19160, 200, 530, 0)
    OP_67(0, 4950, -10000, 0)
    CameraSetDistance(2500, 0)
    OP_6C(296000, 0)
    OP_6E(415, 0)
    OP_6E(415, 0)
    ChrSetPos(0x0101, -17120, 200, -110, 90)
    ChrSetPos(0x00F9, -18810, 200, 970, 90)
    ChrSetPos(0x00F8, -18420, 200, -1010, 90)
    ChrSetPos(0x0008, -7470, 200, 90, 270)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010420339V#1002F#5P──无论面对任何诱惑和逆境\n',
            '也毫不动摇的绝对理性？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420340V还有不会因感情而迷惑，\n',
            '专心追求真理的究极才智？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420341V那些东西，\n',
            '真的有什么价值吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420342V#1152F#5P……你到底有没有在听\n',
            '我刚才说过的话啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420343V为了避免物质上或精神上的灭亡，\n',
            '人类只有进行自身的进化才……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420344V#1007F#5P和那些无关！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420345V#1006F我想说的只是……\n',
            '在面对着巨大的困境时\n',
            '我们自己是否能做些什么呢？！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420346V#1152F#5P……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4003')
    def lambda_4003():
        CameraSetDistance(2300, 20000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4003)

    ChrTalk(
        0x0101,
        (
            '#0010420347V#1025F#5P约修亚也曾说过的……\n',
            '我们并不只是软弱无力的存在。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420348V就像这次的异变，\n',
            '在一开始，大家都是一筹莫展，\n',
            '但最终我们还是齐心协力，一直走到了这里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420349V#1012F在周游王国的旅途中\n',
            '我更加确信了这一点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420350V#1006F即使不靠什么进化，我们也完全可以凭自己\n',
            '的力量克服一切困难的！你难道不这么想吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420351V#1151F#5P……团结一致谋求生存的的行为\n',
            '即使是野兽和虫蚁也都懂得。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420352V你难以认为人类的潜力就只是\n',
            '那种牲畜程度的本能行为吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420353V#1007F#5P就算是又怎样呢，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420354V#1006F生命本来就是平等的，\n',
            '人也只不过是动物的一种。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420355V努力谋求生存不也正是\n',
            '生命坚强的体现吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420356V#1153F#5P什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420357V#1006F#5P当然了……\n',
            '人并不只是那么简单的存在。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420358V为了绽放生命的光辉，\n',
            '我们每个人都会努力奋斗，\n',
            '寻求自己的价值。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420359V#1012F因此，我们根本就不需要\n',
            '你刚才说的那种万能超人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420360V只要大家彼此关怀，相互体贴，\n',
            '就足以战胜一切困难了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420361V#1152F#5P………………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420362V#1015F#5P我想……\n',
            '封印『辉之环』的人们\n',
            '也是出于同样的考虑吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420363V过分依赖奇迹的力量\n',
            '自然是不对……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420364V#1007F但让人与人的感情逐渐淡漠，\n',
            '彼此之间失去交流和协作…\n',
            '这些才是最可怕的吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_44E1')
    def lambda_44E1():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_44E1)

    Sleep(50)

    @scena.Lambda('lambda_44F4')
    def lambda_44F4():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_44F4)

    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)
    Sleep(300)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4542',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420365V#027F#5P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4704')

    def _loc_4542(): pass

    label('loc_4542')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4579',
    )

    ChrTalk(
        0x0107,
        (
            '#0070420366V#560F#5P艾丝蒂尔姐姐',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4704')

    def _loc_4579(): pass

    label('loc_4579')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_45B1',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420367V#1168F#5P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4704')

    def _loc_45B1(): pass

    label('loc_45B1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_45E8',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420368V#051F#5P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4704')

    def _loc_45E8(): pass

    label('loc_45E8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_461F',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420369V#070F#5P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4704')

    def _loc_461F(): pass

    label('loc_461F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4656',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420370V#030F#5P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4704')

    def _loc_4656(): pass

    label('loc_4656')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_468C',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420371V#171F5P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4704')

    def _loc_468C(): pass

    label('loc_468C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_46C4',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420372V#1060F#5P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4704')

    def _loc_46C4(): pass

    label('loc_46C4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4704',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420373V#213F……啊…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4704(): pass

    label('loc_4704')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4797',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420374V#277F人看似独自生存，但实际上却\n',
            '依赖着许多东西才能活下去……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110420375V#278F哼……确实如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C5E')

    def _loc_4797(): pass

    label('loc_4797')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_482A',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420376V#211F#5P嘿嘿，平时总是一副没大脑的\n',
            '样子，这次竟然能说出这么精辟的话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090420377V#210F看来要对你另眼相看了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C5E')

    def _loc_482A(): pass

    label('loc_482A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_48AA',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420378V#1065F#5P人只有和同伴们团结互助\n',
            '才能算是真正的坚强……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180420379V#1060F正如艾丝蒂尔所说啊。',
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C5E')

    def _loc_48AA(): pass

    label('loc_48AA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4979',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420380V#179F嗯……没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100420381V人类本该互相帮助\n',
            '共同生存……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100420382V#170F若没有这种精神，我们\n',
            '不可能走到今天这一步。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C5E')

    def _loc_4979(): pass

    label('loc_4979')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_49EC',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420383V#035F#5P呵呵……不愧是艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040420384V#030F这一番话……\n',
            '真是太精彩了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C5E')

    def _loc_49EC(): pass

    label('loc_49EC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4A77',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420385V#074F#5P人只有和同伴们团结互助\n',
            '才能算是真正的坚强……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080420386V#070F确实就是如此，正像你说的那样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C5E')

    def _loc_4A77(): pass

    label('loc_4A77')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4AFD',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420387V#053F#5P确实，人类\n',
            '是不能脱离集体的，\n',
            '只有相互团结才能生存下去……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050420388V#051F你说的没错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C5E')

    def _loc_4AFD(): pass

    label('loc_4AFD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4B85',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420389V#1167F#5P艾丝蒂尔的话……\n',
            '我也完全赞成。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060420390V#1168F人与人之间只有团结合作\n',
            '才可以生存延续……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C5E')

    def _loc_4B85(): pass

    label('loc_4B85')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4C5E',
    )

    ChrTalk(
        0x0107,
        (
            '#0070420391V#560F嗯、嗯……\n',
            '我也是这么想的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070420392V#563F没有人是\n',
            '一个人活着的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070420393V回忆、感情……\n',
            '大家都是与他人\n',
            '联系在一起生活下去的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4C5E(): pass

    label('loc_4C5E')

    ChrTalk(
        0x0008,
        (
            '#0150420394V#1154F#5P哼哼……\n',
            '什么，原来只是互助互信而已吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420395V#1151F在说那些蠢话之前，\n',
            '我劝你先多读几本历史书吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420396V就像曾经发生过无数次的\n',
            '重大战争……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420397V在那种情形之下，所谓的感情和互助\n',
            '不也只是毫无价值的无力存在吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010420398V#1022F#5P#3S──才没有那种事！#2S',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420399V#1002F我的妈妈正是为了保护我\n',
            '才在战火中失去了生命！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420400V从那时开始\n',
            '我就立志要当一名合格的游击士！\n',
            '而如今……我正是以游击士的身份，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420401V为了防止异变，\n',
            '为了避免战火而站在这里！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420402V#1005F这样的话……\n',
            '你还能说人类是无力的存在吗！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420403V#1152F#5P哼……\n',
            '……如果那么说的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420404V#1002F#5P而且，如果你真的如此\n',
            '深信人类是无力的存在，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420405V必须要靠进化才能\n',
            '活下去的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420406V#1003F那我只能说，\n',
            '你也只是一个可怜虫而已！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420407V#1153F#5P！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420408V#1007F#5P你无法体会人与人之间的互信互助，\n',
            '还有因此而产生的喜悦和幸福。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420409V#1003F你只能在看到别人\n',
            '痛苦和悲伤时才能感觉到\n',
            '病态的快乐和满足感，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420410V你真是……太可悲了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420411V#1152F#5P………………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420412V#1007F#5P但是，我身为一名游击士……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420413V绝对不能对你种种为了私欲而伤害\n',
            '他人的行为视而不见。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420414V#1002F很抱歉……\n',
            '就算动用武力，我也要阻止你！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 3)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(500)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetDirection(0x00F8, 90, 0)
    ChrSetChipByIndex(0x00F8, 11)
    ChrSetSubChip(0x00F8, 0)
    Sleep(50)

    PlaySE(213, 0x00, 0x64)
    ChrSetDirection(0x00F9, 90, 0)
    ChrSetChipByIndex(0x00F9, 13)
    ChrSetSubChip(0x00F9, 0)
    OP_0D()
    Sleep(500)

    TerminateThread(0x0101, 0x01)
    Fade(500)
    CameraMove(900, 2760, 250, 0)
    OP_67(0, 4220, -10000, 0)
    CameraSetDistance(2040, 0)
    OP_6C(91000, 0)
    OP_6E(524, 0)
    ChrSetPos(0x0008, -1440, 3200, 70, 270)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0150420415V#1152F#5P………………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420416V#1154F哼哼哼哼……\n',
            '无知的小丫头……就会信口开河……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420417V#1151F既然如此，你就用自己的身体\n',
            '来证明一下刚才的那些话吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrSetChipByIndex(0x0008, 21)
    ChrSetSubChip(0x0008, 0)
    OP_0D()
    Sleep(500)

    PlaySE(188, 0x00, 0x64)
    ChrSetSubChip(0x0008, 1)
    Sleep(300)

    ChrSetChipByIndex(0x0008, 15)
    ChrSetSubChip(0x0008, 0)
    Fade(500)
    CameraMove(-16640, 200, 780, 0)
    OP_67(0, 5640, -10000, 0)
    CameraSetDistance(2400, 0)
    OP_6C(45000, 0)
    OP_6E(415, 0)
    ChrSetPos(0x0101, -16570, 200, -110, 90)
    ChrSetPos(0x00F9, -18040, 200, 590, 90)
    ChrSetPos(0x00F8, -18430, 200, -1130, 90)
    OP_0D()
    LoadEffect(0x00, 'monster\\msc0647a.eff')
    LoadEffect(0x01, 'monster\\msc0647b.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -16000, 3200, 0, 0, 0, 0, 800, 800, 800, 0x00FF, 0, 0, -5000, 0)
    Sleep(1200)

    PlayEffect(0x01, 0x01, 0x00F8, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0x02, 0x00F9, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    PlaySE(912, 0x00, 0x64)
    PlaySE(266, 0x00, 0x64)
    Fade(500)
    CameraSetDistance(2160, 500)

    @scena.Lambda('lambda_547D')
    def lambda_547D():
        OP_9E(0x00FE, 15, 0, 300, 4000)
        Yield()

        Jump('lambda_547D')

    DispatchAsync2(0x00F8, 0x0001, lambda_547D)

    @scena.Lambda('lambda_549A')
    def lambda_549A():
        OP_9E(0x00FE, 15, 0, 300, 4000)
        Yield()

        Jump('lambda_549A')

    DispatchAsync2(0x00F9, 0x0001, lambda_549A)

    Sleep(500)

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
        'loc_5508',
    )

    ChrTalk(
        0x0107,
        (
            '#0070420418V#068F#6P呀啊啊啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_56C9')

    def _loc_5508(): pass

    label('loc_5508')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5544',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420419V#1381F#6P啊啊啊啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_56C9')

    def _loc_5544(): pass

    label('loc_5544')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_557D',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420420V#216F#6P哇哇哇……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_56C9')

    def _loc_557D(): pass

    label('loc_557D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_55B2',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420421V#523F#6P呜……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_56C9')

    def _loc_55B2(): pass

    label('loc_55B2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_55ED',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420422V#172F呜……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_56C9')

    def _loc_55ED(): pass

    label('loc_55ED')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5622',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420423V#077F#6P呜……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_56C9')

    def _loc_5622(): pass

    label('loc_5622')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5659',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420424V#039F#6P啊啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_56C9')

    def _loc_5659(): pass

    label('loc_5659')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5694',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420425V#273F唔……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_56C9')

    def _loc_5694(): pass

    label('loc_5694')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_56C9',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420426V#1070F#6P不好了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_56C9(): pass

    label('loc_56C9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5706',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420427V#055F#6P身…身体被……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_58E5')

    def _loc_5706(): pass

    label('loc_5706')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_573E',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420428V#1070F#6P魔眼吗……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_58E5')

    def _loc_573E(): pass

    label('loc_573E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_577F',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420429V#271F这就是魔眼吗……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_58E5')

    def _loc_577F(): pass

    label('loc_577F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_57BE',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420430V#039F#6P这、这就是魔眼吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_58E5')

    def _loc_57BE(): pass

    label('loc_57BE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_57F7',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420431V#077F#6P……魔眼吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_58E5')

    def _loc_57F7(): pass

    label('loc_57F7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5836',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420432V#172F这就是魔眼……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_58E5')

    def _loc_5836(): pass

    label('loc_5836')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_586B',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420433V#523F#6P魔…魔眼…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_58E5')

    def _loc_586B(): pass

    label('loc_586B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_58AA',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420434V#216F#6P这、这是什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_58E5')

    def _loc_58AA(): pass

    label('loc_58AA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_58E5',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420435V#1381F#6P这…这是魔眼……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_58E5(): pass

    label('loc_58E5')

    @scena.Lambda('lambda_58EB')
    def lambda_58EB():
        ChrSetDirection(0x00FE, 270, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_58EB)

    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010420436V#1020F#5P什么……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    StopEffect(0x00, 0x02)
    StopEffect(0x01, 0x02)
    StopEffect(0x02, 0x02)
    OP_23(0x010A)

    ChrTalk(
        0x0008,
        (
            '#0150420437V#1151F#6P哼哼哼，你们\n',
            '就在那里乖乖地地看着吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420438V接下来的好戏会很精彩的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 600)
    PlaySE(216, 0x00, 0x64)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010420439V#1005F#6P什、什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420440V#1154F#6P……约修亚。\n',
            '去陪她稍微玩一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Fade(500)
    CameraMove(-7340, 200, 2720, 0)
    OP_67(0, 5250, -10000, 0)
    CameraSetDistance(2730, 0)
    OP_6C(45000, 0)
    OP_6E(453, 0)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x00F8, 0x0080)
    ChrSetFlags(0x00F9, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0010, -2100, 3200, -950, 270)
    ChrSetPos(0x0012, -18040, 200, 590, 90)
    ChrSetPos(0x0011, -18430, 200, -1130, 90)
    ChrSetChipByIndex(0x0010, 22)
    ChrSetChipByIndex(0x0011, 11)
    ChrSetChipByIndex(0x0012, 13)
    ChrSetSubChip(0x0010, 0)
    ChrSetSubChip(0x0011, 0)
    ChrSetSubChip(0x0012, 0)

    @scena.Lambda('lambda_5AD6')
    def lambda_5AD6():
        OP_9E(0x00FE, 15, 0, 300, 4000)
        Yield()

        Jump('lambda_5AD6')

    DispatchAsync2(0x0011, 0x0001, lambda_5AD6)

    @scena.Lambda('lambda_5AF3')
    def lambda_5AF3():
        OP_9E(0x00FE, 15, 0, 300, 4000)
        Yield()

        Jump('lambda_5AF3')

    DispatchAsync2(0x0012, 0x0001, lambda_5AF3)

    OP_0D()
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0010, 6)
    ChrSetSubChip(0x0010, 0)
    OP_0D()

    ChrTalk(
        0x0010,
        (
            '#0020420441V#1058F#6P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420442V#1020F#5P约、约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420443V#1151F#6P哈哈哈，艾丝蒂尔。\n',
            '请无论如何也让我见识一下啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420444V在绝望中，人到底可以\n',
            '展现出怎样的坚强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420445V#1005F#5P呜……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0010, 10)
    ChrSetAfterImage(0x00, 0x0010, 0x0032, 0x01F4)
    OP_99(0x0010, 0x00, 0x04, 1500)

    @scena.Lambda('lambda_5C4A')
    def lambda_5C4A():
        CameraMove(-15190, 200, -90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5C4A)

    @scena.Lambda('lambda_5C62')
    def lambda_5C62():
        OP_67(0, 6330, -10000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5C62)

    @scena.Lambda('lambda_5C7A')
    def lambda_5C7A():
        CameraSetDistance(1880, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_5C7A)

    @scena.Lambda('lambda_5C8A')
    def lambda_5C8A():
        OP_99(0x00FE, 0x04, 0x06, 2500)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5C8A)

    @scena.Lambda('lambda_5C9A')
    def lambda_5C9A():
        ChrJumpTo(0x00FE, -15000, 3200, -350, 500, 7000)

        ExitThread()

    DispatchAsync(0x0010, 0x0000, lambda_5C9A)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    FormationDelMember(0x01, 0xFF)

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushValueByIndex, 0xB),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0008,
        (
            (Expr.PushValueByIndex, 0xC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x000A,
        (
            (Expr.PushValueByIndex, 0x3D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x000B,
        (
            (Expr.PushValueByIndex, 0x3E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x000C,
        (
            (Expr.PushValueByIndex, 0x3F),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    ChrSetChipByIndex(0x0101, 3)
    ChrSetSubChip(0x0101, 0)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0010, 0xFF)
    OP_C4(0x00, 0x00000100)
    Battle(0x00002714, 0x00300013, 0x00, 0x0000, 0xFF)
    OP_C4(0x01, 0x00000100)

    Return()

# id: 0x0008 offset: 0x5D1F
@scena.Code('func_08_5D1F')
def func_08_5D1F():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0010, 0x00)
    Call(0, 0x0003)
    ChrClearFlags(0x0102, 0x0080)
    ChrClearFlags(0x00F8, 0x0080)
    ChrClearFlags(0x00F9, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetChipByIndex(0x0008, 15)
    ChrSetPos(0x0008, -1440, 3200, 70, 270)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0101, -10370, 200, -800, 135)
    ChrSetPos(0x0102, -8480, 200, -2730, 315)
    ChrSetPos(0x00F9, -18810, 200, 970, 90)
    ChrSetPos(0x00F8, -18420, 200, -1010, 90)
    ChrSetChipByIndex(0x0101, 3)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x00F8, 11)
    ChrSetSubChip(0x00F8, 0)
    ChrSetChipByIndex(0x00F9, 13)
    ChrSetSubChip(0x00F9, 0)

    @scena.Lambda('lambda_5DD8')
    def lambda_5DD8():
        OP_9E(0x00FE, 15, 0, 300, 4000)
        Yield()

        Jump('lambda_5DD8')

    DispatchAsync2(0x00F8, 0x0003, lambda_5DD8)

    @scena.Lambda('lambda_5DF5')
    def lambda_5DF5():
        OP_9E(0x00FE, 15, 0, 300, 4000)
        Yield()

        Jump('lambda_5DF5')

    DispatchAsync2(0x00F9, 0x0003, lambda_5DF5)

    StopEffect(0x81, 0x00)
    StopEffect(0x80, 0x00)
    CameraMove(-8440, 200, -1890, 0)
    OP_67(0, 8960, -10000, 0)
    CameraSetDistance(2200, 0)
    OP_6C(90000, 0)
    OP_6E(382, 0)
    LoadEffect(0x01, 'Craft\\\\cr161_00.eff')

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_5E79'),
        (0x00000007, 'loc_5E86'),
        (0x00000001, 'loc_5E93'),
        (-1, 'loc_5EA0'),
    )

    def _loc_5E79(): pass

    label('loc_5E79')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5EA0')

    def _loc_5E86(): pass

    label('loc_5E86')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5EA0')

    def _loc_5E93(): pass

    label('loc_5E93')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5EA0')

    def _loc_5EA0(): pass

    label('loc_5EA0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5F19',
    )

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
            TXT(0x00, '【◆获胜】（未使用）\n'),
            TXT(0x01, '【◆承受住了约修亚的S必杀技】（未使用）\n'),
            TXT(0x02, '【◆没有承受住】\n'),
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

    def _loc_5F19(): pass

    label('loc_5F19')

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_5F2E'),
        (0x00000001, 'loc_5F31'),
        (0x00000002, 'loc_6093'),
        (-1, 'loc_6253'),
    )

    def _loc_5F2E(): pass

    label('loc_5F2E')

    Jump('loc_6253')

    def _loc_5F31(): pass

    label('loc_5F31')

    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x0102, 6)

    @scena.Lambda('lambda_5F41')
    def lambda_5F41():
        CameraSetDistance(2000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5F41)

    FadeIn(1000, 0)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020420446V#1058F#2P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420447V#1003F#6P……呜……约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420448V#1151F#6P噢噢……\n',
            '真是好厉害的招式啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420449V看来把他放置在『剑圣』\n',
            '身边的决定是明智的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420450V#1154F如今这件作品的完成度\n',
            '再次提高了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010361120V#1005F#6P你…你这个……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6253')

    def _loc_6093(): pass

    label('loc_6093')

    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x0102, 6)
    ChrSetSubChip(0x0101, 3)
    ChrSetChipByIndex(0x0101, 5)

    @scena.Lambda('lambda_60AD')
    def lambda_60AD():
        CameraSetDistance(2000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_60AD)

    FadeIn(1000, 0)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020420452V#1058F#2P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420447V#1003F#6P……呜……约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420448V#1151F#6P噢噢……\n',
            '真是好厉害的招式啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420449V看来把他放置在『剑圣』\n',
            '身边的决定是明智的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420450V#1154F如今这件作品的完成度\n',
            '再次提高了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_61D7')
    def lambda_61D7():
        OP_9E(0x00FE, 30, 0, 5000, 2000)
        Yield()

        Jump('lambda_61D7')

    DispatchAsync2(0x0101, 0x0000, lambda_61D7)

    Sleep(250)

    @scena.Lambda('lambda_61F9')
    def lambda_61F9():
        OP_99(0x00FE, 0x03, 0x00, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_61F9)

    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x0101, 0x00)
    Sleep(250)

    Fade(500)
    ChrSetChipByIndex(0x0101, 3)
    ChrSetSubChip(0x0101, 0)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010361120V#1005F#6P你…你这个……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6253')

    def _loc_6253(): pass

    label('loc_6253')

    ChrTalk(
        0x0008,
        (
            '#0150420458V#1154F#6P好了……\n',
            '真正的余兴节目现在才刚开始。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420459V#1150F约修亚，把她制住！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420460V#1020F#6P！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_62EC')
    def lambda_62EC():
        CameraMove(-10000, 200, 0, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_62EC)

    @scena.Lambda('lambda_6304')
    def lambda_6304():
        OP_67(0, 7100, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_6304)

    @scena.Lambda('lambda_631C')
    def lambda_631C():
        CameraSetDistance(2000, 1000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_631C)

    ChrSetChipByIndex(0x0102, 10)
    ChrSetSubChip(0x0102, 0)
    OP_99(0x0102, 0x00, 0x05, 2500)
    ChrSetChipByIndex(0x0102, 1)
    ChrSetSubChip(0x0102, 13)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetFlags(0x0102, 0x0002)
    ChrSetFlags(0x0102, 0x0020)
    ChrSetAfterImage(0x00, 0x0102, 0x0032, 0x01F4)
    PlaySE(571, 0x00, 0x64)

    @scena.Lambda('lambda_6365')
    def lambda_6365():
        ChrJumpTo(0x00FE, -10270, 400, -1150, 500, 16000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_6365)

    Sleep(70)

    PlaySE(521, 0x00, 0x64)
    ChrSetFlags(0x0101, 0x0800)
    ChrSetFlags(0x0101, 0x8000)
    ChrSetChipByIndex(0x0101, 1)
    ChrSetSubChip(0x0101, 0)
    ChrSetFlags(0x0101, 0x0002)
    ChrSetFlags(0x0101, 0x0020)
    ChrClearFlags(0x0101, 0x0001)

    @scena.Lambda('lambda_63B0')
    def lambda_63B0():
        OP_99(0x00FE, 0x00, 0x03, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_63B0)

    WaitForThreadExit(0x0101, 0x0000)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetAfterImage(0x01, 0x0102, 0x0000, 0x0000)
    OP_99(0x0101, 0x04, 0x07, 2500)
    WaitForThreadExit(0x0101, 0x0003)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetPos(0x001E, -11540, 200, 0, 0)

    NpcTalk(
        0x001E,
        '艾丝蒂尔',
        (
            '#0010420461V#1021F#6P啊啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_645C',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420462V#1069F#5P艾丝蒂尔……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6611')

    def _loc_645C(): pass

    label('loc_645C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6491',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420463V#054F#5P艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6611')

    def _loc_6491(): pass

    label('loc_6491')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_64CA',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420464V#530F#5P艾丝蒂尔……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6611')

    def _loc_64CA(): pass

    label('loc_64CA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_64FF',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420465V#076F#5P艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6611')

    def _loc_64FF(): pass

    label('loc_64FF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6534',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420466V#024F#5P艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6611')

    def _loc_6534(): pass

    label('loc_6534')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6569',
    )

    ChrTalk(
        0x0107,
        (
            '#0070420467V#065F#5P姐、姐姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6611')

    def _loc_6569(): pass

    label('loc_6569')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_65A3',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420468V#1163F#5P艾、艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6611')

    def _loc_65A3(): pass

    label('loc_65A3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_65D9',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420469V#177F艾丝蒂尔……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6611')

    def _loc_65D9(): pass

    label('loc_65D9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6611',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420470V#216F啊啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6611(): pass

    label('loc_6611')

    @scena.Lambda('lambda_6617')
    def lambda_6617():
        CameraSetDistance(1900, 20000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_6617)

    Sleep(100)

    OP_21()
    PlayBGM(91)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0150420471V#1154F#6P哼哼哼，看来你根本\n',
            '就不能证明人类的坚强。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420472V#1150F而我既然身为一名学者，\n',
            '也有义务将理论证实。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420473V#1151F所以就让约修亚来代替你\n',
            '证明给我看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x10),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(150)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x11),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(150)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x10),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(150)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(150)

    Sleep(500)

    NpcTalk(
        0x001E,
        '艾丝蒂尔',
        (
            '#0010420474V#1026F#6P…………哎………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420475V#1154F#6P没什么，只是个简单的实验而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420476V#1150F……就这样让约修亚\n',
            '结果你的性命。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420477V然后我再解除对他的暗示，\n',
            '让他恢复原状。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(
        0x001E,
        '艾丝蒂尔',
        (
            '#0010420478V#1020F#6P#3S！！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420479V#1151F#6P呵呵呵……到那时约修亚\n',
            '会是一副怎样的表情呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420480V光是想象一下就让人很兴奋了对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x001E,
        '艾丝蒂尔',
        (
            '#0010420481V#1022F#6P别、别开玩笑了！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420482V#1023F如果那样做的话………\n',
            '约修亚……约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420483V#1154F#6P哈哈哈哈，也许他的心这次\n',
            '就会彻底崩溃粉碎了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420484V#1151F但就算那样也没关系，\n',
            '我会再次对他进行改造，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420485V像以前一样，再给他一次\n',
            '做回人类的机会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420486V呵呵呵呵……实在太有趣了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x001E,
        '艾丝蒂尔',
        (
            '#0010420487V#1027F#6P不要……\n',
            '……那样的话……太残酷了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420488V#1155F#6P哈哈哈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420489V好了！约修亚……\n',
            '给她致命一击吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x12, 0x13, 1000)
    Sleep(500)

    NpcTalk(
        0x001E,
        '约修亚',
        (
            '#0010420490V#1035F#2P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    PlaySE(501, 0x00, 0x64)
    OP_99(0x0101, 0x07, 0x09, 1200)

    @scena.Lambda('lambda_6B24')
    def lambda_6B24():
        CameraSetDistance(1700, 20000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_6B24)

    Sleep(1000)

    OP_99(0x0101, 0x09, 0x0B, 800)
    Sleep(500)

    NpcTalk(
        0x001E,
        '艾丝蒂尔',
        (
            '#0010420491V#1027F#6P……约修……亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420492V对不起……\n',
            '我们曾经约定过……绝对不会死',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420493V对不起……\n',
            '……要两个人一起走下去，可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6C22',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420494V#418F#5P约修亚……不要啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6CDB')

    def _loc_6C22(): pass

    label('loc_6C22')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6C5E',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420495V#1169F#5P约修亚……不要！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6CDB')

    def _loc_6C5E(): pass

    label('loc_6C5E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6C9F',
    )

    ChrTalk(
        0x0107,
        (
            '#0070420496V#069F#5P约修亚哥哥……不要啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6CDB')

    def _loc_6C9F(): pass

    label('loc_6C9F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6CDB',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420497V#523F#5P约修亚……快住手啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6CDB(): pass

    label('loc_6CDB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6D19',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420498V#177F约修亚君……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6D19(): pass

    label('loc_6D19')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6D5E',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420499V#271F可恶……快醒过来！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6E2D')

    def _loc_6D5E(): pass

    label('loc_6D5E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6D9B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420500V#077F#5P醒醒啊！　约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6E2D')

    def _loc_6D9B(): pass

    label('loc_6D9B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6DE2',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420501V#530F#5P拜托你了……快点清醒过来吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6E2D')

    def _loc_6DE2(): pass

    label('loc_6DE2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6E2D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420502V#550F#5P约修亚！！！\n',
            '你快点给我清醒过来！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6E2D(): pass

    label('loc_6E2D')

    NpcTalk(
        0x001E,
        '艾丝蒂尔',
        (
            '#0010420503V#1003F#6P可是……\n',
            '我……相信你……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420504V#1025F约修亚是绝对……绝对不会输的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420505V即使没有了我……\n',
            '……你也绝不会再逃避现实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x16, 0x17, 1000)
    Sleep(500)

    ChrSetPos(0x001E, -11540, 200, -200, 0)

    NpcTalk(
        0x001E,
        '约修亚',
        (
            '#0010420506V#1035F#2P……抱歉。\n',
            '我可没有那个自信啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x001E, 0xFFFFFED4, 1400, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    PlayBGM(43)
    Sleep(500)

    LoadEffect(0x00, 'craft\\\\cr162_02.eff')
    LoadEffect(0x02, 'map\\\\mp009_00.eff')
    PlayEffect(0x00, 0x00, 0x0101, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ChrSetSubChip(0x0101, 31)
    ChrSetFlags(0x0102, 0x1000)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetFlags(0x0102, 0x0020)

    @scena.Lambda('lambda_6FF6')
    def lambda_6FF6():
        ChrMoveTo(0x00FE, -9860, 2200, 600, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6FF6)

    ChrSetRGBAMask(0x0102, 255, 255, 255, 0, 200)
    Sleep(500)

    Fade(500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(-620, 4500, 40, 0)
    OP_67(0, 6210, -10000, 0)
    CameraSetDistance(1900, 0)
    OP_6C(140000, 0)
    OP_6E(446, 0)
    ChrSetAfterImage(0x00, 0x0102, 0x0032, 0x01F4)
    ChrSetPos(0x0102, -1990, 6500, 630, 90)
    ChrSetChipByIndex(0x0102, 24)
    ChrSetSubChip(0x0102, 2)
    ChrSetPos(0x0008, -800, 3200, 500, 270)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 19)
    OP_0D()

    @scena.Lambda('lambda_70AB')
    def lambda_70AB():
        CameraMove(-620, 3200, 40, 200)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_70AB)

    @scena.Lambda('lambda_70C3')
    def lambda_70C3():
        CameraSetDistance(1670, 200)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_70C3)

    ChrClearFlags(0x0102, 0x0002)
    ChrClearFlags(0x0102, 0x0080)

    @scena.Lambda('lambda_70DD')
    def lambda_70DD():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 100)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_70DD)

    @scena.Lambda('lambda_70EF')
    def lambda_70EF():
        ChrMoveTo(0x00FE, -1990, 3200, 630, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_70EF)

    @scena.Lambda('lambda_710A')
    def lambda_710A():
        OP_99(0x00FE, 0x03, 0x08, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_710A)

    @scena.Lambda('lambda_711A')
    def lambda_711A():
        OP_99(0x00FE, 0x00, 0x05, 4500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_711A)

    Sleep(300)

    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x02, 0x01, 0x0008, 0, 2000, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 300, 3000, 100)

    @scena.Lambda('lambda_717A')
    def lambda_717A():
        OP_9E(0x00FE, 30, 0, 3000, 100)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_717A)

    @scena.Lambda('lambda_7194')
    def lambda_7194():
        OP_9E(0x00FE, 30, 0, 3000, 100)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_7194)

    WaitForThreadExit(0x0102, 0x0000)
    WaitForThreadExit(0x0102, 0x0001)
    WaitForThreadExit(0x0102, 0x0002)
    ChrSetAfterImage(0x01, 0x0102, 0x0000, 0x0000)
    Sleep(500)

    @scena.Lambda('lambda_71CA')
    def lambda_71CA():
        CameraMove(1670, 2700, -700, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_71CA)

    @scena.Lambda('lambda_71E2')
    def lambda_71E2():
        CameraSetDistance(1880, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_71E2)

    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_71F7')
    def lambda_71F7():
        ChrJumpTo(0x00FE, 3180, 2700, 790, 500, 8000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_71F7)

    @scena.Lambda('lambda_7215')
    def lambda_7215():
        OP_99(0x00FE, 0x05, 0x00, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_7215)

    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(164, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0002)
    Sleep(500)

    PlaySE(501, 0x00, 0x64)
    OP_99(0x0102, 0x09, 0x0C, 1500)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0008, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#0150420507V#1153F#5P哦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0102, 0x0004)
    ChrClearFlags(0x0102, 0x0020)
    ChrClearFlags(0x0102, 0x1000)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x0102, 22)
    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_7299')
    def lambda_7299():
        ChrJumpTo(0x00FE, -8460, 200, 200, 1000, 10000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_7299)

    Sleep(200)

    Fade(500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(-14300, 200, -110, 0)
    OP_67(0, 5480, -10000, 0)
    CameraSetDistance(1950, 0)
    OP_6C(135000, 0)
    OP_6E(482, 0)
    WaitForThreadExit(0x0102, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 15)
    ChrSetSubChip(0x0101, 30)
    ChrClearFlags(0x0101, 0x8000)
    OP_0D()
    Sleep(500)

    TerminateThread(0x00F8, 0x03)
    TerminateThread(0x00F9, 0x03)
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7360',
    )

    ChrTalk(
        0x0107,
        (
            '#0070420508V#064F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_74E4')

    def _loc_7360(): pass

    label('loc_7360')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_738F',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420509V#1164F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_74E4')

    def _loc_738F(): pass

    label('loc_738F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_73C4',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420510V#273F嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_74E4')

    def _loc_73C4(): pass

    label('loc_73C4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_73F4',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420511V#213F啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_74E4')

    def _loc_73F4(): pass

    label('loc_73F4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7422',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420512V#023F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_74E4')

    def _loc_7422(): pass

    label('loc_7422')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7457',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420513V#173F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_74E4')

    def _loc_7457(): pass

    label('loc_7457')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7487',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420514V#073F喔啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_74E4')

    def _loc_7487(): pass

    label('loc_7487')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_74B7',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420515V#033F噢噢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_74E4')

    def _loc_74B7(): pass

    label('loc_74B7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_74E4',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420516V#052F喔喔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_74E4(): pass

    label('loc_74E4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7526',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420517V#1060F嘿嘿……\n',
            '缚咒解开了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7713')

    def _loc_7526(): pass

    label('loc_7526')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7562',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420518V#051F缚咒……解开了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7713')

    def _loc_7562(): pass

    label('loc_7562')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_75A1',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420519V#030F缚咒……\n',
            '好象解开了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7713')

    def _loc_75A1(): pass

    label('loc_75A1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_75DD',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420520V#070F缚咒……解开了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7713')

    def _loc_75DD(): pass

    label('loc_75DD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7624',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420521V#171F缚咒……解开了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7713')

    def _loc_7624(): pass

    label('loc_7624')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7660',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420522V#020F缚咒……解开了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7713')

    def _loc_7660(): pass

    label('loc_7660')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_769A',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420523V#210F身、身体自由了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7713')

    def _loc_769A(): pass

    label('loc_769A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_76DB',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420524V#275F缚咒解开了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7713')

    def _loc_76DB(): pass

    label('loc_76DB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7713',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420525V#1382F缚咒……解开了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7713(): pass

    label('loc_7713')

    @scena.Lambda('lambda_7719')
    def lambda_7719():
        CameraMove(-9410, 200, 40, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_7719)

    @scena.Lambda('lambda_7731')
    def lambda_7731():
        OP_67(0, 5160, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7731)

    @scena.Lambda('lambda_7749')
    def lambda_7749():
        CameraSetDistance(1810, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7749)

    @scena.Lambda('lambda_7759')
    def lambda_7759():
        OP_6E(482, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_7759)

    @scena.Lambda('lambda_7769')
    def lambda_7769():
        ChrWalkTo(0x00FE, -13710, 200, 20, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_7769)

    Sleep(100)

    @scena.Lambda('lambda_7789')
    def lambda_7789():
        ChrWalkTo(0x00FE, -14180, 200, 1820, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_7789)

    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(300)

    @scena.Lambda('lambda_77B8')
    def lambda_77B8():
        OP_9E(0x00FE, 30, 0, 5000, 2000)
        Yield()

        Jump('lambda_77B8')

    DispatchAsync2(0x0101, 0x0000, lambda_77B8)

    Sleep(250)

    Fade(500)
    ChrSetPos(0x0101, -11500, 200, 300, 135)
    ChrClearFlags(0x0101, 0x0002)
    ChrSetFlags(0x0101, 0x0001)
    ChrClearFlags(0x0101, 0x0800)
    ChrSetSubChip(0x0101, 3)
    ChrSetChipByIndex(0x0101, 5)
    OP_0D()

    @scena.Lambda('lambda_780A')
    def lambda_780A():
        OP_99(0x00FE, 0x03, 0x00, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_780A)

    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x0101, 0x00)
    Sleep(250)

    Fade(500)
    ChrSetChipByIndex(0x0101, 3)
    ChrSetSubChip(0x0101, 0)
    ChrSetDirection(0x0101, 90, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010420526V#1026F#6P……约修……亚……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390249V#1035F#5P……真对不起，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420528V#1054F这次真是让你\n',
            '受惊了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0008, -1400, 3100, 0, 270)
    ChrSetFlags(0x0008, 0x0800)

    @scena.Lambda('lambda_78E6')
    def lambda_78E6():
        CameraMove(-4500, 2000, -2290, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_78E6)

    @scena.Lambda('lambda_78FE')
    def lambda_78FE():
        OP_67(0, 2600, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_78FE)

    @scena.Lambda('lambda_7916')
    def lambda_7916():
        CameraSetDistance(2600, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7916)

    @scena.Lambda('lambda_7926')
    def lambda_7926():
        OP_6E(490, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_7926)

    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0008,
        (
            '#0150420529V#1153F#5P不、不可能的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420530V怎么可能从那种状态下\n',
            '恢复意志……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0150420531V#1157F#5P等等……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(-7170, 200, -820, 0)
    OP_67(0, 4380, -10000, 0)
    CameraSetDistance(1760, 0)
    OP_6C(135000, 0)
    OP_6E(490, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0150420532V#1158F#6P你……\n',
            '肩上的『圣痕』为何不见了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420533V#1035F#6P…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420534V#1042F……我的深层意识里\n',
            '已经没有你刻下的『圣痕』了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420535V就在刚才，它已经彻底粉碎了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420536V#1156F#6P什、什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(-4500, 2000, -2290, 0)
    OP_67(0, 2600, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(135000, 0)
    OP_6E(490, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020420537V#1042F#6P之前我已经请人替我在『圣痕』\n',
            '的一点上打上了暗示之楔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420538V当此点产生活动的时候，\n',
            '就会反复触发让『圣痕』崩溃的\n',
            '自我暗示。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420539V#1157F#5P！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420540V#1026F#2P暗、暗示之楔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420541V#1040F#5P──不把『圣痕』粉碎的话，\n',
            '我就永远无法保守和你之间的约定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420542V因此在埃尔赛尤号迫降到这座都市时\n',
            '我就请凯文神父打下了暗示之楔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420543V#1004F#2P凯、凯文神父！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_804D',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420544V#1068F#2P啊～他当时找我商量的时候\n',
            '我也吃了一惊呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180420545V#1067F说实话，这种法术\n',
            '只要稍有偏差，就有可能导致\n',
            '无法挽回的后果。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180420546V#1062F不过，约修亚君啊……\n',
            '最后你还是获胜了，不是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420547V#1054F#5P是的……\n',
            '真是非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420548V#1008F#2P啊哈哈哈……\n',
            '就是如此了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420549V#1157F#5P凯文·格拉汉姆……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420550V不过是骑士团的新丁，便没把他放在眼里，\n',
            '没想到竟然坏了我的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180420551V#1065F#2P哈，这也是女神的保佑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180420552V#1060F像你这种教会的叛徒，\n',
            '运气不好也是注定的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180420553V#1066F还有，我也只不过是\n',
            '出了些力气而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180420554V有意见的话你还是去找出主意的人好啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420555V#1156F#5P什、什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0150420556V#1158F#5P难道是……\n',
            '卡西乌斯·布莱特的指点吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_81A8')

    def _loc_804D(): pass

    label('loc_804D')

    ChrTalk(
        0x0008,
        (
            '#0150420557V#1152F#5P凯文·格拉汉姆……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420550V不过是骑士团的新丁，便没把他放在眼里，\n',
            '没想到竟然坏了我的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420559V#1035F#6P我实在要感谢他。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420560V#1040F还有……教导\n',
            '我这么做的那个人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420555V#1156F#5P什、什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0150420556V#1158F#5P难道是……\n',
            '卡西乌斯·布莱特的指点吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_81A8(): pass

    label('loc_81A8')

    ChrTalk(
        0x0101,
        (
            '#0010420563V#1004F#2P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_AD('ED6_DT24/C_VIS174._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    Sleep(2000)

    OP_AE(0x000001F4)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010420564V#1025F#2P对了……那时候……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420565V#1040F#5P嗯……爸爸把一封信交给了我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420566V#1035F『解除你身上缚咒的钥匙\n',
            '就在凯文神父身上。』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420567V『但是，要如何使用那把钥匙\n',
            '就是你自己的问题了。』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420568V#1040F『希望你能在看破怀斯曼行动的同时\n',
            '赢回属于你自己的自由。』',
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
        'loc_8349',
    )

    ChrTalk(
        0x0107,
        (
            '#0070380536V#560F#2P哇……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8349(): pass

    label('loc_8349')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_838C',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420570V#021F#2P呵呵呵……不愧是老师啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8501')

    def _loc_838C(): pass

    label('loc_838C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_83D6',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420571V#051F#2P嘿嘿……\n',
            '果然是大叔的一贯风格。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8501')

    def _loc_83D6(): pass

    label('loc_83D6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_841F',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420572V#071F#2P哈哈哈……不愧是卡西乌斯大人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8501')

    def _loc_841F(): pass

    label('loc_841F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_846C',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420573V#1168F#2P呵呵呵……\n',
            '到底是卡西乌斯先生啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8501')

    def _loc_846C(): pass

    label('loc_846C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_84BA',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420574V#171F呵呵……\n',
            '不愧是卡西乌斯准将……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8501')

    def _loc_84BA(): pass

    label('loc_84BA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8501',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420575V#031F#2P呵呵……\n',
            '真不愧是卡西乌斯先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8501(): pass

    label('loc_8501')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_855B',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420576V#275F哼，真是让我佩服……\n',
            '……精准的预判啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_85BE')

    def _loc_855B(): pass

    label('loc_855B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_85BE',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420577V#210F#2P虽、虽然还没搞懂是怎么回事，\n',
            '不过那个大叔还真是了不起啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_85BE(): pass

    label('loc_85BE')

    ChrTalk(
        0x0101,
        (
            '#0010420578V#1016F#2P真是的……\n',
            '那个臭老爸……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420579V#1157F#5P……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420580V#1043F#6P说实话……我当时真的很烦恼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420581V再次操纵我的你，\n',
            '到底会要我做些什么呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420582V#1035F思考再三，我还是将所有的希望……\n',
            '压到了一点上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420583V以你的性格来推测，让我去做\n',
            '自己最惧怕的事情的可能性最大。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420584V#1042F不出所料，你果然让我这么做……\n',
            '这样一来『圣痕』也就彻底粉碎了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420585V现在的我……已经完全摆脱你的操控了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420586V#1025F#2P约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420587V#1157F#5P……愚蠢……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420588V你只要乖乖追随我的话\n',
            '未来便无可限量……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420589V不但能力会越来越强，\n',
            '更可以进化为完美的人种……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420590V#1035F#6P我和艾丝蒂尔一样……\n',
            '对你说的那些东西一点兴趣也没有。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420591V#1040F人生的道路……\n',
            '并不是他人可以施舍赐予的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420592V而是需要在黑暗中不断摸索，\n',
            '以自身的力量探寻才能得到的宝藏！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420593V#1151F#5P哈哈哈……\n',
            '真是无稽之谈！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420594V回顾一下人类的历史吧，那就是一部黑暗的历史！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420595V如果没有伟大光芒的引导，\n',
            '人类永远也不可能从迷途中找到前进的道路！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420596V#1042F#6P不──！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420597V即使在无尽的黑暗中，\n',
            '人类也可以依靠友情和信赖的灯火照亮\n',
            '前方的道路，携手并肩前进！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420598V#1046F这些就是……\n',
            '我们真正的力量！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420599V#1006F#2P约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420600V#1154F#5P……哼哼……\n',
            '执行者中最没用的废物竟然\n',
            '也敢对我出言不逊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420601V#1151F那就让我看看吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420602V你们那盏在黑暗中也能\n',
            '照亮前方的灯火……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x00000BB8)
    LoadEffect(0x00, 'battle\\\\mgaria0.eff')
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 19)
    OP_99(0x0008, 0x00, 0x03, 1500)
    PlaySE(216, 0x00, 0x64)
    OP_99(0x0008, 0x04, 0x06, 1500)
    PlayEffect(0x00, 0x00, 0x0008, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    Fade(1000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(370, 3800, 0, 0)
    OP_67(0, 3590, -10000, 0)
    CameraSetDistance(2280, 0)
    OP_6C(90000, 0)
    OP_6E(437, 0)
    ChrSetPos(0x0008, -1400, 3200, 0, 270)
    ChrClearFlags(0x0008, 0x0800)
    OP_21()
    PlayBGM(58)
    Sleep(500)

    @scena.Lambda('lambda_8C67')
    def lambda_8C67():
        CameraMove(370, 3600, 0, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_8C67)

    @scena.Lambda('lambda_8C7F')
    def lambda_8C7F():
        CameraSetDistance(2100, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8C7F)

    CreateThread(0x0019, 0x00, 0x00, func_14_D182)
    Sleep(120)

    CreateThread(0x001B, 0x00, 0x00, func_16_D29E)
    Sleep(130)

    CreateThread(0x001C, 0x00, 0x00, func_17_D32C)
    Sleep(110)

    CreateThread(0x001A, 0x00, 0x00, func_15_D210)
    WaitForThreadExit(0x0019, 0x0000)
    WaitForThreadExit(0x001A, 0x0000)
    WaitForThreadExit(0x001B, 0x0000)
    WaitForThreadExit(0x001C, 0x0000)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(1000)

    StopEffect(0x00, 0x02)
    ChrSetPos(0x0102, -10900, 200, 800, 90)
    ChrSetPos(0x0101, -10900, 200, -820, 90)
    ChrSetPos(0x00F9, -13200, 200, 1100, 90)
    ChrSetPos(0x00F8, -13200, 200, -1100, 90)
    ChrSetChipByIndex(0x0101, 3)
    ChrSetChipByIndex(0x0102, 22)
    ChrSetChipByIndex(0x00F8, 11)
    ChrSetChipByIndex(0x00F9, 13)
    ChrSetSubChip(0x0000, 0)
    ChrSetSubChip(0x0001, 0)
    ChrSetSubChip(0x0002, 0)
    ChrSetSubChip(0x0003, 0)
    OP_99(0x0008, 0x06, 0x00, 1500)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0150420603V#1155F#5P『盟主』忠实的部下──',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420604V『蛇之使徒』之一柱，\n',
            '『白面』的力量，现在就让你们见识！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_8DD9')
    def lambda_8DD9():
        CameraMove(-6310, 2180, 60, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_8DD9)

    @scena.Lambda('lambda_8DF1')
    def lambda_8DF1():
        OP_67(0, 2840, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8DF1)

    @scena.Lambda('lambda_8E09')
    def lambda_8E09():
        CameraSetDistance(2950, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_8E09)

    @scena.Lambda('lambda_8E19')
    def lambda_8E19():
        OP_6C(90000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_8E19)

    @scena.Lambda('lambda_8E29')
    def lambda_8E29():
        OP_6E(441, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_8E29)

    WaitForThreadExit(0x0101, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x0101,
        (
            '#0010410824V#1005F#6P……求之不得啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420606V#1046F#6P我们也会全力应战的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_8EA1')
    def lambda_8EA1():
        CameraMove(-3100, 2200, -20, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8EA1)

    @scena.Lambda('lambda_8EB9')
    def lambda_8EB9():
        OP_67(0, 2950, -10000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_8EB9)

    @scena.Lambda('lambda_8ED1')
    def lambda_8ED1():
        CameraSetDistance(2050, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_8ED1)

    @scena.Lambda('lambda_8EE1')
    def lambda_8EE1():
        ChrMoveToRelativeAsync(0x00FE, 6000, 0, 0, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_8EE1)

    @scena.Lambda('lambda_8EFC')
    def lambda_8EFC():
        ChrMoveTo(0x00FE, -4500, 2200, 540, 6500, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0000, lambda_8EFC)

    Sleep(10)

    @scena.Lambda('lambda_8F1C')
    def lambda_8F1C():
        ChrMoveToRelativeAsync(0x00FE, 6000, 0, 0, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_8F1C)

    @scena.Lambda('lambda_8F37')
    def lambda_8F37():
        ChrMoveTo(0x00FE, -4500, 2200, -540, 6500, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0000, lambda_8F37)

    Sleep(10)

    @scena.Lambda('lambda_8F57')
    def lambda_8F57():
        ChrMoveToRelativeAsync(0x00FE, 6000, 0, 0, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0000, lambda_8F57)

    @scena.Lambda('lambda_8F72')
    def lambda_8F72():
        ChrMoveTo(0x00FE, -4500, 1700, 540, 6500, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0000, lambda_8F72)

    Sleep(10)

    @scena.Lambda('lambda_8F92')
    def lambda_8F92():
        ChrMoveToRelativeAsync(0x00FE, 6000, 0, 0, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_8F92)

    @scena.Lambda('lambda_8FAD')
    def lambda_8FAD():
        ChrMoveTo(0x00FE, -4500, 1700, -540, 6500, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0000, lambda_8FAD)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x00F8, 0xFF)
    TerminateThread(0x00F9, 0xFF)
    TerminateThread(0x0019, 0xFF)
    TerminateThread(0x001A, 0xFF)
    TerminateThread(0x001B, 0xFF)
    TerminateThread(0x001C, 0xFF)
    OP_BB(0x01, 0x01, 0x0000001C)
    ChrSetStatus(ChrTable['艾丝蒂尔'], 0xFE, 0)
    ChrSetStatus(ChrTable['约修亚'], 0xFE, 0)
    ChrSetStatus(ChrTable['提妲'], 0xFE, 0)
    ChrSetStatus(ChrTable['阿加特'], 0xFE, 0)
    ChrSetStatus(ChrTable['乔丝特'], 0xFE, 0)
    ChrSetStatus(ChrTable['奥利维尔'], 0xFE, 0)
    ChrSetStatus(ChrTable['金'], 0xFE, 0)
    ChrSetStatus(ChrTable['雪拉扎德'], 0xFE, 0)
    ChrSetStatus(ChrTable['科洛丝'], 0xFE, 0)
    ChrSetStatus(ChrTable['凯文神父'], 0xFE, 0)
    ChrSetStatus(ChrTable['尤莉亚上尉'], 0xFE, 0)
    ChrSetStatus(ChrTable['穆拉'], 0xFE, 0)
    Battle(0x00000459, 0x0030000C, 0x00, 0x0000, 0xFF)

    Return()

# id: 0x0009 offset: 0x9042
@scena.Code('func_09_9042')
def func_09_9042():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x0019, 0x00)
    TerminateThread(0x001A, 0x00)
    TerminateThread(0x001B, 0x00)
    TerminateThread(0x001C, 0x00)
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0102, 0x00)
    TerminateThread(0x00F8, 0x00)
    TerminateThread(0x00F9, 0x00)
    Call(0, 0x0004)
    ChrSetFlags(0x0019, 0x0080)
    ChrSetFlags(0x001A, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -1400, 3200, 0, 270)
    ChrSetChipByIndex(0x0008, 15)
    ChrSetSubChip(0x0008, 0)
    ChrSetPos(0x0101, -8200, 200, -700, 90)
    ChrSetPos(0x0102, -8200, 200, 700, 90)
    ChrSetPos(0x00F8, -9600, 200, -800, 90)
    ChrSetPos(0x00F9, -9600, 200, 800, 90)
    ChrSetChipByIndex(0x0101, 3)
    ChrSetChipByIndex(0x0102, 6)
    ChrSetChipByIndex(0x00F8, 11)
    ChrSetChipByIndex(0x00F9, 13)
    ChrSetSubChip(0x0000, 0)
    ChrSetSubChip(0x0001, 0)
    ChrSetSubChip(0x0002, 0)
    ChrSetSubChip(0x0003, 0)
    CameraMove(-5400, 3000, -70, 0)
    OP_67(0, 2500, -10000, 0)
    CameraSetDistance(2700, 0)
    OP_6C(44000, 0)
    OP_6E(478, 0)
    FadeIn(1000, 0)
    CameraSetDistance(2500, 2000)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0150420607V#1153F#2P哎呀，真让人吃惊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420608V你们这群杂碎竟然能\n',
            '和我纠缠到这种地步……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420609V#1022F#6P呼～～呼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420610V#1006F一向斯文有礼的教授\n',
            '竟然也开始说粗口了啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9278',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420611V#210F#6P这也正是他气急败坏\n',
            '的最好证据了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_94C8')

    def _loc_9278(): pass

    label('loc_9278')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_92BE',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420612V#027F#6P看来他已经彻底\n',
            '气急败坏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_94C8')

    def _loc_92BE(): pass

    label('loc_92BE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9315',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420613V#277F#5P哼……\n',
            '看来你现在没什么余裕了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_94C8')

    def _loc_9315(): pass

    label('loc_9315')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9359',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420614V#051F#6P嘿……\n',
            '已经气急败坏了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_94C8')

    def _loc_9359(): pass

    label('loc_9359')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_93A3',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420615V#035F#6P呼……\n',
            '这是他气急败坏的证据啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_94C8')

    def _loc_93A3(): pass

    label('loc_93A3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_93F3',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420616V#170F看来……\n',
            '你似乎已经没什么余裕了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_94C8')

    def _loc_93F3(): pass

    label('loc_93F3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9439',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420617V#070F#6P嗯……\n',
            '他已经气急败坏了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_94C8')

    def _loc_9439(): pass

    label('loc_9439')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9482',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420618V#1167F#6P……他已经……\n',
            '气急败坏了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_94C8')

    def _loc_9482(): pass

    label('loc_9482')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_94C8',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420619V#1060F#6P他已经……\n',
            '完全气急败坏了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_94C8(): pass

    label('loc_94C8')

    ChrTalk(
        0x0008,
        (
            '#0150420620V#1154F#2P哼哼哼哼……真是可悲啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420621V#1155F脚都已经踏进了鬼门关，\n',
            '自己却还毫无察觉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010420622V#1004F#6P哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    LoadEffect(0x00, 'craft\\\\cr162_02.eff')
    PlayEffect(0x00, 0x00, 0x0008, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x0008, 0x0020)

    @scena.Lambda('lambda_95BB')
    def lambda_95BB():
        ChrMoveTo(0x00FE, -1400, 4500, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_95BB)

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 400)
    TerminateThread(0x0008, 0x01)
    ChrSetPos(0x0008, 8150, 4000, 0, 270)
    Fade(500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(8119, 2800, 0, 0)
    OP_67(0, 3340, -10000, 0)
    CameraSetDistance(2130, 0)
    OP_6C(90000, 0)
    OP_6E(478, 0)
    OP_0D()

    @scena.Lambda('lambda_9642')
    def lambda_9642():
        ChrMoveTo(0x00FE, 8150, 2580, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_9642)

    ChrSetRGBAMask(0x0008, 255, 255, 255, 255, 500)
    WaitForThreadExit(0x0101, 0x0002)
    PlaySE(164, 0x00, 0x64)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010420623V#1020F啊#5P……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420624V#1042F#5P……你要做什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150420625V#1155F#5P本来是想直接将它献给『盟主』的，\n',
            '但现在我改变主意了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420626V就让你们这些鼠辈真正体会一下\n',
            '自己的对手是多伟大的存在吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    OP_DB()
    PlayBGM(112)
    Sleep(500)

    LoadEffect(0x00, 'map\\mp062_02.eff')
    LoadEffect(0x01, 'map\\mp098_00.eff')
    Fade(250)
    OP_E8(0xD0, 0x07, 0x00, 0x00)
    ChrClearFlags(0x0008, 0x0001)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 18)
    OP_0D()
    Sleep(500)

    @scena.Lambda('lambda_97B7')
    def lambda_97B7():
        CameraMove(8119, 9660, 0, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_97B7)

    @scena.Lambda('lambda_97CF')
    def lambda_97CF():
        OP_67(0, 4930, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_97CF)

    @scena.Lambda('lambda_97E7')
    def lambda_97E7():
        CameraSetDistance(1800, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_97E7)

    @scena.Lambda('lambda_97F7')
    def lambda_97F7():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_97F7')

    DispatchAsync2(0x0008, 0x0001, lambda_97F7)

    PlaySE(325, 0x00, 0x64)

    @scena.Lambda('lambda_980F')
    def lambda_980F():
        ChrMoveTo(0x00FE, 8150, 9350, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_980F)

    Sleep(200)

    @scena.Lambda('lambda_982F')
    def lambda_982F():
        ChrMoveTo(0x00FE, 8150, 9350, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_982F)

    Sleep(400)

    @scena.Lambda('lambda_984F')
    def lambda_984F():
        ChrMoveTo(0x00FE, 8150, 9350, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_984F)

    Sleep(700)

    @scena.Lambda('lambda_986F')
    def lambda_986F():
        ChrMoveTo(0x00FE, 8150, 9350, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_986F)

    Sleep(400)

    @scena.Lambda('lambda_988F')
    def lambda_988F():
        ChrMoveTo(0x00FE, 8150, 9350, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_988F)

    WaitForThreadExit(0x0008, 0x0000)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(1500)

    @scena.Lambda('lambda_98BE')
    def lambda_98BE():
        CameraMove(14380, 2700, 360, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_98BE)

    @scena.Lambda('lambda_98D6')
    def lambda_98D6():
        OP_67(0, 9500, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_98D6)

    @scena.Lambda('lambda_98EE')
    def lambda_98EE():
        CameraSetDistance(3380, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_98EE)

    PlayEffect(0x00, 0x00, 0x00FF, 8031, 5100, 92, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(326, 0x00, 0x64)
    Sleep(2500)

    @scena.Lambda('lambda_9972')
    def lambda_9972():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_9972)

    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1000)

    Fade(500)
    StopEffect(0x83, 0x00)
    StopEffect(0x84, 0x00)
    StopEffect(0x85, 0x00)
    StopEffect(0x86, 0x00)
    StopEffect(0x87, 0x00)
    CameraMove(8180, 2580, 200, 0)
    OP_67(0, 593740, -10000, 0)
    CameraSetDistance(120, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_99DF')
    def lambda_99DF():
        CameraMove(8039, 2580, 320, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_99DF)

    @scena.Lambda('lambda_99F7')
    def lambda_99F7():
        CameraSetDistance(180, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_99F7)

    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1500)

    Fade(500)
    OP_E8(0xE8, 0x03, 0x00, 0x00)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    CameraMove(-7680, 200, 820, 0)
    OP_67(0, 7710, -10000, 0)
    CameraSetDistance(3020, 0)
    OP_6C(45000, 0)
    OP_6E(275, 0)
    OP_0D()
    Sleep(300)

    OP_DC()

    ChrTalk(
        0x0101,
        (
            '#0010420627V#1020F#6P什、什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420628V#1044F#6P这、这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9B25',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420629V#1069F#6P难道……\n',
            '和『环』融合了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9DCE')

    def _loc_9B25(): pass

    label('loc_9B25')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9B70',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420630V#1163F#6P难道……\n',
            '和『环』融合了……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9DCE')

    def _loc_9B70(): pass

    label('loc_9B70')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9BBC',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420631V#023F#6P难道……\n',
            '和『环』融合了么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9DCE')

    def _loc_9BBC(): pass

    label('loc_9BBC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9C4F',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9C13',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420632V#072F#6P难道……\n',
            '和『环』融合了吗……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9C4C')

    def _loc_9C13(): pass

    label('loc_9C13')

    ChrTalk(
        0x0108,
        (
            '#0080420633V#072F#6P难道……\n',
            '和『环』融合了吗……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9C4C(): pass

    label('loc_9C4C')

    Jump('loc_9DCE')

    def _loc_9C4F(): pass

    label('loc_9C4F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9CA5',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420634V#172F难道说……\n',
            '正在和『环』融合……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9DCE')

    def _loc_9CA5(): pass

    label('loc_9CA5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9CEB',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420635V#033F#6P难道……\n',
            '和『环』融合了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9DCE')

    def _loc_9CEB(): pass

    label('loc_9CEB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9D33',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420636V#055F#6P难道……\n',
            '和『环』融合了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9DCE')

    def _loc_9D33(): pass

    label('loc_9D33')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9D79',
    )

    ChrTalk(
        0x0107,
        (
            '#0070420637V#065F#6P难道……\n',
            '和『环』融合了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9DCE')

    def _loc_9D79(): pass

    label('loc_9D79')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9DCE',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420638V#273F难道……\n',
            '和『环』融合了吗……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9DCE(): pass

    label('loc_9DCE')

    OP_DB()
    Sleep(100)

    Fade(500)
    StopEffect(0x82, 0x00)
    CameraMove(14340, 2700, 350, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(4010, 0)
    OP_6C(90000, 0)
    OP_6E(372, 0)
    PlayEffect(0x01, 0x01, 0x0008, 0, 0, 0, 0, -45, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_9E54')
    def lambda_9E54():
        CameraSetDistance(2600, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_9E54)

    PlaySE(326, 0x00, 0x64)
    PlaySE(327, 0x00, 0x64)
    Sleep(5000)

    FadeOut(2000, 16777215, -1)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    StopEffect(0x80, 0x00)
    StopEffect(0x81, 0x00)
    StopEffect(0x88, 0x00)
    StopEffect(0x00, 0x00)
    StopEffect(0x01, 0x00)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x86, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x87, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    TerminateThread(0x0008, 0x01)
    ChrClearFlags(0x0008, 0x0002)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, 9580, 5500, 0, 270)
    OP_A1(0x0008, 0x0000)
    OP_72(0x0000, 0x0004)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 171)
    OP_70(0x0000, 210)
    ChrSetPos(0x0101, -8200, 200, -700, 90)
    ChrSetPos(0x0102, -8200, 200, 700, 90)
    ChrSetPos(0x00F8, -9600, 200, -800, 90)
    ChrSetPos(0x00F9, -9600, 200, 800, 90)
    Sleep(4000)

    CameraMove(3940, 6130, -250, 0)
    OP_67(0, 3440, -10000, 0)
    CameraSetDistance(2610, 0)
    OP_6C(269000, 0)
    OP_6E(502, 0)
    FadeIn(1000, 16777215)
    OP_0D()
    Sleep(1000)

    FadeOut(500, 16777215, -1)
    OP_0D()
    CameraMove(15590, 3120, 1900, 0)
    OP_67(0, 3150, -10000, 0)
    CameraSetDistance(2220, 0)
    OP_6C(75000, 0)
    OP_6E(494, 0)
    FadeIn(500, 16777215)
    OP_0D()
    Sleep(1000)

    FadeOut(500, 16777215, -1)
    OP_0D()
    PlaySE(329, 0x00, 0x64)
    CameraMove(11650, 9940, -380, 0)
    OP_67(0, 4420, -10000, 0)
    CameraSetDistance(1700, 0)
    OP_6C(117000, 0)
    OP_6E(492, 0)
    FadeIn(500, 16777215)
    OP_0D()
    Sleep(1000)

    FadeOut(500, 16777215, -1)
    OP_0D()
    CameraMove(-8520, 200, 0, 0)
    OP_67(0, 4500, -10000, 0)
    CameraSetDistance(1540, 0)
    OP_6C(90000, 0)
    OP_6E(665, 0)
    FadeIn(500, 16777215)
    Sleep(500)

    @scena.Lambda('lambda_A1AF')
    def lambda_A1AF():
        CameraMove(13450, 8300, 0, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_A1AF)

    @scena.Lambda('lambda_A1C7')
    def lambda_A1C7():
        OP_67(0, 2410, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_A1C7)

    @scena.Lambda('lambda_A1DF')
    def lambda_A1DF():
        CameraSetDistance(2300, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_A1DF)

    @scena.Lambda('lambda_A1EF')
    def lambda_A1EF():
        OP_6E(600, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_A1EF)

    WaitForThreadExit(0x0101, 0x0000)
    ChrSetPos(0x0101, -1810, 3200, -920, 90)
    ChrSetPos(0x0102, -1810, 3200, 920, 90)
    ChrSetPos(0x00F8, -2800, 2700, -940, 90)
    ChrSetPos(0x00F9, -2800, 2700, 940, 90)
    Sleep(500)

    @scena.Lambda('lambda_A24D')
    def lambda_A24D():
        CameraMove(13450, 8500, 0, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_A24D)

    @scena.Lambda('lambda_A265')
    def lambda_A265():
        OP_67(0, 290, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_A265)

    @scena.Lambda('lambda_A27D')
    def lambda_A27D():
        CameraSetDistance(2200, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_A27D)

    OP_DC()

    ChrTalk(
        0x0101,
        (
            '#0010420639V#1020F#5P啊…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A2F0',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420640V#216F#5P啊、啊啊啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A4D4')

    def _loc_A2F0(): pass

    label('loc_A2F0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A32F',
    )

    ChrTalk(
        0x0107,
        (
            '#0070420641V#065F#5P这、这究竟是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A4D4')

    def _loc_A32F(): pass

    label('loc_A32F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A36C',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420642V#270F可恶………！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A4D4')

    def _loc_A36C(): pass

    label('loc_A36C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A3A9',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420643V#055F#5P这、这家伙……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A4D4')

    def _loc_A3A9(): pass

    label('loc_A3A9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A3E2',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420644V#039F#5P这、这是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A4D4')

    def _loc_A3E2(): pass

    label('loc_A3E2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A41D',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420645V#077F#5P这东西是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A4D4')

    def _loc_A41D(): pass

    label('loc_A41D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A45A',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420646V#523F#5P这、这个是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A4D4')

    def _loc_A45A(): pass

    label('loc_A45A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A496',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420647V#1163F#5P怎、怎么会……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A4D4')

    def _loc_A496(): pass

    label('loc_A496')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A4D4',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420648V#173F不、不会吧……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A4D4(): pass

    label('loc_A4D4')

    ChrTalk(
        0x0102,
        (
            '#0020420649V#1042F#5P这、这种灵压……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 131)
    OP_70(0x0000, 170)
    PlaySE(328, 0x00, 0x64)
    OP_73(0x0000)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 11)
    OP_70(0x0000, 50)
    Sleep(1000)

    SetMessageWindowPos(180, 260, -1, -1)
    TalkSetChrName('怀斯曼的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150420650V哼哼哼……这感觉……\n',
            '比想象中还要好啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420651V那么……\n',
            '先来做个热身运动吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420652V让你们体会一下引导人类进入\n',
            '新时代的『天使』所拥有的力量……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    WaitForThreadExit(0x0101, 0x0000)
    SetScenaFlags(ScenaFlag(0x0453, 0, 0x2298))
    Battle(0x00000465, 0x00300014, 0x00, 0x0000, 0xFF)
    ClearScenaFlags(ScenaFlag(0x0453, 0, 0x2298))

    Return()

# id: 0x000A offset: 0xA622
@scena.Code('func_0A_A622')
def func_0A_A622():
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0x112),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C4(0x00, 0x00000010)
    OP_C0(0x16, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    OP_C4(0x01, 0x00000010)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    Call(0, 0x0005)
    ChrSetPos(0x0101, -8200, 200, -700, 90)
    ChrSetPos(0x0102, -8200, 200, 700, 90)
    ChrSetPos(0x00F8, -9600, 200, -800, 90)
    ChrSetPos(0x00F9, -9600, 200, 800, 90)
    ChrSetChipByIndex(0x0101, 5)
    ChrSetChipByIndex(0x0102, 9)
    ChrSetChipByIndex(0x00F8, 15)
    ChrSetChipByIndex(0x00F9, 16)
    ChrSetSubChip(0x0101, 3)
    ChrSetSubChip(0x0102, 3)
    ChrSetSubChip(0x00F8, 3)
    ChrSetSubChip(0x00F9, 3)
    StopEffect(0x80, 0x00)
    StopEffect(0x81, 0x00)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    StopEffect(0x88, 0x00)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, 9580, 5500, 0, 270)
    OP_A1(0x0008, 0x0000)
    OP_72(0x0000, 0x0004)
    CameraMove(-8410, 200, -30, 0)
    OP_67(0, 5530, -10000, 0)
    CameraSetDistance(2270, 0)
    OP_6C(45000, 0)
    OP_6E(466, 0)
    ChrSetStatus(ChrTable['艾丝蒂尔'], 0xFE, 0)
    ChrSetStatus(ChrTable['约修亚'], 0xFE, 0)
    ChrSetStatus(ChrTable['提妲'], 0xFE, 0)
    ChrSetStatus(ChrTable['阿加特'], 0xFE, 0)
    ChrSetStatus(ChrTable['乔丝特'], 0xFE, 0)
    ChrSetStatus(ChrTable['奥利维尔'], 0xFE, 0)
    ChrSetStatus(ChrTable['金'], 0xFE, 0)
    ChrSetStatus(ChrTable['雪拉扎德'], 0xFE, 0)
    ChrSetStatus(ChrTable['科洛丝'], 0xFE, 0)
    ChrSetStatus(ChrTable['凯文神父'], 0xFE, 0)
    ChrSetStatus(ChrTable['尤莉亚上尉'], 0xFE, 0)
    ChrSetStatus(ChrTable['穆拉'], 0xFE, 0)
    PlaySE(329, 0x00, 0x64)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_A7CB')
    def lambda_A7CB():
        CameraMove(12800, 7190, 1790, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_A7CB)

    @scena.Lambda('lambda_A7E3')
    def lambda_A7E3():
        OP_67(0, 2980, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_A7E3)

    @scena.Lambda('lambda_A7FB')
    def lambda_A7FB():
        CameraSetDistance(2720, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_A7FB)

    @scena.Lambda('lambda_A80B')
    def lambda_A80B():
        OP_6C(69000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_A80B)

    @scena.Lambda('lambda_A81B')
    def lambda_A81B():
        OP_6E(466, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_A81B)

    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    SetMessageWindowPos(220, 240, -1, -1)
    TalkSetChrName('怀斯曼的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150420653V呼呼……\n',
            '终于明白了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420654V这才是真正的力量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0101,
        (
            '#0010420655V#1020F#2P怎、怎么会……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420656V为什么我们的攻击\n',
            '完全都没有用呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420657V#1047F#5P他的周围有一道\n',
            '强大的壁障……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020420658V因此……\n',
            '我们的任何攻击丝毫无效……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(220, 240, -1, -1)
    TalkSetChrName('怀斯曼的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150420659V哈哈哈！即使在七至宝中，\n',
            '『辉之环』也是专门掌管『空间』的存在……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420660V它展开的『绝对壁障』完全\n',
            '不是导力魔法可以相提并论的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420661V现在你们根本无法\n',
            '再跟我抗衡了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(100)

    LoadEffect(0x00, 'monster\\msc0647a.eff')
    LoadEffect(0x01, 'monster\\msc0647b.eff')
    Fade(500)
    CameraMove(-7000, 200, 1060, 0)
    OP_67(0, 5860, -10000, 0)
    CameraSetDistance(2000, 0)
    OP_6C(45000, 0)
    OP_6E(466, 0)
    OP_0D()
    PlayEffect(0x00, 0x00, 0x00FF, -5200, 3000, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1200)

    PlayEffect(0x01, 0x01, 0x0101, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0x02, 0x0102, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0x03, 0x00F8, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0x04, 0x00F9, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    PlaySE(912, 0x00, 0x64)
    PlaySE(266, 0x00, 0x64)
    Fade(500)
    CameraSetDistance(1800, 500)

    @scena.Lambda('lambda_ABD2')
    def lambda_ABD2():
        OP_9E(0x00FE, 15, 0, 300, 4000)
        Yield()

        Jump('lambda_ABD2')

    DispatchAsync2(0x0101, 0x0003, lambda_ABD2)

    @scena.Lambda('lambda_ABEF')
    def lambda_ABEF():
        OP_9E(0x00FE, 15, 0, 300, 4000)
        Yield()

        Jump('lambda_ABEF')

    DispatchAsync2(0x0102, 0x0003, lambda_ABEF)

    @scena.Lambda('lambda_AC0C')
    def lambda_AC0C():
        OP_9E(0x00FE, 15, 0, 300, 4000)
        Yield()

        Jump('lambda_AC0C')

    DispatchAsync2(0x00F8, 0x0003, lambda_AC0C)

    @scena.Lambda('lambda_AC29')
    def lambda_AC29():
        OP_9E(0x00FE, 15, 0, 300, 4000)
        Yield()

        Jump('lambda_AC29')

    DispatchAsync2(0x00F9, 0x0003, lambda_AC29)

    Sleep(1500)

    ChrTalk(
        0x0101,
        (
            '#0010420662V#1021F#6P呜……',
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
        'loc_AC96',
    )

    ChrTalk(
        0x0107,
        (
            '#0070420663V#068F#6P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AC96(): pass

    label('loc_AC96')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_ACCF',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420664V#216F#6P这、这个……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AD0E')

    def _loc_ACCF(): pass

    label('loc_ACCF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AD0E',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420665V#175F#5P……可恶………！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AD0E(): pass

    label('loc_AD0E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AD48',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420666V#1070F#6P又是魔眼吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AD7F')

    def _loc_AD48(): pass

    label('loc_AD48')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AD7F',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420667V#1381F#6P魔、魔眼……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AD7F(): pass

    label('loc_AD7F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_ADBE',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420668V#523F#6P这个……卑鄙的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ADFE')

    def _loc_ADBE(): pass

    label('loc_ADBE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_ADFE',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420669V#057F#6P可恶……卑鄙的家伙……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_ADFE(): pass

    label('loc_ADFE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AE4B',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420670V#271F#5P可恶……\n',
            '竟敢如此轻视我……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AE92')

    def _loc_AE4B(): pass

    label('loc_AE4B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AE92',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420671V#077F#6P可恶……\n',
            '又是这种无耻的招术……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AE92(): pass

    label('loc_AE92')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AEDB',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420672V#039F#6P哎呀呀……\n',
            '真是已经无药可救了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AEDB(): pass

    label('loc_AEDB')

    ChrTalk(
        0x0102,
        (
            '#0020420673V#1038F#5P#6P怀斯曼……你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    StopEffect(0x00, 0x00)
    StopEffect(0x01, 0x00)
    StopEffect(0x02, 0x00)
    StopEffect(0x03, 0x00)
    StopEffect(0x04, 0x00)
    OP_23(0x010A)
    CameraMove(12800, 7190, 1790, 0)
    OP_67(0, 2980, -10000, 0)
    CameraSetDistance(2720, 0)
    OP_6C(69000, 0)
    OP_6E(466, 0)
    OP_0D()
    Sleep(500)

    SetMessageWindowPos(220, 240, -1, -1)
    TalkSetChrName('怀斯曼的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150420674V哼哼哼……很好的眼神……\n',
            '杀掉你的话果然还是太可惜了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420675V不如再好好修理调整一番，\n',
            '重新刻上『圣痕』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420676V等你心中新的希望再次发芽时，\n',
            '我就再次把它连根拔除掉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420677V一想到你那由希望变成绝望的表情……\n',
            '我就兴奋不已啊……哇哈哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 280)
    OP_70(0x0001, 300)
    OP_72(0x0001, 0x0004)
    OP_CF(0x0009, 0x01, 'Frame143_on_head')
    OP_A1(0x0020, 0x0001)
    ChrSetPos(0x0020, 4500, 20000, 8200, 160)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 280)
    OP_70(0x0001, 300)
    ChrSetChipByIndex(0x0009, 20)
    ChrSetSubChip(0x0009, 0)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0009, 0x0001)
    ChrSetFlags(0x0009, 0x0020)
    ChrSetFlags(0x0009, 0x0010)
    ChrSetFlags(0x0009, 0x1000)
    SetMessageWindowPos(50, 75, -1, -1)
    TalkSetChrName('青年的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0150420678V真是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420679V这已经不能用低级趣味来形容了，\n',
            '根本就是一个病入膏肓的疯子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_20(0x000003E8)

    ChrTalk(
        0x0101,
        (
            '#0010330788V#1020F#2P！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_21()
    OP_59()
    PlayBGM(123)
    Sleep(1000)

    PlaySE(344, 0x00, 0x64)
    Fade(500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(5800, 15000, 6210, 0)
    OP_67(0, 5430, -10000, 0)
    CameraSetDistance(2300, 0)
    OP_6C(332000, 0)
    OP_6E(513, 0)
    OP_0D()

    @scena.Lambda('lambda_B21B')
    def lambda_B21B():
        ChrMoveTo(0x00FE, 4500, 3000, 8200, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_B21B)

    @scena.Lambda('lambda_B236')
    def lambda_B236():
        CameraMove(3430, 5000, 11850, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_B236)

    @scena.Lambda('lambda_B24E')
    def lambda_B24E():
        OP_67(0, 3440, -10000, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_B24E)

    @scena.Lambda('lambda_B266')
    def lambda_B266():
        CameraSetDistance(2150, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_B266)

    @scena.Lambda('lambda_B276')
    def lambda_B276():
        OP_6C(348000, 1200)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_B276)

    @scena.Lambda('lambda_B286')
    def lambda_B286():
        OP_6E(513, 1200)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_B286)

    OP_71(0x0000, 0x0004)
    Sleep(400)

    OP_72(0x0001, 0x0020)
    OP_6F(0x0001, 300)
    OP_70(0x0001, 310)
    WaitForThreadExit(0x0020, 0x0001)
    OP_23(0x0158)
    PlaySE(236, 0x00, 0x64)
    OP_7C(0, 500, 3000, 1300)
    OP_73(0x0001)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 20)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010420681V#1004F#2P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420682V#1044F#5P莱维！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    OP_72(0x0000, 0x0004)
    CameraMove(13040, 2700, -4200, 0)
    OP_67(0, 4450, -10000, 0)
    CameraSetDistance(3730, 0)
    OP_6C(146000, 0)
    OP_6E(588, 0)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x00F8, 0x0080)
    ChrSetFlags(0x00F9, 0x0080)
    ChrSetPos(0x0101, -10920, 200, -19120, 90)
    ChrSetPos(0x0102, -10920, 200, -19120, 90)
    ChrSetPos(0x00F8, -10920, 200, -19120, 90)
    ChrSetPos(0x00F9, -10920, 200, -19120, 90)
    OP_0D()

    @scena.Lambda('lambda_B3DC')
    def lambda_B3DC():
        CameraMove(6380, 6000, -2730, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_B3DC)

    @scena.Lambda('lambda_B3F4')
    def lambda_B3F4():
        OP_67(0, 2760, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_B3F4)

    @scena.Lambda('lambda_B40C')
    def lambda_B40C():
        CameraSetDistance(3560, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_B40C)

    @scena.Lambda('lambda_B41C')
    def lambda_B41C():
        OP_6C(185000, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_B41C)

    @scena.Lambda('lambda_B42C')
    def lambda_B42C():
        OP_6E(553, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_B42C)

    LoadEffect(0x00, 'map\\mp095_00.eff')
    LoadEffect(0x02, 'map\\mp100_00.eff')
    LoadEffect(0x03, 'monster\\ms31004a.eff')
    LoadEffect(0x04, 'map\\mp099_00.eff')
    OP_72(0x0001, 0x0020)
    OP_D8(0x01, 0x01F4)
    OP_6F(0x0001, 880)
    OP_70(0x0001, 940)
    PlaySE(322, 0x00, 0x64)
    Sleep(2000)

    Play3DEffect(0x00, 0x00, 0x01, 'Frame34_Bone__33_', 0x00000000, 0x00000000, 0x00000000, 0x00AA, 0x0000, 0xFFEC, 0x000003E8, 0x000003E8, 0x000003E8, 0x00000000)
    Sleep(50)

    PlaySE(323, 0x00, 0x64)
    Play3DEffect(0x00, 0x01, 0x01, 'Frame26_Bone__25_', 0x00000000, 0x00000000, 0x00000000, 0x00A0, 0x0000, 0xFFFB, 0x000003E8, 0x000003E8, 0x000003E8, 0x00000000)
    OP_73(0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    PlayEffect(0x03, 0x02, 0x0008, 0, 0, 0, 0, 0, 0, 11000, 21000, 11000, 0x00FF, 0, 0, 0, 0)
    Fade(500)

    @scena.Lambda('lambda_B569')
    def lambda_B569():
        CameraSetDistance(2760, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_B569)

    OP_D8(0x01, 0x01F4)
    OP_B0(0x0001, 0x14)
    OP_6F(0x0001, 1070)
    OP_70(0x0001, 1080)
    OP_73(0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    StopEffect(0x00, 0x00)
    OP_7C(600, 600, 3000, 500)
    PlayEffect(0x02, 0x03, 0x00FF, 7000, 6800, 2700, 0, 0, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x04, 0xFF, 0x0008, 0, 1500, 0, 40, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    CreateThread(0x0020, 0x03, 0x00, func_0F_CFC7)
    OP_71(0x0001, 0x0020)
    OP_B0(0x0001, 0x0F)
    OP_6F(0x0001, 1080)
    OP_70(0x0001, 1085)
    PlaySE(330, 0x00, 0x64)

    @scena.Lambda('lambda_B638')
    def lambda_B638():
        ChrSetDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_B638)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_B64B')
    def lambda_B64B():
        ChrSetDirection(0x00FE, 335, 50)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_B64B)

    WaitForThreadExit(0x0008, 0x0000)
    Sleep(500)

    @scena.Lambda('lambda_B663')
    def lambda_B663():
        OP_7C(30, 30, 3000, 100)
        Yield()

        Jump('lambda_B663')

    DispatchAsync2(0x0101, 0x0000, lambda_B663)

    SetMessageWindowPos(50, 150, -1, -1)
    TalkSetChrName('怀斯曼的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150420683V哼……\n',
            '想来给我致命的一击吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420684V可是莱维啊。\n',
            '就算你来了又能怎样？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420685V即使是幻想乐曲·德尔基昂，\n',
            '想破坏『环』之壁障也是完全不可能的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0009,
        (
            '#0140420686V#124F#6P……也许吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140420687V#121F怀斯曼。\n',
            '我只有一件事想问你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140420688V『哈梅尔的悲剧』……\n',
            '究竟和你有多少关联？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0101, -3840, 200, 11780, 135)
    ChrSetPos(0x0102, -2670, 200, 13060, 135)
    ChrSetPos(0x00F8, -4660, 200, 13340, 135)
    ChrSetPos(0x00F9, -3540, 200, 14580, 135)

    ChrTalk(
        0x0102,
        (
            '#0020420689V#1044F#1P！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(50, 150, -1, -1)
    TalkSetChrName('怀斯曼的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150420690V喔喔，你不要凭空\n',
            '污人清白啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420691V那是帝国主战派\n',
            '谋划的事件吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420692V和我有什么关系？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0009,
        (
            '#0140420693V#121F#6P你的本性就是『蛇』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140420694V#124F在心术不正的人耳边\n',
            '呢喃低语……将恶毒的计划传授给他们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140420695V即使不亲身参与其中，\n',
            '也可以利用他人……来达成自己的目的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140420696V#120F……那也正是你的惯用手段吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420697V#1042F#1P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140420698V#124F#6P我曾听闻，当时在帝国内部中，\n',
            '那些主战派的首谋者们在政权斗争中失败，\n',
            '已经处在无人响应的落魄境界了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140420699V如果说10年前的那场战争\n',
            '是在为你这次的计划而布局的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140420700V#120F那么一切也就都变得合情合理了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(60, 150, -1, -1)
    TalkSetChrName('怀斯曼的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150420701V哼哼哼哼……算你聪明。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420702V算了，那我就承认好了，\n',
            '你的推测基本正确。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0101,
        (
            '#0010420703V#1020F#1P！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(50, 150, -1, -1)
    TalkSetChrName('怀斯曼的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150420704V其实我所做的事情也只不过是\n',
            '把猎兵介绍给他们，然后让他们\n',
            '牢牢地记住了哈梅尔这个名字而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420705V而自那之后事态就发生了急转，\n',
            '转眼之间战争就爆发了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420706V哈哈哈哈……真是一次\n',
            '了不起的实验结果啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BCBD',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420707V#550F#1P……你……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050420708V就因为你这个混蛋……\n',
            '米夏……我的妹妹才会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BCBD(): pass

    label('loc_BCBD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BCFE',
    )

    ChrTalk(
        0x0107,
        (
            '#0070420709V#069F#1P过分……\n',
            '……太过分了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BCFE(): pass

    label('loc_BCFE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BD55',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420710V#039F#1P……竟然可以面不改色地\n',
            '说出这些没有人性的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BD55(): pass

    label('loc_BD55')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BDB9',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420711V#177F#1P像你这种家伙，害得多少\n',
            '无辜的人……！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BDB9(): pass

    label('loc_BDB9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BE09',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420712V#1162F#1P……不能原谅……\n',
            '你……简直令人恶心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BE09(): pass

    label('loc_BE09')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BE45',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420713V#523F#1P恶棍……下地狱去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BE45(): pass

    label('loc_BE45')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BE8E',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420714V#077F#1P恶有恶报……\n',
            '你一定会遭到报应的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BE8E(): pass

    label('loc_BE8E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BEDF',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420715V#216F#1P真…真是无法相信…\n',
            '竟然还会有这样的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BEDF(): pass

    label('loc_BEDF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BF33',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420716V#276F#1P你这家伙……\n',
            '不会有好下场的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BF33(): pass

    label('loc_BF33')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BF78',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420717V#1063F#1P……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BF78(): pass

    label('loc_BF78')

    ChrTalk(
        0x0101,
        (
            '#0010420718V#1027F#1P……总算是真相大白了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140420719V#124F#6P原来如此……\n',
            '大致上和我推想的差不多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(75, 150, -1, -1)
    TalkSetChrName('怀斯曼的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150420720V……哎呀，真意外，你竟然如此平静。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420721V我本来还想欣赏一下你\n',
            '愤怒到发狂的表情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0009,
        (
            '#0140420722V#1430F#6P呵呵，我的心早已经\n',
            '变得和坚冰一样了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140420723V#123F不过，被你从背后偷袭\n',
            '击晕的丑态，\n',
            '对『剑帝』来说才是屈辱的极致。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140420724V仅此一点，我也要让你付出代价！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(70, 150, -1, -1)
    TalkSetChrName('怀斯曼的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150420725V什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(100)

    LoadEffect(0x06, 'map\\\\mp009_00.eff')
    PlaySE(213, 0x00, 0x64)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x0009, 23)
    ChrSetDirection(0x0009, 0, 0)
    Sleep(500)

    Fade(500)
    LoadEffect(0x02, 'map\\mp102_00.eff')
    OP_23(0x014A)
    OP_23(0x0143)
    StopEffect(0x03, 0x00)

    @scena.Lambda('lambda_C1BD')
    def lambda_C1BD():
        ChrMoveTo(0x00FE, 3500, 3000, 9200, 0, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_C1BD)

    CameraMove(9480, 3200, 9470, 0)
    OP_67(0, 4720, -10000, 0)
    CameraSetDistance(2200, 0)
    OP_6C(44000, 0)
    OP_6E(553, 0)

    @scena.Lambda('lambda_C215')
    def lambda_C215():
        CameraMove(10810, 3700, 8730, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_C215)

    OP_72(0x0001, 0x0020)
    OP_70(0x0001, 1085)
    ChrSetFlags(0x0009, 0x0004)
    StopEffect(0x00, 0x02)
    PlaySE(163, 0x00, 0x64)
    OP_CF(0x0009, 0x01, 'Frame140_on_r_arm')
    ChrSetDirection(0x0009, 180, 0)

    @scena.Lambda('lambda_C263')
    def lambda_C263():
        ChrJumpTo(0x00FE, 4760, 7000, 3580, 1300, 5000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_C263)

    @scena.Lambda('lambda_C281')
    def lambda_C281():
        OP_99(0x00FE, 0x00, 0x02, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_C281)

    Sleep(300)

    @scena.Lambda('lambda_C296')
    def lambda_C296():
        OP_99(0x00FE, 0x02, 0x04, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_C296)

    WaitForThreadExit(0x0009, 0x0001)
    WaitForThreadExit(0x0009, 0x0002)
    LoadEffect(0x07, 'map\\mp101_00.eff')
    ChrSetDirection(0x0009, 180, 0)
    ChrSetFlags(0x0009, 0x0020)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x0009, 17)
    OP_CF(0x0009, 0x01, 'Frame141_on_r_arm')
    ChrClearFlags(0x0009, 0x0004)
    ChrSetDirection(0x0009, 0, 0)
    PlayEffect(0x07, 0xFF, 0x0008, 1300, 2600, -5200, 140, 0, -2, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(214, 0x00, 0x64)
    PlaySE(155, 0x00, 0x64)
    PlaySE(331, 0x00, 0x64)

    @scena.Lambda('lambda_C33F')
    def lambda_C33F():
        OP_7C(300, 300, 3000, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_C33F)

    CreateThread(0x0009, 0x03, 0x00, func_12_D106)
    ChrSetAfterImage(0x01, 0x0009, 0x0000, 0x0000)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0140420726V#126F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(370, 70, -1, -1)
    TalkSetChrName('怀斯曼的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150420727V不可能……\n',
            '『环』的绝对壁障怎么会……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420728V！！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420729V原来如此……那把剑是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0009,
        (
            '#0140420730V#124F#5P不错……\n',
            '这是『盟主』赐给我的剑……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140420731V#123F和你的杖一样，\n',
            '是以『外』之理打造的魔剑……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(370, 70, -1, -1)
    TalkSetChrName('怀斯曼的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150420732V可恶……我太大意了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420733V……够了……快点滚开……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420734V快滚开……你这个疯子！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    @scena.Lambda('lambda_C51B')
    def lambda_C51B():
        CameraSetDistance(3000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_C51B)

    LoadEffect(0x05, 'monster\\ms31002a.eff')
    CreateThread(0x0008, 0x00, 0x00, func_11_D08A)
    Sleep(500)

    @scena.Lambda('lambda_C54E')
    def lambda_C54E():
        OP_9E(0x00FE, 1500, 1500, 500, 5000)
        Yield()

        Jump('lambda_C54E')

    DispatchAsync2(0x0020, 0x0002, lambda_C54E)

    Sleep(1000)

    ChrSetPos(0x0101, -8200, 200, -900, 90)
    ChrSetPos(0x0102, -8200, 200, 750, 90)
    ChrSetPos(0x00F8, -9600, 200, -850, 90)
    ChrSetPos(0x00F9, -9600, 200, 850, 90)

    ChrTalk(
        0x0009,
        (
            '#0140420735V#1432F#5P#10A呜啊……！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(1000)

    Sleep(1000)

    CreateThread(0x0008, 0x00, 0x00, func_10_D00E)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0140420736V#1430F#5P#15A呵呵……已经晚了……',
            TxtCtl.Enter,
        ),
    )

    Sleep(2000)

    TerminateThread(0x0020, 0x03)
    Sleep(500)

    StopEffect(0x02, 0x02)
    PlayEffect(0x02, 0x01, 0x0008, 0, 3000, 0, 150, 0, 0, 1200, 800, 1200, 0x00FF, 0, 0, 0, 0)
    ChrClearFlags(0x0009, 0x0002)
    ChrSetChipByIndex(0x0009, 23)
    ChrSetSubChip(0x0009, 5)

    @scena.Lambda('lambda_C67A')
    def lambda_C67A():
        OP_99(0x00FE, 0x05, 0x06, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_C67A)

    TerminateThread(0x0009, 0x03)
    TerminateThread(0x0101, 0x00)
    PlaySE(155, 0x00, 0x64)
    PlaySE(313, 0x00, 0x64)
    Fade(500)
    LoadEffect(0x07, 'monster\\ms31002c.eff')
    OP_0D()
    StopEffect(0x03, 0x02)
    StopEffect(0x06, 0x02)
    TerminateThread(0x0008, 0x00)
    TerminateThread(0x0020, 0x02)

    @scena.Lambda('lambda_C6C7')
    def lambda_C6C7():
        CameraMove(-5870, 200, 14300, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_C6C7)

    @scena.Lambda('lambda_C6DF')
    def lambda_C6DF():
        OP_67(0, 5510, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_C6DF)

    @scena.Lambda('lambda_C6F7')
    def lambda_C6F7():
        CameraSetDistance(2200, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_C6F7)

    @scena.Lambda('lambda_C707')
    def lambda_C707():
        OP_6E(500, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_C707)

    CreateThread(0x0009, 0x00, 0x00, func_0D_CEF1)
    CreateThread(0x0020, 0x00, 0x00, func_0E_CF4E)
    WaitForThreadExit(0x0009, 0x0001)
    WaitForThreadExit(0x0020, 0x0000)
    OP_73(0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010420737V#1020F#1P啊啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420738V#1046F#1P#3S莱、莱维！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)

    @scena.Lambda('lambda_C795')
    def lambda_C795():
        CameraSetDistance(1900, 0)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_C795)

    ChrSetSubChip(0x0009, 5)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0140420739V#121F#5P不要管我……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140420740V前方的路已经拓开……！\n',
            '……接下来就要看你们的了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420741V#1043F#1P哼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(-5210, 200, 7340, 0)
    OP_67(0, 3780, -10000, 0)
    CameraSetDistance(3140, 0)
    OP_6C(45000, 0)
    OP_6E(479, 0)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0102, 0x0080)
    ChrClearFlags(0x00F8, 0x0080)
    ChrClearFlags(0x00F9, 0x0080)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0102, 0x0080)
    ChrClearFlags(0x00F8, 0x0080)
    ChrClearFlags(0x00F9, 0x0080)
    ChrSetPos(0x0101, -8200, 200, -900, 90)
    ChrSetPos(0x0102, -8200, 200, 750, 90)
    ChrSetPos(0x00F8, -9600, 200, -850, 90)
    ChrSetPos(0x00F9, -9600, 200, 850, 90)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0102, 0)
    ChrSetSubChip(0x00F8, 0)
    ChrSetSubChip(0x00F9, 0)
    ChrSetChipByIndex(0x0101, 3)
    ChrSetChipByIndex(0x0102, 6)
    ChrSetChipByIndex(0x00F8, 11)
    ChrSetChipByIndex(0x00F9, 13)
    TerminateThread(0x0101, 0x03)
    TerminateThread(0x0102, 0x03)
    TerminateThread(0x00F8, 0x03)
    TerminateThread(0x00F9, 0x03)
    ChrSetDirection(0x0101, 0, 0)
    ChrSetDirection(0x0102, 0, 0)
    ChrSetDirection(0x00F8, 0, 0)
    ChrSetDirection(0x00F9, 0, 0)
    ChrSetPos(0x0008, 9580, 5500, 0, 270)

    @scena.Lambda('lambda_C954')
    def lambda_C954():
        CameraMove(12800, 7190, 1790, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_C954)

    @scena.Lambda('lambda_C96C')
    def lambda_C96C():
        OP_67(0, 2980, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_C96C)

    @scena.Lambda('lambda_C984')
    def lambda_C984():
        CameraSetDistance(2520, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_C984)

    @scena.Lambda('lambda_C994')
    def lambda_C994():
        OP_6C(69000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_C994)

    @scena.Lambda('lambda_C9A4')
    def lambda_C9A4():
        OP_6E(466, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_C9A4)

    @scena.Lambda('lambda_C9B4')
    def lambda_C9B4():
        ChrSetDirection(0x00FE, 90, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_C9B4)

    Sleep(100)

    @scena.Lambda('lambda_C9C7')
    def lambda_C9C7():
        ChrSetDirection(0x00FE, 90, 500)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_C9C7)

    Sleep(100)

    @scena.Lambda('lambda_C9DA')
    def lambda_C9DA():
        ChrSetDirection(0x00FE, 90, 500)

        ExitThread()

    DispatchAsync(0x00F8, 0x0000, lambda_C9DA)

    Sleep(100)

    @scena.Lambda('lambda_C9ED')
    def lambda_C9ED():
        ChrSetDirection(0x00FE, 90, 500)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_C9ED)

    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    TalkSetChrName('怀斯曼的声音')
    SetMessageWindowPos(210, 260, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150420742V……干得不错嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150420743V算了……这绝对壁障\n',
            '也只不过是『环』的部分力量而已……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(100)

    LoadEffect(0x00, 'monster\\\\ms31000.eff')
    Sleep(500)

    @scena.Lambda('lambda_CAA6')
    def lambda_CAA6():
        CameraSetDistance(3600, 20000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_CAA6)

    CreateThread(0x0008, 0x01, 0x00, func_0C_CE84)
    Sleep(3500)

    TalkSetChrName('怀斯曼的声音')
    SetMessageWindowPos(200, 260, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150420744V……接下来我要将全部的力量释放，\n',
            '让你们这些蝼蚁好好体会一下……什么才是绝望！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CB7F',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420745V#271F那是我们的台词……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CD7E')

    def _loc_CB7F(): pass

    label('loc_CB7F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CBBE',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420746V#054F#5P那是我们的台词……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CD7E')

    def _loc_CBBE(): pass

    label('loc_CBBE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CBFF',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420747V#024F#5P那是我们的台词啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CD7E')

    def _loc_CBFF(): pass

    label('loc_CBFF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CC3E',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420748V#076F#5P那是我们的台词……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CD7E')

    def _loc_CC3E(): pass

    label('loc_CC3E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CC7B',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420749V#530F#5P那是我们的台词啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CD7E')

    def _loc_CC7B(): pass

    label('loc_CC7B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CCBB',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420750V#1069F#5P那是我们的台词……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CD7E')

    def _loc_CCBB(): pass

    label('loc_CCBB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CD04',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420751V#177F那是我们的台词……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CD7E')

    def _loc_CD04(): pass

    label('loc_CD04')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CD41',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420752V#214F#5P那是我们的台词呀！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CD7E')

    def _loc_CD41(): pass

    label('loc_CD41')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CD7E',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420753V#1166F#5P那是我们的台词……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CD7E(): pass

    label('loc_CD7E')

    ChrTalk(
        0x0101,
        (
            '#0010420754V#1022F#5P身为游击士！\n',
            '身为利贝尔的市民！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420755V#1005F身为一个普通的人类！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020420756V#1046F#5P怀斯曼……\n',
            '我们一定要打倒你！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    WaitForThreadExit(0x0008, 0x0001)
    Blur(1000, 0xBBFFFFFF, 0, 0x01, 12)
    PlaySE(332, 0x00, 0x64)
    Sleep(1000)

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x1E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TerminateThread(0x0008, 0xFF)
    OP_23(0x0149)
    Battle(0x00000451, 0x00300016, 0x00, 0x0080, 0xFF)

    Return()

# id: 0x000B offset: 0xCE5C
@scena.Code('func_0B_CE5C')
def func_0B_CE5C():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_BB(0x01, 0x00, 0x00200042)
    OP_BB(0x01, 0x01, 0x0000001C)
    OP_BD()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5318._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0xCE84
@scena.Code('func_0C_CE84')
def func_0C_CE84():
    Fade(500)
    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 211)
    OP_70(0x0000, 250)
    PlaySE(143, 0x00, 0x64)
    OP_73(0x0000)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 251)
    OP_70(0x0000, 290)
    Play3DEffect(0x00, 0x03, 0x00, 'Frame95__ball', 0x00000000, 0x00000000, 0x00000000, 0x0000, 0x0000, 0x0000, 0x000007D0, 0x000007D0, 0x000007D0, 0x00000000)
    PlaySE(215, 0x00, 0x64)

    Return()

# id: 0x000D offset: 0xCEF1
@scena.Code('func_0D_CEF1')
def func_0D_CEF1():
    OP_CF(0x0009, 0x01, 'Frame140_on_r_arm')
    ChrClearFlags(0x0009, 0x0002)
    ChrSetDirection(0x0009, 180, 0)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x0009, 24)
    ChrJumpTo(0x0009, -8090, 200, 12500, 3000, 3000)
    ChrClearFlags(0x0009, 0x0004)
    ChrSetFlags(0x0009, 0x0002)
    ChrSetSubChip(0x0009, 4)
    ChrSetChipByIndex(0x0009, 2)

    Return()

# id: 0x000E offset: 0xCF4E
@scena.Code('func_0E_CF4E')
def func_0E_CF4E():
    @scena.Lambda('lambda_CF54')
    def lambda_CF54():
        ChrMoveTo(0x00FE, 3800, 3000, 7300, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0002, lambda_CF54)

    OP_72(0x0001, 0x0020)
    OP_D8(0x01, 0x01F4)
    OP_B0(0x0001, 0x19)
    OP_6F(0x0001, 1078)
    OP_70(0x0001, 1080)
    OP_73(0x0001)
    OP_B0(0x0001, 0x14)
    OP_6F(0x0001, 1101)
    OP_70(0x0001, 1150)
    Sleep(100)

    @scena.Lambda('lambda_CFA4')
    def lambda_CFA4():
        ChrJumpTo(0x00FE, -3000, 200, 10000, 500, 15000)

        ExitThread()

    DispatchAsync(0x0020, 0x0002, lambda_CFA4)

    WaitForThreadExit(0x0020, 0x0002)
    PlaySE(246, 0x00, 0x64)

    Return()

# id: 0x000F offset: 0xCFC7
@scena.Code('func_0F_CFC7')
def func_0F_CFC7():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_D00D',
    )

    Sleep(1500)

    PlayEffect(0x04, 0xFF, 0x0008, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('func_0F_CFC7')

    def _loc_D00D(): pass

    label('loc_D00D')

    Return()

# id: 0x0010 offset: 0xD00E
@scena.Code('func_10_D00E')
def func_10_D00E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_D089',
    )

    PlayEffect(0x05, 0xFF, 0x0008, 0, 1500, 3000, 0, 0, 0, 3000, 3000, 3000, 0x0020, 0, 2500, 0, 0)
    PlayEffect(0x05, 0xFF, 0x0008, 0, 1500, 3000, 0, 0, 0, 2000, 2000, 2000, 0x0009, 0, 0, 0, 0)
    Sleep(2000)

    Jump('func_10_D00E')

    def _loc_D089(): pass

    label('loc_D089')

    Return()

# id: 0x0011 offset: 0xD08A
@scena.Code('func_11_D08A')
def func_11_D08A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_D105',
    )

    PlayEffect(0x05, 0xFF, 0x0008, 0, 1500, 3000, 0, 0, 0, 3000, 3000, 3000, 0x0020, 0, 2500, 0, 0)
    PlayEffect(0x05, 0xFF, 0x0008, 0, 1500, 3000, 0, 0, 0, 2000, 2000, 2000, 0x0009, 0, 500, 0, 0)
    Sleep(3500)

    Jump('func_11_D08A')

    def _loc_D105(): pass

    label('loc_D105')

    Return()

# id: 0x0012 offset: 0xD106
@scena.Code('func_12_D106')
def func_12_D106():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_D14C',
    )

    PlayEffect(0x06, 0x07, 0x0009, -200, 1000, 1000, 140, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    Jump('func_12_D106')

    def _loc_D14C(): pass

    label('loc_D14C')

    Return()

# id: 0x0013 offset: 0xD14D
@scena.Code('func_13_D14D')
def func_13_D14D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_D181',
    )

    PlaySE(248, 0x00, 0x64)
    Sleep(1000)

    PlaySE(248, 0x00, 0x64)
    Sleep(1400)

    PlaySE(248, 0x00, 0x64)
    Sleep(1200)

    PlaySE(248, 0x00, 0x64)
    Sleep(1300)

    Jump('func_13_D14D')

    def _loc_D181(): pass

    label('loc_D181')

    Return()

# id: 0x0014 offset: 0xD182
@scena.Code('func_14_D182')
def func_14_D182():
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetFlags(0x00FE, 0x0002)
    ChrSetChipByIndex(0x00FE, 25)
    ChrSetPos(0x00FE, -2400, 6000, 4300, 270)

    @scena.Lambda('lambda_D1A8')
    def lambda_D1A8():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_D1A8')

    DispatchAsync2(0x00FE, 0x0003, lambda_D1A8)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    PlaySE(153, 0x00, 0x64)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)
    Sleep(100)

    ChrSetAfterImage(0x00, 0x00FE, 0x0046, 0x01F4)
    ChrClearFlags(0x00FE, 0x0002)
    ChrSetChipByIndex(0x00FE, 20)
    ChrMoveToRelative(0x00FE, 0, -2300, -2000, 14000, 0x00)
    ChrSetAfterImage(0x01, 0x00FE, 0x0000, 0x0000)
    ChrSetDirection(0x00FE, 270, 100)

    Return()

# id: 0x0015 offset: 0xD210
@scena.Code('func_15_D210')
def func_15_D210():
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetFlags(0x00FE, 0x0002)
    ChrSetChipByIndex(0x00FE, 25)
    ChrSetPos(0x00FE, 2000, 6500, 3200, 270)

    @scena.Lambda('lambda_D236')
    def lambda_D236():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_D236')

    DispatchAsync2(0x00FE, 0x0003, lambda_D236)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    PlaySE(153, 0x00, 0x64)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)
    Sleep(150)

    ChrSetAfterImage(0x00, 0x00FE, 0x0046, 0x01F4)
    ChrClearFlags(0x00FE, 0x0002)
    ChrSetChipByIndex(0x00FE, 20)
    ChrMoveToRelative(0x00FE, -2000, -1800, -2000, 14000, 0x00)
    ChrSetAfterImage(0x01, 0x00FE, 0x0000, 0x0000)
    ChrSetDirection(0x00FE, 270, 100)

    Return()

# id: 0x0016 offset: 0xD29E
@scena.Code('func_16_D29E')
def func_16_D29E():
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetFlags(0x00FE, 0x0002)
    ChrSetChipByIndex(0x00FE, 25)
    ChrSetPos(0x00FE, -2400, 5500, -4300, 270)

    @scena.Lambda('lambda_D2C4')
    def lambda_D2C4():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_D2C4')

    DispatchAsync2(0x00FE, 0x0003, lambda_D2C4)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    PlaySE(153, 0x00, 0x64)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)
    Sleep(200)

    ChrSetAfterImage(0x00, 0x00FE, 0x0046, 0x01F4)
    ChrClearFlags(0x00FE, 0x0002)
    ChrSetChipByIndex(0x00FE, 20)
    ChrMoveToRelative(0x00FE, 0, -1800, 2000, 14000, 0x00)
    ChrSetAfterImage(0x01, 0x00FE, 0x0000, 0x0000)
    ChrSetDirection(0x00FE, 270, 100)

    Return()

# id: 0x0017 offset: 0xD32C
@scena.Code('func_17_D32C')
def func_17_D32C():
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetFlags(0x00FE, 0x0002)
    ChrSetChipByIndex(0x00FE, 25)
    ChrSetPos(0x00FE, 1500, 6000, -2700, 270)

    @scena.Lambda('lambda_D352')
    def lambda_D352():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_D352')

    DispatchAsync2(0x00FE, 0x0003, lambda_D352)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    PlaySE(153, 0x00, 0x64)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)
    Sleep(180)

    ChrSetAfterImage(0x00, 0x00FE, 0x0046, 0x01F4)
    ChrClearFlags(0x00FE, 0x0002)
    ChrSetChipByIndex(0x00FE, 20)
    ChrMoveToRelative(0x00FE, -1500, -1300, 1500, 14000, 0x00)
    ChrSetAfterImage(0x01, 0x00FE, 0x0000, 0x0000)
    ChrSetDirection(0x00FE, 270, 100)

    Return()

# id: 0x0018 offset: 0xD3BA
@scena.Code('func_18_D3BA')
def func_18_D3BA():
    ChrSetAfterImage(0x00, 0x00FE, 0x0055, 0x0FA0)
    OP_97(0x00FE, -11370, 200, -180000, 9000, 0x0002)
    OP_97(0x00FE, -11370, 200, -180000, 10000, 0x0002)
    OP_97(0x00FE, -11370, 200, -180000, 12000, 0x0002)

    def _loc_D401(): pass

    label('loc_D401')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_D428',
    )

    ChrSetAfterImage(0x00, 0x00FE, 0x0055, 0x0CE4)
    OP_97(0x00FE, -11370, 200, -360000, 14000, 0x0002)

    Jump('loc_D401')

    def _loc_D428(): pass

    label('loc_D428')

    ChrSetAfterImage(0x01, 0x00FE, 0x0000, 0x0000)
    OP_97(0x00FE, -11370, 200, -180000, 12000, 0x0002)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0019 offset: 0xD449
@scena.Code('func_19_D449')
def func_19_D449():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 200, 0)
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetFlags(0x00FE, 0x0020)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 10)
    ChrSetPos(0x00FE, -7890, 200, 290, 270)
    ChrSetSubChip(0x00FE, 6)
    PlayEffect(0x01, 0xFF, 0x0101, -200, 400, 200, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_D4BE')
    def lambda_D4BE():
        ChrMoveTo(0x00FE, -11370, 200, 200, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_D4BE)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x001A offset: 0xD4DE
@scena.Code('func_1A_D4DE')
def func_1A_D4DE():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 200, 0)
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetFlags(0x00FE, 0x0020)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 10)
    ChrSetPos(0x00FE, -16270, 200, 50, 90)
    ChrSetSubChip(0x00FE, 6)
    PlayEffect(0x01, 0xFF, 0x0101, 300, 300, -100, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_D553')
    def lambda_D553():
        ChrMoveTo(0x00FE, -11370, 200, 200, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_D553)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x001B offset: 0xD573
@scena.Code('func_1B_D573')
def func_1B_D573():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 200, 0)
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetFlags(0x00FE, 0x0020)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 10)
    ChrSetPos(0x00FE, -9630, 200, -3370, 315)
    ChrSetSubChip(0x00FE, 6)
    PlayEffect(0x01, 0xFF, 0x0101, 100, 0, 200, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_D5E8')
    def lambda_D5E8():
        ChrMoveTo(0x00FE, -11370, 200, 200, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_D5E8)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x001C offset: 0xD608
@scena.Code('func_1C_D608')
def func_1C_D608():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 200, 0)
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetFlags(0x00FE, 0x0020)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 10)
    ChrSetPos(0x00FE, -14920, 200, 3400, 135)
    ChrSetSubChip(0x00FE, 6)
    PlayEffect(0x01, 0xFF, 0x0101, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_D67D')
    def lambda_D67D():
        ChrMoveTo(0x00FE, -11370, 200, 200, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_D67D)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x001D offset: 0xD69D
@scena.Code('func_1D_D69D')
def func_1D_D69D():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 200, 0)
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetFlags(0x00FE, 0x0020)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 10)
    ChrSetPos(0x00FE, -9510, 200, 3440, 225)
    ChrSetSubChip(0x00FE, 6)
    PlayEffect(0x01, 0xFF, 0x0101, 200, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_D712')
    def lambda_D712():
        ChrMoveTo(0x00FE, -11370, 200, 200, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_D712)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x001E offset: 0xD732
@scena.Code('func_1E_D732')
def func_1E_D732():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 200, 0)
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetFlags(0x00FE, 0x0020)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 10)
    ChrSetPos(0x00FE, -14510, 200, -3560, 45)
    ChrSetSubChip(0x00FE, 6)
    PlayEffect(0x01, 0xFF, 0x0101, 0, 0, 300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_D7A7')
    def lambda_D7A7():
        ChrMoveTo(0x00FE, -11370, 200, 200, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_D7A7)

    @scena.Lambda('lambda_D7C2')
    def lambda_D7C2():
        ChrTurnDirection(0x00FE, 0x001D, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_D7C2)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x001F offset: 0xD7D5
@scena.Code('func_1F_D7D5')
def func_1F_D7D5():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_D821',
    )

    ExecExpressionWithValue(
        0x0009,
        0x01,
        (
            (Expr.GetChrWork, 0x1D, 0x1),
            (Expr.GetChrWork, 0x1D, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x02,
        (
            (Expr.GetChrWork, 0x1D, 0x2),
            (Expr.GetChrWork, 0x1D, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x03,
        (
            (Expr.GetChrWork, 0x1D, 0x3),
            (Expr.GetChrWork, 0x1D, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Yield()

    Jump('func_1F_D7D5')

    def _loc_D821(): pass

    label('loc_D821')

    Return()

# id: 0x0020 offset: 0xD822
@scena.Code('func_20_D822')
def func_20_D822():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_D866',
    )

    PlayEffect(0x00, 0x00, 0x0008, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    WaitEffect(0x00, 0x02)

    Jump('func_20_D822')

    def _loc_D866(): pass

    label('loc_D866')

    Return()

# id: 0x0021 offset: 0xD867
@scena.Code('func_21_D867')
def func_21_D867():
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
        (0x00000000, 'loc_D8E1'),
        (0x00000001, 'loc_D8E7'),
        (-1, 'loc_D8ED'),
    )

    def _loc_D8E1(): pass

    label('loc_D8E1')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_D8ED')

    def _loc_D8E7(): pass

    label('loc_D8E7')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_D8ED')

    def _loc_D8ED(): pass

    label('loc_D8ED')

    Return()

# id: 0x0022 offset: 0xD8EE
@scena.Code('func_22_D8EE')
def func_22_D8EE():
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
