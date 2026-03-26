# Enumerate-ETWProviders.ps1
# Lists all registered ETW providers, separated by schema source.
# SchemaSource: 0 = XML manifest, 1 = WMI MOF class

Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;

public class Tdh
{
    [StructLayout(LayoutKind.Sequential)]
    public struct TRACE_PROVIDER_INFO
    {
        public Guid ProviderGuid;
        public uint SchemaSource;    // 0 = Manifest, 1 = MOF
        public uint ProviderNameOffset;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct PROVIDER_ENUMERATION_INFO
    {
        public uint NumberOfProviders;
        public uint Reserved;
    }

    [DllImport("tdh.dll", SetLastError = true)]
    public static extern int TdhEnumerateProviders(
        IntPtr pBuffer,
        ref int pBufferSize
    );

    public const int ERROR_INSUFFICIENT_BUFFER = 122;
    public const int ERROR_SUCCESS = 0;
}
"@

$bufferSize = 0
$null = [Tdh]::TdhEnumerateProviders([IntPtr]::Zero, [ref]$bufferSize)

$buffer = [System.Runtime.InteropServices.Marshal]::AllocHGlobal($bufferSize)
try {
    $status = [Tdh]::TdhEnumerateProviders($buffer, [ref]$bufferSize)
    if ($status -ne [Tdh]::ERROR_SUCCESS) {
        Write-Error "TdhEnumerateProviders failed with error $status"
        return
    }

    $enumInfo = [System.Runtime.InteropServices.Marshal]::PtrToStructure(
        $buffer, [Type][Tdh+PROVIDER_ENUMERATION_INFO]
    )

    $totalCount = $enumInfo.NumberOfProviders
    $entrySize  = [System.Runtime.InteropServices.Marshal]::SizeOf(
        [Type][Tdh+TRACE_PROVIDER_INFO]
    )
    $arrayOffset = 8

    $manifestProviders = @()
    $mofProviders      = @()

    for ($i = 0; $i -lt $totalCount; $i++) {
        $entryPtr = [IntPtr]::Add($buffer, $arrayOffset + ($i * $entrySize))
        $entry = [System.Runtime.InteropServices.Marshal]::PtrToStructure(
            $entryPtr, [Type][Tdh+TRACE_PROVIDER_INFO]
        )

        $name = ""
        if ($entry.ProviderNameOffset -gt 0) {
            $namePtr = [IntPtr]::Add($buffer, $entry.ProviderNameOffset)
            $name = [System.Runtime.InteropServices.Marshal]::PtrToStringUni($namePtr)
        }

        $obj = [PSCustomObject]@{
            Name = $name
            GUID = $entry.ProviderGuid.ToString("B").ToUpper()
        }

        if ($entry.SchemaSource -eq 0) {
            $manifestProviders += $obj
        } else {
            $mofProviders += $obj
        }
    }

    # Manifest-based providers
    Write-Host "=== Manifest-based providers ($($manifestProviders.Count)) ===" -ForegroundColor Cyan
    Write-Host ""
    $manifestProviders | Sort-Object Name | Format-Table -AutoSize

    # MOF-based providers
    Write-Host "=== MOF-based providers ($($mofProviders.Count)) ===" -ForegroundColor Yellow
    Write-Host ""
    $mofProviders | Sort-Object Name | Format-Table -AutoSize

    # Summary
    Write-Host "=== Summary ===" -ForegroundColor Green
    Write-Host "  Total      : $totalCount"
    Write-Host "  Manifest   : $($manifestProviders.Count)"
    Write-Host "  MOF        : $($mofProviders.Count)"

} finally {
    [System.Runtime.InteropServices.Marshal]::FreeHGlobal($buffer)
}