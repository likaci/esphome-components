import esphome.codegen as cg
import esphome.config_validation as cv
from esphome import automation
from esphome.const import (
    CONF_ON_CLICK,
    CONF_ON_DOUBLE_CLICK,
    CONF_TRIGGER_ID,
)
from .. import miot  # pylint: disable=relative-beyond-top-level

CONF_BUTTON = "button"
CONF_ON_LONG_PRESS = "on_long_press"

CODEOWNERS = ["@dentra"]
AUTO_LOAD = ["miot"]

miot_ptx_yk1_qmimb_ns = cg.esphome_ns.namespace("miot_ptx_yk1_qmimb")
MiotPTX_YK1_QMIMB = miot_ptx_yk1_qmimb_ns.class_("MiotPTX_YK1_QMIMB", miot.MiotComponent)
MiotPTX_YK1_QMIMBTrigger = miot_ptx_yk1_qmimb_ns.class_(
    "MiotPTX_YK1_QMIMBTrigger", automation.Trigger.template(), miot.MiotListener
)
MIID = miot.miot_ns.namespace("MIID")

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(MiotPTX_YK1_QMIMB),
        cv.Optional(CONF_ON_CLICK): automation.validate_automation(
            cv.Schema(
                {
                    cv.GenerateID(CONF_TRIGGER_ID): cv.declare_id(MiotPTX_YK1_QMIMBTrigger),
                }
            ),
        ),
        cv.Optional(CONF_ON_DOUBLE_CLICK): automation.validate_automation(
            cv.Schema(
                {
                    cv.GenerateID(CONF_TRIGGER_ID): cv.declare_id(MiotPTX_YK1_QMIMBTrigger),
                }
            ),
        ),
        cv.Optional(CONF_ON_LONG_PRESS): automation.validate_automation(
            cv.Schema(
                {
                    cv.GenerateID(CONF_TRIGGER_ID): cv.declare_id(MiotPTX_YK1_QMIMBTrigger),
                }
            ),
        ),
    },
).extend(miot.MIOT_BLE_DEVICE_SCHEMA)


async def new_trigger_(config, field, button_type):
    for conf in config.get(field, []):
        trigger = cg.new_Pvariable(conf[CONF_TRIGGER_ID], button_type)
        await miot.register_miot_device(trigger, config)
        await miot.setup_device_core_(trigger, config)
        await automation.build_automation(trigger, [], conf)


async def to_code(config):
    """Code generation entry point"""
    await miot.new_device(config)
    await new_trigger_(config, CONF_ON_CLICK, MIID.MIID_BUTTON_EVENT_PTX_CLICK)
    await new_trigger_(config, CONF_ON_DOUBLE_CLICK, MIID.MIID_BUTTON_EVENT_PTX_DOUBLE_CLICK)
    await new_trigger_(config, CONF_ON_LONG_PRESS, MIID.MIID_BUTTON_EVENT_PTX_LONG_PRESS)
