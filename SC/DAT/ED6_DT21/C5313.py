import sys
sys.path.append(r'C:\nw_profile\IDE\pycharm\pycharmProj\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5313_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5313   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5313.x'
    header.mapIndex       = 1
    header.bgm            = 64
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/C5313._SN', 'ED6_DT21/C5313_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
            name                = '穆拉少校',
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
            name                = '尤莉亚上尉',
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
            name                = '拉赛尔博士',
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
            name                = '多伦',
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
            name                = '吉尔',
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
            name                = '阿加特',
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
            name                = '雪拉扎德',
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
            name                = '奥利维尔',
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
            name                = '科洛丝',
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
            name                = '提妲',
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
            name                = '金',
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
            name                = '凯文神父',
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
            name                = '乔丝特',
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
            name                = '血狮',
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
            name                = '血狮',
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
        ScenaNpcData(
            name                = '飞刀',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '飞刀',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '飞刀',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '莱维的大剑',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01E7,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '目标用照相机',
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
            npcIndex            = 0x01C5,
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
            npcIndex            = 0x01C5,
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
            name                = '分身',
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
        ScenaNpcData(
            name                = '分身',
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
        ScenaNpcData(
            name                = '分身',
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
        ScenaNpcData(
            name                = '分身',
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
        ScenaNpcData(
            name                = '分身',
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
        ScenaNpcData(
            name                = '分身',
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

# id: 0x10002 offset: 0x4C8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x4C8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x4C8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x4C8
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_4D6',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_05_9D0)

    def _loc_4D6(): pass

    label('loc_4D6')

    Return()

# id: 0x0001 offset: 0x4D7
@scena.Code('func_01_4D7')
def func_01_4D7():
    PlaySE(451, 0x01, 0x64)

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x466),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4F1',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_4F1(): pass

    label('loc_4F1')

    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_6F(0x0000, 0)
    OP_72(0x0001, 0x0020)
    OP_72(0x0001, 0x0008)
    OP_6F(0x0001, 0)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)

    ExecExpressionWithValue(
        0x001E,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x52F
@scena.Code('func_02_52F')
def func_02_52F():
    LoadChip('ED6_DT26/CH20364._CH', 'ED6_DT26/CH20364P._CP', 0)
    LoadChip('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP', 1)
    LoadChip('ED6_DT27/CH04018._CH', 'ED6_DT27/CH04018P._CP', 2)
    LoadChip('ED6_DT26/CH20470._CH', 'ED6_DT26/CH20470P._CP', 3)
    LoadChip('ED6_DT07/CH02470._CH', 'ED6_DT07/CH02470P._CP', 4)
    LoadChip('ED6_DT07/CH02470._CH', 'ED6_DT07/CH02470P._CP', 5)
    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 6)
    LoadChip('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP', 7)
    LoadChip('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP', 8)
    LoadChip('ED6_DT27/CH04011._CH', 'ED6_DT27/CH04011P._CP', 9)
    LoadChip('ED6_DT27/CH04014._CH', 'ED6_DT27/CH04014P._CP', 10)
    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 11)
    LoadChip('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP', 12)
    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 13)
    LoadChip('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP', 14)
    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 15)
    LoadChip('ED6_DT27/CH04211._CH', 'ED6_DT27/CH04211P._CP', 16)
    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 17)
    LoadChip('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP', 18)
    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 19)
    LoadChip('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP', 20)
    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 21)
    LoadChip('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP', 22)
    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 23)
    LoadChip('ED6_DT27/CH04081._CH', 'ED6_DT27/CH04081P._CP', 24)
    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 25)
    LoadChip('ED6_DT07/CH00311._CH', 'ED6_DT07/CH00311P._CP', 26)
    LoadChip('ED6_DT07/CH02040._CH', 'ED6_DT07/CH02040P._CP', 27)
    LoadChip('ED6_DT27/CH04540._CH', 'ED6_DT27/CH04540P._CP', 28)
    LoadChip('ED6_DT27/CH04541._CH', 'ED6_DT27/CH04541P._CP', 29)
    LoadChip('ED6_DT27/CH04545._CH', 'ED6_DT27/CH04545P._CP', 30)
    LoadChip('ED6_DT27/CH04548._CH', 'ED6_DT27/CH04548P._CP', 31)
    LoadChip('ED6_DT29/CH12510._CH', 'ED6_DT29/CH12510P._CP', 32)
    LoadChip('ED6_DT29/CH12511._CH', 'ED6_DT29/CH12511P._CP', 33)
    LoadChip('ED6_DT27/CH04570._CH', 'ED6_DT27/CH04570P._CP', 34)
    LoadChip('ED6_DT27/CH04571._CH', 'ED6_DT27/CH04571P._CP', 35)
    LoadChip('ED6_DT27/CH04580._CH', 'ED6_DT27/CH04580P._CP', 36)
    LoadChip('ED6_DT27/CH04581._CH', 'ED6_DT27/CH04581P._CP', 37)
    OP_C0(0x17, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)

    Return()

# id: 0x0003 offset: 0x6CE
@scena.Code('func_03_6CE')
def func_03_6CE():
    LoadChip('ED6_DT26/CH20364._CH', 'ED6_DT26/CH20364P._CP', 0)
    LoadChip('ED6_DT27/CH03010._CH', 'ED6_DT27/CH03010P._CP', 1)
    LoadChip('ED6_DT26/CH20475._CH', 'ED6_DT26/CH20475P._CP', 2)
    LoadChip('ED6_DT26/CH20363._CH', 'ED6_DT26/CH20363P._CP', 3)
    LoadChip('ED6_DT27/CH04550._CH', 'ED6_DT27/CH04550P._CP', 4)
    LoadChip('ED6_DT27/CH04558._CH', 'ED6_DT27/CH04558P._CP', 5)
    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 6)
    LoadChip('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP', 7)
    LoadChip('ED6_DT27/CH0401A._CH', 'ED6_DT27/CH0401AP._CP', 8)
    LoadChip('ED6_DT26/CH20476._CH', 'ED6_DT26/CH20476P._CP', 9)
    LoadChip('ED6_DT27/CH04014._CH', 'ED6_DT27/CH04014P._CP', 10)
    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 11)
    LoadChip('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP', 12)
    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 13)
    LoadChip('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP', 14)
    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 15)
    LoadChip('ED6_DT27/CH04211._CH', 'ED6_DT27/CH04211P._CP', 16)
    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 17)
    LoadChip('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP', 18)
    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 19)
    LoadChip('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP', 20)
    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 21)
    LoadChip('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP', 22)
    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 23)
    LoadChip('ED6_DT27/CH04081._CH', 'ED6_DT27/CH04081P._CP', 24)
    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 25)
    LoadChip('ED6_DT07/CH00311._CH', 'ED6_DT07/CH00311P._CP', 26)
    LoadChip('ED6_DT07/CH02040._CH', 'ED6_DT07/CH02040P._CP', 27)
    LoadChip('ED6_DT27/CH04540._CH', 'ED6_DT27/CH04540P._CP', 28)
    LoadChip('ED6_DT26/CH20472._CH', 'ED6_DT26/CH20472P._CP', 29)
    LoadChip('ED6_DT26/CH20497._CH', 'ED6_DT26/CH20497P._CP', 30)
    LoadChip('ED6_DT27/CH03011._CH', 'ED6_DT27/CH03011P._CP', 31)
    LoadChip('ED6_DT26/CH20473._CH', 'ED6_DT26/CH20473P._CP', 32)
    LoadChip('ED6_DT26/CH20474._CH', 'ED6_DT26/CH20474P._CP', 33)
    LoadChip('ED6_DT27/CH04570._CH', 'ED6_DT27/CH04570P._CP', 34)
    LoadChip('ED6_DT27/CH04580._CH', 'ED6_DT27/CH04580P._CP', 36)
    OP_C0(0x17, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)

    Return()

# id: 0x0004 offset: 0x859
@scena.Code('func_04_859')
def func_04_859():
    LoadChip('ED6_DT26/CH20364._CH', 'ED6_DT26/CH20364P._CP', 0)
    LoadChip('ED6_DT27/CH03010._CH', 'ED6_DT27/CH03010P._CP', 1)
    LoadChip('ED6_DT27/CH04546._CH', 'ED6_DT27/CH04546P._CP', 2)
    LoadChip('ED6_DT27/CH04018._CH', 'ED6_DT27/CH04018P._CP', 3)
    LoadChip('ED6_DT27/CH04014._CH', 'ED6_DT27/CH04014P._CP', 4)
    LoadChip('ED6_DT26/CH20243._CH', 'ED6_DT26/CH20243P._CP', 5)
    LoadChip('ED6_DT27/CH04019._CH', 'ED6_DT27/CH04019P._CP', 6)
    LoadChip('ED6_DT27/CH04541._CH', 'ED6_DT27/CH04541P._CP', 7)
    LoadChip('ED6_DT27/CH0401A._CH', 'ED6_DT27/CH0401AP._CP', 8)
    LoadChip('ED6_DT27/CH04012._CH', 'ED6_DT27/CH04012P._CP', 9)
    LoadChip('ED6_DT27/CH04011._CH', 'ED6_DT27/CH04011P._CP', 10)
    LoadChip('ED6_DT27/CH04013._CH', 'ED6_DT27/CH04013P._CP', 11)
    LoadChip('ED6_DT26/CH20496._CH', 'ED6_DT26/CH20496P._CP', 12)
    LoadChip('ED6_DT27/CH04545._CH', 'ED6_DT27/CH04545P._CP', 13)
    LoadChip('ED6_DT27/CH04016._CH', 'ED6_DT27/CH04016P._CP', 14)
    LoadChip('ED6_DT26/CH20470._CH', 'ED6_DT26/CH20470P._CP', 15)
    LoadChip('ED6_DT26/CH20471._CH', 'ED6_DT26/CH20471P._CP', 16)
    LoadChip('ED6_DT26/CH20472._CH', 'ED6_DT26/CH20472P._CP', 17)
    LoadChip('ED6_DT26/CH20363._CH', 'ED6_DT26/CH20363P._CP', 18)
    LoadChip('ED6_DT27/CH04549._CH', 'ED6_DT27/CH04549P._CP', 19)
    LoadChip('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP', 20)
    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 21)
    LoadChip('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP', 22)
    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 23)
    LoadChip('ED6_DT27/CH04081._CH', 'ED6_DT27/CH04081P._CP', 24)
    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 25)
    LoadChip('ED6_DT07/CH00311._CH', 'ED6_DT07/CH00311P._CP', 26)
    LoadChip('ED6_DT07/CH02040._CH', 'ED6_DT07/CH02040P._CP', 27)
    LoadChip('ED6_DT27/CH04540._CH', 'ED6_DT27/CH04540P._CP', 28)
    LoadChip('ED6_DT27/CH04542._CH', 'ED6_DT27/CH04542P._CP', 29)
    LoadChip('ED6_DT27/CH04547._CH', 'ED6_DT27/CH04547P._CP', 30)
    LoadChip('ED6_DT27/CH04548._CH', 'ED6_DT27/CH04548P._CP', 31)
    LoadChip('ED6_DT26/CH20473._CH', 'ED6_DT26/CH20473P._CP', 32)
    LoadChip('ED6_DT26/CH20474._CH', 'ED6_DT26/CH20474P._CP', 33)
    OP_C0(0x17, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)

    Return()

# id: 0x0005 offset: 0x9D0
@scena.Code('func_05_9D0')
def func_05_9D0():
    Call(0, 0x0006)
    Call(0, 0x001D)

    Return()

# id: 0x0006 offset: 0x9D9
@scena.Code('func_06_9D9')
def func_06_9D9():
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
        'loc_9F0',
    )

    Call(0, 0x001E)
    Call(0, 0x001F)

    def _loc_9F0(): pass

    label('loc_9F0')

    Call(0, 0x0002)
    CameraMove(0, 4010, 33840, 0)
    OP_67(0, 13290, -10000, 0)
    CameraSetDistance(7080, 0)
    OP_6C(45000, 0)
    OP_6E(462, 0)
    OP_6F(0x0000, 150)
    OP_89(0x0101, 0, 3510, -41450, 0)
    OP_89(0x0102, 1000, 3510, -42450, 0)
    OP_89(0x00F8, -1000, 3510, -42450, 0)
    OP_89(0x00F9, 0, 3510, -43450, 0)
    Yield()
    LoadEffect(0x00, 'craft\\\\cr162_02.eff')
    FadeIn(1000, 0)

    @scena.Lambda('lambda_0AA2')
    def lambda_0AA2():
        CameraMove(0, 3510, -42450, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0AA2)

    Sleep(8000)

    OP_B0(0x0000, 0x14)
    OP_6F(0x0000, 150)
    OP_70(0x0000, 0)
    WaitForThreadExit(0x0101, 0x0001)
    Fade(500)
    CameraMove(0, 3510, -42450, 0)
    OP_67(0, 9000, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_0B18')
    def lambda_0B18():
        CameraMove(50, 3510, -42180, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0B18)

    @scena.Lambda('lambda_0B30')
    def lambda_0B30():
        CameraSetDistance(3000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B30)

    PlaySE(235, 0x00, 0x64)
    Sleep(3500)

    OP_24(0x00EB, 0x5A)
    Sleep(50)

    OP_24(0x00EB, 0x50)
    Sleep(50)

    OP_24(0x00EB, 0x46)
    Sleep(50)

    OP_24(0x00EB, 0x3C)
    Sleep(50)

    OP_24(0x00EB, 0x32)
    Sleep(50)

    OP_24(0x00EB, 0x28)
    Sleep(50)

    OP_24(0x00EB, 0x1E)
    Sleep(50)

    OP_24(0x00EB, 0x14)
    Sleep(50)

    OP_24(0x00EB, 0x0A)
    Sleep(50)

    OP_23(0x00EB)
    OP_73(0x0000)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    ChrSetChipByIndex(0x0008, 28)
    ChrSetPos(0x0008, 0, -370, 3000, 180)
    ChrClearFlags(0x0008, 0x0080)

    NpcTalk(
        0x0008,
        '青年的声音',
        (
            '#0140410773V……来了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C4D',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_C8B')

    def _loc_C4D(): pass

    label('loc_C4D')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C74',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_C8B')

    def _loc_C74(): pass

    label('loc_C74')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_C8B(): pass

    label('loc_C8B')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CB7',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_CF5')

    def _loc_CB7(): pass

    label('loc_CB7')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CDE',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_CF5')

    def _loc_CDE(): pass

    label('loc_CDE')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_CF5(): pass

    label('loc_CF5')

    Sleep(1000)

    @scena.Lambda('lambda_0D00')
    def lambda_0D00():
        CameraMove(580, -370, 3680, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0D00)

    @scena.Lambda('lambda_0D18')
    def lambda_0D18():
        OP_67(0, 5820, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0D18)

    @scena.Lambda('lambda_0D30')
    def lambda_0D30():
        CameraSetDistance(3400, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0D30)

    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0102,
        (
            '#0020410774V#1042F莱维……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    PlayBGM(111)
    Sleep(500)

    ChrSetPos(0x0101, 400, 0, -18760, 0)
    ChrSetPos(0x0102, -400, 0, -18760, 0)
    ChrSetPos(0x00F8, 1600, 0, -20200, 0)
    ChrSetPos(0x00F9, -1600, 0, -20200, 0)

    @scena.Lambda('lambda_0DB1')
    def lambda_0DB1():
        CameraMove(1340, -370, -500, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0DB1)

    @scena.Lambda('lambda_0DC9')
    def lambda_0DC9():
        OP_67(0, 4730, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0DC9)

    @scena.Lambda('lambda_0DE1')
    def lambda_0DE1():
        CameraSetDistance(3500, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0DE1)

    @scena.Lambda('lambda_0DF1')
    def lambda_0DF1():
        OP_6E(349, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_0DF1)

    @scena.Lambda('lambda_0E01')
    def lambda_0E01():
        ChrWalkTo(0x00FE, -1000, 0, -7200, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0E01)

    Sleep(100)

    @scena.Lambda('lambda_0E21')
    def lambda_0E21():
        ChrWalkTo(0x00FE, 300, 0, -7100, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0E21)

    Sleep(100)

    @scena.Lambda('lambda_0E41')
    def lambda_0E41():
        ChrWalkTo(0x00FE, -1200, 0, -8800, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0E41)

    Sleep(100)

    @scena.Lambda('lambda_0E61')
    def lambda_0E61():
        ChrWalkTo(0x00FE, 400, 0, -8600, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0E61)

    WaitForThreadExit(0x0101, 0x0002)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140410775V#123F……想不到这么快啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410776V本以为\n',
            '还要再等一会儿的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410777V#1006F#6P因为我们也\n',
            '有所成长了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410778V不过你的那些同伴们倒也\n',
            '让我们感到很棘手呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140410779V#123F呵呵……真是伶牙俐齿啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410780V#124F但是，你们可不要把我『剑帝』\n',
            '同他们相提并论。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410781V在正面对决中，\n',
            '没有任何人可以凌驾于我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410782V#121F就算是Ｓ级游击士\n',
            '或『蛇之使徒』也不例外。',
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
        'loc_1061',
    )

    ChrTalk(
        0x0106,
        (
            '#0050410783V#057F#4P哼……\n',
            '还真是大言不惭啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1260')

    def _loc_1061(): pass

    label('loc_1061')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_109D',
    )

    ChrTalk(
        0x010F,
        (
            '#0100410784V#178F呃…………!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1260')

    def _loc_109D(): pass

    label('loc_109D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10DA',
    )

    ChrTalk(
        0x0103,
        (
            '#0030410785V#022F#4P……真会说大话啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1260')

    def _loc_10DA(): pass

    label('loc_10DA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1115',
    )

    ChrTalk(
        0x0108,
        (
            '#0080410786V#072F#4P……真是狂妄啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1260')

    def _loc_1115(): pass

    label('loc_1115')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_115F',
    )

    ChrTalk(
        0x010B,
        (
            '#0090410787V#212F#4P哼哼……\n',
            '嘴上功夫倒是很厉害嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1260')

    def _loc_115F(): pass

    label('loc_115F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11A9',
    )

    ChrTalk(
        0x0104,
        (
            '#0040410788V#034F#4P哎呀哎呀……\n',
            '真是好大的自信啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1260')

    def _loc_11A9(): pass

    label('loc_11A9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11ED',
    )

    ChrTalk(
        0x0109,
        (
            '#0180410789V#1063F#4P哟，你真是充满自信啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1260')

    def _loc_11ED(): pass

    label('loc_11ED')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_122E',
    )

    ChrTalk(
        0x0110,
        (
            '#0110410790V#278F……很有自信啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1260')

    def _loc_122E(): pass

    label('loc_122E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1260',
    )

    ChrTalk(
        0x0107,
        (
            '#0070410791V#065F#4P啊、啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1260(): pass

    label('loc_1260')

    ChrTalk(
        0x0101,
        (
            '#0010410792V#1003F#6P……你的实力之强，\n',
            '我们早就明白。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410793V#1010F但是，我们来到这里\n',
            '也是有自己的理由的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410794V为了阻止『辉之环』的异变\n',
            '以及防止混乱和战火……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410795V我们在很多人的帮助下\n',
            '置身于此地。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410796V#1002F所以……我们不会退缩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140410797V#124F呵……\n',
            '这个理由倒是不坏。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410798V#123F不过，约修亚。\n',
            '你的理由好象不一样吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270406V#1004F#6P哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410800V#1035F#4P好像……被你看穿了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_142D')
    def lambda_142D():
        CameraMove(1500, -370, 60, 1800)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_142D)

    @scena.Lambda('lambda_1445')
    def lambda_1445():
        CameraSetDistance(3200, 1800)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1445)

    @scena.Lambda('lambda_1455')
    def lambda_1455():
        OP_67(0, 4360, -10000, 1800)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1455)

    ChrMoveTo(0x0102, 330, -370, -4300, 1500, 0x00)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020410801V#1042F#4P我是……为了直面自己的\n',
            '软弱而来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410802V#1043F那时，我为了逃避姐姐死亡\n',
            '的现实而毁坏自己的心……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410803V以及对教授惟命是从……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410804V全部都是……\n',
            '因为我自身的软弱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410805V#1035F为了回报让我\n',
            '认清这一点的人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410806V以及为了守护重要的东西……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410807V#1042F我……\n',
            '必须要正面挑战\n',
            '莱维和教授。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410808V#1025F#6P约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140410809V#120F……………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410810V#124F……你已经长大了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410811V看来我已经不用再替卡琳\n',
            '来担心你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)

    @scena.Lambda('lambda_16A8')
    def lambda_16A8():
        CameraSetDistance(3000, 500)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_16A8)

    PlaySE(213, 0x00, 0x64)
    ChrSetPos(0x0008, 0, -370, 2900, 180)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 0)
    OP_0D()
    WaitForThreadExit(0x0102, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140410812V#123F……这样一来\n',
            '终于不必再手下留情了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410813V接下来我要使出全力了。',
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
        'loc_177E',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_17BC')

    def _loc_177E(): pass

    label('loc_177E')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17A5',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_17BC')

    def _loc_17A5(): pass

    label('loc_17A5')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_17BC(): pass

    label('loc_17BC')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17E8',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_1826')

    def _loc_17E8(): pass

    label('loc_17E8')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_180F',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_1826')

    def _loc_180F(): pass

    label('loc_180F')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_1826(): pass

    label('loc_1826')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010410814V#1020F#6P等、等等！\n',
            '怎么会变成这样！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410815V你之前那么担心约修亚，\n',
            '为什么要──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410816V#1035F#5P没关系的，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x0102, 8)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020410817V#1042F#5P光有决心的话，\n',
            '莱维是不会认可的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410818V我必须要拥有能够贯彻\n',
            '自己决心的实力才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140410819V#123F呵呵，就是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x00, 'battle\\\\mgaria0.eff')
    Sleep(100)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 30)
    MapClearFlags(0x00000010)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_19BF')
    def lambda_19BF():
        CameraMove(1810, 0, 7830, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_19BF)

    @scena.Lambda('lambda_19D7')
    def lambda_19D7():
        OP_67(0, 3400, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_19D7)

    @scena.Lambda('lambda_19EF')
    def lambda_19EF():
        CameraSetDistance(2180, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_19EF)

    @scena.Lambda('lambda_19FF')
    def lambda_19FF():
        OP_6C(43000, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_19FF)

    @scena.Lambda('lambda_1A0F')
    def lambda_1A0F():
        OP_6E(389, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1A0F)

    OP_0D()
    PlayEffect(0x00, 0x00, 0x0008, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    ChrSetFlags(0x0017, 0x0800)
    ChrSetFlags(0x0018, 0x0800)
    CreateThread(0x0017, 0x00, 0x00, func_07_248B)
    Sleep(500)

    CreateThread(0x0018, 0x00, 0x00, func_08_2502)
    WaitForThreadExit(0x0017, 0x0000)
    WaitForThreadExit(0x0018, 0x0000)
    StopEffect(0x00, 0x02)
    Sleep(1000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetPos(0x00F8, -900, 0, -8610, 340)
    ChrSetPos(0x00F9, 630, 0, -7630, 340)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x00F8, 0)
    ChrSetSubChip(0x00F9, 0)
    ChrSetChipByIndex(0x0101, 6)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1AD5',
    )

    ChrSetChipByIndex(0x0103, 11)

    def _loc_1AD5(): pass

    label('loc_1AD5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1AE8',
    )

    ChrSetChipByIndex(0x0104, 13)

    def _loc_1AE8(): pass

    label('loc_1AE8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1AFB',
    )

    ChrSetChipByIndex(0x0105, 15)

    def _loc_1AFB(): pass

    label('loc_1AFB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B0E',
    )

    ChrSetChipByIndex(0x0106, 17)

    def _loc_1B0E(): pass

    label('loc_1B0E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B21',
    )

    ChrSetChipByIndex(0x0107, 19)

    def _loc_1B21(): pass

    label('loc_1B21')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B34',
    )

    ChrSetChipByIndex(0x0108, 21)

    def _loc_1B34(): pass

    label('loc_1B34')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B47',
    )

    ChrSetChipByIndex(0x0109, 23)

    def _loc_1B47(): pass

    label('loc_1B47')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B5A',
    )

    ChrSetChipByIndex(0x010B, 25)

    def _loc_1B5A(): pass

    label('loc_1B5A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B6D',
    )

    ChrSetChipByIndex(0x010F, 36)

    def _loc_1B6D(): pass

    label('loc_1B6D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B80',
    )

    ChrSetChipByIndex(0x0110, 34)

    def _loc_1B80(): pass

    label('loc_1B80')

    OP_20(0x00000BB8)

    @scena.Lambda('lambda_1B8B')
    def lambda_1B8B():
        CameraMove(1010, -370, 50, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1B8B)

    @scena.Lambda('lambda_1BA3')
    def lambda_1BA3():
        OP_6C(35000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1BA3)

    @scena.Lambda('lambda_1BB3')
    def lambda_1BB3():
        OP_67(0, 4730, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1BB3)

    @scena.Lambda('lambda_1BCB')
    def lambda_1BCB():
        CameraSetDistance(2940, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1BCB)

    @scena.Lambda('lambda_1BDB')
    def lambda_1BDB():
        OP_6E(389, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_1BDB)

    WaitForThreadExit(0x0101, 0x0000)
    Fade(250)
    MapSetFlags(0x00000010)
    PlaySE(213, 0x00, 0x64)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 28)
    OP_0D()
    Sleep(500)

    PlayBGM(43)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140410820V#124F#5P──我也有我的觉悟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410821V如果，你们的觉悟\n',
            '超越了我的修罗之道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410822V#126F就用自己的实力来证明吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410823V#1042F#4P嗯……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410824V#1005F#6P……求之不得啊！',
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
        'loc_1D4C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050410825V#051F#4P嘿，长久以来的新仇旧恨，\n',
            '今天就连本带利地奉还给你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_203B')

    def _loc_1D4C(): pass

    label('loc_1D4C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1D9A',
    )

    ChrTalk(
        0x0103,
        (
            '#0030410826V#024F#4P女王宫的那笔帐…\n',
            '就这里还给你吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_203B')

    def _loc_1D9A(): pass

    label('loc_1D9A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1DF1',
    )

    ChrTalk(
        0x0110,
        (
            '#0110410827V#277F『剑帝』的实力，\n',
            '让我来确认一下吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_203B')

    def _loc_1DF1(): pass

    label('loc_1DF1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E4B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080410828V#072F#4P你在比武大会时放水的事，\n',
            '就在现在作个了断吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_203B')

    def _loc_1E4B(): pass

    label('loc_1E4B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1EAF',
    )

    ChrTalk(
        0x0104,
        (
            '#0040410829V#035F#4P呵呵，虽然和你并无仇恨，\n',
            '不过这也是为了我亲爱的约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_203B')

    def _loc_1EAF(): pass

    label('loc_1EAF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F0A',
    )

    ChrTalk(
        0x0109,
        (
            '#0180410830V#1060F#4P嗯，在湖畔劫走艾丝蒂尔\n',
            '的事情还没和你清算呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_203B')

    def _loc_1F0A(): pass

    label('loc_1F0A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F60',
    )

    ChrTalk(
        0x010B,
        (
            '#0090410831V#212F#4P利用陷害我们的事情…\n',
            '现在就来清算一下吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_203B')

    def _loc_1F60(): pass

    label('loc_1F60')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1FE3',
    )

    ChrTalk(
        0x010F,
        (
            '#0100410832V#176F『罗伦斯少尉』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100410833V#178F我本来有\n',
            '很多问题想问你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_203B')

    def _loc_1FE3(): pass

    label('loc_1FE3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_203B',
    )

    ChrTalk(
        0x0105,
        (
            '#0060410834V#1167F#4P虽然我对你并无怨恨，\n',
            '但为了大家和王国的未来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_203B(): pass

    label('loc_203B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2087',
    )

    ChrTalk(
        0x0107,
        (
            '#0070410835V#062F#4P我会努力加油，\n',
            '不给大家拖后腿的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2329')

    def _loc_2087(): pass

    label('loc_2087')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_20CE',
    )

    ChrTalk(
        0x0105,
        (
            '#0060410836V#1166F#4P让我竭尽全力地\n',
            '向您挑战吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2329')

    def _loc_20CE(): pass

    label('loc_20CE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_213B',
    )

    ChrTalk(
        0x010F,
        (
            '#0100410837V#177F但现在，王室亲卫队\n',
            '大队长尤莉亚·舒华兹，\n',
            '在此向你发起挑战！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2329')

    def _loc_213B(): pass

    label('loc_213B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_218F',
    )

    ChrTalk(
        0x010B,
        (
            '#0090410838V#214F#4P我要让你见识一下卡普亚家族的\n',
            '自豪和坚韧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2329')

    def _loc_218F(): pass

    label('loc_218F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_21E2',
    )

    ChrTalk(
        0x0109,
        (
            '#0180410839V#1069F#4P作为『星杯骑士』的一员，\n',
            '我会尽我所能！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2329')

    def _loc_21E2(): pass

    label('loc_21E2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2232',
    )

    ChrTalk(
        0x0104,
        (
            '#0040410840V#530F#4P为了回应约修亚的爱，\n',
            '我也要全力以赴！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2329')

    def _loc_2232(): pass

    label('loc_2232')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2280',
    )

    ChrTalk(
        0x0108,
        (
            '#0080410841V#076F#4P让我赌上『不动』之名\n',
            '全力向你挑战！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2329')

    def _loc_2280(): pass

    label('loc_2280')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_22DC',
    )

    ChrTalk(
        0x0110,
        (
            '#0110410842V#271F让我尽情\n',
            '挥舞范德尔之剑吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2329')

    def _loc_22DC(): pass

    label('loc_22DC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2329',
    )

    ChrTalk(
        0x0103,
        (
            '#0030410843V#024F#4P赌上我的『银闪』之名，\n',
            '来决一胜负吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2329(): pass

    label('loc_2329')

    @scena.Lambda('lambda_232F')
    def lambda_232F():
        CameraMove(-60, -370, -160, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_232F)

    @scena.Lambda('lambda_2347')
    def lambda_2347():
        OP_67(0, 5850, -10000, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2347)

    @scena.Lambda('lambda_235F')
    def lambda_235F():
        CameraSetDistance(2000, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_235F)

    @scena.Lambda('lambda_236F')
    def lambda_236F():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 5000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_236F)

    Sleep(20)

    ChrSetChipByIndex(0x0017, 33)

    @scena.Lambda('lambda_2394')
    def lambda_2394():
        ChrMoveToRelativeAsync(0x00FE, -500, 0, -5000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0000, lambda_2394)

    @scena.Lambda('lambda_23AF')
    def lambda_23AF():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 5000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0000, lambda_23AF)

    Sleep(20)

    ChrSetChipByIndex(0x0018, 33)

    @scena.Lambda('lambda_23D4')
    def lambda_23D4():
        ChrMoveToRelativeAsync(0x00FE, 500, 0, -5000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0000, lambda_23D4)

    @scena.Lambda('lambda_23EF')
    def lambda_23EF():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 5000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_23EF)

    Sleep(20)

    ChrSetChipByIndex(0x0008, 29)

    @scena.Lambda('lambda_2414')
    def lambda_2414():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -5000, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_2414)

    @scena.Lambda('lambda_242F')
    def lambda_242F():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 5000, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_242F)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x00F8, 0xFF)
    TerminateThread(0x00F9, 0xFF)
    TerminateThread(0x0017, 0xFF)
    TerminateThread(0x0018, 0xFF)

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0x190),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00000466, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetStatus(0x00FF, 0xF9, 0)

    Return()

# id: 0x0007 offset: 0x248B
@scena.Code('func_07_248B')
def func_07_248B():
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetChipByIndex(0x00FE, 32)
    ChrSetPos(0x00FE, 2460, 10000, 12620, 180)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_24B1')
    def lambda_24B1():
        ChrJumpTo(0x00FE, 2460, 300, 6620, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_24B1)

    WaitForThreadExit(0x00FE, 0x0001)
    PlaySE(200, 0x00, 0x64)
    OP_7C(0, 500, 3000, 100)

    @scena.Lambda('lambda_24EA')
    def lambda_24EA():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_24EA')

    DispatchAsync2(0x00FE, 0x0001, lambda_24EA)

    Sleep(500)

    PlaySE(403, 0x00, 0x64)

    Return()

# id: 0x0008 offset: 0x2502
@scena.Code('func_08_2502')
def func_08_2502():
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetChipByIndex(0x00FE, 32)
    ChrSetPos(0x00FE, -2460, 10000, 12120, 180)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_2528')
    def lambda_2528():
        ChrJumpTo(0x00FE, -2460, 300, 6120, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_2528)

    WaitForThreadExit(0x00FE, 0x0001)
    PlaySE(200, 0x00, 0x64)
    OP_7C(0, 500, 3000, 100)

    @scena.Lambda('lambda_2561')
    def lambda_2561():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_2561')

    DispatchAsync2(0x00FE, 0x0001, lambda_2561)

    Sleep(500)

    PlaySE(403, 0x00, 0x64)

    Return()

# id: 0x0009 offset: 0x2579
@scena.Code('func_09_2579')
def func_09_2579():
    WaitForThreadExit(0x00FE, 0x0001)
    PlaySE(164, 0x00, 0x64)

    Return()

# id: 0x000A offset: 0x2584
@scena.Code('func_0A_2584')
def func_0A_2584():
    ChrClearFlags(0x0022, 0x0002)
    ChrSetChipByIndex(0x0022, 10)
    ChrSetSubChip(0x0022, 0)

    @scena.Lambda('lambda_2599')
    def lambda_2599():
        ChrSetDirection(0x00FE, 262, 200)

        ExitThread()

    DispatchAsync(0x0022, 0x0003, lambda_2599)

    @scena.Lambda('lambda_25A7')
    def lambda_25A7():
        ChrJumpTo(0x00FE, 11130, 0, -2460, 1000, 4000)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_25A7)

    WaitForThreadExit(0x0022, 0x0001)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_25CF')
    def lambda_25CF():
        ChrJumpTo(0x00FE, 14650, 0, -2460, 800, 4000)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_25CF)

    WaitForThreadExit(0x0022, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetChipByIndex(0x0022, 4)
    ChrSetSubChip(0x0022, 0)

    Return()

# id: 0x000B offset: 0x25FC
@scena.Code('func_0B_25FC')
def func_0B_25FC():
    @scena.Lambda('lambda_2602')
    def lambda_2602():
        OP_99(0x00FE, 0x18, 0x1F, 8000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_2602)

    @scena.Lambda('lambda_2612')
    def lambda_2612():
        ChrJumpTo(0x00FE, 4590, -370, -3570, 500, 2000)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_2612)

    WaitForThreadExit(0x0022, 0x0002)

    @scena.Lambda('lambda_2635')
    def lambda_2635():
        OP_99(0x00FE, 0x18, 0x1F, 8000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_2635)

    WaitForThreadExit(0x0022, 0x0002)

    @scena.Lambda('lambda_264A')
    def lambda_264A():
        OP_99(0x00FE, 0x18, 0x1F, 8000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_264A)

    WaitForThreadExit(0x0022, 0x0002)

    @scena.Lambda('lambda_265F')
    def lambda_265F():
        OP_99(0x00FE, 0x18, 0x19, 8000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_265F)

    WaitForThreadExit(0x0022, 0x0001)
    WaitForThreadExit(0x0022, 0x0002)
    ChrSetPos(0x0022, 4590, 900, -3570, 310)
    ChrSetSubChip(0x0022, 34)
    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x0008, 0, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 400, 3000, 200)

    Return()

# id: 0x000C offset: 0x26D5
@scena.Code('func_0C_26D5')
def func_0C_26D5():
    WaitForThreadExit(0x0008, 0x0001)
    TerminateThread(0x0008, 0x02)
    ChrSetChipByIndex(0x0008, 28)
    ChrSetSubChip(0x0008, 0)
    Sleep(1000)

    ChrSetChipByIndex(0x0008, 30)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_26FD')
    def lambda_26FD():
        OP_99(0x00FE, 0x00, 0x07, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_26FD)

    Sleep(400)

    PlaySE(213, 0x00, 0x64)

    Return()

# id: 0x000D offset: 0x2712
@scena.Code('func_0D_2712')
def func_0D_2712():
    PlayEffect(0x02, 0x01, 0x0008, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_274D')
    def lambda_274D():
        OP_99(0x00FE, 0x07, 0x0F, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_274D)

    WaitForThreadExit(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 31)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_276C')
    def lambda_276C():
        OP_99(0x00FE, 0x00, 0x05, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_276C)

    WaitForThreadExit(0x0008, 0x0002)

    Return()

# id: 0x000E offset: 0x277C
@scena.Code('func_0E_277C')
def func_0E_277C():
    @scena.Lambda('lambda_2782')
    def lambda_2782():
        CameraMove(3890, -370, 2110, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2782)

    @scena.Lambda('lambda_279A')
    def lambda_279A():
        OP_6C(135000, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_279A)

    @scena.Lambda('lambda_27AA')
    def lambda_27AA():
        CameraSetDistance(1230, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_27AA)

    ChrSetChipByIndex(0x001B, 12)
    ChrSetSubChip(0x001B, 2)
    ChrClearFlags(0x001B, 0x0002)
    ChrClearFlags(0x001B, 0x0080)
    ChrSetPos(0x001B, -9680, 0, 2560, 90)

    @scena.Lambda('lambda_27DF')
    def lambda_27DF():
        ChrMoveTo(0x00FE, 17980, 0, 2860, 40000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_27DF)

    Sleep(450)

    ChrSetChipByIndex(0x001C, 12)
    ChrSetSubChip(0x001C, 2)
    ChrClearFlags(0x001C, 0x0002)
    ChrClearFlags(0x001C, 0x0080)
    ChrSetPos(0x001C, -9680, 0, 2560, 90)

    @scena.Lambda('lambda_2824')
    def lambda_2824():
        ChrMoveTo(0x00FE, 16660, 0, 4420, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_2824)

    Sleep(450)

    ChrSetPos(0x001B, -9680, 0, 2560, 90)

    @scena.Lambda('lambda_2855')
    def lambda_2855():
        ChrMoveTo(0x00FE, 17910, 0, 1490, 50000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_2855)

    Sleep(450)

    ChrSetPos(0x001C, -9680, 0, 2560, 90)

    @scena.Lambda('lambda_2886')
    def lambda_2886():
        ChrMoveTo(0x00FE, 14320, 0, 5460, 40000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_2886)

    Return()

# id: 0x000F offset: 0x289C
@scena.Code('func_0F_289C')
def func_0F_289C():
    Sleep(600)

    ChrSetAfterImage(0x00, 0x0008, 0x0014, 0x01F4)

    @scena.Lambda('lambda_28AF')
    def lambda_28AF():
        ChrMoveTo(0x00FE, 3180, -370, 3400, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_28AF)

    PlaySE(132, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0001)
    Sleep(200)

    @scena.Lambda('lambda_28D9')
    def lambda_28D9():
        CameraMove(2009, 0, 1650, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_28D9)

    @scena.Lambda('lambda_28F1')
    def lambda_28F1():
        CameraSetDistance(1390, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_28F1)

    ChrSetChipByIndex(0x0008, 2)
    ChrSetSubChip(0x0008, 0)
    ChrSetAfterImage(0x00, 0x0008, 0x0014, 0x0190)

    @scena.Lambda('lambda_2913')
    def lambda_2913():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_2913)

    @scena.Lambda('lambda_2921')
    def lambda_2921():
        ChrMoveTo(0x00FE, 1700, -370, 1750, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2921)

    PlaySE(132, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0001)
    Sleep(200)

    @scena.Lambda('lambda_294B')
    def lambda_294B():
        CameraMove(1080, -370, 2980, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_294B)

    @scena.Lambda('lambda_2963')
    def lambda_2963():
        CameraSetDistance(1550, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2963)

    ChrSetAfterImage(0x00, 0x0008, 0x0014, 0x012C)

    @scena.Lambda('lambda_297B')
    def lambda_297B():
        ChrSetDirection(0x00FE, 270, 800)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_297B)

    @scena.Lambda('lambda_2989')
    def lambda_2989():
        ChrJumpTo(0x00FE, 390, -370, 3940, 200, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2989)

    PlaySE(132, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(164, 0x00, 0x64)
    Sleep(200)

    @scena.Lambda('lambda_29BB')
    def lambda_29BB():
        CameraMove(10, -370, 490, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_29BB)

    ChrSetChipByIndex(0x0008, 2)
    ChrSetSubChip(0x0008, 0)
    ChrSetAfterImage(0x00, 0x0008, 0x0014, 0x00C8)

    @scena.Lambda('lambda_29E5')
    def lambda_29E5():
        ChrSetDirection(0x00FE, 0, 800)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_29E5)

    @scena.Lambda('lambda_29F3')
    def lambda_29F3():
        ChrJumpTo(0x00FE, -470, -370, 1220, 200, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_29F3)

    PlaySE(132, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0001)
    ChrSetAfterImage(0x01, 0x0008, 0x0000, 0x0000)
    PlaySE(164, 0x00, 0x64)
    Sleep(200)

    @scena.Lambda('lambda_2A2D')
    def lambda_2A2D():
        CameraMove(-5490, -370, 1080, 200)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2A2D)

    ChrSetFlags(0x0008, 0x0800)
    ChrSetChipByIndex(0x0008, 30)
    ChrSetSubChip(0x0008, 11)
    ChrSetDirection(0x0008, 270, 0)

    @scena.Lambda('lambda_2A5B')
    def lambda_2A5B():
        ChrJumpTo(0x00FE, -9320, 0, 2490, 800, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2A5B)

    Sleep(200)

    ChrSetChipByIndex(0x0008, 29)
    ChrSetSubChip(0x0008, 2)

    @scena.Lambda('lambda_2A88')
    def lambda_2A88():
        OP_99(0x00FE, 0x02, 0x06, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_2A88)

    Sleep(200)

    PlayEffect(0x00, 0x01, 0x0022, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_2AD2')
    def lambda_2AD2():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 100)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_2AD2)

    WaitForThreadExit(0x0008, 0x0001)

    Return()

# id: 0x0010 offset: 0x2AE4
@scena.Code('func_10_2AE4')
def func_10_2AE4():
    ChrSetDirection(0x0008, 130, 0)
    ChrSetChipByIndex(0x0008, 30)
    ChrSetSubChip(0x0008, 13)

    @scena.Lambda('lambda_2AFB')
    def lambda_2AFB():
        OP_99(0x00FE, 0x0D, 0x0F, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_2AFB)

    WaitForThreadExit(0x0008, 0x0003)
    ChrSetChipByIndex(0x0008, 31)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_2B1A')
    def lambda_2B1A():
        OP_99(0x00FE, 0x00, 0x05, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_2B1A)

    WaitForThreadExit(0x0008, 0x0003)

    Return()

# id: 0x0011 offset: 0x2B2A
@scena.Code('func_11_2B2A')
def func_11_2B2A():
    @scena.Lambda('lambda_2B30')
    def lambda_2B30():
        ChrMoveTo(0x00FE, 0, -370, 0, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2B30)

    ChrSetChipByIndex(0x0008, 30)
    ChrSetSubChip(0x0008, 10)

    @scena.Lambda('lambda_2B55')
    def lambda_2B55():
        OP_99(0x00FE, 0x0A, 0x0F, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_2B55)

    WaitForThreadExit(0x0008, 0x0003)
    PlaySE(132, 0x00, 0x64)
    ChrSetChipByIndex(0x0008, 31)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_2B79')
    def lambda_2B79():
        OP_99(0x00FE, 0x00, 0x05, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_2B79)

    WaitForThreadExit(0x0008, 0x0003)

    Return()

# id: 0x0012 offset: 0x2B89
@scena.Code('func_12_2B89')
def func_12_2B89():
    ChrSetChipByIndex(0x0008, 2)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_2B99')
    def lambda_2B99():
        ChrSetDirection(0x00FE, 0, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_2B99)

    WaitForThreadExit(0x0008, 0x0003)

    @scena.Lambda('lambda_2BAC')
    def lambda_2BAC():
        ChrSetDirection(0x00FE, 225, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_2BAC)

    Return()

# id: 0x0013 offset: 0x2BB5
@scena.Code('func_13_2BB5')
def func_13_2BB5():
    ChrSetChipByIndex(0x0022, 9)
    ChrSetSubChip(0x0022, 0)
    ChrSetDirection(0x0022, 180, 0)

    @scena.Lambda('lambda_2BCC')
    def lambda_2BCC():
        OP_9E(0x00FE, 0, 40, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_2BCC)

    @scena.Lambda('lambda_2BE6')
    def lambda_2BE6():
        ChrJumpTo(0x00FE, 0, -370, -3020, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_2BE6)

    WaitForThreadExit(0x0022, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetChipByIndex(0x0022, 10)
    ChrSetSubChip(0x0022, 0)

    @scena.Lambda('lambda_2C18')
    def lambda_2C18():
        ChrJumpTo(0x00FE, 0, -370, -220, 600, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_2C18)

    WaitForThreadExit(0x0022, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetChipByIndex(0x0022, 9)
    ChrSetSubChip(0x0022, 0)

    Return()

# id: 0x0014 offset: 0x2C45
@scena.Code('func_14_2C45')
def func_14_2C45():
    ChrClearFlags(0x0022, 0x0002)
    ChrSetFlags(0x0022, 0x0004)
    ChrSetChipByIndex(0x0022, 8)
    ChrSetSubChip(0x0022, 0)
    PlaySE(213, 0x00, 0x64)
    Sleep(400)

    ChrSetDirection(0x0022, 250, 400)

    Return()

# id: 0x0015 offset: 0x2C6B
@scena.Code('func_15_2C6B')
def func_15_2C6B():
    @scena.Lambda('lambda_2C71')
    def lambda_2C71():
        ChrMoveTo(0x00FE, -4260, -370, -1130, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2C71)

    ChrSetChipByIndex(0x0008, 30)
    ChrSetSubChip(0x0008, 9)

    @scena.Lambda('lambda_2C96')
    def lambda_2C96():
        OP_99(0x00FE, 0x09, 0x0C, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2C96)

    WaitForThreadExit(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 31)
    ChrSetSubChip(0x0008, 2)

    @scena.Lambda('lambda_2CB5')
    def lambda_2CB5():
        OP_99(0x00FE, 0x02, 0x05, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2CB5)

    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(132, 0x00, 0x64)
    Sleep(400)

    ChrSetChipByIndex(0x0008, 7)
    ChrSetSubChip(0x0008, 2)

    @scena.Lambda('lambda_2CDE')
    def lambda_2CDE():
        ChrTurnDirection(0x00FE, 0x0022, 0)
        Yield()

        Jump('lambda_2CDE')

    DispatchAsync2(0x0008, 0x0003, lambda_2CDE)

    @scena.Lambda('lambda_2CEF')
    def lambda_2CEF():
        ChrJumpTo(0x00FE, -4730, 0, -5040, 500, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2CEF)

    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(164, 0x00, 0x64)
    Sleep(300)

    @scena.Lambda('lambda_2D1C')
    def lambda_2D1C():
        CameraMove(-3770, -370, 660, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2D1C)

    @scena.Lambda('lambda_2D34')
    def lambda_2D34():
        OP_6C(228000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2D34)

    TerminateThread(0x0008, 0x03)
    ChrSetDirection(0x0008, 30, 0)
    ChrSetChipByIndex(0x0008, 29)
    ChrSetSubChip(0x0008, 2)

    @scena.Lambda('lambda_2D59')
    def lambda_2D59():
        OP_99(0x00FE, 0x02, 0x06, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2D59)

    @scena.Lambda('lambda_2D69')
    def lambda_2D69():
        ChrJumpTo(0x00FE, -1960, -370, -1460, 500, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2D69)

    Sleep(300)

    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x0008, 1000, 500, 1000, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 400, 3000, 200)
    ChrSetDirection(0x0022, 210, 0)

    @scena.Lambda('lambda_2DDE')
    def lambda_2DDE():
        OP_9E(0x00FE, 40, 0, 500, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_2DDE)

    @scena.Lambda('lambda_2DF8')
    def lambda_2DF8():
        ChrJumpTo(0x00FE, 1540, -370, 2980, 500, 2000)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_2DF8)

    Sleep(600)

    @scena.Lambda('lambda_2E1B')
    def lambda_2E1B():
        CameraMove(210, 0, 150, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2E1B)

    @scena.Lambda('lambda_2E33')
    def lambda_2E33():
        OP_6C(263000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2E33)

    ChrSetDirection(0x0023, 130, 0)
    ChrSetChipByIndex(0x0008, 7)
    ChrSetSubChip(0x0008, 2)

    @scena.Lambda('lambda_2E54')
    def lambda_2E54():
        ChrJumpTo(0x00FE, 1960, -370, -2330, 500, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2E54)

    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(164, 0x00, 0x64)
    TerminateThread(0x0023, 0x02)
    ChrSetChipByIndex(0x0008, 30)
    ChrSetSubChip(0x0008, 11)
    ChrSetChipByIndex(0x0023, 30)
    ChrSetSubChip(0x0023, 11)
    Sleep(400)

    @scena.Lambda('lambda_2E99')
    def lambda_2E99():
        ChrMoveTo(0x00FE, 4500, -370, 630, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2E99)

    @scena.Lambda('lambda_2EB4')
    def lambda_2EB4():
        ChrMoveTo(0x00FE, 4500, -370, 630, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_2EB4)

    @scena.Lambda('lambda_2ECF')
    def lambda_2ECF():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2ECF)

    @scena.Lambda('lambda_2EE1')
    def lambda_2EE1():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 200)

        ExitThread()

    DispatchAsync(0x0023, 0x0002, lambda_2EE1)

    WaitForThreadExit(0x0008, 0x0002)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0023, 0x01)
    ChrSetFlags(0x0023, 0x0080)
    ChrSetRGBAMask(0x0008, 255, 255, 255, 255, 0)
    ChrClearFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, 12070, 0, 1670, 260)
    ChrSetChipByIndex(0x0008, 30)
    ChrSetSubChip(0x0008, 11)

    @scena.Lambda('lambda_2F30')
    def lambda_2F30():
        CameraMove(1910, -370, 300, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2F30)

    CreateThread(0x0008, 0x03, 0x00, func_17_3287)
    Sleep(400)

    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x0008, -2000, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 400, 3000, 200)
    ChrSetDirection(0x0022, 80, 0)

    @scena.Lambda('lambda_2FA6')
    def lambda_2FA6():
        OP_9E(0x00FE, 40, 0, 500, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_2FA6)

    @scena.Lambda('lambda_2FC0')
    def lambda_2FC0():
        ChrJumpTo(0x00FE, -600, -370, -50, 500, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_2FC0)

    WaitForThreadExit(0x0022, 0x0001)
    PlaySE(164, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0003)

    Return()

# id: 0x0016 offset: 0x2FE8
@scena.Code('func_16_2FE8')
def func_16_2FE8():
    ChrSetChipByIndex(0x0023, 30)
    ChrSetSubChip(0x0023, 11)

    @scena.Lambda('lambda_2FF8')
    def lambda_2FF8():
        ChrMoveTo(0x00FE, -7980, 0, -2120, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_2FF8)

    WaitForThreadExit(0x0023, 0x0001)

    @scena.Lambda('lambda_3018')
    def lambda_3018():
        CameraMove(-8310, 0, 730, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3018)

    @scena.Lambda('lambda_3030')
    def lambda_3030():
        OP_6C(265000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3030)

    ChrSetChipByIndex(0x0023, 7)
    ChrSetSubChip(0x0023, 2)

    @scena.Lambda('lambda_304A')
    def lambda_304A():
        ChrSetDirection(0x00FE, 120, 400)

        ExitThread()

    DispatchAsync(0x0023, 0x0003, lambda_304A)

    @scena.Lambda('lambda_3058')
    def lambda_3058():
        ChrJumpTo(0x00FE, -8000, 0, 2770, 500, 2000)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_3058)

    WaitForThreadExit(0x0023, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetChipByIndex(0x0023, 29)
    ChrSetSubChip(0x0023, 2)
    Sleep(50)

    ChrSetChipByIndex(0x0023, 29)
    ChrSetSubChip(0x0023, 3)

    @scena.Lambda('lambda_3099')
    def lambda_3099():
        OP_99(0x00FE, 0x03, 0x06, 3000)

        ExitThread()

    DispatchAsync(0x0023, 0x0002, lambda_3099)

    @scena.Lambda('lambda_30A9')
    def lambda_30A9():
        ChrMoveTo(0x00FE, -6960, 0, 2200, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_30A9)

    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x0023, 1000, 500, -1000, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 400, 3000, 200)
    ChrSetDirection(0x0022, 300, 0)

    @scena.Lambda('lambda_3116')
    def lambda_3116():
        OP_9E(0x00FE, 40, 0, 500, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_3116)

    @scena.Lambda('lambda_3130')
    def lambda_3130():
        ChrJumpTo(0x00FE, -1070, -370, -290, 500, 2000)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_3130)

    Sleep(400)

    ChrSetChipByIndex(0x0023, 30)
    ChrSetSubChip(0x0023, 11)

    @scena.Lambda('lambda_315D')
    def lambda_315D():
        ChrSetDirection(0x00FE, 150, 400)

        ExitThread()

    DispatchAsync(0x0023, 0x0003, lambda_315D)

    @scena.Lambda('lambda_316B')
    def lambda_316B():
        ChrJumpTo(0x00FE, -2170, 0, 6290, 500, 2000)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_316B)

    WaitForThreadExit(0x0023, 0x0001)
    PlaySE(164, 0x00, 0x64)
    Sleep(200)

    @scena.Lambda('lambda_3198')
    def lambda_3198():
        CameraMove(-110, 0, 2100, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3198)

    @scena.Lambda('lambda_31B0')
    def lambda_31B0():
        OP_6C(268000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_31B0)

    ChrSetChipByIndex(0x0023, 31)
    ChrSetSubChip(0x0023, 1)

    @scena.Lambda('lambda_31CA')
    def lambda_31CA():
        OP_99(0x00FE, 0x01, 0x05, 1500)

        ExitThread()

    DispatchAsync(0x0023, 0x0002, lambda_31CA)

    @scena.Lambda('lambda_31DA')
    def lambda_31DA():
        ChrJumpTo(0x00FE, 1260, -370, 3240, 200, 2000)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_31DA)

    Sleep(200)

    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x0023, 1000, 500, -1000, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 400, 3000, 200)
    ChrSetDirection(0x0022, 315, 0)

    @scena.Lambda('lambda_324F')
    def lambda_324F():
        OP_9E(0x00FE, 40, 0, 500, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_324F)

    @scena.Lambda('lambda_3269')
    def lambda_3269():
        ChrJumpTo(0x00FE, 4500, -370, 630, 500, 2000)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_3269)

    WaitForThreadExit(0x0022, 0x0001)

    Return()

# id: 0x0017 offset: 0x3287
@scena.Code('func_17_3287')
def func_17_3287():
    @scena.Lambda('lambda_328D')
    def lambda_328D():
        ChrJumpTo(0x00FE, 6590, 0, 830, 200, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_328D)

    @scena.Lambda('lambda_32AB')
    def lambda_32AB():
        OP_99(0x00FE, 0x0B, 0x0F, 2500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_32AB)

    WaitForThreadExit(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 31)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_32CA')
    def lambda_32CA():
        OP_99(0x00FE, 0x00, 0x05, 2500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_32CA)

    WaitForThreadExit(0x0008, 0x0002)

    Return()

# id: 0x0018 offset: 0x32DA
@scena.Code('func_18_32DA')
def func_18_32DA():
    ChrSetChipByIndex(0x0008, 29)
    ChrSetSubChip(0x0008, 2)

    @scena.Lambda('lambda_32EA')
    def lambda_32EA():
        ChrJumpTo(0x00FE, 0, -370, 0, 1500, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_32EA)

    Sleep(200)

    @scena.Lambda('lambda_330D')
    def lambda_330D():
        OP_99(0x00FE, 0x02, 0x06, 2500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_330D)

    Sleep(200)

    PlaySE(132, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0001)

    Return()

# id: 0x0019 offset: 0x3327
@scena.Code('func_19_3327')
def func_19_3327():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_33A7',
    )

    PlayEffect(0x01, 0xFF, 0x00FF, 0, 500, 0, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(400)

    PlayEffect(0x01, 0xFF, 0x00FF, 0, 600, 0, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(400)

    Jump('func_19_3327')

    def _loc_33A7(): pass

    label('loc_33A7')

    Return()

# id: 0x001A offset: 0x33A8
@scena.Code('func_1A_33A8')
def func_1A_33A8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_34C1',
    )

    OP_7C(100, 0, 3000, 400)
    PlayEffect(0x01, 0xFF, 0x0008, -140, 600, -140, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(214, 0x00, 0x64)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x0008, -240, 700, -40, 0, 0, 0, 1200, 1200, 1200, 0x00FF, 0, 0, 0, 0)
    PlaySE(214, 0x00, 0x64)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x0008, -140, 600, -140, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(214, 0x00, 0x64)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x0008, -40, 700, -240, 0, 0, 0, 1100, 1100, 1100, 0x00FF, 0, 0, 0, 0)
    PlaySE(214, 0x00, 0x64)
    Sleep(100)

    Jump('func_1A_33A8')

    def _loc_34C1(): pass

    label('loc_34C1')

    Return()

# id: 0x001B offset: 0x34C2
@scena.Code('func_1B_34C2')
def func_1B_34C2():
    ChrSetChipByIndex(0x00FE, 32)
    ChrSetFlags(0x00FE, 0x0002)
    ChrClearFlags(0x00FE, 0x0080)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetPos(0x00FE, 4270, 700, 2870, 0)

    @scena.Lambda('lambda_34ED')
    def lambda_34ED():
        OP_99(0x00FE, 0x00, 0x07, 3000)
        Yield()

        Jump('lambda_34ED')

    DispatchAsync2(0x00FE, 0x0002, lambda_34ED)

    @scena.Lambda('lambda_3500')
    def lambda_3500():
        ChrJumpTo(0x00FE, 8380, 0, 3440, 1000, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3500)

    WaitForThreadExit(0x00FE, 0x0001)
    PlaySE(214, 0x00, 0x64)
    TerminateThread(0x00FE, 0x02)

    @scena.Lambda('lambda_352C')
    def lambda_352C():
        ChrJumpTo(0x00FE, 10770, 0, 3430, 500, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_352C)

    @scena.Lambda('lambda_354A')
    def lambda_354A():
        OP_99(0x00FE, 0x10, 0x20, 3000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_354A)

    WaitForThreadExit(0x00FE, 0x0001)
    PlaySE(214, 0x00, 0x64)
    WaitForThreadExit(0x00FE, 0x0002)

    Return()

# id: 0x001C offset: 0x3564
@scena.Code('func_1C_3564')
def func_1C_3564():
    PlayEffect(0x02, 0x01, 0x0008, -1000, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ChrSetFlags(0x00FE, 0x0002)
    ChrSetFlags(0x00FE, 0x0800)
    ChrSetChipByIndex(0x00FE, 2)
    ChrSetSubChip(0x00FE, 0)

    @scena.Lambda('lambda_35B3')
    def lambda_35B3():
        OP_99(0x00FE, 0x00, 0x05, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_35B3)

    @scena.Lambda('lambda_35C3')
    def lambda_35C3():
        ChrJumpTo(0x00FE, 0, -370, 4400, 1500, 3000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_35C3)

    PlaySE(524, 0x00, 0x64)
    WaitForThreadExit(0x00FE, 0x0001)
    WaitForThreadExit(0x00FE, 0x0002)

    Return()

# id: 0x001D offset: 0x35EB
@scena.Code('func_1D_35EB')
def func_1D_35EB():
    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_35FB'),
        (0x00000000, 'loc_3608'),
        (-1, 'loc_3615'),
    )

    def _loc_35FB(): pass

    label('loc_35FB')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3615')

    def _loc_3608(): pass

    label('loc_3608')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3615')

    def _loc_3615(): pass

    label('loc_3615')

    EventBegin(0x00)
    FadeOut(0, 0, -1)
    MapSetFlags(0x00000010)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0102, 0x0080)
    ChrClearFlags(0x0022, 0x0080)
    TerminateThread(0x0017, 0x00)
    TerminateThread(0x0018, 0x00)
    TerminateThread(0x0008, 0x00)
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0022, 0x00)
    TerminateThread(0x00F8, 0x00)
    TerminateThread(0x00F9, 0x00)
    Call(0, 0x0003)
    ChrSetPos(0x0101, -760, -370, -4800, 0)
    ChrSetPos(0x0022, 760, -370, -4800, 0)
    ChrSetPos(0x00F8, -1680, 0, -6800, 0)
    ChrSetPos(0x00F9, -160, 0, -6800, 0)
    ChrSetChipByIndex(0x0101, 6)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0022, 8)
    ChrSetSubChip(0x0022, 0)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_36C4',
    )

    ChrSetChipByIndex(0x0103, 11)

    def _loc_36C4(): pass

    label('loc_36C4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_36D7',
    )

    ChrSetChipByIndex(0x0104, 13)

    def _loc_36D7(): pass

    label('loc_36D7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_36EA',
    )

    ChrSetChipByIndex(0x0105, 15)

    def _loc_36EA(): pass

    label('loc_36EA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_36FD',
    )

    ChrSetChipByIndex(0x0106, 17)

    def _loc_36FD(): pass

    label('loc_36FD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3710',
    )

    ChrSetChipByIndex(0x0107, 19)

    def _loc_3710(): pass

    label('loc_3710')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3723',
    )

    ChrSetChipByIndex(0x0108, 21)

    def _loc_3723(): pass

    label('loc_3723')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3736',
    )

    ChrSetChipByIndex(0x0109, 23)

    def _loc_3736(): pass

    label('loc_3736')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3749',
    )

    ChrSetChipByIndex(0x010B, 25)

    def _loc_3749(): pass

    label('loc_3749')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_375C',
    )

    ChrSetChipByIndex(0x010F, 36)

    def _loc_375C(): pass

    label('loc_375C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_376F',
    )

    ChrSetChipByIndex(0x0110, 34)

    def _loc_376F(): pass

    label('loc_376F')

    ChrSetSubChip(0x00F8, 0)
    ChrSetSubChip(0x00F9, 0)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetSubChip(0x0008, 0)
    ChrSetPos(0x0008, 0, -370, 2320, 180)
    ChrSetChipByIndex(0x0008, 28)
    LoadEffect(0x00, 'craft\\\\cr162_02.eff')
    LoadEffect(0x01, 'map\\\\mp009_00.eff')
    LoadEffect(0x02, 'scraft\\\\sc480_00.eff')
    LoadEffect(0x03, 'scraft\\\\sc480_03.eff')
    LoadEffect(0x04, 'craft\\\\cr161_00.eff')
    LoadEffect(0x05, 'scraft\\\\sc007_10.eff')
    LoadEffect(0x06, 'map\\\\mp056_00.eff')
    StopEffect(0x80, 0x00)
    StopEffect(0x82, 0x00)
    CameraMove(530, -370, -1200, 0)
    OP_67(0, 5960, -10000, 0)
    CameraSetDistance(2500, 0)
    OP_6C(45000, 0)
    OP_6E(433, 0)
    OP_D0(360000, 0)
    ChrClearFlags(0x0023, 0x0004)
    ChrClearFlags(0x0024, 0x0004)
    ChrClearFlags(0x0025, 0x0004)
    ChrClearFlags(0x0026, 0x0004)
    ChrClearFlags(0x0027, 0x0004)
    ChrClearFlags(0x0028, 0x0004)
    ChrSetPos(0x0023, -310, -370, 2320, 97)
    ChrSetPos(0x0024, -310, 0, 2320, 0)
    ChrSetPos(0x0025, -310, 0, 2320, 0)
    ChrSetPos(0x0026, -310, 0, 2320, 0)
    ChrSetPos(0x0027, -310, 0, 2320, 0)
    ChrSetPos(0x0028, -310, -370, 2320, 0)

    @scena.Lambda('lambda_3912')
    def lambda_3912():
        OP_97(0x00FE, 4740, 1700, 60000, 40000, 0x0002)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_3912)

    @scena.Lambda('lambda_392E')
    def lambda_392E():
        OP_97(0x00FE, 4740, 1700, 120000, 40000, 0x0002)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_392E)

    @scena.Lambda('lambda_394A')
    def lambda_394A():
        OP_97(0x00FE, 4740, 1700, 180000, 40000, 0x0002)

        ExitThread()

    DispatchAsync(0x0026, 0x0001, lambda_394A)

    @scena.Lambda('lambda_3966')
    def lambda_3966():
        OP_97(0x00FE, 4740, 1700, 240000, 40000, 0x0002)

        ExitThread()

    DispatchAsync(0x0027, 0x0001, lambda_3966)

    @scena.Lambda('lambda_3982')
    def lambda_3982():
        OP_97(0x00FE, 4740, 1700, 300000, 40000, 0x0002)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_3982)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3F4A',
    )

    ChrSetChipByIndex(0x0008, 3)

    @scena.Lambda('lambda_39B0')
    def lambda_39B0():
        CameraSetDistance(2200, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_39B0)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0028, 0x0001)
    ChrSetFlags(0x0023, 0x0004)
    ChrSetFlags(0x0024, 0x0004)
    ChrSetFlags(0x0025, 0x0004)
    ChrSetFlags(0x0026, 0x0004)
    ChrSetFlags(0x0027, 0x0004)
    ChrSetFlags(0x0028, 0x0004)

    ChrTalk(
        0x0101,
        (
            '#0010410844V#1006F#6P终、终于……！',
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
        'loc_3A4D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050410845V#051F#4P嘿……看到了吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3A4D(): pass

    label('loc_3A4D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3A7D',
    )

    ChrTalk(
        0x0108,
        (
            '#0080410846V#070F#4P好……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3A7D(): pass

    label('loc_3A7D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3ACC',
    )

    ChrTalk(
        0x0103,
        (
            '#0030410847V#524F#4P女王宮时的耻辱……\n',
            '总算是报偿还了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3ACC(): pass

    label('loc_3ACC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3B00',
    )

    ChrTalk(
        0x0107,
        (
            '#0070410848V#561F#4P呼呜呜～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B00(): pass

    label('loc_3B00')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3B46',
    )

    ChrTalk(
        0x0109,
        (
            '#0180410849V#1066F#4P嘿嘿……\n',
            '正义还是胜利了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B46(): pass

    label('loc_3B46')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3B86',
    )

    ChrTalk(
        0x010B,
        (
            '#0090410850V#413F#4P心、心脏跳得好厉害啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B86(): pass

    label('loc_3B86')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3BC9',
    )

    ChrTalk(
        0x0104,
        (
            '#0040410851V#031F#4P呼……\n',
            '历史性的大胜利啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3BC9(): pass

    label('loc_3BC9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3C1A',
    )

    ChrTalk(
        0x0110,
        (
            '#0110410852V#278F没想到……\n',
            '竟然会被压制到这种程度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C1A(): pass

    label('loc_3C1A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3C69',
    )

    ChrTalk(
        0x010F,
        (
            '#0100410853V#170F这一局……\n',
            '我赢了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C69(): pass

    label('loc_3C69')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3CA8',
    )

    ChrTalk(
        0x0105,
        (
            '#0060410854V#1382F#4P太好了……这样的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3CA8(): pass

    label('loc_3CA8')

    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140410855V#124F#5P……干得还不错嘛，\n',
            '但这种实力还无法压倒我的修罗之道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0022, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3D5B',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_3D99')

    def _loc_3D5B(): pass

    label('loc_3D5B')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3D82',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_3D99')

    def _loc_3D82(): pass

    label('loc_3D82')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_3D99(): pass

    label('loc_3D99')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DC5',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_3E03')

    def _loc_3DC5(): pass

    label('loc_3DC5')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DEC',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_3E03')

    def _loc_3DEC(): pass

    label('loc_3DEC')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_3E03(): pass

    label('loc_3E03')

    Sleep(1000)

    Fade(500)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0008, 28)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010410856V#1020F#6P为、为什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140410857V#121F#5P归根到底，你们游击士\n',
            '也只是守护他人的存在。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410858V如果不能领悟『理』之境界的话，\n',
            '自然也不可能追及『修罗』的境界。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410859V#123F热身运动就到此为止──\n',
            '接下来我就要使出全力来击溃你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310610V#1002F#6P呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42FB')

    def _loc_3F4A(): pass

    label('loc_3F4A')

    @scena.Lambda('lambda_3F50')
    def lambda_3F50():
        CameraSetDistance(2200, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3F50)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0028, 0x0001)
    ChrSetFlags(0x0023, 0x0004)
    ChrSetFlags(0x0024, 0x0004)
    ChrSetFlags(0x0025, 0x0004)
    ChrSetFlags(0x0026, 0x0004)
    ChrSetFlags(0x0027, 0x0004)
    ChrSetFlags(0x0028, 0x0004)

    ChrTalk(
        0x0101,
        (
            '#0010410861V#1020F#6P唔，好强……！',
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
        'loc_3FF2',
    )

    ChrTalk(
        0x0106,
        (
            '#0050410862V#057F#4P哼……\n',
            '好难缠的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3FF2(): pass

    label('loc_3FF2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_403D',
    )

    ChrTalk(
        0x0108,
        (
            '#0080410863V#072F#4P……如此年轻，\n',
            '竟能达到这般境界……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_403D(): pass

    label('loc_403D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_406F',
    )

    ChrTalk(
        0x0103,
        (
            '#0030410864V#022F#4P好厉害……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_406F(): pass

    label('loc_406F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_409F',
    )

    ChrTalk(
        0x0107,
        (
            '#0070410865V#065F#4P啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_409F(): pass

    label('loc_409F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_40D6',
    )

    ChrTalk(
        0x0109,
        (
            '#0180410866V#1063F#4P太、太强了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_40D6(): pass

    label('loc_40D6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4115',
    )

    ChrTalk(
        0x010B,
        (
            '#0090410867V#216F#4P强、强得\n',
            '难以想象啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4115(): pass

    label('loc_4115')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4155',
    )

    ChrTalk(
        0x0110,
        (
            '#0110410868V#276F……唔…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4155(): pass

    label('loc_4155')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4198',
    )

    ChrTalk(
        0x0104,
        (
            '#0040410869V#032F#4P哎呀呀……\n',
            '比穆拉还要强啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4198(): pass

    label('loc_4198')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_41D8',
    )

    ChrTalk(
        0x010F,
        (
            '#0100410870V#172F竟然，强到这种地步……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_41D8(): pass

    label('loc_41D8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4215',
    )

    ChrTalk(
        0x0105,
        (
            '#0060410871V#1163F#4P……到底该怎么办……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4215(): pass

    label('loc_4215')

    ChrTalk(
        0x0008,
        (
            '#0140410872V#124F#5P哼……只懂嘴上功夫是没用的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410873V#121F那种程度的实力，就算能战胜我，\n',
            '也难逃『白面』的魔掌。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410874V死在这里，还是夹着尾巴逃跑。\n',
            '你们自己选择吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410875V#1005F#6P别、别开玩笑了──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_42FB(): pass

    label('loc_42FB')

    Sleep(100)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0022, 1)
    ChrSetSubChip(0x0022, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0022,
        (
            '#0020410876V#1035F#4P……那么，莱维。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410877V#1042F接下来\n',
            '就让我一个人来挑战你吧。',
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
        'loc_43BB',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_43F9')

    def _loc_43BB(): pass

    label('loc_43BB')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_43E2',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_43F9')

    def _loc_43E2(): pass

    label('loc_43E2')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_43F9(): pass

    label('loc_43F9')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4425',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_4463')

    def _loc_4425(): pass

    label('loc_4425')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_444C',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_4463')

    def _loc_444C(): pass

    label('loc_444C')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_4463(): pass

    label('loc_4463')

    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0140410878V#123F哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410879V#1020F#6P约、约修亚……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0020410880V#1035F#5P没关系，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410881V#1040F莱维确实非常强，\n',
            '但刚才的一战也使他的体力消耗不轻。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410882V接下来……就让我来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410883V#1026F#6P约修亚……',
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
        'loc_464D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050410884V#053F#4P嘿，本来我也想\n',
            '向他讨回旧帐的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050410885V#051F但没办法了，既然是你的话，\n',
            '我也只能让步啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050410886V#054F作为条件……\n',
            '你可绝对不许输啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0020410887V#1054F#5P嗯！一定！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_464D(): pass

    label('loc_464D')

    Sleep(100)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0001, 0)
    ChrSetSubChip(0x00F9, 0)
    OP_0D()

    @scena.Lambda('lambda_4681')
    def lambda_4681():
        CameraMove(0, -370, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_4681)

    @scena.Lambda('lambda_4699')
    def lambda_4699():
        OP_67(0, 3940, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4699)

    @scena.Lambda('lambda_46B1')
    def lambda_46B1():
        CameraSetDistance(1900, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_46B1)

    @scena.Lambda('lambda_46C1')
    def lambda_46C1():
        OP_6C(0, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_46C1)

    @scena.Lambda('lambda_46D1')
    def lambda_46D1():
        OP_6E(465, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_46D1)

    @scena.Lambda('lambda_46E1')
    def lambda_46E1():
        ChrSetDirection(0x00FE, 0, 100)

        ExitThread()

    DispatchAsync(0x00F8, 0x0003, lambda_46E1)

    @scena.Lambda('lambda_46EF')
    def lambda_46EF():
        ChrSetDirection(0x00FE, 0, 100)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_46EF)

    @scena.Lambda('lambda_46FD')
    def lambda_46FD():
        ChrMoveTo(0x00FE, 0, -370, -3100, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0000, lambda_46FD)

    Sleep(300)

    @scena.Lambda('lambda_471D')
    def lambda_471D():
        ChrMoveTo(0x00FE, -2760, 0, -10600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_471D)

    Sleep(150)

    @scena.Lambda('lambda_473D')
    def lambda_473D():
        ChrMoveTo(0x00FE, -3680, 0, -12640, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0000, lambda_473D)

    @scena.Lambda('lambda_4758')
    def lambda_4758():
        ChrMoveTo(0x00FE, -2160, 0, -12640, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_4758)

    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140410888V#124F#5P哼哼，刚才的战斗的确\n',
            '让我的行动力打了一些折扣。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410889V从这一点上说，\n',
            '说不定你也有一丝取胜之机……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410890V#123F但这种可能性有多渺茫，你自己也清楚吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0020410891V#1043F#6P……我明白。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410892V#1035F被姐姐拯救、被教授改造、\n',
            '被父亲解放…如今，\n',
            '我的灵魂与艾丝蒂尔共存……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410893V在游击士生涯中学习到的一切心得，\n',
            '还有『漆黑之牙』的所有本领……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4906')
    def lambda_4906():
        CameraSetDistance(2100, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4906)

    Sleep(100)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0022, 8)
    ChrSetSubChip(0x0022, 0)
    OP_99(0x0022, 0x00, 0x07, 2000)
    PlayBGM(119)
    Sleep(500)

    ChrTalk(
        0x0022,
        (
            '#0020410894V#1046F#6P如今我就要利用这一切……\n',
            '来向『剑帝』挑战！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140410895V#123F#5P很好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetPos(0x0008, 0, -370, 2220, 180)
    OP_0D()
    Sleep(1000)

    TerminateThread(0x0101, 0x00)

    ChrTalk(
        0x0008,
        (
            '#0140410896V#126F放马过来吧……『漆黑之牙』！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_59()
    Call(0, 0x0004)
    Sleep(20)

    ChrSetPos(0x0101, -2920, 0, -11860, 0)
    MapClearFlags(0x00000010)
    ChrSetFlags(0x0008, 0x0040)
    ChrSetFlags(0x0008, 0x0020)
    ChrSetFlags(0x0008, 0x1000)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x0022, 0x0040)
    ChrSetFlags(0x0022, 0x0020)
    ChrSetFlags(0x0022, 0x1000)
    ChrSetFlags(0x0022, 0x0004)

    @scena.Lambda('lambda_4A69')
    def lambda_4A69():
        CameraMove(3370, -370, 690, 1600)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4A69)

    @scena.Lambda('lambda_4A81')
    def lambda_4A81():
        OP_6C(94000, 1600)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4A81)

    ChrSetAfterImage(0x00, 0x0022, 0x0064, 0x01F4)

    @scena.Lambda('lambda_4A99')
    def lambda_4A99():
        ChrSetDirection(0x00FE, 140, 100)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_4A99)

    @scena.Lambda('lambda_4AA7')
    def lambda_4AA7():
        ChrSetDirection(0x00FE, 310, 100)

        ExitThread()

    DispatchAsync(0x0022, 0x0003, lambda_4AA7)

    @scena.Lambda('lambda_4AB5')
    def lambda_4AB5():
        ChrMoveTo(0x00FE, 4000, -370, -770, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_4AB5)

    Sleep(500)

    @scena.Lambda('lambda_4AD5')
    def lambda_4AD5():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_4AD5)

    Sleep(1500)

    ChrSetPos(0x0022, -7610, 0, 8360, 140)
    ChrSetSubChip(0x0022, 8)
    ChrSetRGBAMask(0x0022, 255, 255, 255, 255, 0)
    ChrSetAfterImage(0x01, 0x0022, 0x0000, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_4B1E')
    def lambda_4B1E():
        ChrMoveTo(0x00FE, 0, -670, 2220, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_4B1E)

    Sleep(300)

    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x0022, 2000, 500, -2000, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 400, 3000, 200)

    @scena.Lambda('lambda_4B89')
    def lambda_4B89():
        CameraMove(3890, -370, 80, 200)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4B89)

    @scena.Lambda('lambda_4BA1')
    def lambda_4BA1():
        OP_67(0, 3290, -10000, 200)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4BA1)

    ChrSetChipByIndex(0x0008, 30)
    ChrSetSubChip(0x0008, 2)
    ChrSetDirection(0x0008, 310, 0)

    @scena.Lambda('lambda_4BCA')
    def lambda_4BCA():
        OP_99(0x00FE, 0x02, 0x03, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_4BCA)

    @scena.Lambda('lambda_4BDA')
    def lambda_4BDA():
        ChrJumpTo(0x00FE, 4460, -570, -1520, 1000, 8000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4BDA)

    CreateThread(0x0008, 0x00, 0x00, func_09_2579)
    Sleep(300)

    @scena.Lambda('lambda_4C04')
    def lambda_4C04():
        CameraMove(3210, -370, 1560, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4C04)

    @scena.Lambda('lambda_4C1C')
    def lambda_4C1C():
        OP_6C(353000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4C1C)

    ChrSetChipByIndex(0x0022, 9)
    ChrSetSubChip(0x0022, 1)
    ChrSetPos(0x0022, 0, -470, 2220, 140)

    @scena.Lambda('lambda_4C47')
    def lambda_4C47():
        ChrMoveTo(0x00FE, 4460, -370, -1520, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_4C47)

    @scena.Lambda('lambda_4C62')
    def lambda_4C62():
        OP_99(0x00FE, 0x01, 0x07, 2500)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_4C62)

    Sleep(200)

    ChrSetSubChip(0x0008, 1)
    ChrSetDirection(0x0008, 40, 0)
    ChrSetAfterImage(0x00, 0x0008, 0x0032, 0x01F4)

    @scena.Lambda('lambda_4C8B')
    def lambda_4C8B():
        ChrMoveTo(0x00FE, 3310, -470, -3150, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4C8B)

    PlaySE(132, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0001)
    ChrSetAfterImage(0x01, 0x0008, 0x0000, 0x0000)
    Sleep(300)

    ChrSetChipByIndex(0x0008, 2)
    ChrSetSubChip(0x0008, 0)
    Sleep(50)

    PlayEffect(0x00, 0x01, 0x0022, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_4D01')
    def lambda_4D01():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 100)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_4D01)

    Sleep(50)

    ChrSetChipByIndex(0x0008, 31)
    ChrSetSubChip(0x0008, 3)

    @scena.Lambda('lambda_4D22')
    def lambda_4D22():
        OP_99(0x00FE, 0x03, 0x05, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_4D22)

    @scena.Lambda('lambda_4D32')
    def lambda_4D32():
        ChrMoveTo(0x00FE, 3890, -370, -2560, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4D32)

    PlaySE(132, 0x00, 0x64)
    WaitForThreadExit(0x0022, 0x0002)
    WaitEffect(0x01, 0x02)

    @scena.Lambda('lambda_4D5A')
    def lambda_4D5A():
        CameraMove(5050, -370, -760, 200)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4D5A)

    ChrSetPos(0x0022, 9210, 1000, -7280, 310)
    ChrSetRGBAMask(0x0022, 255, 255, 255, 255, 0)
    ChrSetFlags(0x0022, 0x0002)
    ChrSetChipByIndex(0x0022, 3)
    ChrSetSubChip(0x0022, 24)
    CreateThread(0x0022, 0x00, 0x00, func_0B_25FC)
    Sleep(500)

    ChrSetDirection(0x0008, 270, 0)
    ChrSetChipByIndex(0x0008, 30)
    ChrSetSubChip(0x0008, 13)

    @scena.Lambda('lambda_4DBA')
    def lambda_4DBA():
        OP_99(0x00FE, 0x0D, 0x0F, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_4DBA)

    WaitForThreadExit(0x0022, 0x0000)

    @scena.Lambda('lambda_4DCF')
    def lambda_4DCF():
        OP_9E(0x00FE, 20, 0, 500, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_4DCF)

    @scena.Lambda('lambda_4DE9')
    def lambda_4DE9():
        OP_9E(0x00FE, 20, 0, 500, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_4DE9)

    Sleep(500)

    @scena.Lambda('lambda_4E08')
    def lambda_4E08():
        CameraMove(7800, 0, -1860, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4E08)

    @scena.Lambda('lambda_4E20')
    def lambda_4E20():
        OP_6C(50000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4E20)

    @scena.Lambda('lambda_4E30')
    def lambda_4E30():
        CameraSetDistance(2200, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4E30)

    ChrSetChipByIndex(0x0008, 2)
    ChrSetSubChip(0x0008, 1)
    ChrSetDirection(0x0008, 170, 0)
    CreateThread(0x0022, 0x00, 0x00, func_0A_2584)
    Sleep(200)

    ChrSetDirection(0x0008, 82, 0)
    ChrSetChipByIndex(0x0008, 7)
    ChrSetSubChip(0x0008, 6)

    @scena.Lambda('lambda_4E6E')
    def lambda_4E6E():
        ChrJumpTo(0x00FE, 1750, -370, -2550, 600, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4E6E)

    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetChipByIndex(0x0008, 18)
    ChrSetSubChip(0x0008, 0)
    Sleep(100)

    @scena.Lambda('lambda_4EA5')
    def lambda_4EA5():
        CameraMove(16520, -370, -300, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4EA5)

    @scena.Lambda('lambda_4EBD')
    def lambda_4EBD():
        CameraSetDistance(1890, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4EBD)

    ChrSetChipByIndex(0x0008, 30)
    ChrSetSubChip(0x0008, 11)
    ChrSetAfterImage(0x00, 0x0008, 0x0014, 0x00C8)

    @scena.Lambda('lambda_4EDF')
    def lambda_4EDF():
        ChrJumpTo(0x00FE, 13310, 0, -2240, 600, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4EDF)

    Sleep(200)

    ChrSetChipByIndex(0x0008, 29)
    ChrSetSubChip(0x0008, 3)

    @scena.Lambda('lambda_4F0C')
    def lambda_4F0C():
        OP_99(0x00FE, 0x03, 0x06, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_4F0C)

    WaitForThreadExit(0x0008, 0x0001)
    TerminateThread(0x0022, 0x00)

    @scena.Lambda('lambda_4F25')
    def lambda_4F25():
        ChrMoveTo(0x00FE, 15970, 0, -2470, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_4F25)

    @scena.Lambda('lambda_4F40')
    def lambda_4F40():
        OP_9E(0x00FE, 40, 0, 500, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_4F40)

    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x0008, 2000, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 400, 3000, 200)
    Sleep(100)

    ChrSetChipByIndex(0x0022, 9)
    ChrSetSubChip(0x0022, 0)
    ChrSetChipByIndex(0x0008, 2)
    ChrSetSubChip(0x0008, 0)
    Sleep(200)

    ChrSetAfterImage(0x01, 0x0008, 0x0000, 0x0000)
    ChrSetChipByIndex(0x0008, 2)
    ChrSetSubChip(0x0008, 1)

    @scena.Lambda('lambda_4FD5')
    def lambda_4FD5():
        ChrMoveTo(0x00FE, 14780, 0, -2380, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4FD5)

    PlaySE(132, 0x00, 0x64)
    ChrSetChipByIndex(0x0022, 6)
    ChrSetSubChip(0x0022, 0)
    ChrSetAfterImage(0x00, 0x0022, 0x0014, 0x00C8)

    @scena.Lambda('lambda_5007')
    def lambda_5007():
        ChrSetDirection(0x00FE, 172, 400)

        ExitThread()

    DispatchAsync(0x0022, 0x0003, lambda_5007)

    @scena.Lambda('lambda_5015')
    def lambda_5015():
        OP_99(0x00FE, 0x00, 0x04, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_5015)

    @scena.Lambda('lambda_5025')
    def lambda_5025():
        ChrJumpTo(0x00FE, 15130, 0, 490, 200, 6000)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_5025)

    WaitForThreadExit(0x0022, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetAfterImage(0x01, 0x0022, 0x0000, 0x0000)
    Sleep(100)

    @scena.Lambda('lambda_505A')
    def lambda_505A():
        OP_99(0x00FE, 0x04, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_505A)

    @scena.Lambda('lambda_506A')
    def lambda_506A():
        ChrMoveTo(0x00FE, 14800, 0, -2230, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_506A)

    PlaySE(132, 0x00, 0x64)
    ChrSetAfterImage(0x00, 0x0008, 0x0014, 0x00C8)
    ChrSetChipByIndex(0x0008, 29)
    ChrSetSubChip(0x0008, 3)

    @scena.Lambda('lambda_509C')
    def lambda_509C():
        ChrSetDirection(0x00FE, 12, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_509C)

    @scena.Lambda('lambda_50AA')
    def lambda_50AA():
        ChrJumpTo(0x00FE, 13660, 0, -5360, 500, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_50AA)

    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetAfterImage(0x01, 0x0008, 0x0000, 0x0000)
    Sleep(100)

    @scena.Lambda('lambda_50DF')
    def lambda_50DF():
        OP_99(0x00FE, 0x03, 0x06, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_50DF)

    @scena.Lambda('lambda_50EF')
    def lambda_50EF():
        ChrMoveTo(0x00FE, 14420, 0, -3160, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_50EF)

    Sleep(50)

    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x0022, 0, 500, -500, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 400, 3000, 200)
    ChrSetChipByIndex(0x0022, 9)
    ChrSetSubChip(0x0022, 0)

    @scena.Lambda('lambda_5164')
    def lambda_5164():
        OP_9E(0x00FE, 60, 0, 500, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_5164)

    @scena.Lambda('lambda_517E')
    def lambda_517E():
        ChrMoveTo(0x00FE, 15480, 0, 1700, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_517E)

    WaitForThreadExit(0x0022, 0x0001)
    Sleep(100)

    ChrSetChipByIndex(0x0008, 2)
    ChrSetSubChip(0x0008, 0)
    Sleep(100)

    @scena.Lambda('lambda_51B2')
    def lambda_51B2():
        CameraMove(18190, 1030, 6640, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_51B2)

    @scena.Lambda('lambda_51CA')
    def lambda_51CA():
        OP_67(0, 3290, -10000, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_51CA)

    @scena.Lambda('lambda_51E2')
    def lambda_51E2():
        CameraSetDistance(2330, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_51E2)

    ChrSetChipByIndex(0x0008, 2)
    ChrSetSubChip(0x0008, 1)

    @scena.Lambda('lambda_51FC')
    def lambda_51FC():
        ChrMoveTo(0x00FE, 15010, 0, 390, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_51FC)

    PlaySE(132, 0x00, 0x64)
    ChrSetFlags(0x0022, 0x0800)
    ChrClearFlags(0x0022, 0x0001)
    ChrSetChipByIndex(0x0022, 10)
    ChrSetSubChip(0x0022, 2)
    ChrSetAfterImage(0x00, 0x0022, 0x0014, 0x00C8)

    @scena.Lambda('lambda_5238')
    def lambda_5238():
        ChrJumpTo(0x00FE, 16300, 3450, 9360, 3500, 8000)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_5238)

    WaitForThreadExit(0x0022, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetChipByIndex(0x0022, 4)
    ChrSetSubChip(0x0022, 3)
    Sleep(100)

    ChrSetChipByIndex(0x0022, 10)
    ChrSetSubChip(0x0022, 2)

    @scena.Lambda('lambda_5279')
    def lambda_5279():
        ChrJumpTo(0x00FE, -310, -370, 2320, 200, 8000)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_5279)

    Sleep(200)

    Fade(500)
    CameraMove(7810, -370, 1420, 0)
    OP_67(0, 3290, -10000, 0)
    CameraSetDistance(2330, 0)
    OP_6C(97000, 0)
    OP_6E(465, 0)
    ChrClearFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, 15010, 0, 390, 280)
    ChrSetChipByIndex(0x0008, 7)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_52FE')
    def lambda_52FE():
        OP_99(0x00FE, 0x00, 0x07, 2000)
        Yield()

        Jump('lambda_52FE')

    DispatchAsync2(0x0008, 0x0002, lambda_52FE)

    @scena.Lambda('lambda_5311')
    def lambda_5311():
        ChrMoveTo(0x00FE, 4740, -370, 1700, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_5311)

    CreateThread(0x0008, 0x00, 0x00, func_0C_26D5)
    ChrClearFlags(0x0022, 0x0800)
    ChrSetFlags(0x0022, 0x0001)
    ChrSetPos(0x0022, 16300, 3450, 9360, 100)

    @scena.Lambda('lambda_534E')
    def lambda_534E():
        ChrJumpTo(0x00FE, -310, -370, 2320, 200, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_534E)

    WaitForThreadExit(0x0022, 0x0001)
    ChrSetAfterImage(0x01, 0x0022, 0x0000, 0x0000)
    PlaySE(164, 0x00, 0x64)
    ChrSetChipByIndex(0x0022, 4)
    ChrSetSubChip(0x0022, 3)
    Sleep(100)

    @scena.Lambda('lambda_538D')
    def lambda_538D():
        CameraMove(5250, -370, 1730, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_538D)

    @scena.Lambda('lambda_53A5')
    def lambda_53A5():
        OP_67(0, 6880, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_53A5)

    @scena.Lambda('lambda_53BD')
    def lambda_53BD():
        CameraSetDistance(2130, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_53BD)

    ChrClearFlags(0x0022, 0x0004)
    ChrSetChipByIndex(0x0022, 8)
    ChrSetSubChip(0x0022, 0)
    ChrSetAfterImage(0x00, 0x0022, 0x0064, 0x01F4)

    @scena.Lambda('lambda_53E4')
    def lambda_53E4():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 100, 12000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_53E4)

    @scena.Lambda('lambda_53F6')
    def lambda_53F6():
        OP_97(0x00FE, 4740, 1700, 360000, 12000, 0x0002)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_53F6)

    ChrSetChipByIndex(0x0023, 8)
    ChrSetSubChip(0x0023, 0)
    ChrSetChipByIndex(0x0024, 8)
    ChrSetSubChip(0x0024, 0)
    ChrSetChipByIndex(0x0025, 8)
    ChrSetSubChip(0x0025, 0)
    ChrSetChipByIndex(0x0026, 8)
    ChrSetSubChip(0x0026, 0)
    ChrSetChipByIndex(0x0027, 8)
    ChrSetSubChip(0x0027, 0)
    ChrSetChipByIndex(0x0028, 8)
    ChrSetSubChip(0x0028, 0)
    ChrSetRGBAMask(0x0023, 255, 255, 255, 235, 0)
    ChrClearFlags(0x0023, 0x0080)
    Sleep(434)

    ChrSetRGBAMask(0x0024, 255, 255, 255, 185, 0)
    ChrClearFlags(0x0024, 0x0080)
    Sleep(434)

    ChrSetRGBAMask(0x0025, 255, 255, 255, 185, 0)
    ChrClearFlags(0x0025, 0x0080)
    Sleep(434)

    ChrSetRGBAMask(0x0026, 255, 255, 255, 185, 0)
    ChrClearFlags(0x0026, 0x0080)
    Sleep(434)

    ChrSetRGBAMask(0x0027, 255, 255, 255, 185, 0)
    ChrClearFlags(0x0027, 0x0080)
    Sleep(434)

    ChrSetRGBAMask(0x0028, 255, 255, 255, 235, 0)
    ChrClearFlags(0x0028, 0x0080)
    WaitForThreadExit(0x0022, 0x0001)
    ChrSetFlags(0x0022, 0x0008)
    ChrSetAfterImage(0x01, 0x0022, 0x0000, 0x0000)

    @scena.Lambda('lambda_54D9')
    def lambda_54D9():
        OP_99(0x00FE, 0x00, 0x07, 1500)

        ExitThread()

    DispatchAsync(0x0023, 0x0002, lambda_54D9)

    @scena.Lambda('lambda_54E9')
    def lambda_54E9():
        OP_99(0x00FE, 0x00, 0x07, 1500)

        ExitThread()

    DispatchAsync(0x0024, 0x0002, lambda_54E9)

    @scena.Lambda('lambda_54F9')
    def lambda_54F9():
        OP_99(0x00FE, 0x00, 0x07, 1500)

        ExitThread()

    DispatchAsync(0x0025, 0x0002, lambda_54F9)

    @scena.Lambda('lambda_5509')
    def lambda_5509():
        OP_99(0x00FE, 0x00, 0x07, 1500)

        ExitThread()

    DispatchAsync(0x0026, 0x0002, lambda_5509)

    @scena.Lambda('lambda_5519')
    def lambda_5519():
        OP_99(0x00FE, 0x00, 0x07, 1500)

        ExitThread()

    DispatchAsync(0x0027, 0x0002, lambda_5519)

    @scena.Lambda('lambda_5529')
    def lambda_5529():
        OP_99(0x00FE, 0x00, 0x07, 1500)

        ExitThread()

    DispatchAsync(0x0028, 0x0002, lambda_5529)

    Sleep(400)

    PlaySE(213, 0x00, 0x64)
    WaitForThreadExit(0x0023, 0x0002)
    Sleep(400)

    @scena.Lambda('lambda_554D')
    def lambda_554D():
        CameraMove(5440, -370, 1710, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_554D)

    @scena.Lambda('lambda_5565')
    def lambda_5565():
        CameraSetDistance(1400, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5565)

    CreateThread(0x0008, 0x00, 0x00, func_0D_2712)
    ChrSetSubChip(0x0023, 8)
    ChrSetSubChip(0x0024, 8)
    ChrSetSubChip(0x0025, 8)
    ChrSetSubChip(0x0026, 8)
    ChrSetSubChip(0x0027, 8)
    ChrSetSubChip(0x0028, 8)

    @scena.Lambda('lambda_559A')
    def lambda_559A():
        ChrMoveTo(0x00FE, 4740, -370, 1700, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_559A)

    @scena.Lambda('lambda_55B5')
    def lambda_55B5():
        ChrMoveTo(0x00FE, 4740, -370, 1700, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_55B5)

    @scena.Lambda('lambda_55D0')
    def lambda_55D0():
        ChrMoveTo(0x00FE, 4740, -370, 1700, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_55D0)

    @scena.Lambda('lambda_55EB')
    def lambda_55EB():
        ChrMoveTo(0x00FE, 4740, -370, 1700, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0026, 0x0001, lambda_55EB)

    @scena.Lambda('lambda_5606')
    def lambda_5606():
        ChrMoveTo(0x00FE, 4740, -370, 1700, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0027, 0x0001, lambda_5606)

    @scena.Lambda('lambda_5621')
    def lambda_5621():
        ChrMoveTo(0x00FE, 4740, -370, 1700, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_5621)

    Sleep(200)

    OP_7C(0, 400, 3000, 200)
    TerminateThread(0x0023, 0x01)
    TerminateThread(0x0024, 0x01)
    TerminateThread(0x0025, 0x01)
    TerminateThread(0x0026, 0x01)
    TerminateThread(0x0027, 0x01)
    TerminateThread(0x0028, 0x01)
    ChrSetChipByIndex(0x0023, 11)
    ChrSetSubChip(0x0023, 0)
    ChrSetChipByIndex(0x0024, 11)
    ChrSetSubChip(0x0024, 0)
    ChrSetChipByIndex(0x0025, 11)
    ChrSetSubChip(0x0025, 0)
    ChrSetChipByIndex(0x0026, 11)
    ChrSetSubChip(0x0026, 0)
    ChrSetChipByIndex(0x0027, 11)
    ChrSetSubChip(0x0027, 0)
    ChrSetChipByIndex(0x0028, 11)
    ChrSetSubChip(0x0028, 0)
    PlayEffect(0x03, 0xFF, 0x0023, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0xFF, 0x0024, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0xFF, 0x0025, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0xFF, 0x0026, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0xFF, 0x0027, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0xFF, 0x0028, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_57E4')
    def lambda_57E4():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00003A98, 0x00)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_57E4)

    @scena.Lambda('lambda_57FA')
    def lambda_57FA():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00003A98, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_57FA)

    @scena.Lambda('lambda_5810')
    def lambda_5810():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00003A98, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_5810)

    @scena.Lambda('lambda_5826')
    def lambda_5826():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00003A98, 0x00)

        ExitThread()

    DispatchAsync(0x0026, 0x0001, lambda_5826)

    @scena.Lambda('lambda_583C')
    def lambda_583C():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00003A98, 0x00)

        ExitThread()

    DispatchAsync(0x0027, 0x0001, lambda_583C)

    @scena.Lambda('lambda_5852')
    def lambda_5852():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00003A98, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_5852)

    @scena.Lambda('lambda_5868')
    def lambda_5868():
        OP_9E(0x00FE, 60, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0023, 0x0002, lambda_5868)

    @scena.Lambda('lambda_5882')
    def lambda_5882():
        OP_9E(0x00FE, 60, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0024, 0x0002, lambda_5882)

    @scena.Lambda('lambda_589C')
    def lambda_589C():
        OP_9E(0x00FE, 60, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0025, 0x0002, lambda_589C)

    @scena.Lambda('lambda_58B6')
    def lambda_58B6():
        OP_9E(0x00FE, 60, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0026, 0x0002, lambda_58B6)

    @scena.Lambda('lambda_58D0')
    def lambda_58D0():
        OP_9E(0x00FE, 60, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0027, 0x0002, lambda_58D0)

    @scena.Lambda('lambda_58EA')
    def lambda_58EA():
        OP_9E(0x00FE, 60, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0028, 0x0002, lambda_58EA)

    Sleep(1000)

    @scena.Lambda('lambda_5909')
    def lambda_5909():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0023, 0x0003, lambda_5909)

    @scena.Lambda('lambda_591B')
    def lambda_591B():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0024, 0x0003, lambda_591B)

    @scena.Lambda('lambda_592D')
    def lambda_592D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0025, 0x0003, lambda_592D)

    @scena.Lambda('lambda_593F')
    def lambda_593F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0026, 0x0003, lambda_593F)

    @scena.Lambda('lambda_5951')
    def lambda_5951():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0027, 0x0003, lambda_5951)

    @scena.Lambda('lambda_5963')
    def lambda_5963():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0028, 0x0003, lambda_5963)

    WaitForThreadExit(0x0023, 0x0003)
    ChrSetFlags(0x0023, 0x0080)
    ChrSetFlags(0x0024, 0x0080)
    ChrSetFlags(0x0025, 0x0080)
    ChrSetFlags(0x0026, 0x0080)
    ChrSetFlags(0x0027, 0x0080)
    ChrSetFlags(0x0028, 0x0080)

    @scena.Lambda('lambda_5998')
    def lambda_5998():
        CameraMove(6570, -370, 680, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5998)

    @scena.Lambda('lambda_59B0')
    def lambda_59B0():
        OP_67(0, 3340, -10000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_59B0)

    @scena.Lambda('lambda_59C8')
    def lambda_59C8():
        CameraSetDistance(1720, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_59C8)

    @scena.Lambda('lambda_59D8')
    def lambda_59D8():
        OP_6C(124000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_59D8)

    ChrSetPos(0x0022, 8900, 0, -4070, 320)
    ChrSetRGBAMask(0x0022, 255, 255, 255, 0, 0)
    ChrSetChipByIndex(0x0022, 9)
    ChrSetSubChip(0x0022, 4)
    ChrClearFlags(0x0022, 0x0008)
    ChrSetAfterImage(0x00, 0x0022, 0x0014, 0x00C8)

    @scena.Lambda('lambda_5A1B')
    def lambda_5A1B():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_5A1B)

    @scena.Lambda('lambda_5A2D')
    def lambda_5A2D():
        ChrMoveTo(0x00FE, 3040, -370, 4100, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_5A2D)

    Sleep(200)

    @scena.Lambda('lambda_5A4D')
    def lambda_5A4D():
        OP_99(0x00FE, 0x04, 0x08, 1500)

        ExitThread()

    DispatchAsync(0x0022, 0x0003, lambda_5A4D)

    PlaySE(132, 0x00, 0x64)
    ChrSetChipByIndex(0x0008, 7)
    ChrSetSubChip(0x0008, 2)
    ChrSetDirection(0x0008, 260, 0)

    @scena.Lambda('lambda_5A73')
    def lambda_5A73():
        ChrJumpTo(0x00FE, 7860, 0, 3630, 500, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_5A73)

    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetChipByIndex(0x0008, 18)
    ChrSetSubChip(0x0008, 0)
    Sleep(100)

    ChrSetChipByIndex(0x0008, 29)
    ChrSetSubChip(0x0008, 2)

    @scena.Lambda('lambda_5AB4')
    def lambda_5AB4():
        OP_99(0x00FE, 0x02, 0x06, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_5AB4)

    @scena.Lambda('lambda_5AC4')
    def lambda_5AC4():
        ChrJumpTo(0x00FE, 3710, -370, 4140, 500, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_5AC4)

    Sleep(250)

    @scena.Lambda('lambda_5AE7')
    def lambda_5AE7():
        CameraMove(4240, -370, 2140, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5AE7)

    TerminateThread(0x0022, 0x03)
    ChrSetChipByIndex(0x0022, 4)
    ChrSetSubChip(0x0022, 0)
    ChrSetDirection(0x0022, 80, 0)

    @scena.Lambda('lambda_5B14')
    def lambda_5B14():
        OP_9E(0x00FE, 40, 0, 500, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_5B14)

    @scena.Lambda('lambda_5B2E')
    def lambda_5B2E():
        ChrMoveTo(0x00FE, -1250, -370, 3990, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_5B2E)

    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x0022, 1000, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 400, 3000, 200)
    WaitForThreadExit(0x0022, 0x0002)
    ChrSetAfterImage(0x01, 0x0022, 0x0000, 0x0000)

    @scena.Lambda('lambda_5BA1')
    def lambda_5BA1():
        CameraMove(-10360, -370, 640, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5BA1)

    @scena.Lambda('lambda_5BB9')
    def lambda_5BB9():
        OP_6C(229000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5BB9)

    @scena.Lambda('lambda_5BC9')
    def lambda_5BC9():
        OP_67(0, 4920, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5BC9)

    ChrSetChipByIndex(0x0022, 10)
    ChrSetSubChip(0x0022, 0)

    @scena.Lambda('lambda_5BEB')
    def lambda_5BEB():
        ChrJumpTo(0x00FE, -6570, 0, 3020, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_5BEB)

    WaitForThreadExit(0x0022, 0x0001)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_5C13')
    def lambda_5C13():
        ChrJumpTo(0x00FE, -10500, 0, 2630, 500, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_5C13)

    WaitForThreadExit(0x0022, 0x0001)
    PlaySE(164, 0x00, 0x64)
    Fade(100)
    CameraSetDistance(1620, 0)
    ChrSetPos(0x0008, 3780, -370, 2540, 260)
    ChrSetChipByIndex(0x0008, 28)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0022, 12)
    ChrSetSubChip(0x0022, 0)
    OP_0D()
    Sleep(200)

    ChrSetSubChip(0x0022, 1)
    CreateThread(0x0022, 0x00, 0x00, func_0E_277C)
    CreateThread(0x0008, 0x00, 0x00, func_0F_289C)
    WaitForThreadExit(0x0008, 0x0000)
    WaitEffect(0x01, 0x02)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)

    @scena.Lambda('lambda_5C99')
    def lambda_5C99():
        CameraMove(-9650, -370, 2680, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5C99)

    @scena.Lambda('lambda_5CB1')
    def lambda_5CB1():
        OP_6C(105000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5CB1)

    @scena.Lambda('lambda_5CC1')
    def lambda_5CC1():
        OP_67(0, 6160, -10000, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5CC1)

    WaitForThreadExit(0x0101, 0x0002)

    @scena.Lambda('lambda_5CDE')
    def lambda_5CDE():
        OP_67(0, 5320, -10000, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5CDE)

    ChrSetChipByIndex(0x0022, 8)
    ChrSetSubChip(0x0022, 0)
    ChrSetRGBAMask(0x0022, 255, 255, 255, 0, 0)
    ChrSetPos(0x0022, -11360, 0, 4430, 130)
    ChrSetChipByIndex(0x0023, 8)
    ChrSetSubChip(0x0023, 0)
    ChrClearFlags(0x0023, 0x0080)
    ChrSetFlags(0x0023, 0x0001)
    ChrSetRGBAMask(0x0023, 255, 255, 255, 0, 0)
    ChrSetPos(0x0023, -12050, 0, 1860, 70)

    @scena.Lambda('lambda_5D4C')
    def lambda_5D4C():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 200, 1000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_5D4C)

    @scena.Lambda('lambda_5D5E')
    def lambda_5D5E():
        ChrMoveTo(0x00FE, -13100, 0, 6160, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_5D5E)

    @scena.Lambda('lambda_5D79')
    def lambda_5D79():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 200, 1000)

        ExitThread()

    DispatchAsync(0x0023, 0x0002, lambda_5D79)

    @scena.Lambda('lambda_5D8B')
    def lambda_5D8B():
        ChrMoveTo(0x00FE, -14220, 0, 1260, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_5D8B)

    Sleep(200)

    @scena.Lambda('lambda_5DAB')
    def lambda_5DAB():
        OP_99(0x00FE, 0x00, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x0022, 0x0003, lambda_5DAB)

    @scena.Lambda('lambda_5DBB')
    def lambda_5DBB():
        OP_99(0x00FE, 0x00, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x0023, 0x0003, lambda_5DBB)

    WaitForThreadExit(0x0022, 0x0003)
    Sleep(100)

    ChrSetSubChip(0x0022, 8)

    @scena.Lambda('lambda_5DDA')
    def lambda_5DDA():
        ChrMoveTo(0x00FE, -4180, -370, -2460, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_5DDA)

    ChrSetSubChip(0x0023, 8)

    @scena.Lambda('lambda_5DFA')
    def lambda_5DFA():
        ChrMoveTo(0x00FE, -2150, -370, 4440, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_5DFA)

    Fade(250)
    CameraMove(-13770, -370, 3660, 0)
    OP_67(0, 4920, -10000, 0)
    CameraSetDistance(1550, 0)
    OP_6C(285000, 0)
    OP_6E(465, 0)

    @scena.Lambda('lambda_5E57')
    def lambda_5E57():
        CameraMove(-7780, -370, 2060, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5E57)

    @scena.Lambda('lambda_5E6F')
    def lambda_5E6F():
        CameraSetDistance(1970, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5E6F)

    @scena.Lambda('lambda_5E7F')
    def lambda_5E7F():
        OP_67(0, 3810, -10000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5E7F)

    ChrClearFlags(0x0008, 0x0800)
    TerminateThread(0x0022, 0x01)
    TerminateThread(0x0023, 0x01)
    ChrSetPos(0x0022, -13100, 0, 6160, 130)
    ChrSetPos(0x0023, -14220, 0, 1260, 70)
    ChrSetAfterImage(0x00, 0x0022, 0x0014, 0x00C8)

    @scena.Lambda('lambda_5ECE')
    def lambda_5ECE():
        ChrMoveTo(0x00FE, -4180, -370, -2460, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_5ECE)

    ChrSetAfterImage(0x00, 0x0023, 0x0014, 0x00C8)

    @scena.Lambda('lambda_5EF1')
    def lambda_5EF1():
        ChrMoveTo(0x00FE, -2150, -370, 4440, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_5EF1)

    OP_7C(0, 400, 3000, 200)
    PlayEffect(0x01, 0xFF, 0x0008, -1000, 500, 500, 0, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x04, 0x01, 0x0008, -1000, 500, 500, 0, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x04, 0x02, 0x0008, -1000, 500, 500, 0, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)
    ChrSetChipByIndex(0x0008, 13)
    ChrSetSubChip(0x0008, 1)

    @scena.Lambda('lambda_5FC6')
    def lambda_5FC6():
        OP_9E(0x00FE, 60, 0, 800, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_5FC6)

    @scena.Lambda('lambda_5FE0')
    def lambda_5FE0():
        ChrMoveTo(0x00FE, -8700, 0, 2320, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_5FE0)

    WaitForThreadExit(0x0022, 0x0001)

    @scena.Lambda('lambda_6000')
    def lambda_6000():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0023, 0x0002, lambda_6000)

    Sleep(600)

    @scena.Lambda('lambda_6017')
    def lambda_6017():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 200)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_6017)

    Sleep(200)

    @scena.Lambda('lambda_602E')
    def lambda_602E():
        CameraMove(-6710, -370, -1870, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_602E)

    @scena.Lambda('lambda_6046')
    def lambda_6046():
        OP_6C(181000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6046)

    @scena.Lambda('lambda_6056')
    def lambda_6056():
        ChrSetDirection(0x00FE, 136, 200)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_6056)

    ChrSetDirection(0x0022, 316, 0)
    ChrSetChipByIndex(0x0022, 10)
    ChrSetSubChip(0x0022, 2)

    @scena.Lambda('lambda_6075')
    def lambda_6075():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1100)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_6075)

    @scena.Lambda('lambda_6087')
    def lambda_6087():
        ChrJumpTo(0x00FE, -5560, -280, 1730, 500, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_6087)

    WaitForThreadExit(0x0022, 0x0001)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_60AF')
    def lambda_60AF():
        ChrJumpTo(0x00FE, -7180, 0, -1930, 500, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_60AF)

    WaitForThreadExit(0x0022, 0x0001)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_60D7')
    def lambda_60D7():
        ChrJumpTo(0x00FE, -8700, 0, 2320, 500, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_60D7)

    WaitForThreadExit(0x0022, 0x0001)
    TerminateThread(0x0022, 0x02)
    ChrSetAfterImage(0x01, 0x0022, 0x0000, 0x0000)

    @scena.Lambda('lambda_6106')
    def lambda_6106():
        CameraMove(-8630, -370, -260, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_6106)

    @scena.Lambda('lambda_611E')
    def lambda_611E():
        OP_6C(193000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_611E)

    @scena.Lambda('lambda_612E')
    def lambda_612E():
        OP_D0(365000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_612E)

    ChrSetPos(0x0022, -13560, 0, 6720, 130)
    ChrSetRGBAMask(0x0022, 255, 255, 255, 255, 0)
    ChrSetChipByIndex(0x0022, 8)
    ChrSetSubChip(0x0022, 8)

    @scena.Lambda('lambda_6164')
    def lambda_6164():
        ChrMoveTo(0x00FE, -2810, -370, -3100, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_6164)

    Sleep(150)

    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x0008, -500, 500, -500, 0, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 400, 3000, 200)
    ChrSetChipByIndex(0x0008, 13)
    ChrSetSubChip(0x0008, 1)
    ChrSetDirection(0x0008, 226, 0)

    @scena.Lambda('lambda_61E0')
    def lambda_61E0():
        OP_9E(0x00FE, 40, 0, 500, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_61E0)

    @scena.Lambda('lambda_61FA')
    def lambda_61FA():
        ChrJumpTo(0x00FE, -7480, 0, 3920, 500, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_61FA)

    Sleep(350)

    @scena.Lambda('lambda_621D')
    def lambda_621D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 100)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_621D)

    WaitForThreadExit(0x0022, 0x0002)

    @scena.Lambda('lambda_6234')
    def lambda_6234():
        CameraMove(-7650, -370, 1910, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_6234)

    @scena.Lambda('lambda_624C')
    def lambda_624C():
        OP_6C(166000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_624C)

    @scena.Lambda('lambda_625C')
    def lambda_625C():
        OP_D0(355000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_625C)

    ChrSetPos(0x0022, -3170, 0, 8420, 225)
    ChrSetRGBAMask(0x0022, 255, 255, 255, 255, 0)

    @scena.Lambda('lambda_6288')
    def lambda_6288():
        ChrMoveTo(0x00FE, -13240, 0, -2000, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_6288)

    Sleep(150)

    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x0008, 500, 500, -500, 0, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 400, 3000, 200)
    ChrSetChipByIndex(0x0008, 30)
    ChrSetSubChip(0x0008, 3)
    ChrSetDirection(0x0008, 30, 0)

    @scena.Lambda('lambda_6304')
    def lambda_6304():
        OP_9E(0x00FE, 40, 0, 500, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_6304)

    @scena.Lambda('lambda_631E')
    def lambda_631E():
        ChrJumpTo(0x00FE, -8570, 0, 5550, 500, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_631E)

    Sleep(350)

    @scena.Lambda('lambda_6341')
    def lambda_6341():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 100)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_6341)

    WaitForThreadExit(0x0022, 0x0002)

    @scena.Lambda('lambda_6358')
    def lambda_6358():
        CameraMove(-7890, -370, 2870, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_6358)

    @scena.Lambda('lambda_6370')
    def lambda_6370():
        CameraSetDistance(1510, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6370)

    @scena.Lambda('lambda_6380')
    def lambda_6380():
        OP_D0(365000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6380)

    CreateThread(0x0008, 0x00, 0x00, func_10_2AE4)
    ChrSetFlags(0x0022, 0x0004)
    ChrSetPos(0x0022, 1380, 0, -420, 300)
    ChrSetRGBAMask(0x0022, 255, 255, 255, 255, 0)

    @scena.Lambda('lambda_63B8')
    def lambda_63B8():
        ChrMoveTo(0x00FE, -13600, 0, 9000, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_63B8)

    Sleep(370)

    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x0008, 800, 500, -500, 0, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 400, 3000, 200)
    TerminateThread(0x0022, 0x01)
    ChrSetChipByIndex(0x0022, 11)
    ChrSetSubChip(0x0022, 0)
    ChrClearFlags(0x0022, 0x0004)

    @scena.Lambda('lambda_6436')
    def lambda_6436():
        OP_9E(0x00FE, 40, 0, 500, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_6436)

    @scena.Lambda('lambda_6450')
    def lambda_6450():
        ChrJumpTo(0x00FE, -2890, -370, 1730, 500, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_6450)

    WaitForThreadExit(0x0022, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetChipByIndex(0x0022, 4)
    ChrSetSubChip(0x0022, 3)
    Sleep(100)

    ChrSetChipByIndex(0x0008, 29)
    ChrSetSubChip(0x0008, 2)

    @scena.Lambda('lambda_6491')
    def lambda_6491():
        ChrJumpTo(0x00FE, -3800, -370, 2370, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_6491)

    Sleep(200)

    Fade(100)
    CameraMove(-6020, 0, 3310, 0)
    OP_67(0, 3810, -10000, 0)
    CameraSetDistance(1510, 0)
    OP_6C(295000, 0)
    OP_6E(465, 0)
    OP_D0(360000, 0)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, -7480, 1000, 3920, 110)

    @scena.Lambda('lambda_6515')
    def lambda_6515():
        ChrJumpTo(0x00FE, -3800, -370, 2370, 200, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_6515)

    @scena.Lambda('lambda_6533')
    def lambda_6533():
        OP_99(0x00FE, 0x02, 0x06, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_6533)

    Sleep(250)

    @scena.Lambda('lambda_6548')
    def lambda_6548():
        CameraMove(-4059, 0, 2400, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_6548)

    @scena.Lambda('lambda_6560')
    def lambda_6560():
        CameraSetDistance(1940, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6560)

    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x0008, 500, 0, -500, 0, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 400, 3000, 200)
    ChrSetChipByIndex(0x0022, 14)
    ChrSetSubChip(0x0022, 0)

    @scena.Lambda('lambda_65C5')
    def lambda_65C5():
        OP_9E(0x00FE, 40, 0, 500, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_65C5)

    @scena.Lambda('lambda_65DF')
    def lambda_65DF():
        ChrMoveTo(0x00FE, 120, -370, 0, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_65DF)

    Sleep(100)

    ChrSetChipByIndex(0x0022, 4)
    ChrSetSubChip(0x0022, 0)

    @scena.Lambda('lambda_6609')
    def lambda_6609():
        OP_99(0x00FE, 0x00, 0x01, 1000)

        ExitThread()

    DispatchAsync(0x0022, 0x0003, lambda_6609)

    Sleep(400)

    @scena.Lambda('lambda_661E')
    def lambda_661E():
        CameraMove(-2810, -370, -620, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_661E)

    @scena.Lambda('lambda_6636')
    def lambda_6636():
        OP_6C(305000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6636)

    CreateThread(0x0008, 0x00, 0x00, func_11_2B2A)
    ChrSetAfterImage(0x00, 0x0022, 0x0014, 0x00C8)
    ChrSetChipByIndex(0x0022, 10)
    ChrSetSubChip(0x0022, 0)

    @scena.Lambda('lambda_665F')
    def lambda_665F():
        ChrSetDirection(0x00FE, 0, 200)

        ExitThread()

    DispatchAsync(0x0022, 0x0003, lambda_665F)

    @scena.Lambda('lambda_666D')
    def lambda_666D():
        ChrJumpTo(0x00FE, 0, -370, -4680, 500, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_666D)

    WaitForThreadExit(0x0022, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetAfterImage(0x01, 0x0022, 0x0000, 0x0000)
    ChrSetChipByIndex(0x0022, 6)
    ChrSetSubChip(0x0022, 5)
    Sleep(200)

    @scena.Lambda('lambda_66AC')
    def lambda_66AC():
        CameraMove(-760, -130, 5790, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_66AC)

    @scena.Lambda('lambda_66C4')
    def lambda_66C4():
        OP_67(0, 3000, -10000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_66C4)

    @scena.Lambda('lambda_66DC')
    def lambda_66DC():
        OP_6C(335000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_66DC)

    @scena.Lambda('lambda_66EC')
    def lambda_66EC():
        CameraSetDistance(2260, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_66EC)

    @scena.Lambda('lambda_66FC')
    def lambda_66FC():
        ChrMoveTo(0x00FE, 140, -370, -980, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_66FC)

    Sleep(50)

    @scena.Lambda('lambda_671C')
    def lambda_671C():
        OP_99(0x00FE, 0x05, 0x07, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_671C)

    Sleep(50)

    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x0008, 0, 500, -1000, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 400, 3000, 200)
    ChrSetChipByIndex(0x0008, 30)
    ChrSetSubChip(0x0008, 2)
    ChrSetDirection(0x0008, 180, 0)

    @scena.Lambda('lambda_678D')
    def lambda_678D():
        OP_9E(0x00FE, 40, 0, 500, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_678D)

    @scena.Lambda('lambda_67A7')
    def lambda_67A7():
        ChrJumpTo(0x00FE, 0, -370, 4660, 500, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_67A7)

    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetChipByIndex(0x0008, 7)
    ChrSetSubChip(0x0008, 6)

    @scena.Lambda('lambda_67D9')
    def lambda_67D9():
        ChrJumpTo(0x00FE, 0, 0, 8720, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_67D9)

    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 19)
    ChrSetSubChip(0x0008, 0)
    ChrClearFlags(0x0008, 0x0100)
    OP_D1(0x0008, 4000, -25000, 0, 0)

    ExecExpressionWithValue(
        0x0008,
        0x2D,
        (
            (Expr.PushLong, 0x30C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x2E,
        (
            (Expr.PushLong, 0x30C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x2F,
        (
            (Expr.PushLong, 0x30C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0022, 0x0002)
    ChrSetSubChip(0x0022, 59)

    @scena.Lambda('lambda_6853')
    def lambda_6853():
        CameraSetDistance(2060, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_6853)

    Sleep(1000)

    OP_DC()

    ChrTalk(
        0x0008,
        (
            '#0140410897V#124F#5P呵呵……很不错嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410898V#123F……那么我也要\n',
            '施展全力了哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0020410899V#1042F#3P#3S！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_DB()

    @scena.Lambda('lambda_68EA')
    def lambda_68EA():
        CameraMove(0, 240, 11440, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_68EA)

    @scena.Lambda('lambda_6902')
    def lambda_6902():
        OP_67(0, 2000, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6902)

    @scena.Lambda('lambda_691A')
    def lambda_691A():
        OP_6C(0, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_691A)

    @scena.Lambda('lambda_692A')
    def lambda_692A():
        CameraSetDistance(1460, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_692A)

    @scena.Lambda('lambda_693A')
    def lambda_693A():
        OP_D1(0x00FE, 8000, 0, 0, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_693A)

    @scena.Lambda('lambda_6954')
    def lambda_6954():
        OP_99(0x00FE, 0x00, 0x0B, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_6954)

    WaitForThreadExit(0x0008, 0x0002)

    @scena.Lambda('lambda_6969')
    def lambda_6969():
        OP_99(0x00FE, 0x11, 0x14, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_6969)

    WaitForThreadExit(0x0008, 0x0002)
    PlaySE(213, 0x00, 0x64)
    WaitForThreadExit(0x0101, 0x0000)
    ChrClearFlags(0x0022, 0x0002)
    ChrSetChipByIndex(0x0022, 9)
    ChrSetSubChip(0x0022, 0)
    ChrSetPos(0x0022, 0, -370, -980, 0)
    Sleep(500)

    PlayEffect(0x05, 0x01, 0x0008, 0, -200, 0, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 20, 3000, 200)
    Sleep(200)

    OP_7C(0, 40, 3000, 200)
    Sleep(200)

    OP_7C(0, 80, 3000, 200)
    Sleep(200)

    OP_7C(0, 140, 3000, 200)
    Sleep(200)

    OP_7C(0, 200, 3000, 5000)

    @scena.Lambda('lambda_6A4B')
    def lambda_6A4B():
        CameraMove(0, -800, 4140, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_6A4B)

    @scena.Lambda('lambda_6A63')
    def lambda_6A63():
        OP_67(0, 4680, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6A63)

    @scena.Lambda('lambda_6A7B')
    def lambda_6A7B():
        CameraSetDistance(860, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6A7B)

    @scena.Lambda('lambda_6A8B')
    def lambda_6A8B():
        OP_6E(1058, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_6A8B)

    Sleep(5000)

    StopEffect(0x01, 0x02)
    Sleep(2500)

    @scena.Lambda('lambda_6AA8')
    def lambda_6AA8():
        CameraMove(-400, -800, 3140, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_6AA8)

    @scena.Lambda('lambda_6AC0')
    def lambda_6AC0():
        OP_6C(332000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6AC0)

    @scena.Lambda('lambda_6AD0')
    def lambda_6AD0():
        CameraSetDistance(1020, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6AD0)

    @scena.Lambda('lambda_6AE0')
    def lambda_6AE0():
        OP_6E(706, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_6AE0)

    ChrSetFlags(0x0008, 0x0100)

    ExecExpressionWithValue(
        0x0008,
        0x2D,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x2E,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x2F,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 30)
    ChrSetSubChip(0x0008, 11)

    @scena.Lambda('lambda_6B25')
    def lambda_6B25():
        ChrMoveTo(0x00FE, 0, -370, -980, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_6B25)

    @scena.Lambda('lambda_6B40')
    def lambda_6B40():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_6B40)

    WaitForThreadExit(0x0008, 0x0002)
    TerminateThread(0x0008, 0x01)
    ChrSetPos(0x0008, 0, -370, 3200, 180)

    @scena.Lambda('lambda_6B6C')
    def lambda_6B6C():
        ChrMoveTo(0x00FE, 800, -370, -200, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_6B6C)

    @scena.Lambda('lambda_6B87')
    def lambda_6B87():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 100)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_6B87)

    @scena.Lambda('lambda_6B99')
    def lambda_6B99():
        OP_99(0x00FE, 0x0B, 0x0C, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_6B99)

    WaitForThreadExit(0x0008, 0x0003)
    PlaySE(155, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x0008, 0, 500, -1000, 0, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x04, 0x01, 0x0008, 0, 500, -2000, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 400, 3000, 200)
    ChrSetChipByIndex(0x0008, 31)
    ChrSetSubChip(0x0008, 4)

    @scena.Lambda('lambda_6C38')
    def lambda_6C38():
        OP_99(0x00FE, 0x04, 0x05, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_6C38)

    ChrSetChipByIndex(0x0022, 4)
    ChrSetSubChip(0x0022, 0)

    @scena.Lambda('lambda_6C52')
    def lambda_6C52():
        OP_99(0x00FE, 0x00, 0x03, 500)

        ExitThread()

    DispatchAsync(0x0022, 0x0003, lambda_6C52)

    @scena.Lambda('lambda_6C62')
    def lambda_6C62():
        OP_9E(0x00FE, 0, 60, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_6C62)

    @scena.Lambda('lambda_6C7C')
    def lambda_6C7C():
        ChrJumpTo(0x00FE, 0, 0, -8680, 1800, 1000)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_6C7C)

    Sleep(400)

    TerminateThread(0x0008, 0x01)

    @scena.Lambda('lambda_6CA3')
    def lambda_6CA3():
        CameraMove(-1460, -800, -5780, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_6CA3)

    @scena.Lambda('lambda_6CBB')
    def lambda_6CBB():
        OP_6C(220000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6CBB)

    @scena.Lambda('lambda_6CCB')
    def lambda_6CCB():
        CameraSetDistance(1400, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6CCB)

    @scena.Lambda('lambda_6CDB')
    def lambda_6CDB():
        OP_6E(558, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_6CDB)

    @scena.Lambda('lambda_6CEB')
    def lambda_6CEB():
        OP_67(0, 6520, -10000, 400)

        ExitThread()

    DispatchAsync(0x0023, 0x0000, lambda_6CEB)

    ChrSetAfterImage(0x00, 0x0008, 0x000A, 0x0064)
    ChrSetChipByIndex(0x0008, 30)
    ChrSetSubChip(0x0008, 11)

    @scena.Lambda('lambda_6D15')
    def lambda_6D15():
        ChrJumpTo(0x00FE, -4220, -370, -3980, 600, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_6D15)

    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_6D3D')
    def lambda_6D3D():
        ChrSetDirection(0x00FE, 0, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_6D3D)

    @scena.Lambda('lambda_6D4B')
    def lambda_6D4B():
        ChrJumpTo(0x00FE, 0, 0, -10100, 900, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_6D4B)

    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(164, 0x00, 0x64)
    Sleep(100)

    ChrSetAfterImage(0x01, 0x0008, 0x0000, 0x0000)
    ChrSetChipByIndex(0x0008, 2)
    ChrSetSubChip(0x0008, 1)

    @scena.Lambda('lambda_6D8A')
    def lambda_6D8A():
        ChrMoveTo(0x00FE, 0, 0, -8680, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_6D8A)

    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x0008, 0, 500, 1000, 0, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 400, 3000, 200)
    CreateThread(0x0022, 0x00, 0x00, func_13_2BB5)

    @scena.Lambda('lambda_6DF7')
    def lambda_6DF7():
        CameraMove(-1940, -800, -2440, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_6DF7)

    @scena.Lambda('lambda_6E0F')
    def lambda_6E0F():
        OP_67(0, 4019, -10000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6E0F)

    @scena.Lambda('lambda_6E27')
    def lambda_6E27():
        OP_6C(322000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6E27)

    @scena.Lambda('lambda_6E37')
    def lambda_6E37():
        CameraSetDistance(1520, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_6E37)

    Sleep(400)

    ChrSetChipByIndex(0x0008, 30)
    ChrSetSubChip(0x0008, 11)
    ChrSetAfterImage(0x00, 0x0008, 0x0014, 0x00C8)

    @scena.Lambda('lambda_6E5E')
    def lambda_6E5E():
        ChrJumpTo(0x00FE, 0, -370, -3790, 100, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_6E5E)

    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_6E86')
    def lambda_6E86():
        ChrJumpTo(0x00FE, -3480, -370, -2220, 200, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_6E86)

    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetDirection(0x0008, 50, 0)

    @scena.Lambda('lambda_6EB5')
    def lambda_6EB5():
        ChrJumpTo(0x00FE, 610, -370, -10, 200, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_6EB5)

    @scena.Lambda('lambda_6ED3')
    def lambda_6ED3():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_6ED3)

    WaitForThreadExit(0x0008, 0x0002)
    TerminateThread(0x0008, 0x01)
    ChrSetAfterImage(0x01, 0x0008, 0x0000, 0x0000)

    @scena.Lambda('lambda_6EF6')
    def lambda_6EF6():
        CameraMove(-320, -800, 1400, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_6EF6)

    ChrSetPos(0x0008, 8340, 0, -1220, 235)
    ChrSetRGBAMask(0x0008, 255, 255, 255, 255, 0)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetChipByIndex(0x0008, 31)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_6F39')
    def lambda_6F39():
        ChrJumpTo(0x00FE, 1300, -370, 360, 400, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_6F39)

    Sleep(250)

    @scena.Lambda('lambda_6F5C')
    def lambda_6F5C():
        OP_99(0x00FE, 0x00, 0x04, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_6F5C)

    Sleep(200)

    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x0008, -2000, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 400, 3000, 200)
    ChrSetDirection(0x0022, 80, 0)

    @scena.Lambda('lambda_6FC3')
    def lambda_6FC3():
        OP_9E(0x00FE, 40, 0, 500, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_6FC3)

    @scena.Lambda('lambda_6FDD')
    def lambda_6FDD():
        ChrJumpTo(0x00FE, -8440, -370, -3160, 2000, 1000)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_6FDD)

    Sleep(400)

    @scena.Lambda('lambda_7000')
    def lambda_7000():
        CameraMove(-7590, 0, -1460, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_7000)

    @scena.Lambda('lambda_7018')
    def lambda_7018():
        OP_67(0, 2480, -10000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7018)

    @scena.Lambda('lambda_7030')
    def lambda_7030():
        OP_6C(304000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7030)

    PlaySE(164, 0x00, 0x64)
    ChrSetDirection(0x0008, 260, 0)
    ChrSetChipByIndex(0x0008, 29)
    ChrSetSubChip(0x0008, 3)

    @scena.Lambda('lambda_7056')
    def lambda_7056():
        ChrJumpTo(0x00FE, -8440, -370, -3060, 2000, 4500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_7056)

    Sleep(200)

    @scena.Lambda('lambda_7079')
    def lambda_7079():
        OP_99(0x00FE, 0x03, 0x06, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_7079)

    Sleep(100)

    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x0022, 1000, 500, 200, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 400, 3000, 200)
    TerminateThread(0x0022, 0x01)
    ChrSetChipByIndex(0x0022, 11)
    ChrSetSubChip(0x0022, 0)

    @scena.Lambda('lambda_70E7')
    def lambda_70E7():
        ChrMoveTo(0x00FE, -7440, 0, -1970, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_70E7)

    @scena.Lambda('lambda_7102')
    def lambda_7102():
        OP_9E(0x00FE, 60, 0, 500, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_7102)

    TerminateThread(0x0008, 0x01)

    @scena.Lambda('lambda_7120')
    def lambda_7120():
        ChrMoveTo(0x00FE, -4680, -370, -1490, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_7120)

    WaitForThreadExit(0x0022, 0x0001)
    PlaySE(521, 0x00, 0x64)
    ChrSetChipByIndex(0x0022, 4)
    ChrSetSubChip(0x0022, 3)
    Sleep(100)

    ChrSetChipByIndex(0x0022, 10)
    ChrSetSubChip(0x0022, 2)

    @scena.Lambda('lambda_715E')
    def lambda_715E():
        ChrJumpTo(0x00FE, -11350, 0, -3240, 500, 4000)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_715E)

    WaitForThreadExit(0x0022, 0x0001)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_7186')
    def lambda_7186():
        OP_9E(0x00FE, 40, 0, 500, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_7186)

    ChrSetChipByIndex(0x0022, 4)
    ChrSetSubChip(0x0022, 3)
    WaitForThreadExit(0x0022, 0x0002)

    @scena.Lambda('lambda_71AF')
    def lambda_71AF():
        CameraMove(-6430, 0, -690, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_71AF)

    @scena.Lambda('lambda_71C7')
    def lambda_71C7():
        OP_67(0, 3590, -10000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_71C7)

    @scena.Lambda('lambda_71DF')
    def lambda_71DF():
        OP_6C(304000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_71DF)

    @scena.Lambda('lambda_71EF')
    def lambda_71EF():
        CameraSetDistance(1110, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_71EF)

    ChrSetFlags(0x0022, 0x0002)
    ChrClearFlags(0x0022, 0x0004)
    ChrSetChipByIndex(0x0022, 3)
    ChrSetSubChip(0x0022, 16)

    @scena.Lambda('lambda_7213')
    def lambda_7213():
        ChrMoveTo(0x00FE, -5850, -170, -1690, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_7213)

    @scena.Lambda('lambda_722E')
    def lambda_722E():
        OP_99(0x00FE, 0x10, 0x12, 1500)

        ExitThread()

    DispatchAsync(0x0022, 0x0003, lambda_722E)

    Sleep(200)

    PlaySE(132, 0x00, 0x64)
    PlayEffect(0x00, 0x01, 0x0008, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_727D')
    def lambda_727D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 100)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_727D)

    WaitEffect(0x01, 0x00)

    @scena.Lambda('lambda_7292')
    def lambda_7292():
        CameraMove(-6620, 0, -790, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_7292)

    @scena.Lambda('lambda_72AA')
    def lambda_72AA():
        CameraSetDistance(1500, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_72AA)

    WaitForThreadExit(0x0101, 0x0000)
    CreateThread(0x0022, 0x00, 0x00, func_14_2C45)
    ChrSetPos(0x0008, -1460, -370, -620, 255)
    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrSetChipByIndex(0x0008, 30)
    ChrSetSubChip(0x0008, 8)
    ChrSetPos(0x0023, -11040, 0, -2980, 75)
    ChrSetRGBAMask(0x0023, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0023, 0x0080)
    ChrSetChipByIndex(0x0023, 30)
    ChrSetSubChip(0x0023, 8)
    PlayEffect(0x06, 0x01, 0x0008, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0x02, 0x0023, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_7381')
    def lambda_7381():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_7381)

    @scena.Lambda('lambda_7393')
    def lambda_7393():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 200)

        ExitThread()

    DispatchAsync(0x0023, 0x0002, lambda_7393)

    StopEffect(0x01, 0x02)
    StopEffect(0x02, 0x02)
    ChrSetAfterImage(0x01, 0x0008, 0x0000, 0x0000)
    ChrSetAfterImage(0x01, 0x0023, 0x0000, 0x0000)
    Sleep(1000)

    @scena.Lambda('lambda_73C0')
    def lambda_73C0():
        CameraMove(-6530, 0, -1780, 200)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_73C0)

    @scena.Lambda('lambda_73D8')
    def lambda_73D8():
        CameraSetDistance(1360, 200)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_73D8)

    CreateThread(0x0008, 0x00, 0x00, func_15_2C6B)
    Sleep(100)

    ChrSetChipByIndex(0x0022, 10)
    ChrSetSubChip(0x0022, 0)
    ChrSetDirection(0x0022, 165, 0)

    @scena.Lambda('lambda_7405')
    def lambda_7405():
        ChrJumpTo(0x00FE, -6460, 0, 1910, 500, 2000)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_7405)

    Sleep(100)

    CreateThread(0x0023, 0x00, 0x00, func_16_2FE8)
    WaitForThreadExit(0x0022, 0x0001)
    ChrSetChipByIndex(0x0022, 8)
    ChrSetSubChip(0x0022, 0)
    PlaySE(164, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0000)
    CreateThread(0x0008, 0x00, 0x00, func_18_32DA)

    @scena.Lambda('lambda_744F')
    def lambda_744F():
        CameraMove(-1410, -370, 870, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_744F)

    @scena.Lambda('lambda_7467')
    def lambda_7467():
        OP_6C(305000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7467)

    @scena.Lambda('lambda_7477')
    def lambda_7477():
        OP_67(0, 3810, -10000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7477)

    @scena.Lambda('lambda_748F')
    def lambda_748F():
        CameraSetDistance(1770, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_748F)

    @scena.Lambda('lambda_749F')
    def lambda_749F():
        OP_6E(465, 400)

        ExitThread()

    DispatchAsync(0x0023, 0x0000, lambda_749F)

    ChrSetAfterImage(0x00, 0x0022, 0x0014, 0x00C8)
    ChrSetChipByIndex(0x0022, 10)
    ChrSetSubChip(0x0022, 0)

    @scena.Lambda('lambda_74C1')
    def lambda_74C1():
        ChrSetDirection(0x00FE, 0, 200)

        ExitThread()

    DispatchAsync(0x0022, 0x0003, lambda_74C1)

    @scena.Lambda('lambda_74CF')
    def lambda_74CF():
        ChrJumpTo(0x00FE, 0, -370, -4680, 500, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_74CF)

    WaitForThreadExit(0x0022, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetAfterImage(0x01, 0x0022, 0x0000, 0x0000)

    @scena.Lambda('lambda_74FF')
    def lambda_74FF():
        CameraMove(-1530, -370, 600, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_74FF)

    @scena.Lambda('lambda_7517')
    def lambda_7517():
        OP_6C(0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7517)

    ChrSetChipByIndex(0x0022, 10)
    ChrSetSubChip(0x0022, 4)

    @scena.Lambda('lambda_7531')
    def lambda_7531():
        ChrSetDirection(0x00FE, 45, 200)

        ExitThread()

    DispatchAsync(0x0022, 0x0003, lambda_7531)

    @scena.Lambda('lambda_753F')
    def lambda_753F():
        ChrJumpTo(0x00FE, -3310, -370, -3310, 500, 4000)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_753F)

    WaitForThreadExit(0x0022, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetChipByIndex(0x0022, 6)
    ChrSetSubChip(0x0022, 5)
    Sleep(100)

    @scena.Lambda('lambda_7576')
    def lambda_7576():
        CameraMove(0, -370, 2000, 120)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_7576)

    @scena.Lambda('lambda_758E')
    def lambda_758E():
        OP_67(0, 4080, -10000, 120)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_758E)

    @scena.Lambda('lambda_75A6')
    def lambda_75A6():
        OP_6C(0, 120)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_75A6)

    @scena.Lambda('lambda_75B6')
    def lambda_75B6():
        CameraSetDistance(1860, 120)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_75B6)

    @scena.Lambda('lambda_75C6')
    def lambda_75C6():
        ChrMoveTo(0x00FE, 0, -370, -200, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_75C6)

    CreateThread(0x0008, 0x00, 0x00, func_12_2B89)
    WaitForThreadExit(0x0101, 0x0000)
    TerminateThread(0x0022, 0x01)
    TerminateThread(0x0008, 0x00)
    TerminateThread(0x0008, 0x03)
    Fade(100)
    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x00FF, 0, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 400, 3000, 200)
    ChrSetFlags(0x0008, 0x0008)
    ChrSetFlags(0x0022, 0x0002)
    ChrSetChipByIndex(0x0022, 15)
    ChrSetSubChip(0x0022, 0)

    ExecExpressionWithValue(
        0x0022,
        0x01,
        (
            (Expr.GetChrWork, 0x22, 0x1),
            (Expr.PushLong, 0x2BC),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0022,
        0x03,
        (
            (Expr.GetChrWork, 0x22, 0x3),
            (Expr.PushLong, 0x2BC),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_767D')
    def lambda_767D():
        OP_9E(0x00FE, 40, 0, 500, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_767D)

    @scena.Lambda('lambda_7697')
    def lambda_7697():
        ChrMoveTo(0x00FE, 0, -370, -200, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_7697)

    WaitForThreadExit(0x0022, 0x0002)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_76C0')
    def lambda_76C0():
        OP_99(0x00FE, 0x00, 0x07, 2500)
        Yield()

        Jump('lambda_76C0')

    DispatchAsync2(0x0022, 0x0002, lambda_76C0)

    @scena.Lambda('lambda_76D3')
    def lambda_76D3():
        OP_9E(0x00FE, 15, 4294967288, 0, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0003, lambda_76D3)

    CreateThread(0x0008, 0x00, 0x00, func_19_3327)
    WaitForThreadExit(0x0022, 0x0001)

    @scena.Lambda('lambda_76F9')
    def lambda_76F9():
        CameraSetDistance(1660, 20000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_76F9)

    Sleep(1000)

    OP_DC()

    ChrTalk(
        0x0022,
        (
            '#0020410900V#1047F#6P唔……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140410901V#126F#2P怎么了，约修亚！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410902V不好好利用你唯一的速度优势，\n',
            '你又怎有丝毫的胜算可言！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0020410903V#1043F#6P……………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410904V#1042F……喂，莱维。\n',
            '我只希望你回答一个问题……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410905V为什么你要协助教授\n',
            '做出这些事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000096, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Sleep(500)

    ChrTalk(
        0x0022,
        (
            '#0020410906V#1043F#6P你之前说过……目的并不是\n',
            '为了给卡琳姐姐报仇。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410907V#1035F而是『为了向这世界作出质问』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410908V#1042F那究竟是……什么意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140410909V#120F#2P…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410910V#124F……没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410911V#123F我只想证实一下\n',
            '人类这种生物的“存在价值”罢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0020410912V#1044F#6P人类的存在价值……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140410913V#124F#2P时代的转换、国家的理论、\n',
            '价值观和伦理观的变化……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410914V总之，人类这种生物\n',
            '总会受各种事物的影响而改变。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410915V并且时而会失去自我，坠入深渊，\n',
            '被时代的洪流吞噬而消失……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410916V#121F就像我们的哈梅尔村一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0020410917V#1042F#6P！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140410918V#120F#2P这座都市也是一样的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410919V曾几何时，人们在这座天空都市中\n',
            '过着幸福满足的生活。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410920V但是，随着『大崩坏』的到来，\n',
            '人们不得不舍弃了乐园，逃到大地上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410921V#124F然后这都市被封印……\n',
            '人们也渐渐忘记了它的存在。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410922V不仅如此，还将它当作一段痛苦的回忆，\n',
            '不愿意再提起、回忆……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0020410923V#1043F#6P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140410924V#124F#2P真相往往最容易被蒙蔽，\n',
            '人们愿意相信的只有眼前的现实。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410925V这就是人类的软弱，也是无法克服的界限。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410926V#123F但『辉之环』却以\n',
            '它压倒性的力量和存在感\n',
            '将真实呈现在人类的眼前。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410927V失去了国家这一后盾的时候，\n',
            '自己是多么地无力……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410928V自己的舒适生活\n',
            '是多么地不堪一击……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410929V#124F没错……因为自我欺骗而视而不见\n',
            '的一切真相，都会彻底呈现在眼前。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0020410930V#1043F#6P这么说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410931V#1042F让世人知晓这一切，\n',
            '这就是莱维的目的……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140410932V#126F#2P正是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410933V#124F如果人们继续活在欺瞒中，\n',
            '过去的错误就只会不断重现。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410934V今后也会不断发生\n',
            '第二个、第三个哈梅尔惨剧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410935V还有很多的卡琳将会死去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410936V#123F我──为了防止这些，\n',
            '才投身加入『噬身之蛇』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410937V为了这个目标……\n',
            '即使化为修罗又有何憾？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0020410938V#1042F#6P……………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410939V#1043F这才是……真正的欺骗吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140410940V#121F#2P…………什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0020410941V#1043F#6P我也是软弱的人类……\n',
            '莱维的话让我非常痛心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410942V#1035F但是……人类在时代的洪流中\n',
            '并不只是无力的存在。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410943V#1042F就像十年前的那一天……\n',
            '救下了我的姐姐一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000096, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0140410944V#126F#2P………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0020410945V#1043F#6P莱维不可能\n',
            '没注意到这一点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410946V在你的心中，\n',
            '姐姐一直都是那么重要……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410947V#1040F所以……\n',
            '你说的那些话才是自我欺骗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140410948V#126F#2P…………唔………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(100)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TerminateThread(0x0008, 0x00)
    Fade(250)

    @scena.Lambda('lambda_821D')
    def lambda_821D():
        CameraMove(1030, -370, 1030, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_821D)

    @scena.Lambda('lambda_8235')
    def lambda_8235():
        OP_67(0, 3450, -10000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8235)

    @scena.Lambda('lambda_824D')
    def lambda_824D():
        CameraSetDistance(2100, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_824D)

    @scena.Lambda('lambda_825D')
    def lambda_825D():
        OP_6C(45000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_825D)

    TerminateThread(0x0022, 0x02)
    TerminateThread(0x0022, 0x03)
    ChrClearFlags(0x0022, 0x0002)
    ChrSetChipByIndex(0x0022, 10)
    ChrSetSubChip(0x0022, 4)
    ChrSetPos(0x0022, -450, -370, -450, 45)
    ChrClearFlags(0x0008, 0x0008)
    ChrSetChipByIndex(0x0008, 7)
    ChrSetSubChip(0x0008, 2)
    ChrSetPos(0x0008, 450, -370, 450, 225)
    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x00FF, 0, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_82EF')
    def lambda_82EF():
        ChrJumpTo(0x00FE, -3150, -370, -3150, 1500, 4500)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_82EF)

    @scena.Lambda('lambda_830D')
    def lambda_830D():
        ChrJumpTo(0x00FE, 2770, -370, 2770, 1500, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_830D)

    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0022, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0022, 9)
    ChrSetSubChip(0x0022, 0)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140410949V#127F#5P卡琳是特别的！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410950V像她那样的人\n',
            '世上又有几个！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410951V#127F所以──\n',
            '人类必须要接受试炼！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410952V试炼他们能否偿还\n',
            '软弱和欺骗造成的罪！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410953V试验他们是否值得卡琳为之牺牲！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0020410954V#1042F#6P那么──\n',
            '就由我来证明给你看！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410955V#1035F我这个靠姐姐的牺牲才\n',
            '存活至今的软弱者……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410956V#1046F因为和艾丝蒂尔她们相遇\n',
            '而找到了属于自己的道路！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410957V并且历尽艰难地\n',
            '来到了莱维的面前！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)

    @scena.Lambda('lambda_8528')
    def lambda_8528():
        CameraSetDistance(2000, 500)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_8528)

    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0022, 14)
    ChrSetSubChip(0x0022, 0)
    Sleep(250)

    PlaySE(501, 0x00, 0x64)
    ChrSetSubChip(0x0022, 1)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0022,
        (
            '#0020410958V#1046F#6P#3S人──只要在同伴的身边，\n',
            '就绝对不是无力的存在！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140410959V#126F#5P#10A！！！',
            TxtCtl.Enter,
        ),
    )

    Sleep(500)

    OP_56(0x00)

    @scena.Lambda('lambda_85E6')
    def lambda_85E6():
        CameraMove(4059, -370, 2660, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_85E6)

    @scena.Lambda('lambda_85FE')
    def lambda_85FE():
        OP_67(0, 5600, -10000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_85FE)

    @scena.Lambda('lambda_8616')
    def lambda_8616():
        CameraSetDistance(1440, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_8616)

    @scena.Lambda('lambda_8626')
    def lambda_8626():
        OP_6C(90000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_8626)

    ChrSetFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetSubChip(0x0008, 6)
    ChrSetFlags(0x0022, 0x0002)
    ChrSetChipByIndex(0x0022, 10)
    ChrSetSubChip(0x0022, 18)
    ChrSetAfterImage(0x00, 0x0022, 0x0014, 0x00C8)

    @scena.Lambda('lambda_865C')
    def lambda_865C():
        ChrJumpTo(0x00FE, 1850, -370, 1850, 200, 4000)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_865C)

    Sleep(100)

    ChrSetChipByIndex(0x0008, 17)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0022, 16)
    ChrSetSubChip(0x0022, 0)

    @scena.Lambda('lambda_8693')
    def lambda_8693():
        OP_99(0x00FE, 0x00, 0x03, 4000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_8693)

    Sleep(50)

    ChrSetChipByIndex(0x0008, 17)
    ChrSetSubChip(0x0008, 1)
    WaitForThreadExit(0x0022, 0x0001)
    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x0008, -300, 500, -300, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 400, 3000, 200)

    @scena.Lambda('lambda_8702')
    def lambda_8702():
        OP_9E(0x00FE, 20, 0, 500, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_8702)

    @scena.Lambda('lambda_871C')
    def lambda_871C():
        OP_9E(0x00FE, 40, 0, 500, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_871C)

    @scena.Lambda('lambda_8736')
    def lambda_8736():
        ChrMoveTo(0x00FE, 2840, -370, 2840, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_8736)

    ChrSetChipByIndex(0x0008, 17)
    ChrSetSubChip(0x0008, 2)
    WaitForThreadExit(0x0008, 0x0001)
    ChrSetAfterImage(0x01, 0x0022, 0x0000, 0x0000)
    Sleep(250)

    ChrSetChipByIndex(0x0022, 16)
    ChrSetSubChip(0x0022, 4)
    Sleep(100)

    ChrSetChipByIndex(0x0022, 16)
    ChrSetSubChip(0x0022, 5)
    Sleep(100)

    CreateThread(0x0008, 0x00, 0x00, func_1A_33A8)

    @scena.Lambda('lambda_8792')
    def lambda_8792():
        OP_99(0x00FE, 0x06, 0x07, 2500)
        Yield()

        Jump('lambda_8792')

    DispatchAsync2(0x0022, 0x0002, lambda_8792)

    @scena.Lambda('lambda_87A5')
    def lambda_87A5():
        ChrMoveTo(0x00FE, 1990, -370, 1990, 100, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_87A5)

    @scena.Lambda('lambda_87C0')
    def lambda_87C0():
        OP_99(0x00FE, 0x02, 0x03, 2500)
        Yield()

        Jump('lambda_87C0')

    DispatchAsync2(0x0008, 0x0002, lambda_87C0)

    @scena.Lambda('lambda_87D3')
    def lambda_87D3():
        OP_9E(0x00FE, 30, 0, 0, 2500)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_87D3)

    @scena.Lambda('lambda_87ED')
    def lambda_87ED():
        ChrMoveTo(0x00FE, 2980, -370, 2980, 50, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_87ED)

    WaitForThreadExit(0x0022, 0x0001)
    TerminateThread(0x0008, 0x00)
    TerminateThread(0x0008, 0x02)
    TerminateThread(0x0008, 0x03)
    TerminateThread(0x0022, 0x02)
    Fade(200)
    CameraSetDistance(1340, 0)
    ChrSetChipByIndex(0x0022, 16)
    ChrSetSubChip(0x0022, 8)

    @scena.Lambda('lambda_8835')
    def lambda_8835():
        ChrJumpTo(0x00FE, 1710, -370, 1710, 100, 800)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_8835)

    WaitForThreadExit(0x0022, 0x0001)

    @scena.Lambda('lambda_8858')
    def lambda_8858():
        ChrMoveTo(0x00FE, 2140, -370, 2140, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_8858)

    @scena.Lambda('lambda_8873')
    def lambda_8873():
        OP_99(0x00FE, 0x08, 0x0D, 2500)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_8873)

    Sleep(50)

    @scena.Lambda('lambda_8888')
    def lambda_8888():
        CameraMove(3760, 1000, 2360, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_8888)

    @scena.Lambda('lambda_88A0')
    def lambda_88A0():
        OP_67(0, 5280, -10000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_88A0)

    @scena.Lambda('lambda_88B8')
    def lambda_88B8():
        OP_6C(80000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_88B8)

    OP_20(0x00000000)
    PlaySE(155, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x0008, -300, 500, -300, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 400, 3000, 200)

    @scena.Lambda('lambda_8918')
    def lambda_8918():
        ChrMoveTo(0x00FE, 3270, -370, 3270, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_8918)

    @scena.Lambda('lambda_8933')
    def lambda_8933():
        OP_99(0x00FE, 0x04, 0x05, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_8933)

    @scena.Lambda('lambda_8943')
    def lambda_8943():
        OP_9E(0x00FE, 20, 0, 500, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_8943)

    WaitForThreadExit(0x0008, 0x0002)
    CreateThread(0x001E, 0x00, 0x00, func_1B_34C2)

    @scena.Lambda('lambda_8969')
    def lambda_8969():
        OP_99(0x00FE, 0x06, 0x07, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_8969)

    WaitForThreadExit(0x0008, 0x0002)

    @scena.Lambda('lambda_897E')
    def lambda_897E():
        OP_99(0x00FE, 0x07, 0x0A, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_897E)

    WaitForThreadExit(0x001E, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0140410960V#126F#3P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_89C1')
    def lambda_89C1():
        CameraMove(5000, 0, 2920, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_89C1)

    @scena.Lambda('lambda_89D9')
    def lambda_89D9():
        CameraSetDistance(1680, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_89D9)

    Fade(250)
    ChrClearFlags(0x0022, 0x0002)
    ChrSetDirection(0x0022, 45, 0)
    ChrSetChipByIndex(0x0022, 4)
    PlaySE(209, 0x00, 0x50)
    ChrSetSubChip(0x0022, 2)
    OP_99(0x0022, 0x02, 0x03, 800)
    Sleep(1000)

    ChrTalk(
        0x0022,
        (
            '#0020410961V#1047F#6P呼……呼……\n',
            '……呼……呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_8A4F')
    def lambda_8A4F():
        OP_99(0x00FE, 0x0A, 0x0D, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_8A4F)

    WaitForThreadExit(0x0101, 0x0000)
    OP_59()
    PlayBGM(1)
    Call(0, 0x0003)
    ChrSetChipByIndex(0x0022, 10)
    ChrSetSubChip(0x0022, 3)
    ChrSetChipByIndex(0x0008, 29)
    ChrSetSubChip(0x0008, 13)
    ChrSetPos(0x0101, -2520, 0, -11240, 0)
    ChrSetPos(0x00F8, -4220, 0, -12720, 0)
    Fade(500)
    CameraMove(-2140, 0, -11280, 0)
    OP_67(0, 6160, -10000, 0)
    CameraSetDistance(1680, 0)
    OP_6C(35000, 0)
    OP_6E(465, 0)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010410962V#1004F#6P成、成功了……',
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
        'loc_8B4B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050410963V#051F#4P嘿……\n',
            '分出胜负了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8C99')

    def _loc_8B4B(): pass

    label('loc_8B4B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8B93',
    )

    ChrTalk(
        0x0103,
        (
            '#0030410964V#021F#4P呵呵……\n',
            '胜负，好像揭晓了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8C99')

    def _loc_8B93(): pass

    label('loc_8B93')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8BD3',
    )

    ChrTalk(
        0x0104,
        (
            '#0040410965V#031F#4P呼……\n',
            '胜负揭晓了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8C99')

    def _loc_8BD3(): pass

    label('loc_8BD3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8C1E',
    )

    ChrTalk(
        0x0110,
        (
            '#0110410966V#277F哼……看来胜负已定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8C99')

    def _loc_8C1E(): pass

    label('loc_8C1E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8C57',
    )

    ChrTalk(
        0x0108,
        (
            '#0080410967V#070F#4P胜负，揭晓了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8C99')

    def _loc_8C57(): pass

    label('loc_8C57')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8C99',
    )

    ChrTalk(
        0x0109,
        (
            '#0180410968V#1060F#4P嘿嘿……\n',
            '胜负，揭晓了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8C99(): pass

    label('loc_8C99')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8CCC',
    )

    ChrTalk(
        0x0105,
        (
            '#0060410969V#1168F#4P约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8CCC(): pass

    label('loc_8CCC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8D0A',
    )

    ChrTalk(
        0x010B,
        (
            '#0090410970V#415F#4P了不起啊，约修亚……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8D0A(): pass

    label('loc_8D0A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8D4E',
    )

    ChrTalk(
        0x010F,
        (
            '#0100410971V#171F真是了不起，约修亚君……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8D4E(): pass

    label('loc_8D4E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8D8B',
    )

    ChrTalk(
        0x0107,
        (
            '#0070410972V#067F#4P太好了！\n',
            '约修亚哥哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8D8B(): pass

    label('loc_8D8B')

    Sleep(100)

    Fade(500)
    CameraMove(4240, -370, 3040, 0)
    OP_67(0, 6160, -10000, 0)
    CameraSetDistance(1680, 0)
    OP_6C(80000, 0)
    OP_6E(465, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0022,
        (
            '#0020410973V#1043F#6P呼……呼……\n',
            '……呼……呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140410974V#121F#5P面对我的一丝破绽\n',
            '全力的攻击过来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410975V真是……令人感到吃惊的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0020410976V#1035F#6P哈……哈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410977V#1054F……不……不行吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140410978V#123F#5P呼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410979V身为『剑帝』，却连手中的剑都被打落，\n',
            '再说什么也都没用了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410980V#1430F看来我也只能老老实实地认输了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0020410981V#1044F#6P…………啊……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010410982V#1001F#4S#1P成功了！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    CreateThread(0x0101, 0x00, 0x01, func_09_2579)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_900B',
    )

    Sleep(300)

    ChrTalk(
        0x010B,
        (
            '#0090410983V#214F啊，太棒了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_900B(): pass

    label('loc_900B')

    @scena.Lambda('lambda_9011')
    def lambda_9011():
        CameraMove(2680, -370, 1500, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0000, lambda_9011)

    @scena.Lambda('lambda_9029')
    def lambda_9029():
        OP_67(0, 5720, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_9029)

    @scena.Lambda('lambda_9041')
    def lambda_9041():
        CameraSetDistance(1860, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_9041)

    Sleep(400)

    CreateThread(0x00F8, 0x00, 0x01, func_0A_2584)
    Sleep(250)

    CreateThread(0x00F9, 0x00, 0x01, func_0B_25FC)
    WaitForThreadExit(0x00F8, 0x0000)
    WaitForThreadExit(0x00F9, 0x0000)
    WaitForThreadExit(0x0022, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010410984V#1001F#6P真厉害！　约修亚真厉害！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410985V居然战胜了『剑帝』啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410986V#1008F而且……只是将剑弹飞而已！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0022, 0x03, 0x00, 1000)
    Fade(250)
    ChrSetChipByIndex(0x0022, 1)
    ChrSetSubChip(0x0022, 0)
    OP_0D()
    ChrClearFlags(0x0022, 0x0020)
    ChrTurnDirection(0x0022, 0x0101, 300)
    Sleep(500)

    ChrTalk(
        0x0022,
        (
            '#0020410987V#1035F#5P因为不这么做的话……\n',
            '就一点取胜的希望也没有了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410988V尽量不伤害对方，\n',
            '优先考虑使对方丧失战斗力……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410989V#1054F父亲教我的\n',
            '游击士心得起作用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410990V#1025F#6P是嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140410991V#121F#5P原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410992V#124F『教授』灌输的技术和\n',
            '从『剑圣』那里学到的知识……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410993V把这两者运用自如的话，\n',
            '战胜我也是理所当然的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0022, 0x0008, 400)

    ChrTalk(
        0x0022,
        (
            '#0020410994V#1040F#6P莱维……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140410995V#124F#5P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410996V#120F我为了试验人类\n',
            '而协助了『噬身之蛇』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410997V既然你已找到了我要的答案，\n',
            '我也就没理由继续协助他们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140410998V#124F看来……\n',
            '该是我离开的时候了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0020410999V#1044F#6P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrSetChipByIndex(0x0022, 31)
    ChrSetSubChip(0x0022, 0)

    @scena.Lambda('lambda_93E4')
    def lambda_93E4():
        CameraMove(3580, -370, 2420, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_93E4)

    @scena.Lambda('lambda_93FC')
    def lambda_93FC():
        CameraSetDistance(1700, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_93FC)

    @scena.Lambda('lambda_940C')
    def lambda_940C():
        ChrMoveTo(0x00FE, 2890, -370, 2890, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_940C)

    WaitForThreadExit(0x0022, 0x0001)
    ChrSetFlags(0x0022, 0x0080)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 33)
    ChrSetSubChip(0x0008, 0)
    OP_99(0x0008, 0x00, 0x02, 1200)
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
        'loc_9486',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_94C4')

    def _loc_9486(): pass

    label('loc_9486')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_94AD',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_94C4')

    def _loc_94AD(): pass

    label('loc_94AD')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_94C4(): pass

    label('loc_94C4')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_94F0',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_952E')

    def _loc_94F0(): pass

    label('loc_94F0')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9517',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_952E')

    def _loc_9517(): pass

    label('loc_9517')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_952E(): pass

    label('loc_952E')

    Sleep(1000)

    ChrTalk(
        0x0022,
        (
            '#0020411000V#1055F#6P太好了……真是太好了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020411001V……莱维……\n',
            '莱维回来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0008, 0x02, 0x04, 1000)
    OP_99(0x0008, 0x02, 0x04, 1000)
    ChrSetSubChip(0x0008, 2)

    ChrTalk(
        0x0008,
        (
            '#0140411002V#126F#5P喂、喂喂……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0020411003V#1043F#6P自从被父亲收留之后\n',
            '我就一直很在意……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020411004V……声音和面容虽然还记得，\n',
            '但却完全想不起来你是谁了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020411005V好不容易才回忆起来，\n',
            '……你却已经以敌人的身份出现在我眼前……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020411006V#1035F……我一直都……很不安……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140411007V#124F#5P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0008, 0x05, 0x0A, 1500)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1200)

    CameraMove(2720, -370, 1360, 1350)

    ChrTalk(
        0x0101,
        (
            '#0010411008V#1016F#6P那、那个～……',
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
        'loc_9809',
    )

    ChrTalk(
        0x0105,
        (
            '#0060411009V#1165F#4P（好、好像……\n',
            '  他们关系非常好呢。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060411010V#1380F（……让人羡慕啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411011V#1013F#5P（我说科洛丝啊……\n',
            '  别在那里脸红啊～）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_98BD')

    def _loc_9809(): pass

    label('loc_9809')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_98BD',
    )

    ChrTalk(
        0x010B,
        (
            '#0090411012V#414F#4P（我说那两个人，\n',
            '  是不是关系特别好啊？）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090411013V（都让人感觉有点可疑了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411014V#1019F#5P（你、你在胡思乱想些什么啊！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_98BD(): pass

    label('loc_98BD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9967',
    )

    ChrTalk(
        0x0107,
        (
            '#0070411015V#067F#4P（嘿嘿……\n',
            '  约修亚哥哥\n',
            '  好像在跟他哥哥撒娇呢。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070411016V（挺可爱的呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411017V#1016F#5P（提妲……喂喂。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9A19')

    def _loc_9967(): pass

    label('loc_9967')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9A19',
    )

    ChrTalk(
        0x0109,
        (
            '#0180411018V#1061F#4P（哈哈，约修亚也\n',
            '  有可爱的地方呢。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180411019V#1066F（嗯——\n',
            '  我也想要个那样的弟弟啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411020V#1007F#5P（喂……凯文。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9A19(): pass

    label('loc_9A19')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9AC4',
    )

    ChrTalk(
        0x0108,
        (
            '#0080411021V#071F#4P（哈哈……\n',
            '  因为他们从小就像亲兄弟一样。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080411022V（偶尔撒撒娇也是正常的。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411023V#1025F#5P〈是、是吗……？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9D2C')

    def _loc_9AC4(): pass

    label('loc_9AC4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9BC8',
    )

    ChrTalk(
        0x010F,
        (
            '#0100411024V#171F#2P（呵呵……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100411025V（两个人大概是像兄弟一样长大的。\n',
            '  和好如初当然是最好的结果。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411026V#1025F#2P（是、是啊……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010411027V#1000F（嗯……\n',
            '  谢谢你，尤莉亚。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9D2C')

    def _loc_9BC8(): pass

    label('loc_9BC8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9C7B',
    )

    ChrTalk(
        0x0103,
        (
            '#0030411028V#027F#4P（呵呵……这不是很好吗。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030411029V（他们本来就像亲兄弟一样。\n',
            '  能和好如初当然是最好了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411030V#1025F#5P（雪拉姐……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9D2C')

    def _loc_9C7B(): pass

    label('loc_9C7B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9D2C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050411031V#053F#4P（没办法啊……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050411032V#051F（虽然是少年老成，不过\n',
            '  仍然还处在撒娇的小孩子年龄阶段呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411033V#1025F#5P（是、是吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9D2C(): pass

    label('loc_9D2C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9E86',
    )

    ChrTalk(
        0x0110,
        (
            '#0110411034V#277F（……没想到\n',
            '  他还有这样的一面。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110411035V（之前交手的时候，\n',
            '  他的眼神\n',
            '  就像被黑暗迷住了一样……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411036V#1004F#2P（那、那个……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010411037V#1015F（穆拉居然\n',
            '  跟约修亚战斗过啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0110,
        (
            '#0110411038V#278F（……在空贼们的要塞里有过一次。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9E86(): pass

    label('loc_9E86')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9F4A',
    )

    ChrTalk(
        0x0104,
        (
            '#0040411039V#033F#4P（啊，我的约修亚在对\n',
            '  别的男人那样地撒娇……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040411040V#034F（我羞涩的少男之心\n',
            '  因嫉妒而燃烧起来了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411041V#1022F#5P（你就别瞎搅和了！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9F4A(): pass

    label('loc_9F4A')

    OP_62(0x0022, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Fade(500)
    ChrClearFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 27)
    ChrSetSubChip(0x0008, 0)
    ChrClearFlags(0x0022, 0x0080)
    ChrSetChipByIndex(0x0022, 1)
    ChrSetSubChip(0x0022, 0)
    OP_0D()

    @scena.Lambda('lambda_9F90')
    def lambda_9F90():
        ChrMoveTo(0x00FE, 2140, -370, 2140, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_9F90)

    @scena.Lambda('lambda_9FAB')
    def lambda_9FAB():
        CameraMove(3000, -370, 2000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_9FAB)

    @scena.Lambda('lambda_9FC3')
    def lambda_9FC3():
        CameraSetDistance(1700, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_9FC3)

    WaitForThreadExit(0x0022, 0x0001)
    ChrTurnDirection(0x0022, 0x0101, 400)

    ChrTalk(
        0x0022,
        (
            '#0020411042V#1044F#5P抱、抱歉，艾丝蒂尔……\n',
            '我好像有点忘乎所以了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020411043V#1043F明明还有很多问题没解决呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411044V#1025F#6P约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010411045V#1001F真是的，\n',
            '你根本就不用道歉嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010411046V你们好不容易才重归于好吧？\n',
            '快点继续和你哥哥撒撒娇吧～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0020411047V#1056F#5P撒、撒娇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140411048V#124F#5P呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411049V#123F艾丝蒂尔·布莱特。\n',
            '……我必须向你表示感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411050V#1004F#6P啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140411051V#123F#5P不管是对玲，还是对这小子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411052V我没能做到的事，\n',
            '你却都轻而易举地做到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411053V#1430F而且还引领着众人，\n',
            '一直来到了这里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411054V呵呵……你真是个奇怪的女孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BD86',
    )

    ChrTalk(
        0x0101,
        (
            '#0010411055V#1019F#6P好、好像完全都感觉不到\n',
            '有感谢的意思啊……',
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
        'loc_A439',
    )

    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140411056V#123F#5P阿加特·科洛斯纳。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411057V你那招蕴涵着龙气的必杀重剑技，\n',
            '威力确实相当了得。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411058V呼呼……\n',
            '似乎比以前有少许进步了啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050411059V#052F#4P喔、噢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050411060V#055F喂！不要露出一副自以为了不起\n',
            '的表情说那样的话啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050411061V#555F简直和那个大叔一模一样！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140411062V#1430F#5P呼……\n',
            '能同剑圣相似是我的光荣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A439(): pass

    label('loc_A439')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A743',
    )

    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140411063V#123F#5P雪拉扎德·哈维。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411064V无愧于『银闪』之名的华丽战技，\n',
            '这次我算是彻底见识了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0141070018V在女王宫时的失礼之举，\n',
            '请容我再一次致以歉意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030411065V#021F#4P呵呵呵……\n',
            '你这样说倒让我很不好意思了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030411066V#522F嗯……那个………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030411067V你……\n',
            '和露茜奥拉姐姐……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 0, 0x2238)),
            Expr.Return,
        ),
        'loc_A679',
    )

    ChrTalk(
        0x0008,
        (
            '#0140411068V#124F#5P彼此之间的关系还算不错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411069V在鱼蛇混杂的执行者之中，\n',
            '她是少见的品行优秀之人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411070V#120F……如果可能的话，\n',
            '我也希望她能平安无事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030411071V#023F#4P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030411072V#524F嗯……谢谢你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A743')

    def _loc_A679(): pass

    label('loc_A679')

    ChrTalk(
        0x0008,
        (
            '#0140411073V#124F#5P彼此之间的关系还算不错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411074V在鱼蛇混杂的执行者之中，\n',
            '她是少见的品行优秀之人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411075V#120F……以后也还会有见面的机会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030411076V#524F#4P嗯……谢谢你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A743(): pass

    label('loc_A743')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A9D1',
    )

    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140411077V#120F#5P科洛蒂亚公主……\n',
            '不，应该改称为王太女殿下了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411078V我在女王宫说过的话，\n',
            '现在还记得吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060411079V#1167F#4P『……国家这种东西，\n',
            '　就像是一个巨大复杂的导力器。』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060411080V#1169F你在那时所说的话，\n',
            '如今我才有了深刻的理解。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060411081V#1160F不过……我认为人类社会并不只是\n',
            '那种机械化的固定结构。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060411082V我想探寻的是……\n',
            '在无数巨大齿轮的转动中，\n',
            '每一个人究竟可以做些什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060411083V#1165F也许我的想法还很不成熟吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140411084V#123F#5P既然您能思索到如此地步，\n',
            '我也就不需要再说什么了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411085V请容许我向您那崇高的决意\n',
            '表示敬意吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060411086V#1168F#4P……十分感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A9D1(): pass

    label('loc_A9D1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_ABB0',
    )

    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140411087V#123F#5P提妲·拉赛尔……\n',
            '仔细想想的话，你还真是让人吃惊啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411088V凭借如此柔弱的身躯，竟然能坚持着\n',
            '到达这里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411089V这就是所谓的初生牛犊不怕虎吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070411090V#562F#4P啊、啊呜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070411091V#063F我果然还是……\n',
            '太过任性妄为了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140411092V#1430F#5P呵，我并不是在责备你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411093V#123F不过，以后还是要把\n',
            '自身的安全放在首要地位。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411094V这也是替那些\n',
            '守护着你的人着想。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070411095V#560F#4P是、是的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_ABB0(): pass

    label('loc_ABB0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AD65',
    )

    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140411096V#123F#5P『不动金』……\n',
            '先前的武术大会时真是失礼了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411097V有关你的事情，\n',
            '我曾听瓦鲁特说过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411098V可能的话，我也很想和你\n',
            '一对一正式交手一次啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080411099V#071F#4P喔噢……\n',
            '就算只是客套话，我听了也很高兴。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080411100V#070F只是，如今的我还没有资格\n',
            '完全背负『泰斗』之名。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080411101V如果有朝一日，我的武术能够大成，\n',
            '一定会再来向你挑战的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140411102V#1430F#5P呵……明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AD65(): pass

    label('loc_AD65')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AF9D',
    )

    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140411103V#124F#5P不过……\n',
            '你为什么会来这种地方呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411104V#120F前男爵家的小姐，乔丝特·卡普亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090411105V#212F#4P我、我愿意去哪里就去哪里！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090411106V#214F不过最重要的当然还是\n',
            '将我们被利用的怨恨还给你，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090411107V明白了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140411108V#120F#5P利用你们的人是上校，\n',
            '并不是我……不过算了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411109V#124F很抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090411110V#213F#4P哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140411111V#120F#5P怎么？\n',
            '你不是想要我谢罪吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090411112V#414F#4P啊、嗯嗯、算了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090411113V#413F（……可恶，\n',
            '　怎么感觉被他随随便便就混过去了～！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AF9D(): pass

    label('loc_AF9D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B4D2',
    )

    ChrTalk(
        0x0008,
        (
            '#0140411114V#124F#6P那边是……\n',
            '奥利维尔皇子，\n',
            '还有范德尔家的人吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411115V#120F好像这一年来，\n',
            '你们一直在\n',
            '调查哈梅尔事件啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040411116V#034F#2P哎呀呀，果然\n',
            '还是被『结社』看穿了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0110, 0x0104, 400)

    ChrTalk(
        0x0110,
        (
            '#0110411117V#272F#2P……如果你自己有意识到的话，\n',
            '就尽量避免太显眼的行动吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110411118V#276F说什么打听情报，\n',
            '你穿成那样潜入猎兵团的时候，\n',
            '可真让我捏了把冷汗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0110, 400)

    ChrTalk(
        0x0104,
        (
            '#0040411119V#031F#2P哈哈哈……\n',
            '穆拉君真是操心过度了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140411120V#121F#6P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411121V#124F真搞不懂……\n',
            '你为什么那么执着于此事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411122V#120F好歹也是皇族，\n',
            '乖乖待着\n',
            '不就什么都不用看到了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_B27F')
    def lambda_B27F():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_B27F)

    Sleep(100)

    ChrTurnDirection(0x0110, 0x0008, 400)

    ChrTalk(
        0x0104,
        (
            '#0040411123V#035F#2P……没错，理由\n',
            '或许和你相似吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040411124V#032F我只是不能容忍\n',
            '那些对不利的事情视而不见……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040411125V只追求轻易\n',
            '得来的安宁的自欺行为而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040411126V#034F……不过，我\n',
            '并不打算像你那样\n',
            '要把世上所有的欺瞒都击碎。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040411127V#030F我打算在自己\n',
            '能够触及的范围内，一一揭露真相。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140411128V#1430F#6P哼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411129V#123F你们两个，\n',
            '还是尽量小心点吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411130V眼前的敌人\n',
            '并不一定是唯一会露出獠牙的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0110,
        (
            '#0110411131V#278F#2P……不用你说我也知道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B876')

    def _loc_B4D2(): pass

    label('loc_B4D2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B6CB',
    )

    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140411132V#124F#5P话说回来，奥利维特皇子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411133V#120F没有范德尔的护卫就来到这里，\n',
            '行动未免太过轻率了吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411134V你的万金贵体\n',
            '可并不是只属于自己的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040411135V#035F#4P哼哼，做事要考虑效率性嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040411136V#030F不管怎么说，埃尔赛尤号也是\n',
            '决定我们命运的重要王牌。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040411137V修理保护它也就等于是\n',
            '守护我自己。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140411138V#123F#5P呵呵……\n',
            '真是了不起的胆量和判断力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411139V当皇子真是太可惜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040411140V#031F#4P多谢赞赏，倍感光荣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B876')

    def _loc_B6CB(): pass

    label('loc_B6CB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B876',
    )

    ChrTalk(
        0x0008,
        (
            '#0140411141V#124F#6P……你就是\n',
            '范德尔家的幼狮吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411142V#123F原来如此，帝国世代相传的武门之名\n',
            '果然不是浪得虚名的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0110,
        (
            '#0110411143V#278F#2P……我还没\n',
            '达到武人的巅峰。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110411144V#275F但总有一天，\n',
            '我会让我的剑触及那个极致的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140411145V#123F#6P呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411146V#1430F有空的时候，\n',
            '真想与你\n',
            '痛痛快快地过上几招。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B876(): pass

    label('loc_B876')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BA82',
    )

    ChrTalk(
        0x0008,
        (
            '#0140411147V#123F#6P尤莉亚·舒华兹……\n',
            '作为舰长，你的能力也相当不错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411148V能够在古罗力亚斯的炮火下\n',
            '毫发无伤地脱身的船，这可是头一回。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100411149V#176F#2P……我还差得远呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100411150V#178F毕竟在那之后，埃尔赛尤号\n',
            '还是被你击落了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140411151V#1430F#6P呵呵……\n',
            '那与其说是能力的差距，\n',
            '不如说是手段的不同罢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411152V#123F能在那种情况下安全迫降，\n',
            '你的本事值得称赞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100411153V#179F#2P……我就把这当作是称赞\n',
            '收下了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BA82(): pass

    label('loc_BA82')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BD83',
    )

    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140411155V#121F#5P……还有…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411156V………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180411157V#1064F#4P嗯？我的脸上有什么东西吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140411158V#124F#5P不……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411159V#120F你是凯文·格拉汉姆吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411160V你是否认识一位名叫露菲娜，\n',
            '使用弩枪的女性呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0109, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0109,
        (
            '#0180411161V#1063F你！是从哪里听到那个名字……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140411162V#123F#5P呼……\n',
            '你果然是星杯骑士吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411163V在数年之前，\n',
            '我在某次任务中曾和她有过一面之缘。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411164V当时被她漂亮地抢先一步…\n',
            '她现在还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180411165V#1067F#4P不……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180411166V#1060F……虽然很难启齿，\n',
            '不过她已经在某次事故中去世了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180411167V大概是在４年前左右吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140411168V#124F#5P是吗……\n',
            '那真是太遗憾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411169V#1015F#6P（在说什么人呢……？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BD83(): pass

    label('loc_BD83')

    Jump('loc_BDC8')

    def _loc_BD86(): pass

    label('loc_BD86')

    ChrTalk(
        0x0101,
        (
            '#0010411055V#1019F#6P好、好像完全都感觉不到\n',
            '感谢的意思啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BDC8(): pass

    label('loc_BDC8')

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010411170V#1002F#6P说起来的话……\n',
            '为什么莱维会在这里呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010411171V这个像魔法阵一样的东西\n',
            '不会就是『辉之环』吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140411172V#124F#5P不，这只是简单的光学术式。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411173V#121F为了将『根源区域』传送来的力量\n',
            '转换成『奇迹』而存在的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411174V#1020F#6P！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0022, 0x0008, 400)
    Sleep(300)

    ChrTalk(
        0x0022,
        (
            '#0020411175V#1042F#6P『根源区域』……\n',
            '『辉之环』就在那里吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140411176V#124F#5P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411177V#120F这座『中枢塔』\n',
            '其实就相当于把『环』的能量\n',
            '输送给全城的天线兼传送器。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411178V它的直接影响范围\n',
            '大约有半径１０００塞尔矩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411179V如果以『福音』作为中转的话，\n',
            '别说利贝尔，就连大陆全境\n',
            '都会受到影响。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411180V#1007F#6P这、这可不得了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010411181V#1002F那么要阻止异变的话\n',
            '就有必要对『根源区域』中的\n',
            '『辉之环』采取措施吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140411182V#120F#5P就是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411183V#124F不过『环』可不是\n',
            '那么好对付的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411184V它应该是一种古代遗物，\n',
            '拥有自律性的思考能力，\n',
            '会毫不留情地排除敌对者和外来势力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411185V１２００年前，把『环』封印到异次元的\n',
            '利贝尔王室的始祖也\n',
            '也一定颇费了一番功夫吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411186V#121F而且你们不仅要对付棘手的『环』，\n',
            '还要以『白面』作为对手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411187V#1026F#6P！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0020411188V#1035F#6P……这是必然的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020411189V#1040F可是只要有莱维帮忙，\n',
            '我也有信心对抗教授。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140411190V#123F#5P这小子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411191V已经认定我会\n',
            '跟你们一起行动了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0020411192V#1054F#6P嘿嘿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 80, -1, -1)
    TalkSetChrName('男性的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150411193V呼呼……\n',
            '和好了是好事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('男性的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150411194V可是不是\n',
            '聊得有点过头了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_20(0x000003E8)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0022, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C438',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_C476')

    def _loc_C438(): pass

    label('loc_C438')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C45F',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_C476')

    def _loc_C45F(): pass

    label('loc_C45F')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_C476(): pass

    label('loc_C476')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C4A2',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_C4E0')

    def _loc_C4A2(): pass

    label('loc_C4A2')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C4C9',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_C4E0')

    def _loc_C4C9(): pass

    label('loc_C4C9')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_C4E0(): pass

    label('loc_C4E0')

    Sleep(1000)

    LoadEffect(0x00, 'craft\\\\cr162_02.eff')
    LoadEffect(0x01, 'map\\\\mp049_22.eff')
    LoadEffect(0x02, 'scraft\\\\sc000_11.eff')
    LoadEffect(0x03, 'monster\\\\ms04551b.eff')
    LoadEffect(0x04, 'battle\\\\mgaria0.eff')
    ChrSetChipByIndex(0x0009, 5)
    ChrSetSubChip(0x0009, 0)
    Fade(500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(6340, -100, 10, 0)
    OP_67(0, 4420, -10000, 0)
    CameraSetDistance(2060, 0)
    OP_6C(90000, 0)
    OP_6E(465, 0)
    ChrSetPos(0x0101, 840, -370, 940, 35)
    ChrSetPos(0x00F8, -880, -370, 0, 35)
    ChrSetPos(0x00F9, 540, -370, -940, 35)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_0D()
    ChrSetPos(0x0009, 9140, 0, 0, 270)
    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0009, 0x0080)
    PlaySE(153, 0x00, 0x64)
    PlaySE(184, 0x00, 0x64)
    PlayEffect(0x01, 0x01, 0x0009, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_C6AD')
    def lambda_C6AD():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_C6AD)

    WaitEffect(0x01, 0x02)
    WaitForThreadExit(0x0009, 0x0002)
    Sleep(500)

    @scena.Lambda('lambda_C6CC')
    def lambda_C6CC():
        ChrSetDirection(0x00FE, 125, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_C6CC)

    @scena.Lambda('lambda_C6DA')
    def lambda_C6DA():
        ChrSetDirection(0x00FE, 125, 400)

        ExitThread()

    DispatchAsync(0x0022, 0x0003, lambda_C6DA)

    @scena.Lambda('lambda_C6E8')
    def lambda_C6E8():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_C6E8)

    @scena.Lambda('lambda_C6F6')
    def lambda_C6F6():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0003, lambda_C6F6)

    @scena.Lambda('lambda_C704')
    def lambda_C704():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0003, lambda_C704)

    OP_99(0x0009, 0x00, 0x04, 2000)
    PlaySE(216, 0x00, 0x64)
    OP_99(0x0009, 0x05, 0x09, 2000)
    PlayEffect(0x03, 0x00, 0x0009, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x0008, 0, 0, 0, 0)
    Sleep(300)

    CreateThread(0x0008, 0x00, 0x00, func_1C_3564)

    @scena.Lambda('lambda_C76A')
    def lambda_C76A():
        CameraMove(3840, -370, 3080, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_C76A)

    @scena.Lambda('lambda_C782')
    def lambda_C782():
        OP_67(0, 3760, -10000, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_C782)

    @scena.Lambda('lambda_C79A')
    def lambda_C79A():
        CameraSetDistance(1740, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_C79A)

    @scena.Lambda('lambda_C7AA')
    def lambda_C7AA():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_C7AA')

    DispatchAsync2(0x0101, 0x0003, lambda_C7AA)

    @scena.Lambda('lambda_C7BB')
    def lambda_C7BB():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_C7BB')

    DispatchAsync2(0x0022, 0x0003, lambda_C7BB)

    @scena.Lambda('lambda_C7CC')
    def lambda_C7CC():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_C7CC')

    DispatchAsync2(0x00F8, 0x0003, lambda_C7CC)

    @scena.Lambda('lambda_C7DD')
    def lambda_C7DD():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_C7DD')

    DispatchAsync2(0x00F9, 0x0003, lambda_C7DD)

    ChrTalk(
        0x0008,
        (
            '#0140411195V#1432F#5P唔……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    WaitForThreadExit(0x0008, 0x0000)
    WaitForThreadExit(0x0009, 0x0000)
    WaitEffect(0x00, 0x02)

    ChrTalk(
        0x0101,
        (
            '#0010411196V#1020F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0020411197V#1046F#5P莱维……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0022, 31)
    ChrSetSubChip(0x0022, 0)
    ChrWalkTo(0x0022, 520, -370, 4640, 5000, 0x00)
    Fade(250)
    ChrSetFlags(0x0022, 0x0020)
    ChrSetFlags(0x0022, 0x0002)
    ChrSetChipByIndex(0x0022, 9)
    ChrSetSubChip(0x0022, 0)
    OP_0D()
    ChrSetSubChip(0x0022, 3)
    Sleep(100)

    ChrSetSubChip(0x0022, 4)
    Sleep(100)

    ChrSetSubChip(0x0022, 0)
    Sleep(1000)

    TerminateThread(0x0101, 0x03)
    TerminateThread(0x0022, 0x03)
    TerminateThread(0x00F8, 0x03)
    TerminateThread(0x00F9, 0x03)
    PlayBGM(90)
    Sleep(500)

    @scena.Lambda('lambda_C8D5')
    def lambda_C8D5():
        CameraMove(6120, -110, 830, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_C8D5)

    @scena.Lambda('lambda_C8ED')
    def lambda_C8ED():
        OP_67(0, 4160, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_C8ED)

    @scena.Lambda('lambda_C905')
    def lambda_C905():
        CameraSetDistance(1860, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_C905)

    @scena.Lambda('lambda_C915')
    def lambda_C915():
        OP_6E(628, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_C915)

    @scena.Lambda('lambda_C925')
    def lambda_C925():
        OP_99(0x00FE, 0x09, 0x00, 1000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_C925)

    WaitForThreadExit(0x0008, 0x0000)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0150411198V#1151F#5P呵呵……各位好啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150411199V虽然你们成功地通过试练\n',
            '来到了这里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150411200V不过这种犯规的行为可不让人佩服啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_C9CF')
    def lambda_C9CF():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_C9CF)

    Sleep(50)

    @scena.Lambda('lambda_C9E2')
    def lambda_C9E2():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0003, lambda_C9E2)

    Sleep(50)

    @scena.Lambda('lambda_C9F5')
    def lambda_C9F5():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0003, lambda_C9F5)

    WaitForThreadExit(0x0101, 0x0003)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010411201V#1020F#6P什、什么叫犯规！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010411202V#1022F我们是正大光明地\n',
            '和执行者们战斗了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010411203V而且约修亚……\n',
            '也战胜了莱维！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010411204V#1005F所以你不要\n',
            '在那里说些莫名其妙的话！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0150411205V#1150F#5P呵呵，你还没发现这次\n',
            '计划的主旨呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150411206V#1154F从属于结社的人们\n',
            '都以某种形式得到了\n',
            '『盟主』所授的力量。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150411207V#1151F如果这样的人\n',
            '协助了你们的话，\n',
            '就无法期待正确的实验结果了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411208V#1026F#6P实、实验……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(250)
    ChrSetFlags(0x0022, 0x0002)
    ChrSetChipByIndex(0x0022, 9)
    ChrSetSubChip(0x0022, 7)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x0022,
        (
            '#0020411209V#1038F#6P……莫非……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020411210V#1036F连我们到达这里这件事\n',
            '也是计划的一部分吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0150411211V#1150F#5P呵呵……\n',
            '尽管其中有一些我个人的兴趣。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150411212V不过实验至少要\n',
            '占计划主旨的一半。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CD42',
    )

    ChrTalk(
        0x010F,
        (
            '#0100411213V#178F福音计划……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100411214V至少可以肯定，\n',
            '它占据了计划主旨的一半。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D0AB')

    def _loc_CD42(): pass

    label('loc_CD42')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CDC8',
    )

    ChrTalk(
        0x0110,
        (
            '#0110411215V#270F福音计划……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110411216V看来这个计划\n',
            '不仅仅是为了获取『辉之环』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D0AB')

    def _loc_CDC8(): pass

    label('loc_CDC8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CE33',
    )

    ChrTalk(
        0x0105,
        (
            '#0060411217V#1162F#6P福音计划……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060411218V并不仅仅是获取\n',
            '『辉之环』的计划吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D0AB')

    def _loc_CE33(): pass

    label('loc_CE33')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CE9E',
    )

    ChrTalk(
        0x0109,
        (
            '#0180411219V#1063F#6P福音计划……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180411220V并不仅仅是获取\n',
            '『辉之环』的计划吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D0AB')

    def _loc_CE9E(): pass

    label('loc_CE9E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CF06',
    )

    ChrTalk(
        0x0104,
        (
            '#0040411221V#032F#6P福音计划……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040411222V并不仅仅是获取\n',
            '『辉之环』的计划啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D0AB')

    def _loc_CF06(): pass

    label('loc_CF06')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CF70',
    )

    ChrTalk(
        0x0108,
        (
            '#0080411223V#072F#6P福音计划……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080411224V并不仅仅是获取\n',
            '『辉之环』的计划吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D0AB')

    def _loc_CF70(): pass

    label('loc_CF70')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CFDA',
    )

    ChrTalk(
        0x0103,
        (
            '#0030411225V#022F#6P福音计划……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030411226V并不仅仅是获取\n',
            '『辉之环』的计划呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D0AB')

    def _loc_CFDA(): pass

    label('loc_CFDA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D044',
    )

    ChrTalk(
        0x0106,
        (
            '#0050411227V#057F#6P福音计划……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050411228V并不仅仅是获取\n',
            '『辉之环』的计划啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D0AB')

    def _loc_D044(): pass

    label('loc_D044')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D0AB',
    )

    ChrTalk(
        0x0107,
        (
            '#0070411229V#065F#6P福音计划……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070411230V并不仅仅是获取\n',
            '『辉之环』的计划呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D0AB(): pass

    label('loc_D0AB')

    ChrTalk(
        0x0009,
        (
            '#0150411231V#1154F#5P哼哼……\n',
            '这都是遵循了『盟主』的意图。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150411232V#1151F从这一点上来说，约修亚。\n',
            '你也是扰乱实验精度的因素之一。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150411233V非常抱歉……\n',
            '你该还原到我的人偶状态了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0020411234V#1044F#6P！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrSetChipByIndex(0x0009, 30)
    ChrSetSubChip(0x0009, 0)
    OP_0D()
    Sleep(500)

    PlaySE(188, 0x00, 0x64)
    ChrSetSubChip(0x0009, 1)
    Sleep(300)

    OP_AD('ED6_DT24/C_VIS037._CH', 0x0000, 0x0000, 0x000003E8)
    Sleep(500)

    CameraMove(1340, -370, 2180, 0)
    OP_67(0, 5480, -10000, 0)
    CameraSetDistance(1400, 0)
    OP_6C(90000, 0)
    OP_6E(484, 0)
    ChrSetChipByIndex(0x0009, 4)
    ChrSetSubChip(0x0009, 0)
    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    ExecExpressionWithVar(
        0x1B,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x1A,
        (
            (Expr.PushLong, 0x5DC0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x00000004)
    OP_AE(0x000001F4)
    Sleep(500)

    Fade(250)
    ChrSetSubChip(0x0022, 5)
    OP_99(0x0022, 0x05, 0x06, 1000)

    @scena.Lambda('lambda_D24C')
    def lambda_D24C():
        OP_9E(0x00FE, 10, 0, 0, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_D24C)

    Sleep(500)

    @scena.Lambda('lambda_D26B')
    def lambda_D26B():
        OP_9E(0x00FE, 15, 0, 0, 3000)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_D26B)

    ChrTalk(
        0x0022,
        (
            '#0020411235V#1047F#6P唔……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(128, 0x00, 0x64)

    @scena.Lambda('lambda_D2AD')
    def lambda_D2AD():
        OP_99(0x00FE, 0x08, 0x0F, 1500)
        Yield()

        Jump('lambda_D2AD')

    DispatchAsync2(0x0022, 0x0003, lambda_D2AD)

    @scena.Lambda('lambda_D2C0')
    def lambda_D2C0():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_D2C0)

    Sleep(100)

    @scena.Lambda('lambda_D2D3')
    def lambda_D2D3():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_D2D3)

    Sleep(100)

    @scena.Lambda('lambda_D2E6')
    def lambda_D2E6():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_D2E6)

    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010411236V#1004F#2P约修亚！？',
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
        'loc_D356',
    )

    ChrTalk(
        0x0110,
        (
            '#0110411237V#273F…………啧……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D356(): pass

    label('loc_D356')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D38A',
    )

    ChrTalk(
        0x0107,
        (
            '#0070411238V#064F#2P哥、哥哥！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D38A(): pass

    label('loc_D38A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D3C0',
    )

    ChrTalk(
        0x010B,
        (
            '#0090411239V#213F#2P怎、怎么了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D3C0(): pass

    label('loc_D3C0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D3F9',
    )

    ChrTalk(
        0x0105,
        (
            '#0060411240V#1164F#2P你、你没事吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D3F9(): pass

    label('loc_D3F9')

    Sleep(1000)

    TerminateThread(0x0022, 0x02)
    TerminateThread(0x0022, 0x03)
    ChrSetSubChip(0x0022, 6)
    Sleep(1000)

    ChrTalk(
        0x0022,
        (
            '#0020411241V#1035F#6P……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlayEffect(0x00, 0x00, 0x0022, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ChrSetFlags(0x0022, 0x0004)

    @scena.Lambda('lambda_D487')
    def lambda_D487():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 100)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_D487)

    WaitEffect(0x00, 0x00)
    Fade(500)
    CameraMove(6260, -370, 0, 0)
    OP_67(0, 3600, -10000, 0)
    CameraSetDistance(1860, 0)
    OP_6C(90000, 0)
    OP_6E(628, 0)
    OP_0D()
    ChrClearFlags(0x0022, 0x0020)
    ChrClearFlags(0x0022, 0x0002)
    ChrSetChipByIndex(0x0022, 8)
    ChrSetSubChip(0x0022, 0)
    ChrSetPos(0x0022, 7820, 0, -680, 270)
    PlayEffect(0x00, 0x00, 0x0022, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_D539')
    def lambda_D539():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 200)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_D539)

    WaitForThreadExit(0x0022, 0x0002)
    PlaySE(164, 0x00, 0x64)
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
        'loc_D592',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_D5D0')

    def _loc_D592(): pass

    label('loc_D592')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D5B9',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_D5D0')

    def _loc_D5B9(): pass

    label('loc_D5B9')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_D5D0(): pass

    label('loc_D5D0')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D5FC',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_D63A')

    def _loc_D5FC(): pass

    label('loc_D5FC')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D623',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_D63A')

    def _loc_D623(): pass

    label('loc_D623')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_D63A(): pass

    label('loc_D63A')

    Sleep(1000)

    @scena.Lambda('lambda_D645')
    def lambda_D645():
        ChrSetDirection(0x00FE, 90, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_D645)

    Sleep(50)

    @scena.Lambda('lambda_D658')
    def lambda_D658():
        ChrSetDirection(0x00FE, 90, 600)

        ExitThread()

    DispatchAsync(0x00F8, 0x0003, lambda_D658)

    Sleep(50)

    @scena.Lambda('lambda_D66B')
    def lambda_D66B():
        ChrSetDirection(0x00FE, 90, 600)

        ExitThread()

    DispatchAsync(0x00F9, 0x0003, lambda_D66B)

    WaitForThreadExit(0x00F9, 0x0003)

    @scena.Lambda('lambda_D67E')
    def lambda_D67E():
        CameraSetDistance(1700, 25000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_D67E)

    Sleep(500)

    ChrTalk(
        0x0022,
        (
            '#0020411242V#1058F#5P……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411243V#1020F#6P#3S！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D72C',
    )

    ChrTalk(
        0x010F,
        (
            '#0100411244V#177F约修亚君……！　　　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D72C(): pass

    label('loc_D72C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D764',
    )

    ChrTalk(
        0x010B,
        (
            '#0090411245V#216F#6P不、不会的……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D764(): pass

    label('loc_D764')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D79B',
    )

    ChrTalk(
        0x0105,
        (
            '#0060411246V#1163F#6P怎、怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D79B(): pass

    label('loc_D79B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D7CF',
    )

    ChrTalk(
        0x0107,
        (
            '#0070321381V#065F#6P哥、哥哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D7CF(): pass

    label('loc_D7CF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D803',
    )

    ChrTalk(
        0x0103,
        (
            '#0030411248V#523F#6P难不成……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D803(): pass

    label('loc_D803')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D847',
    )

    ChrTalk(
        0x0110,
        (
            '#0110411249V#271F被操纵了吗……！　　　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D847(): pass

    label('loc_D847')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D881',
    )

    ChrTalk(
        0x0104,
        (
            '#0040411250V#039F#6P竟然来这一手……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D881(): pass

    label('loc_D881')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D8B3',
    )

    ChrTalk(
        0x0106,
        (
            '#0050411251V#054F#6P混蛋……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D8B3(): pass

    label('loc_D8B3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D8E7',
    )

    ChrTalk(
        0x0108,
        (
            '#0080411252V#077F#6P真可恶……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D8E7(): pass

    label('loc_D8E7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DA11',
    )

    ChrTalk(
        0x0109,
        (
            '#0180411253V#1069F#6P歪门邪道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180411254V已经植入深层意识\n',
            '的最底层了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0150411255V#1150F#5P呵呵，你好像是\n',
            '『骑士团』的新兵吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150411256V#1151F那你应该了解，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150411257V我的『绝对暗示』\n',
            '是一种什么样的法术。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180411258V#1067F#6P…………唔…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DA11(): pass

    label('loc_DA11')

    ChrTalk(
        0x0101,
        (
            '#0010411259V#1025F#6P#40W约修亚……不会的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010411260V#40W喂……\n',
            '回到这边来啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0020411261V#1058F#5P……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010411262V#1023F#6P#3S求求你……\n',
            '别用那样的眼神看我！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0151850004V#1154F#5P呵呵，不要做无用功了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150411263V#1151F当年我在\n',
            '修复约修亚已经破碎的心时，\n',
            '对他刻下了源于『绝对暗示』的法术。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150411264V那时我给他刻下的『圣痕』\n',
            '至今还在他的深层意识里沉睡。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150411265V它拥有巨大的影响力，只要一做动，\n',
            '可以轻松地控制他的身体。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411266V#1026F#6P………怎么会…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0150411267V#1151F#5P哦，顺便说一下，\n',
            '约修亚肩上的徽章不是刺青。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150411268V而是我在他身上埋下的\n',
            '『圣痕』的具现化。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150411269V#1154F哼哼哼……\n',
            '随着记忆的恢复而出现了，\n',
            '他想必也感到很不安吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411270V#1027F#6P…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010411271V……你，撒谎。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010411272V将约修亚折磨得这么惨，\n',
            '却说要还给他自由……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010411273V结果……仍然是撒谎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0150411274V#1153F#5P我可没有撒谎。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150411275V#1154F如果约修亚没和你\n',
            '一起来到这里的话，\n',
            '我也不会这么做。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150411276V#1151F呵呵……这都是\n',
            '你自己所选择的道路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411277V#1022F#6P！……别开玩笑了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010411278V你没有资格\n',
            '对我们所选择的道路\n',
            '妄加指责！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 6)
    OP_0D()
    Sleep(200)

    Fade(250)
    PlaySE(213, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DEF4',
    )

    ChrSetChipByIndex(0x0103, 11)

    def _loc_DEF4(): pass

    label('loc_DEF4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DF07',
    )

    ChrSetChipByIndex(0x0104, 13)

    def _loc_DF07(): pass

    label('loc_DF07')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DF1A',
    )

    ChrSetChipByIndex(0x0105, 15)

    def _loc_DF1A(): pass

    label('loc_DF1A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DF2D',
    )

    ChrSetChipByIndex(0x0106, 17)

    def _loc_DF2D(): pass

    label('loc_DF2D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DF40',
    )

    ChrSetChipByIndex(0x0107, 19)

    def _loc_DF40(): pass

    label('loc_DF40')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DF53',
    )

    ChrSetChipByIndex(0x0108, 21)

    def _loc_DF53(): pass

    label('loc_DF53')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DF66',
    )

    ChrSetChipByIndex(0x0109, 23)

    def _loc_DF66(): pass

    label('loc_DF66')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DF79',
    )

    ChrSetChipByIndex(0x010B, 25)

    def _loc_DF79(): pass

    label('loc_DF79')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DF8C',
    )

    ChrSetChipByIndex(0x010F, 36)

    def _loc_DF8C(): pass

    label('loc_DF8C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DF9F',
    )

    ChrSetChipByIndex(0x0110, 34)

    def _loc_DF9F(): pass

    label('loc_DF9F')

    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010411279V#1023F#6P就算你操纵了约修亚，\n',
            '我也不会在这里放弃！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010411280V我一定会打倒你\n',
            '并救出约修亚！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0150411281V#1154F#5P呵呵……这就对了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150411282V#1151F不过，我现在\n',
            '可是有重任在身，就不奉陪了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150411283V我会在『根源区域』等你们的，\n',
            '一定要来拜访哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0009, 5)
    ChrSetSubChip(0x0009, 0)
    PlayEffect(0x04, 0x00, 0x0009, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010411284V#1020F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0020411285V#1058F#5P……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0009, 0x00, 0x04, 2000)
    PlaySE(216, 0x00, 0x64)
    OP_99(0x0009, 0x05, 0x09, 2000)
    Sleep(300)

    PlaySE(153, 0x00, 0x64)
    PlaySE(184, 0x00, 0x64)
    PlayEffect(0x01, 0x01, 0x0009, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_E1C7')
    def lambda_E1C7():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_E1C7)

    Sleep(300)

    PlayEffect(0x01, 0x02, 0x0022, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_E213')
    def lambda_E213():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_E213)

    WaitForThreadExit(0x0022, 0x0002)
    WaitEffect(0x01, 0x02)
    WaitEffect(0x02, 0x02)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x0022, 0x0080)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010411286V#1020F#6P啊啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Sleep(100)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetSubChip(0x00F8, 0)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetSubChip(0x00F9, 0)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E2CA',
    )

    ChrTalk(
        0x010B,
        (
            '#0090411287V#216F#6P约修亚……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E2CA(): pass

    label('loc_E2CA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E2FF',
    )

    ChrTalk(
        0x0105,
        (
            '#0060411288V#1163F#6P约修亚……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E2FF(): pass

    label('loc_E2FF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E333',
    )

    ChrTalk(
        0x0107,
        (
            '#0070411289V#065F#6P约修亚哥哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E333(): pass

    label('loc_E333')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E3A6',
    )

    ChrTalk(
        0x0109,
        (
            '#0180411290V#1063F#6P可恶……麻烦了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180411291V#1067F但是，要怎么去\n',
            '『根源区域』呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E65A')

    def _loc_E3A6(): pass

    label('loc_E3A6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E42F',
    )

    ChrTalk(
        0x010F,
        (
            '#0100411292V#175F糟了……情况不妙……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100411293V#178F可是，到底该怎么\n',
            '找到所谓的『根源区域』呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E65A')

    def _loc_E42F(): pass

    label('loc_E42F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E4A0',
    )

    ChrTalk(
        0x0108,
        (
            '#0080411294V#072F#6P……这可麻烦了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080411295V#572F但是，要怎么去\n',
            '『根源区域』呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E65A')

    def _loc_E4A0(): pass

    label('loc_E4A0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E515',
    )

    ChrTalk(
        0x0106,
        (
            '#0050411296V#057F#6P嘁……这还真麻烦了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050411297V#552F但是，要怎么去\n',
            '『根源区域』呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E65A')

    def _loc_E515(): pass

    label('loc_E515')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E585',
    )

    ChrTalk(
        0x0104,
        (
            '#0040411298V#032F#6P……真是出现危机了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040411299V可是，要怎么去\n',
            '『根源区域』呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E65A')

    def _loc_E585(): pass

    label('loc_E585')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E5F4',
    )

    ChrTalk(
        0x0103,
        (
            '#0030411300V#022F#6P可恶……不妙了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030411301V#522F但是，要怎么去\n',
            '『根源区域』呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E65A')

    def _loc_E5F4(): pass

    label('loc_E5F4')

    ChrTalk(
        0x0101,
        (
            '#0010411302V#1027F#6P可恶……得早点把约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010411303V但、但是要怎么去\n',
            '『根源区域』呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E65A(): pass

    label('loc_E65A')

    LoadChip('ED6_DT26/CH20417._CH', 'ED6_DT26/CH20417P._CP', 0)
    OP_C0(0x17, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)

    ChrTalk(
        0x0008,
        (
            '#0140411304V#2P#30W……用……\n',
            '里面的大型升降梯……',
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
        'loc_E701',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_E73F')

    def _loc_E701(): pass

    label('loc_E701')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E728',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_E73F')

    def _loc_E728(): pass

    label('loc_E728')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_E73F(): pass

    label('loc_E73F')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E76B',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_E7A9')

    def _loc_E76B(): pass

    label('loc_E76B')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E792',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_E7A9')

    def _loc_E792(): pass

    label('loc_E792')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_E7A9(): pass

    label('loc_E7A9')

    Sleep(1000)

    @scena.Lambda('lambda_E7B4')
    def lambda_E7B4():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_E7B4)

    @scena.Lambda('lambda_E7C2')
    def lambda_E7C2():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_E7C2)

    ChrTurnDirection(0x00F9, 0x0008, 400)
    Fade(500)
    OP_6E(319, 0)
    CameraMove(970, -370, 3880, 0)
    OP_67(0, 4910, -10000, 0)
    CameraSetDistance(2720, 0)
    OP_6C(44000, 0)
    OP_6E(319, 0)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetSubChip(0x0008, 0)
    ChrSetPos(0x0008, -400, -370, 3100, 0)
    CreateThread(0x0101, 0x01, 0x01, func_0C_26D5)
    Sleep(100)

    CreateThread(0x00F9, 0x01, 0x01, func_0E_277C)
    Sleep(100)

    CreateThread(0x00F8, 0x01, 0x01, func_0D_2712)
    OP_9E(0x0008, 15, 0, 300, 3000)
    OP_99(0x0008, 0x00, 0x05, 1000)
    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010411305V#1025F#2P莱维……！\n',
            '太好了，你没事啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010411306V#1002F里面的大型升降梯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_E908')
    def lambda_E908():
        CameraMove(-40, 4010, 32640, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_E908)

    @scena.Lambda('lambda_E920')
    def lambda_E920():
        OP_67(0, 9130, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_E920)

    @scena.Lambda('lambda_E938')
    def lambda_E938():
        CameraSetDistance(4230, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_E938)

    @scena.Lambda('lambda_E948')
    def lambda_E948():
        OP_6E(340, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_E948)

    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010411307V#1020F莫非是……\n',
            '那块大的金属板！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(970, -370, 3880, 0)
    OP_67(0, 4910, -10000, 0)
    CameraSetDistance(2720, 0)
    OP_6C(44000, 0)
    OP_6E(319, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140411308V#121F#5P#30W乘坐它的话，应该可以……\n',
            '……下降到沉睡着『环』的『根源区域』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411309V快……已经没有时间了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411310V#1005F#2P明、明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_EA90')
    def lambda_EA90():
        OP_7C(10, 10, 1000, 1000)
        Yield()

        Jump('lambda_EA90')

    DispatchAsync2(0x0101, 0x0003, lambda_EA90)

    PlaySE(344, 0x01, 0x28)
    Sleep(200)

    OP_24(0x0158, 0x32)
    Sleep(200)

    OP_24(0x0158, 0x3C)
    Sleep(200)

    OP_24(0x0158, 0x46)
    Sleep(200)

    OP_24(0x0158, 0x50)
    Sleep(200)

    Call(1, 0x0002)

    Return()

# id: 0x001E offset: 0xEAD8
@scena.Code('func_1E_EAD8')
def func_1E_EAD8():
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
        (0x00000000, 'loc_EB52'),
        (0x00000001, 'loc_EB58'),
        (-1, 'loc_EB5E'),
    )

    def _loc_EB52(): pass

    label('loc_EB52')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_EB5E')

    def _loc_EB58(): pass

    label('loc_EB58')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_EB5E')

    def _loc_EB5E(): pass

    label('loc_EB5E')

    Return()

# id: 0x001F offset: 0xEB5F
@scena.Code('func_1F_EB5F')
def func_1F_EB5F():
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
