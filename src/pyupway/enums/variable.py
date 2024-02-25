from enum import Enum

class Variable(Enum):
    """
    Provides Variable name - Variable ID mapping as enum
    """

    AVG_OUTDOOR_TEMP = 40067
    HOT_WATER_CHARGING = 40014                  # TehoWatti AIR
    HOT_WATER_TOP = 40013                       # TehoWatti AIR
    INDOOR_UNIT_OUTDOOR_TEMP = 40004
    CURRENT_BE1 = 40083
    CURRENT_BE2 = 40081
    CURRENT_BE3 = 40079
    MYUPWAY_DEGREE_MINUTES = 43005
    EXTERNAL_ADJUSTMENT = 43161
    FLOOR_DRYING_FUNCTION = 47276
    CALCULATED_FLOW_TEMP = 43009
    EXTERNAL_FLOW_TEMP = 40071
    EXTERNAL_RETURN_TEMP = 40152
    HEAT_MEDIUM_FLOW = 40008                    # TehoWatti AIR
    HEAT_RETURN_TEMP = 40012                    # TehoWatti AIR
    ROOM_TEMPERATURE = 40033
    ADDITION_BLOCKED = 10033
    ADDITION_MAX_STEP = 47613
    ADDITION_STATUS = 43091
    ADDITION_FUSE_SIZE = 47214
    ADDITION_TIME_FACTOR = 43081                # TehoWatti AIR
    ADDITION_ELECTRICAL_ADDITION_POWER = 43084  # TehoWatti AIR
    ADDITION_SET_MAX_ELECTRICAL_ADD = 47212     # TehoWatti AIR
    ADDITION_TEMPERATURE = 40121                # TehoWatti AIR
    ENERGY_COOLING_COMPRESSOR_ONLY = 44302      # TehoWatti AIR
    ENERGY_HEATING_COMPRESSOR_ONLY = 44308      # TehoWatti AIR
    ENERGY_HEATING_INT_ADD_INCL = 44300         # TehoWatti AIR
    ENERGY_HOTWATER_COMPRESSOR_ONLY = 44306     # TehoWatti AIR
    ENERGY_HW_INCL_INT_ADD = 44298              # TehoWatti AIR
    ENERGY_POOL_COMPRESSOR_ONLY = 44304         # TehoWatti AIR
    ENERGY_FLOW = 40072                         # TehoWatti AIR
    AUX1 = 47411
    AUX2 = 47410
    AUX3 = 47409
    AUX4 = 47408
    AUX5 = 47407
    AUX6 = 48366
    X7 = 47412
    COUNTRY = 48745
    DEFROSTING = 44703
    CHARGE_PUMP_SPEED = 44396
    OUTDOOR_UNIT_OUTDOOR_TEMP = 44362
    COMPRESSOR_BLOCKED = 10014
    COMPRESSOR_STARTS = 44069
    COMPRESSOR_PROTECTION_MODE = 44702
    CONDENSER_OUT = 44058
    EVAPORATOR = 44363
    HOT_GAS = 44059
    LIQUID_LINE = 44060
    RETURN_TEMP = 44055
    SUCTION_GAS = 44061
    HIGH_PRESSURE_SENSOR = 44699
    LOW_PRESSURE_SENSOR = 44700
    COMPRESSOR_OPERATING_TIME = 44071
    COMPRESSOR_OPERATING_TIME_HOT_WATER = 44073
    COMPRESSOR_RUN_TIME_COOLING = 40737
    CURRENT_COMPRESSOR_FREQUENCY = 44701
    REQUESTED_COMPRESSOR_FREQUENCY = 40782
    VERSION = 44014
    SMART_PRICE_STATUS = 44908          # Metro-air 330
    SMART_PRICE_VALUE = 10069             # Metro-air 330
    SMART_PRICE_FACTOR = 44896          # Metro-air 330
    SUPPLY_LINE = 40047                 # MYUPLINK
    RETURN_LINE = 40048                 # MYUPLINK
    OIL_TEMPERATURE_EP15_BT29 = 40145   # MYUPLINK
    OIL_TEMPERATURE_BT29 = 40146        # MYUPLINK
    MYUPLINK_DEGREE_MINUTES = 40940     # MYUPLINK
    SLAVE_EB101 = 44032                 # MYUPLINK
    STATUS_COMPRESSOR_EB101 = 44064     # MYUPLINK
    CHARGE_PUMP_EB101_GP12 = 49996      # MYUPLINK