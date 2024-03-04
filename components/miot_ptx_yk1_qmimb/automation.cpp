#include "esphome/core/log.h"
#include "automation.h"

namespace esphome {
namespace miot_ptx_yk1_qmimb {

static const char *const TAG = "miot_ptx_yk1_qmimb.automation";

bool MiotPTX_YK1_QMIMBTrigger::process_object_(const miot::BLEObject &obj) {
  if (obj.id == this->event_id_)
  {
    this->trigger();
    return true;
  }
  return this->process_unhandled_(obj);
}

}  // namespace miot_ptx_yk1_qmimb
}  // namespace esphome
