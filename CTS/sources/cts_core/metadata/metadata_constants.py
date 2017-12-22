"""
 * @section LICENSE
 *
 * @copyright
 * Copyright (c) 2017 Intel Corporation
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
 * @section DESCRIPTION
"""


class MetadataConstants1_2:
    SERVICE_ROOT_URI = "/redfish/v1"
    SERVICE_ROOT = "ServiceRoot.ServiceRoot"
    CHASSIS = "Chassis.1.0.0.Chassis"
    THERMAL_ZONE = "ThermalZone.1.0.0.ThermalZone"
    POWER_ZONE = "PowerZone.1.0.0.PowerZone"
    POWER = "Power.v1_1_0.Power"
    COMPUTER_SYSTEM = "ComputerSystem.ComputerSystem"
    COMPUTER_SYSTEM_1_0_0 = "ComputerSystem.1.0.0.ComputerSystem"
    PROCESSOR = "Processor.Processor"
    ETHERNET_INTERFACE = "EthernetInterface.EthernetInterface"
    SIMPLE_STORAGE = "SimpleStorage.SimpleStorage"
    DIMM_CONFIG = "DimmConfig.DimmConfig"
    MEMORY_CHUNK = "MemoryChunk.MemoryChunk"
    MANAGER = "Manager.Manager"
    MANAGER_NETWORK_PROTOCOL = "ManagerNetworkProtocol"
    ETHERNET_SWITCH = "EthernetSwitch.1.0.0.EthernetSwitch"
    ETHERNET_SWITCH_PORT = "EthernetSwitchPort.1.0.0.EthernetSwitchPort"
    STORAGE_SERVICE = "StorageService.1.0.0.StorageService"
    STORAGE_SERVICE_COLLECTION = "StorageServiceCollection.StorageServiceCollection"
    LOGICAL_DRIVE = "LogicalDrive.1.0.0.LogicalDrive"
    LOGICAL_DRIVE_COLLECTION = "LogicalDriveCollection.LogicalDriveCollection"
    REMOTE_TARGET = "RemoteTarget.1.0.0.RemoteTarget"
    REMOTE_TARGET_COLLECTION = "RemoteTargetCollection.RemoteTargetCollection"
    VLAN_NETWORK_INTERFACE = "VLanNetworkInterface.1.0.0.VLanNetworkInterface"
    VLAN_NETWORK_INTERFACE_COLLECTION = "VLanNetworkInterfaceCollection.VLanNetworkInterfaceCollection"
    STATIC_MAC = "EthernetSwitchStaticMAC.1.0.0.EthernetSwitchStaticMAC"
    STATIC_MAC_COLLECTION = "EthernetSwitchStaticMACCollection.EthernetSwitchStaticMACCollection"

class MetadataConstants_RMM_1_2:
    SERVICE_ROOT_URI = "/redfish/v1"
    SERVICE_ROOT = "ServiceRoot.ServiceRoot"

class MetadataConstants2_1:
    SERVICE_ROOT_URI = "/redfish/v1"
    SERVICE_ROOT = "ServiceRoot.v1_0_0.ServiceRoot"
    CHASSIS = "Chassis.v1_0_0.Chassis"
    CHASSIS_COLLECTION = "ChassisCollection.ChassisCollection"
    COMPOSED_NODE = "ComposedNode.ComposedNode"
    COMPOSED_NODE_COLLECTION = "ComposedNodeCollection.ComposedNodeCollection"
    THERMAL_ZONE = "ThermalZone.v1_0_0.ThermalZone"
    THERMAL_ZONE_COLLECTION = "ThermalZoneCollection.ThermalZoneCollection"
    POWER_ZONE = "PowerZone.v1_0_0.PowerZone"
    POWER_ZONE_COLLECTION = "PowerZoneCollection.PowerZoneCollection"
    POWER = "Power.v1_1_0.Power"
    COMPUTER_SYSTEM = "ComputerSystem.ComputerSystem"
    COMPUTER_SYSTEM_1_0_0 = "ComputerSystem.v1_0_0.ComputerSystem"
    COMPOSED_SYSTEM_COLLECTION = "ComputerSystemCollection.ComputerSystemCollection"
    PROCESSOR = "Processor.Processor"
    PROCESSOR_COLLECTION = "ProcessorCollection.ProcessorCollection"
    ETHERNET_INTERFACE = "EthernetInterface.EthernetInterface"
    SIMPLE_STORAGE = "SimpleStorage.SimpleStorage"
    DIMM_CONFIG = "DimmConfig.DimmConfig"
    MEMORY = "Memory.Memory"
    MEMORY_COLLECTION = "MemoryCollection.MemoryCollection"
    MEMORY_CHUNK = "MemoryChunk.MemoryChunk"
    MANAGER = "Manager.Manager"
    MANAGER_NETWORK_PROTOCOL = "ManagerNetworkProtocol"
    MANAGER_COLLECTION = "ManagerCollection.ManagerCollection"
    ETHERNET_SWITCH = "EthernetSwitch.v1_0_0.EthernetSwitch"
    ETHERNET_SWITCH_COLLECTION = "EthernetSwitchCollection.EthernetSwitchCollection"
    ETHERNET_SWITCH_ACL = "EthernetSwitchACL.v1_0_0.EthernetSwitchACL"
    ETHERNET_SWITCH_ACL_COLLECTION = "EthernetSwitchACLCollection.EthernetSwitchACLCollection"
    ETHERNET_SWITCH_ACL_RULE = "EthernetSwitchACLRule.v1_0_0.EthernetSwitchACLRule"
    ETHERNET_SWITCH_ACL_RULE_COLLECTION = "EthernetSwitchACLRuleCollection.EthernetSwitchACLRuleCollection"
    ETHERNET_SWITCH_PORT = "EthernetSwitchPort.v1_0_0.EthernetSwitchPort"
    LOGICAL_DRIVE = "LogicalDrive.v1_0_0.LogicalDrive"
    LOGICAL_DRIVE_COLLECTION = "LogicalDriveCollection.LogicalDriveCollection"
    REMOTE_TARGET_COLLECTION = "RemoteTargetCollection.RemoteTargetCollection"
    REMOTE_TARGET = "RemoteTarget.v1_0_0.RemoteTarget"
    VLAN_NETWORK_INTERFACE = "VLanNetworkInterface.v1_0_0.VLanNetworkInterface"
    VLAN_NETWORK_INTERFACE_COLLECTION = "VLanNetworkInterfaceCollection.VLanNetworkInterfaceCollection"
    STATIC_MAC = "EthernetSwitchStaticMAC.v1_0_0.EthernetSwitchStaticMAC"
    STATIC_MAC_COLLECTION = "EthernetSwitchStaticMACCollection.EthernetSwitchStaticMACCollection"
    ENDPOINT_COLLECTION = "EndpointCollection.EndpointCollection"
    FABRIC_COLLECTION = "FabricCollection.FabricCollection"
    PORT = "Port.Port"
    PORT_COLLECTION = "PortCollection.PortCollection"
    SWITCH_COLLECTION = "SwitchCollection.SwitchCollection"
    ZONE_COLLECTION = "ZoneCollection.ZoneCollection"
    EVENT_DESTINATION_COLLECTION = "EventDestinationCollection.EventDestinationCollection"
    EVENT_SERVICE = "EventService.EventService"
    TASK_COLLECTION = "TaskCollection.TaskCollection"
    TASK_SERVICE = "TaskService.TaskService"
    STORAGE_SERVICE = "StorageService.v1_0_0.StorageService"
    STORAGE_SERVICE_COLLECTION = "StorageServiceCollection.StorageServiceCollection"



class MetadataConstants_RMM_2_1:
    SERVICE_ROOT_URI = "/redfish/v1"
    SERVICE_ROOT = "ServiceRoot.ServiceRoot"

class MetadataConstants2_2:
    SERVICE_ROOT_URI = "/redfish/v1"
    SERVICE_ROOT = "ServiceRoot.v1_0_0.ServiceRoot"
    CHASSIS = "Chassis.v1_0_0.Chassis"
    CHASSIS_COLLECTION = "ChassisCollection.ChassisCollection"
    COMPOSED_NODE = "ComposedNode.ComposedNode"
    COMPOSED_NODE_COLLECTION = "ComposedNodeCollection.ComposedNodeCollection"
    THERMAL_ZONE = "ThermalZone.v1_0_0.ThermalZone"
    THERMAL_ZONE_COLLECTION = "ThermalZoneCollection.ThermalZoneCollection"
    POWER_ZONE = "PowerZone.v1_0_0.PowerZone"
    POWER_ZONE_COLLECTION = "PowerZoneCollection.PowerZoneCollection"
    POWER = "Power.v1_1_0.Power"
    COMPUTER_SYSTEM = "ComputerSystem.ComputerSystem"
    COMPUTER_SYSTEM_1_0_0 = "ComputerSystem.v1_0_0.ComputerSystem"
    COMPOSED_SYSTEM_COLLECTION = "ComputerSystemCollection.ComputerSystemCollection"
    PROCESSOR = "Processor.Processor"
    PROCESSOR_COLLECTION = "ProcessorCollection.ProcessorCollection"
    ETHERNET_INTERFACE = "EthernetInterface.EthernetInterface"
    SIMPLE_STORAGE = "SimpleStorage.SimpleStorage"
    DIMM_CONFIG = "DimmConfig.DimmConfig"
    MEMORY = "Memory.Memory"
    MEMORY_COLLECTION = "MemoryCollection.MemoryCollection"
    MEMORY_CHUNK = "MemoryChunk.MemoryChunk"
    MANAGER = "Manager.Manager"
    MANAGER_NETWORK_PROTOCOL = "ManagerNetworkProtocol"
    MANAGER_COLLECTION = "ManagerCollection.ManagerCollection"
    ETHERNET_SWITCH = "EthernetSwitch.v1_0_0.EthernetSwitch"
    ETHERNET_SWITCH_COLLECTION = "EthernetSwitchCollection.EthernetSwitchCollection"
    ETHERNET_SWITCH_ACL = "EthernetSwitchACL.v1_0_0.EthernetSwitchACL"
    ETHERNET_SWITCH_ACL_COLLECTION = "EthernetSwitchACLCollection.EthernetSwitchACLCollection"
    ETHERNET_SWITCH_ACL_RULE = "EthernetSwitchACLRule.v1_0_0.EthernetSwitchACLRule"
    ETHERNET_SWITCH_ACL_RULE_COLLECTION = "EthernetSwitchACLRuleCollection.EthernetSwitchACLRuleCollection"
    ETHERNET_SWITCH_PORT = "EthernetSwitchPort.v1_0_0.EthernetSwitchPort"
    LOGICAL_DRIVE = "LogicalDrive.v1_0_0.LogicalDrive"
    LOGICAL_DRIVE_COLLECTION = "LogicalDriveCollection.LogicalDriveCollection"
    REMOTE_TARGET_COLLECTION = "RemoteTargetCollection.RemoteTargetCollection"
    REMOTE_TARGET = "RemoteTarget.v1_0_0.RemoteTarget"
    VLAN_NETWORK_INTERFACE = "VLanNetworkInterface.v1_0_0.VLanNetworkInterface"
    VLAN_NETWORK_INTERFACE_COLLECTION = "VLanNetworkInterfaceCollection.VLanNetworkInterfaceCollection"
    STATIC_MAC = "EthernetSwitchStaticMAC.v1_0_0.EthernetSwitchStaticMAC"
    STATIC_MAC_COLLECTION = "EthernetSwitchStaticMACCollection.EthernetSwitchStaticMACCollection"
    ENDPOINT_COLLECTION = "EndpointCollection.EndpointCollection"
    FABRIC_COLLECTION = "FabricCollection.FabricCollection"
    PORT = "Port.Port"
    PORT_COLLECTION = "PortCollection.PortCollection"
    SWITCH_COLLECTION = "SwitchCollection.SwitchCollection"
    ZONE_COLLECTION = "ZoneCollection.ZoneCollection"
    EVENT_DESTINATION_COLLECTION = "EventDestinationCollection.EventDestinationCollection"
    EVENT_SERVICE = "EventService.EventService"
    TASK_COLLECTION = "TaskCollection.TaskCollection"
    TASK_SERVICE = "TaskService.TaskService"
    STORAGE_SERVICE = "StorageService.v1_0_0.StorageService"
    STORAGE_SERVICE_COLLECTION = "StorageServiceCollection.StorageServiceCollection"



class MetadataConstants_RMM_2_2:
    SERVICE_ROOT_URI = "/redfish/v1"
    SERVICE_ROOT = "ServiceRoot.ServiceRoot"