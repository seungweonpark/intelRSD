/*!
 * @brief Implementation of GetChassisInfo command.
 *
 * @header{License}
 * @copyright Copyright (c) 2017-2018 Intel Corporation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * @header{Files}
 * @file get_chassis_info.cpp
 */

#include "nvme_agent_commands.hpp"
#include "agent-framework/module/common_components.hpp"

using namespace agent::nvme;
using namespace agent_framework;

REGISTER_NVME_COMMAND(GetChassisInfo,
    [] (GetChassisInfo::ContextPtr, const GetChassisInfo::Request& req, GetChassisInfo::Response& rsp) {
        log_debug("nvme-discovery-agent", "Getting chassis info.");
        rsp = module::get_manager<model::Chassis>().get_entry(req.get_uuid());
    }
);
