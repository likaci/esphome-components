#pragma once

#include "esphome/core/automation.h"
#include "../miot/miot.h"
#include "miot_ptx_yk1_qmimb.h"

namespace esphome {
namespace miot_ptx_yk1_qmimb {

class MiotPTX_YK1_QMIMBTrigger : public Trigger<>, public miot::MiotListener {
 public:
  explicit MiotPTX_YK1_QMIMBTrigger(miot::MIID event_id) : event_id_(event_id) { this->product_id_ = PRODUCT_ID_PTX_YK1_QMIMB; }

 protected:
  miot::MIID event_id_;
  bool process_object_(const miot::BLEObject &obj) override;
};

}  // namespace miot_ptx_yk1_qmimb
}  // namespace esphome
