#pragma once

#include "esphome/core/component.h"
#include "esphome/components/sensor/sensor.h"
#include "../miot/miot.h"

namespace esphome {
namespace miot_ptx_yk1_qmimb {

#define PRODUCT_ID_PTX_YK1_QMIMB 0x38bb

class MiotPTX_YK1_QMIMB : public miot::MiotComponent, public sensor::Sensor{
 public:
  MiotPTX_YK1_QMIMB() { this->product_id_ = PRODUCT_ID_PTX_YK1_QMIMB; }

  void dump_config() override;

 protected:
  bool process_object_(const miot::BLEObject &obj) override;
};

}  // namespace miot_ptx_yk1_qmimb
}  // namespace esphome
