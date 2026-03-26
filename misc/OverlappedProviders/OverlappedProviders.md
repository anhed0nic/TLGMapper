# Overlapped ETW Providers: TraceLogging vs Manifest-based

This document lists ETW providers on Windows 11 (10.0.26200.7705) where the TraceLogging provider name matches or closely resembles a Manifest-based provider name.

> **Methodology:**
> Manifest-based providers were extracted using `Enumerate-ETWProviders.ps1`, which calls the `TdhEnumerateProviders` API and filters by `SchemaSource == 0` (XML manifest). This ensures only Manifest-based providers are included, excluding MOF (Classic) providers. 

---

## Exact Match (12 entries)

Providers whose names are identical (case-insensitive).

| # | TraceLogging Provider | Manifest-based Provider |
|--:|:----------------------|:------------------------|
| 1 | Microsoft-Windows-AppModel-Runtime | Microsoft-Windows-AppModel-Runtime |
| 2 | Microsoft-Windows-AppModel-State | Microsoft-Windows-AppModel-State |
| 3 | Microsoft-Windows-BITS-Client | Microsoft-Windows-Bits-Client |
| 4 | Microsoft-Windows-Diagnostics-Performance | Microsoft-Windows-Diagnostics-Performance |
| 5 | Microsoft-Windows-Hyper-V-VID | Microsoft-Windows-Hyper-V-VID |
| 6 | Microsoft-Windows-NdisImPlatformEventProvider | Microsoft-Windows-NdisImPlatformEventProvider |
| 7 | Microsoft-Windows-PerceptionRuntime | Microsoft-Windows-PerceptionRuntime |
| 8 | Microsoft-Windows-PerceptionSensorDataService | Microsoft-Windows-PerceptionSensorDataService |
| 9 | Microsoft-Windows-Perflib | Microsoft-Windows-Perflib |
| 10 | Microsoft-Windows-TCPIP | Microsoft-Windows-TCPIP |
| 11 | Microsoft-Windows-XAML | Microsoft-Windows-XAML |
| 12 | Microsoft.Windows.ResourceManager | Microsoft.Windows.ResourceManager |

---

## Normalized Match (55 entries)

Providers whose names become identical when dots (`.`) are replaced with hyphens (`-`). This is the most common naming convention difference between TraceLogging and Manifest-based providers.

| # | TraceLogging Provider | Manifest-based Provider |
|--:|:----------------------|:------------------------|
| 1 | Microsoft.Antimalware.Scan.Interface | Microsoft-Antimalware-Scan-Interface |
| 2 | Microsoft.System.Diagnostics.DiagnosticInvoker | Microsoft-System-Diagnostics-DiagnosticInvoker |
| 3 | Microsoft.Windows.AppReadiness | Microsoft-Windows-AppReadiness |
| 4 | Microsoft.Windows.AssignedAccess | Microsoft-Windows-AssignedAccess |
| 5 | Microsoft.Windows.Battery | Microsoft-Windows-Battery |
| 6 | Microsoft.Windows.BrokerInfrastructure | Microsoft-Windows-BrokerInfrastructure |
| 7 | Microsoft.Windows.CloudRestoreLauncher | Microsoft-Windows-CloudRestoreLauncher |
| 8 | Microsoft.Windows.Containers.Wcifs | Microsoft-Windows-Containers-Wcifs |
| 9 | Microsoft.Windows.DesktopActivityModerator | Microsoft-Windows-DesktopActivityModerator |
| 10 | Microsoft.Windows.DeviceSetupManager | Microsoft-Windows-DeviceSetupManager |
| 11 | Microsoft.Windows.DeviceUx | Microsoft-Windows-DeviceUx |
| 12 | Microsoft.Windows.Dui | Microsoft-Windows-DUI |
| 13 | Microsoft.Windows.Dwm.uDWM | Microsoft-Windows-Dwm-Udwm |
| 14 | Microsoft.Windows.FeatureConfiguration | Microsoft-Windows-FeatureConfiguration |
| 15 | Microsoft.Windows.FileHistory.Engine | Microsoft-Windows-FileHistory-Engine |
| 16 | Microsoft.Windows.Firewall | Microsoft-Windows-Firewall |
| 17 | Microsoft.Windows.Hal | Microsoft-Windows-HAL |
| 18 | Microsoft.Windows.Help | Microsoft-Windows-Help |
| 19 | Microsoft.Windows.Hyper-V.NetVsc | Microsoft-Windows-Hyper-V-Netvsc |
| 20 | Microsoft.Windows.Input.HidClass | Microsoft-Windows-Input-HIDCLASS |
| 21 | Microsoft.Windows.IsolatedUserMode | Microsoft-Windows-IsolatedUserMode |
| 22 | Microsoft.Windows.Kernel.Acpi | Microsoft-Windows-Kernel-Acpi |
| 23 | Microsoft.Windows.Kernel.Dump | Microsoft-Windows-Kernel-Dump |
| 24 | Microsoft.Windows.Kernel.LiveDump | Microsoft-Windows-Kernel-LiveDump |
| 25 | Microsoft.Windows.Kernel.PnP | Microsoft-Windows-Kernel-PnP |
| 26 | Microsoft.Windows.Kernel.Power | Microsoft-Windows-Kernel-Power |
| 27 | Microsoft.Windows.Kernel.Registry | Microsoft-Windows-Kernel-Registry |
| 28 | Microsoft.Windows.Ldap.Client | Microsoft-Windows-LDAP-Client |
| 29 | Microsoft.Windows.MPTF | Microsoft-Windows-MPTF |
| 30 | Microsoft.Windows.NDIS | Microsoft-Windows-NDIS |
| 31 | Microsoft.Windows.OfflineFiles | Microsoft-Windows-OfflineFiles |
| 32 | Microsoft.Windows.Pdc | Microsoft-Windows-PDC |
| 33 | Microsoft.Windows.Power.CAD | Microsoft-Windows-Power-CAD |
| 34 | Microsoft.Windows.Power.Troubleshooter | Microsoft-Windows-Power-Troubleshooter |
| 35 | Microsoft.Windows.ProcessStateManager | Microsoft-Windows-ProcessStateManager |
| 36 | Microsoft.Windows.Rdp.Graphics.RdpAvenc | Microsoft-Windows-Rdp-Graphics-RdpAvenc |
| 37 | Microsoft.Windows.Rdp.Graphics.RdpLite | Microsoft-Windows-Rdp-Graphics-RdpLite |
| 38 | Microsoft.Windows.ReFsDedupSvc | Microsoft-Windows-ReFsDedupSvc |
| 39 | Microsoft.Windows.Security.Kerberos | Microsoft-Windows-Security-Kerberos |
| 40 | Microsoft.Windows.Security.Netlogon | Microsoft-Windows-Security-Netlogon |
| 41 | Microsoft.Windows.Sens | Microsoft-Windows-Sens |
| 42 | Microsoft.Windows.Shell.LockScreenContent | Microsoft-Windows-Shell-LockScreenContent |
| 43 | Microsoft.Windows.Shell.OpenWith | Microsoft-Windows-Shell-OpenWith |
| 44 | Microsoft.Windows.SmartScreen | Microsoft-Windows-SmartScreen |
| 45 | Microsoft.Windows.Superfetch | Microsoft-Windows-Superfetch |
| 46 | Microsoft.Windows.Sysprep | Microsoft-Windows-Sysprep |
| 47 | Microsoft.Windows.SystemEventsBroker | Microsoft-Windows-SystemEventsBroker |
| 48 | Microsoft.Windows.TaskScheduler | Microsoft-Windows-TaskScheduler |
| 49 | Microsoft.Windows.TimeBroker | Microsoft-Windows-TimeBroker |
| 50 | Microsoft.Windows.UserDataAccess.Cemapi | Microsoft-Windows-UserDataAccess-CEMAPI |
| 51 | Microsoft.Windows.UserDataAccess.UserDataService | Microsoft-Windows-UserDataAccess-UserDataService |
| 52 | Microsoft.Windows.UxTheme | Microsoft-Windows-UxTheme |
| 53 | Microsoft.Windows.WerKernel | Microsoft-Windows-WerKernel |
| 54 | Microsoft.Windows.WinML | Microsoft-Windows-WinML |
| 55 | Microsoft.Windows.WorkFolders | Microsoft-Windows-WorkFolders |

---

## High Similarity — Selected Examples (37 entries)

Providers whose names share a common base but differ in abbreviations, suffixes, or word boundaries beyond simple dot/hyphen substitution.

> **Note:** The pairs listed below are only a representative selection identified by fuzzy string matching. This is **not** an exhaustive list of all similar provider names, nor is every pair guaranteed to refer to the same underlying component. Many more similar pairs likely exist. Manual verification is recommended before drawing conclusions about any specific pair.

| # | TraceLogging Provider | Manifest-based Provider |
|--:|:----------------------|:------------------------|
| 1 | Microsoft.Windows.WindowsToGo.Startup.Options | Microsoft-Windows-WindowsToGo-StartupOptions |
| 2 | Microsoft.Windows.AppXDeploymentServer | Microsoft-Windows-AppXDeployment-Server |
| 3 | Microsoft.Windows.FolderRedirection | Microsoft-Windows-Folder Redirection |
| 4 | Microsoft.Windows.HyperV.Hypervisor | Microsoft-Windows-Hyper-V-Hypervisor |
| 5 | Microsoft.Windows.SMB.WMIProvider | Microsoft-Windows-SmbWmiProvider |
| 6 | Microsoft.Windows.SRUM.Telemetry | Microsoft-Windows-SrumTelemetry |
| 7 | Microsoft.Windows.WinRE.Agent | Microsoft-Windows-WinREAgent |
| 8 | Microsoft.Windows.Print.Brm | Microsoft-Windows-PrintBRM |
| 9 | Microsoft.Windows.MediaFoundation.MFPlatform | Microsoft-Windows-MediaFoundation-Platform |
| 10 | Microsoft.Windows.AppxPackaging | Microsoft-Windows-AppxPackagingOM |
| 11 | Microsoft.Windows.Shell.SHCore | Microsoft-Windows-Shell-Core |
| 12 | Microsoft.Windows.CleanupMgr | Microsoft-Windows-Cleanmgr |
| 13 | Microsoft.Windows.Ribbon | Microsoft-Windows-UIRibbon |
| 14 | Microsoft.Windows.Storage.Spaceparser | Microsoft-Windows-StorageSpaces-Parser |
| 15 | Microsoft.Windows.Hotpatch.Monitoring | Microsoft-Windows-Hotpatch-Monitor |
| 16 | Microsoft.Windows.DeviceManagement.PushRouterAuth | Microsoft-Windows-DeviceManagement-Pushrouter |
| 17 | Microsoft.Windows.DeviceManagement.PushRouterCore | Microsoft-Windows-DeviceManagement-Pushrouter |
| 18 | Microsoft.Windows.UserDataAccess.UserDataApisBase | Microsoft-Windows-UserDataAccess-UserDataApis |
| 19 | Microsoft.Windows.MMC | Microsoft-Windows-MMCSS |
| 20 | Microsoft.Windows.BitLocker.Fveapi | Microsoft-Windows-BitLocker-API |
| 21 | Microsoft.Windows.UserDataAccess.Unistore | Microsoft-Windows-UserDataAccess-UnifiedStore |
| 22 | Microsoft.Windows.IUIRadioManager | Microsoft-Windows-RadioManager |
| 23 | Microsoft-Windows-FileHistory-ConfigMgr | Microsoft-Windows-FileHistory-ConfigManager |
| 24 | Microsoft.Windows.DeviceManagement.PushRouterProxy | Microsoft-Windows-DeviceManagement-Pushrouter |
| 25 | Microsoft.Windows.Kernel.IoMgr | Microsoft-Windows-Kernel-IO |
| 26 | Microsoft.Windows.Kernel.Timer | Microsoft-Windows-Kernel-Tm |
| 27 | Microsoft.Windows.Dwm.DwmCore | Microsoft-Windows-Dwm-Core |
| 28 | Microsoft.Windows.USB.XHCI | Microsoft-Windows-USB-USBXHCI |
| 29 | Microsoft.Windows.Dwm.DwmApi | Microsoft-Windows-Dwm-Dwm |
| 30 | Microsoft.Windows.Taskbar | Microsoft-Windows-TaskbarCPL |
| 31 | Microsoft.Windows.WpdMtp.Api | Microsoft-Windows-WPD-API |
| 32 | Microsoft.Windows.HyperV.Compute | Microsoft-Windows-Hyper-V-ComputeLib |
| 33 | Microsoft.Windows.SearchBox | Microsoft-Windows-Search |
| 34 | Microsoft.Windows.Security.Vault.Cds | Microsoft-Windows-Security-Vault |
| 35 | Microsoft.Windows.SetupApi | Microsoft-Windows-Setup |
| 36 | Microsoft.Windows.AutoTime.Service | Microsoft-Windows-Time-Service |
| 37 | Microsoft.Windows.UIAutomation | Microsoft-Windows-UIAutomationCore |