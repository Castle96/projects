# Check if the script is running with administrative privileges
if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    # If not, restart the script with elevated privileges
    $newProcess = Start-Process powershell -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs
    exit
}

# Prompt the user to enter the computer name
$computerName = Read-Host -Prompt 'Enter the computer name'

# Check if the computer is reachable
if (Test-Connection -ComputerName $computerName -Count 1 -Quiet) {
    # Get the currently logged-in user
    $loggedInUser = Get-WmiObject -Class Win32_ComputerSystem -ComputerName $computerName | Select-Object -ExpandProperty UserName
    
    if ($loggedInUser) {
        Write-Output "The user currently logged into $computerName is $loggedInUser."
    } else {
        Write-Output "No user is currently logged into $computerName."
    }

    # Connect to the remote PowerShell session
    try {
        Enter-PSSession -ComputerName $computerName
    } catch {
        Write-Output "Failed to connect to the remote PowerShell session on $computerName. Error: $_"
    }
} else {
    Write-Output "The computer $computerName is not reachable."
}
# Check if there are any chocolatey packages installed
$packageName = "chocolatey"

if (Get-Package -Name $packageName -ListAvailable -ErrorAction SilentlyContinue) {
    Write-Host "The package $packageName is available for installation."
} else {
    Write-Host "The package $packageName is not available for installation."
}
# Disconnect from the remote PowerShell session
Get-PSSession | Remove-PSSession



# check to see the list of Chocolatey scripts installed on the pc


