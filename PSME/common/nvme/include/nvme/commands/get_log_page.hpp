/*!
 * @header{License}
 * @copyright Copyright (c) 2017-2018 Intel Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * @header{Filesystem}
 * @file nvme/commands/get_log_page.hpp
 */

#pragma once

#include "nvme/commands/generic_nvme_command.hpp"

namespace nvme {
namespace commands {

class GetLogPage final : public GenericNvmeCommand {
public:

    static constexpr uint16_t BUFFER_SIZE = 512;

    /*!
     * @brief Constructs a valid GetLogPage command
     * @param namespace_id Id of the affected namespace
     * @param log_page_id Id of the log page
     */
    GetLogPage(uint32_t namespace_id, LogPageId log_page_id);

    virtual ~GetLogPage();

    /*!
     * @brief Returns log interpreted as smart log
     * @return Smart log
     */
    const LogPageSmart& get_smart_log() const {
        return m_log_smart;
    }

    /*!
     * @brief Returns log interpreted as smart log
     * @return Smart log
     */
    const LogPageFirmware& get_firmware_log() const {
        return m_log_firmware;
    }

private:

    union {
        LogPageSmart m_log_smart;
        LogPageFirmware m_log_firmware;
        uint8_t m_raw_buffer[BUFFER_SIZE]{};
    };

};

}
}
