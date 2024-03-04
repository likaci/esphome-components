#include "esphome/core/log.h"
#include "miot_ptx_yk1_qmimb.h"

namespace esphome {
namespace miot_ptx_yk1_qmimb {

static const char *const TAG = "miot_ptx_yk1_qmimb";

void MiotPTX_YK1_QMIMB::dump_config() { this->dump_config_(TAG, "PTX_YK1_QMIMB"); }

bool MiotPTX_YK1_QMIMB::process_object_(const miot::BLEObject &obj) {
  switch (obj.id) {
    case miot::MIID_BUTTON_EVENT_PTX_CLICK:
      this->publish_state(miot::MIID_BUTTON_EVENT_PTX_CLICK);
      return true;
    case miot::MIID_BUTTON_EVENT_PTX_DOUBLE_CLICK:
    case miot::MIID_BUTTON_EVENT_PTX_LONG_PRESS:
      // processed by automation
      return false;
    default:
      return this->process_default_(obj);
  }
  return false;
}

}  // namespace miot_ptx_yk1_qmimb
}  // namespace esphome
