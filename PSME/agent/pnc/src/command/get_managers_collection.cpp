/*!
 * @copyright
 * Copyright (c) 2015-2018 Intel Corporation
 *
 * @copyright
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * @copyright
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * @copyright
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * @file command/stubs/get_managers_collection.cpp
 * @brief GetManagersCollection stub implementation
 * */

#include "agent-framework/module/common_components.hpp"
#include "agent-framework/command/registry.hpp"
#include "agent-framework/command/pnc_commands.hpp"

using namespace agent_framework::command;
using namespace agent_framework::module;
using namespace agent_framework::model;

REGISTER_COMMAND(GetManagersCollection,
                 [](const GetManagersCollection::Request&, GetManagersCollection::Response& rsp) {
        auto keys = get_manager<Manager>().get_keys();
        for (const auto& key : keys) {
            rsp.add_entry(agent_framework::model::attribute::ManagerEntry{key});
        }
                     log_debug("pnc-gami", "Getting ManagersCollection successful.");
    }
);
