# Corpus-wide predicate cross-check summary

| Technique | Context | PASS | FLAG | MANUAL REVIEW |
|---|---|---|---|---|
| T1003.001 | — | 1 | 0 | 6 |
| T1018 | — | 7 | 0 | 49 |
| T1021.002 | — | 1 | 0 | 9 |
| T1041 | — | 2 | 0 | 5 |
| T1046 | — | 7 | 0 | 18 |
| T1053.005 | — | 13 | 2 | 29 |
| T1055 | — | 16 | 1 | 37 |
| T1057 | — | 5 | 0 | 16 |
| T1059.001 | — | 0 | 0 | 7 |
| T1070.004 | — | 2 | 0 | 21 |
| T1082 | t1082_elevated | 18 | 0 | 112 |
| T1082 | t1082_normal | 18 | 0 | 110 |
| T1087.001 | — | 1 | 0 | 11 |
| T1112 | — | 87 | 6 | 165 |
| T1136.001 | — | 6 | 0 | 8 |
| T1547.001 | — | 2 | 0 | 4 |
| T1560.001 | — | 1 | 0 | 23 |

---

# Predicate cross-check — T1003.001 Test #11

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `dotnet-v5-installed` | Environment | The YAML dependency explicitly requires .NET v5 to be installed, as checked by resolve-path for createdump.exe. | No matching rule for this predicate | **MANUAL REVIEW** |
| `user-is-admin` | Privilege/User | The executor requires elevation (elevation_required: true), indicating administrative privileges are needed. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `not-process-spawned-createdump` | Process | Evidence shows createdump.exe could not be found or executed, so no process was spawned. | no clear process-spawning pattern in command text | **MANUAL REVIEW** |
| `not-file-created-lsass-dump` | Information | No dump file was created due to missing createdump.exe, as indicated by the resolve-path failure and subsequent command error. | No matching rule for this predicate | **MANUAL REVIEW** |
| `process-running-lsass` | (unclassified) | Assumed as a precondition for all LSASS dumping, but not explicitly checked or failed in this test's evidence. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `file-created-dotnet-lsass-dmp` | (unclassified) | Would be an effect if the dump succeeded, but evidence shows it did not occur. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `command-prompt-invokable` | (unclassified) | Executor is command_prompt, but the failure is due to missing binary, not executor unavailability. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1018 Test #10

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `adfind-executable-present` | Environment | The YAML specifies that AdFind.exe must exist on disk at a specified location, which is a prerequisite for execution. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-command-executed` | Process | The execution evidence shows that the command failed to execute because 'AdFind.exe' was not recognized, indicating the process did not run. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `adfind-executable-present` | (unclassified) | The evidence suggests the executable was missing, but the YAML indicates it should be present; this discrepancy needs human review. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1018 Test #11

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `file-exists` | Environment | The test requires AdFind.exe to exist at the specified location, as indicated by the dependency check in the YAML. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-command-executed` | Process | The execution evidence shows that the command failed to execute because AdFind.exe was not found. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `elevated-privilege` | (unclassified) | The YAML does not specify if elevated privileges are required, but the failure was due to a missing file, not privilege issues. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1018 Test #16

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The test uses a PowerShell script to enumerate domain computers. | YAML executor 'powershell' matches predicate | **PASS** |
| `system-part-of-domain` | Environment | The test requires the system to be part of a domain, as indicated by the dependency check in the YAML. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-domain-contacted` | Information | The execution evidence shows an error indicating the domain could not be contacted. | No matching rule for this predicate | **MANUAL REVIEW** |
| `elevated-privilege` | (unclassified) | The YAML does not specify elevation is required, but the error might imply a privilege issue. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1018 Test #17

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The test uses PowerShell to execute the command. | YAML executor 'powershell' matches predicate | **PASS** |
| `command-not-found` | Process | The evidence shows that 'Get-AdComputer' was not recognized, indicating the command was not found. | YAML executor is 'powershell', predicate does not reference it | **MANUAL REVIEW** |
| `exit-code-zero` | (unclassified) | The exit code was 0 despite the command not being found, which is unusual and may require further investigation. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1018 Test #18

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The test uses a PowerShell script to execute ADSISearcher commands. | YAML executor 'powershell' matches predicate | **PASS** |
| `domain-joined` | Privilege/User | The test requires the system to be part of a domain to enumerate Active Directory computers. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-domain-contacted` | Information | The execution evidence indicates that the domain could not be contacted, resulting in a COMException. | No matching rule for this predicate | **MANUAL REVIEW** |
| `exit-code-zero` | (unclassified) | Despite the exceptions, the exit code was 0, which is unusual and may require further investigation. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1018 Test #19

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The test uses PowerShell to execute the command, as indicated by the executor name. | YAML executor 'powershell' matches predicate | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows an 'Access is denied' error, indicating a privilege issue. | No matching rule for this predicate | **MANUAL REVIEW** |
| `domain-controller-identified` | (unclassified) | The intended effect of identifying a domain controller was not achieved due to the access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1018 Test #1

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses cmd.exe to execute net.exe commands. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `access-denied` | Privilege/User | The execution evidence shows 'System error 6118' indicating a failure to access the list of servers. | No matching rule for this predicate | **MANUAL REVIEW** |
| `network-discovery-attempted` | (unclassified) | The test description implies an attempt to discover remote systems, but the evidence shows failure, so it's unclear if this should be an effect. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1018 Test #20

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The test uses PowerShell to execute the Get-WmiObject command. | YAML executor 'powershell' matches predicate | **PASS** |
| `domain-joined` | Environment | The test requires querying Active Directory, implying the system must be domain-joined. | No matching rule for this predicate | **MANUAL REVIEW** |
| `access-denied` | Privilege/User | The execution evidence shows an 'Invalid query' error, indicating a failure to access the required WMI class. | No matching rule for this predicate | **MANUAL REVIEW** |
| `wmi-class-exists` | (unclassified) | The failure suggests the WMI class 'ds_computer' might not exist or be accessible, but this is not explicitly confirmed. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1018 Test #21

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses cmd.exe to execute the net command. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `domain-controller-accessible` | Environment | The test requires access to a domain controller to list domain controllers, which failed due to the domain not being contacted. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-domain-controller-listed` | Information | The execution failed with 'System error 1355', indicating that no domain controller information was retrieved. | No matching rule for this predicate | **MANUAL REVIEW** |
| `user-is-domain-member` | (unclassified) | The test might assume the user is part of a domain, but the evidence shows a failure due to domain issues. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1018 Test #22

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `file-exists` | Information | The YAML specifies that Netscan must be installed at a specific path, indicating a file existence check is required. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-file-exists` | Information | The execution evidence indicates 'The system cannot find the path specified', suggesting the file did not exist. | No matching rule for this predicate | **MANUAL REVIEW** |
| `execution-success` | (unclassified) | The exit code is 0, which typically indicates success, but the evidence suggests a failure due to missing file. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1018 Test #2

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses cmd.exe to execute the net command. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `domain-controller-accessible` | Environment | The test requires access to a domain controller to query the 'Domain Computers' group. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-domain-controller-accessible` | Environment | The execution evidence shows 'System error 1355', indicating the domain controller could not be contacted. | No matching rule for this predicate | **MANUAL REVIEW** |
| `user-is-domain-member` | (unclassified) | The test assumes the user is part of a domain, but the evidence suggests otherwise. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1018 Test #3

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `command-prompt-available` | Executor | The executor for this test is command_prompt, indicating it requires a command prompt to execute. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `domain-knowledge-required` | Information | The test involves querying a target domain for domain controllers, implying knowledge of a domain is necessary. | No matching rule for this predicate | **MANUAL REVIEW** |
| `domain-controller-query-attempted` | Process | The execution evidence shows an attempt to query domain controllers using nltest.exe. | No matching rule for this predicate | **MANUAL REVIEW** |
| `domain-controller-list-retrieved` | (unclassified) | The evidence indicates a failure to find a domain controller, so it's uncertain if any list was retrieved. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1018 Test #4

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `command-prompt-available` | Executor | The test uses the command prompt to execute the ping sweep. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `ping-sweep-attempted` | Process | The evidence shows multiple ping commands were executed in a loop, indicating an attempt to perform a ping sweep. | No matching rule for this predicate | **MANUAL REVIEW** |
| `network-access-failure` | (unclassified) | The evidence shows 'PING transmit failed. General failure.' for all attempts, suggesting a potential network access issue, but it's unclear if this is due to lack of privilege, network configuration, or other reasons. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1018 Test #5

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `command-available` | Executor | The test requires the 'arp' command to be available on the system, as indicated by the execution of 'arp -a'. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `network-arp-cache-discovered` | Information | The execution of 'arp -a' successfully listed the ARP cache, revealing network information such as IP and MAC addresses. | No matching rule for this predicate | **MANUAL REVIEW** |

---

# Predicate cross-check — T1018 Test #8

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The test uses a PowerShell script to execute nslookup commands. | YAML executor 'powershell' matches predicate | **PASS** |
| `user-is-admin` | Privilege/User | The YAML specifies that elevation is required for the PowerShell execution. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `network-hosts-discovered` | Information | The test aims to discover remote systems by performing nslookup on a range of IPs. | No matching rule for this predicate | **MANUAL REVIEW** |
| `dns-server-unreachable` | (unclassified) | The evidence shows repeated 'No response from server' messages, indicating potential network or DNS server issues. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1018 Test #9

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `python3-installed` | Environment | The YAML specifies that Python 3 must be installed as a prerequisite. | No matching rule for this predicate | **MANUAL REVIEW** |
| `venv-configured` | Environment | The YAML specifies that a virtual environment must be configured at the specified path. | No matching rule for this predicate | **MANUAL REVIEW** |
| `adidnsdump-installed` | Environment | The YAML specifies that adidnsdump must be installed as a prerequisite. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-command-executed` | Process | The execution evidence shows 'The system cannot find the path specified', indicating the command did not execute successfully. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `path-specified` | (unclassified) | The error 'The system cannot find the path specified' suggests a path issue, but it's unclear if this is due to a missing file or incorrect path configuration. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1021.002 Test #1

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor is 'command_prompt' (cmd.exe), so the system must support invoking commands via cmd. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `valid-user-credentials` | Privilege/User | The test requires a username and password for authentication to the admin share, as specified in the input arguments. | No matching rule for this predicate | **MANUAL REVIEW** |
| `admin-share-available` | Environment | The test targets an admin share (e.g., C$), which must exist and be accessible on the target system. | elevation_required not set in YAML | **MANUAL REVIEW** |
| `admin-share-mapped` | Environment | The successful execution of 'net use' maps the admin share, establishing a persistent network connection to the share. | elevation_required not set in YAML | **MANUAL REVIEW** |
| `process-spawned` | Process | The evidence shows cmd.exe was used to execute the mapping command, indicating a process was spawned. | no clear process-spawning pattern in command text | **MANUAL REVIEW** |
| `user-is-admin` | (unclassified) | The test uses an account that may have admin rights, but the evidence does not explicitly confirm the privilege level; flag for review if privilege escalation is a concern. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1021.002 Test #2

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor is PowerShell, as shown by the YAML and the evidence of PowerShell being used to run the command. | YAML executor 'powershell' matches predicate | **PASS** |
| `network-access-to-target` | Environment | Mapping a remote share requires network connectivity to the target (localhost in this case), implied by the successful mapping. | No matching rule for this predicate | **MANUAL REVIEW** |
| `valid-credentials-for-admin-share` | Privilege/User | Mapping an admin share (C$) requires valid credentials with administrative privileges, as indicated by the default user being DOMAIN\Administrator and the successful mapping. | elevation_required not set in YAML | **MANUAL REVIEW** |
| `admin-share-mapped` | Environment | The evidence shows a new PSDrive (g:) mapped to \\localhost\C$, indicating the admin share is now mapped and accessible. | elevation_required not set in YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1041 Test #1

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor specified in the YAML is PowerShell, indicating the need for PowerShell to be invokable. | YAML executor 'powershell' matches predicate | **PASS** |
| `file-exists` | Information | The command checks for the existence of the file at #{filepath} before attempting to exfiltrate it. | No matching rule for this predicate | **MANUAL REVIEW** |
| `web-request-attempted` | Process | The evidence shows an attempt to execute Invoke-WebRequest, indicating a web request was attempted. | No matching rule for this predicate | **MANUAL REVIEW** |
| `proxy-resolution-failed` | (unclassified) | The evidence indicates a failure due to proxy resolution, which may affect the success of the exfiltration but is not directly modeled in the predicates. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1041 Test #2

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor for the test is specified as PowerShell. | YAML executor 'powershell' matches predicate | **PASS** |
| `dns-query-attempted` | Process | The command attempts to resolve a DNS name using Resolve-DnsName. | No matching rule for this predicate | **MANUAL REVIEW** |
| `dns-query-failed-invalid-character` | (unclassified) | The evidence shows a DNS query failure due to invalid characters, which may not be a typical effect. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1046 Test #10

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor for this test is specified as PowerShell. | YAML executor 'powershell' matches predicate | **PASS** |
| `network-service-discovered` | Information | The test successfully identified open ports on the subnet, indicating network services were discovered. | No matching rule for this predicate | **MANUAL REVIEW** |

---

# Predicate cross-check — T1046 Test #11

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor for this test is PowerShell, as specified in the YAML. | YAML executor 'powershell' matches predicate | **PASS** |
| `user-is-admin` | Privilege/User | The executor requires elevation, indicating administrative privileges are needed. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `remote-desktop-services-discovered` | Information | The test successfully queried the status of Remote Desktop Services, indicating discovery of service information. | No matching rule for this predicate | **MANUAL REVIEW** |

---

# Predicate cross-check — T1046 Test #3

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `nmap-installed` | Environment | The YAML specifies a prerequisite check for the nmap command, which failed according to the execution evidence. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-nmap-command-found` | Environment | The execution evidence shows a CommandNotFoundException for nmap, indicating it was not found on the system. | YAML executor is 'powershell', predicate does not reference it | **MANUAL REVIEW** |
| `elevated-privilege-required` | (unclassified) | The YAML specifies elevation_required: true, but the evidence does not confirm if this was a factor in the failure. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1046 Test #4

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `python-installed` | Environment | The YAML specifies a dependency on Python being installed, but the execution evidence indicates Python was not found. | No matching rule for this predicate | **MANUAL REVIEW** |
| `python-not-found` | (unclassified) | The execution evidence indicates Python was not found, but it's unclear if this should be a persistent state change or just a transient error. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1046 Test #5

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor for this test is specified as PowerShell. | YAML executor 'powershell' matches predicate | **PASS** |
| `not-script-downloaded` | Information | The evidence shows a failure to download the script from 'raw.githubusercontent.com'. | No matching rule for this predicate | **MANUAL REVIEW** |
| `command-not-found` | Process | The 'spoolvulnscan' command was not recognized, indicating it was not executed. | YAML executor is 'powershell', predicate does not reference it | **MANUAL REVIEW** |
| `network-service-discovery-attempted` | (unclassified) | The test was intended to perform network service discovery, but due to failures, it's unclear if any discovery was attempted. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1046 Test #6

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor for this test is specified as PowerShell. | YAML executor 'powershell' matches predicate | **PASS** |
| `not-command-executed` | Process | The command 'MS17-10' was not recognized, indicating it did not execute. | YAML executor is 'powershell', predicate does not reference it | **MANUAL REVIEW** |
| `network-access-failure` | (unclassified) | The error 'The remote name could not be resolved' suggests a network issue, but it's unclear if this is a persistent state or transient. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1046 Test #7

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor for this test is specified as PowerShell. | YAML executor 'powershell' matches predicate | **PASS** |
| `not-script-downloaded` | Information | The evidence shows a failure to download the script from 'raw.githubusercontent.com'. | No matching rule for this predicate | **MANUAL REVIEW** |
| `command-not-found` | Process | The 'bluekeep' command was not recognized, indicating it was not executed. | YAML executor is 'powershell', predicate does not reference it | **MANUAL REVIEW** |
| `elevated-privilege-required` | (unclassified) | The YAML specifies 'elevation_required: true', but the evidence does not confirm if this was a factor in the failure. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1046 Test #8

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor for this test is specified as PowerShell. | YAML executor 'powershell' matches predicate | **PASS** |
| `not-script-downloaded` | Information | The evidence shows a failure to download the script from 'raw.githubusercontent.com'. | No matching rule for this predicate | **MANUAL REVIEW** |
| `command-not-found` | Process | The 'fruit' command was not recognized, indicating it was not found or not executed. | YAML executor is 'powershell', predicate does not reference it | **MANUAL REVIEW** |
| `network-unreachable` | (unclassified) | The error 'The remote name could not be resolved' suggests a potential network issue, but it's unclear if this is a persistent state or transient. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1053.005 Test #10

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `file-exists` | Information | The test requires the GhostTask.exe tool to exist in the specified directory as per the YAML dependencies. | No matching rule for this predicate | **MANUAL REVIEW** |
| `psexec-exists` | Information | The test requires the PsExec tool to exist in the specified directory as per the YAML dependencies. | No matching rule for this predicate | **MANUAL REVIEW** |
| `elevated-privilege` | Privilege/User | The executor requires elevation as indicated by 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `not-scheduled-task-created` | Environment | The execution failed with 'The filename, directory name, or volume label syntax is incorrect', indicating the task was not created. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-manipulated` | (unclassified) | The test description mentions registry key manipulation, but the failure suggests this did not occur. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1053.005 Test #11

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The executor requires elevation, indicating administrative privileges are needed. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `scheduled-task-created` | Environment | The command creates a scheduled task named 'CompMgmtBypass' to run 'compmgmt.msc'. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-written` | Information | The command modifies the registry to associate 'compmgmt.msc' with a malicious payload. | command references registry but no explicit hive path matched; no clear output-write pattern in command text | **MANUAL REVIEW** |
| `scheduled-task-console-access-blocked` | (unclassified) | The follow-on step ('Let's open the Computer Management console...') failed with 'Access is denied' — this is a distinct, later action (console invocation via the hijacked association), not the task-creation step itself. Renamed from the original unlabeled 'access-denied' note to read as the same structural pattern as Test #12: creation succeeds, follow-on privileged action is blocked. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1053.005 Test #12

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The executor requires elevation, indicating administrative privileges are needed. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `scheduled-task-created` | Environment | 'The operation completed successfully' confirms the scheduled task registration step succeeded, matching the pattern in Test #11. | No matching rule for this predicate | **MANUAL REVIEW** |
| `scheduled-task-execution-blocked` | (unclassified) | The follow-on step ('Let's run the schedule task...') failed with 'Access is denied' and 'The system cannot find the file specified' — this is a distinct, later action (task execution/invocation), not the creation step, and should not be folded into scheduled-task-created's success/failure. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1053.005 Test #1

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The executor requires elevation, indicating administrative privileges are needed. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'Access is denied' errors, indicating a failure due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `scheduled-task-created` | (unclassified) | The YAML describes creating scheduled tasks, but the execution evidence shows failure, so this effect is uncertain. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1053.005 Test #2

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `windows-platform` | Environment | The test is supported on Windows platforms as specified in the YAML. | No matching rule for this predicate | **MANUAL REVIEW** |
| `scheduled-task-created` | Environment | The evidence shows that a scheduled task named 'spawn' was successfully created. | No matching rule for this predicate | **MANUAL REVIEW** |

---

# Predicate cross-check — T1053.005 Test #3

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-has-remote-access` | Privilege/User | The test involves creating a scheduled task on a remote system, which requires remote access privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `user-has-elevated-privileges` | Privilege/User | The executor specifies that elevation is required, indicating the need for elevated privileges. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | (unclassified) | The execution evidence shows 'Access is denied', indicating a failure to execute the task, but it's unclear if this is due to privilege issues or other factors. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1053.005 Test #4

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor for this test is specified as 'powershell'. | YAML executor 'powershell' matches predicate | **PASS** |
| `user-is-admin` | Privilege/User | The YAML specifies that elevation is not required, but the evidence shows 'Access is denied', indicating admin privileges may be needed. | YAML elevation_required: false — contradicts predicate. Known-unreliable field (see T1046, T1053.005 #4/#9); do not auto-reject, flag for manual privilege-context check. | **FLAG** |
| `access-denied` | (unclassified) | The evidence shows 'Access is denied', but it's unclear if this is due to privilege level or another issue. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1053.005 Test #5

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-available` | Executor | The test uses PowerShell to execute commands, indicating PowerShell must be available. | YAML executor 'powershell' matches predicate | **PASS** |
| `internet-connectivity-required` | Environment | The test attempts to download a script from a remote URL, requiring internet connectivity. | No matching rule for this predicate | **MANUAL REVIEW** |
| `microsoft-word-installed` | Environment | The test requires Microsoft Word to be installed as per the dependency check in the YAML. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-scheduled-task-created` | Environment | The test failed to execute due to network issues, so no scheduled task was created. | No matching rule for this predicate | **MANUAL REVIEW** |
| `invoke-mal-doc-failure` | (unclassified) | The failure to recognize 'Invoke-MalDoc' suggests a missing script or incorrect setup, but it's unclear how this affects the overall state. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1053.005 Test #6

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor for this test is specified as 'powershell', indicating that PowerShell must be invokable. | YAML executor 'powershell' matches predicate | **PASS** |
| `elevated-privilege` | Privilege/User | The YAML specifies 'elevation_required: true', indicating that elevated privileges are needed. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `file-exists` | Information | The dependency requires the XML file to exist at the specified location, as checked by the prereq_command. | No matching rule for this predicate | **MANUAL REVIEW** |
| `access-denied` | Privilege/User | The execution evidence shows 'Access is denied', indicating a failure due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `scheduled-task-created` | (unclassified) | The test intended to create a scheduled task, but the 'Access is denied' error suggests this effect did not occur. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1053.005 Test #7

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor for this test is command_prompt, indicating the use of cmd.exe. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `scheduled-task-created` | Environment | The evidence confirms that a scheduled task 'ATOMIC-T1053.005' was successfully created. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-written` | Information | The command involves writing a Base64 encoded command to the registry at HKCU\SOFTWARE\ATOMIC-T1053.005. | registry hive reference found in command (hkcu\); command text shows an output/write pattern | **PASS** |

---

# Predicate cross-check — T1053.005 Test #8

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor for this test is PowerShell, as specified in the YAML. | YAML executor 'powershell' matches predicate | **PASS** |
| `user-is-admin` | Privilege/User | The test requires elevated privileges, as indicated by 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `file-exists` | Information | The XML file must exist at the specified path, as indicated by the dependency check in the YAML. | No matching rule for this predicate | **MANUAL REVIEW** |
| `access-denied` | (unclassified) | The execution evidence shows 'Access is denied', indicating a failure to execute due to insufficient privileges or permissions. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1053.005 Test #9

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor for this test is PowerShell, as indicated by the YAML definition. | YAML executor 'powershell' matches predicate | **PASS** |
| `user-is-admin` | Privilege/User | The YAML specifies that elevation is not required, but the execution evidence shows 'Access is denied', indicating admin privileges are needed. | YAML elevation_required: false — contradicts predicate. Known-unreliable field (see T1046, T1053.005 #4/#9); do not auto-reject, flag for manual privilege-context check. | **FLAG** |
| `not-scheduled-task-created` | Environment | The execution evidence shows 'Access is denied' and 'The system cannot find the file specified', indicating the scheduled task was not created. | No matching rule for this predicate | **MANUAL REVIEW** |
| `elevated-privilege` | (unclassified) | The YAML indicates elevation is not required, but the evidence suggests otherwise; needs human review. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1055 Test #10

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `file-exists` | Information | The executable 'CreateRemoteThreadNative.exe' must exist at the specified path for the test to run. | No matching rule for this predicate | **MANUAL REVIEW** |
| `process-failed-to-run` | Process | The execution of 'CreateRemoteThreadNative.exe' failed due to it being flagged as a virus or potentially unwanted software. | command text shows a process-spawning pattern | **PASS** |
| `elevated-privilege-required` | (unclassified) | The YAML indicates elevation is not required, but the failure might imply a privilege issue. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1055 Test #11

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor for this test is specified as PowerShell. | YAML executor 'powershell' matches predicate | **PASS** |
| `file-exists` | Information | The executable 'CreateThread.exe' must exist at the specified path for the test to run. | No matching rule for this predicate | **MANUAL REVIEW** |
| `process-failed-to-run` | Process | The execution evidence indicates that 'CreateThread.exe' failed to run due to being flagged as a virus. | no clear process-spawning pattern in command text | **MANUAL REVIEW** |
| `elevated-privilege` | (unclassified) | The YAML specifies 'elevation_required: false', but the failure might imply privilege issues. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1055 Test #12

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor for this test is specified as PowerShell. | YAML executor 'powershell' matches predicate | **PASS** |
| `file-exists` | Information | The executable 'CreateThreadNative.exe' must exist at the specified path to be invoked. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-process-spawned` | Process | The execution failed due to a virus detection, preventing the process from being spawned. | no clear process-spawning pattern in command text | **MANUAL REVIEW** |
| `elevated-privilege` | (unclassified) | The YAML specifies 'elevation_required: false', but the failure might imply privilege issues. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1055 Test #13

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `file-exists` | Information | The test requires the executable 'uuid_injection.exe' to exist at the specified location. | No matching rule for this predicate | **MANUAL REVIEW** |
| `powershell-invokable` | Executor | The executor for this test is PowerShell, as specified in the YAML. | YAML executor 'powershell' matches predicate | **PASS** |
| `execution-failed-virus-detected` | Process | The execution failed because the file was detected as containing a virus or potentially unwanted software. | No matching rule for this predicate | **MANUAL REVIEW** |
| `elevated-privilege` | (unclassified) | The YAML specifies 'elevation_required: true', but the execution evidence does not confirm if privilege elevation was attempted or required. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1055 Test #1

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor specified in the YAML is PowerShell, indicating that PowerShell must be invokable. | YAML executor 'powershell' matches predicate | **PASS** |
| `file-exists` | Information | The prerequisite checks if the VBA macro file exists at the specified path. | No matching rule for this predicate | **MANUAL REVIEW** |
| `microsoft-office-64bit-installed` | Environment | The YAML specifies that a 64-bit installation of Microsoft Office is required. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-shellcode-executed` | Process | The execution evidence shows that the shellcode was not executed due to a failure in resolving the remote name. | No matching rule for this predicate | **MANUAL REVIEW** |
| `network-access-required` | (unclassified) | The failure to resolve 'raw.githubusercontent.com' suggests network access is required, but this is not explicitly stated in the YAML. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1055 Test #2

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `mimikatz-exists-on-disk` | Information | The YAML specifies that the Mimikatz executable must exist at the specified location. | No matching rule for this predicate | **MANUAL REVIEW** |
| `psexec-exists-on-disk` | Information | The YAML specifies that the PsExec tool must exist at the specified location. | No matching rule for this predicate | **MANUAL REVIEW** |
| `user-is-privileged-on-target` | Privilege/User | The YAML notes that the execution must be in the context of a user who is privileged on the remote machine. | YAML elevation_required: false — contradicts predicate. Known-unreliable field (see T1046, T1053.005 #4/#9); do not auto-reject, flag for manual privilege-context check. | **FLAG** |
| `access-denied` | Privilege/User | The execution evidence shows an 'Access is denied' error, indicating a failure due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `process-injection-attempted` | (unclassified) | The YAML describes a process injection attempt, but the evidence shows it failed, so it's unclear if this should be an effect. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1055 Test #3

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor for this test is specified as PowerShell. | YAML executor 'powershell' matches predicate | **PASS** |
| `file-exists` | Information | The test requires the existence of the InjectView.exe file at a specified path. | No matching rule for this predicate | **MANUAL REVIEW** |
| `process-injection-failed` | Process | The execution evidence indicates that the process injection failed due to a virus detection. | command text shows a process-spawning pattern | **PASS** |
| `virus-detected` | (unclassified) | The evidence mentions a virus detection, but it's unclear if this should be a separate predicate or part of the failure reason. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1055 Test #4

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor for this test is specified as PowerShell. | YAML executor 'powershell' matches predicate | **PASS** |
| `file-exists` | Information | The test requires the executable 'redVanity.exe' to be present at the specified path. | No matching rule for this predicate | **MANUAL REVIEW** |
| `process-injection-failed` | Process | The execution evidence indicates that the process injection failed due to a virus detection. | command text shows a process-spawning pattern | **PASS** |
| `elevated-privilege-required` | (unclassified) | The YAML specifies 'elevation_required: false', but the failure might imply privilege issues. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1055 Test #5

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `file-exists` | Information | The test requires the vulnerable DLL to exist at the specified location as per the YAML prerequisites. | No matching rule for this predicate | **MANUAL REVIEW** |
| `elevated-privilege` | Privilege/User | The executor requires elevated privileges as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `not-process-spawned` | Process | The execution evidence shows that the process failed to run due to a virus detection, indicating the process was not successfully spawned. | no clear process-spawning pattern in command text | **MANUAL REVIEW** |
| `virus-detected` | (unclassified) | The evidence indicates a virus detection, but it's unclear how this should be represented in PDDL predicates. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1055 Test #6

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor for this test is specified as PowerShell. | YAML executor 'powershell' matches predicate | **PASS** |
| `file-exists` | Information | The executable 'UuidFromStringA.exe' must exist at the specified path for the test to run. | No matching rule for this predicate | **MANUAL REVIEW** |
| `execution-failed-virus-detected` | Process | The execution failed because the file was detected as a virus or potentially unwanted software. | No matching rule for this predicate | **MANUAL REVIEW** |
| `elevated-privilege` | (unclassified) | The YAML specifies 'elevation_required: false', but the failure might imply privilege issues. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1055 Test #7

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor for this test is specified as PowerShell. | YAML executor 'powershell' matches predicate | **PASS** |
| `file-exists` | Information | The executable 'EtwpCreateEtwThread.exe' must exist at the specified path for the test to run. | No matching rule for this predicate | **MANUAL REVIEW** |
| `process-failed-to-run` | Process | The execution evidence indicates that the program failed to run due to being flagged as a virus or potentially unwanted software. | no clear process-spawning pattern in command text | **MANUAL REVIEW** |
| `elevated-privilege` | (unclassified) | The YAML specifies 'elevation_required: false', but the failure might imply privilege issues; needs human review. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1055 Test #8

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `file-exists` | Information | The test requires the RtlCreateUserThread.exe file to be present at the specified location. | No matching rule for this predicate | **MANUAL REVIEW** |
| `process-running` | Process | The test involves injecting into a process, which implies a target process must be running. | command text shows a process-spawning pattern | **PASS** |
| `not-process-injected` | Process | The execution failed due to the file being flagged as a virus, preventing the injection. | command text shows a process-spawning pattern | **PASS** |
| `elevated-privilege` | (unclassified) | The YAML mentions elevation is not required, but the failure might imply privilege issues. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `access-denied` | (unclassified) | The failure message could suggest access issues, but it's unclear if this is due to privilege or antivirus. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1055 Test #9

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `file-exists` | Information | The test requires the CreateRemoteThread.exe file to be present at the specified location. | No matching rule for this predicate | **MANUAL REVIEW** |
| `process-running` | Process | The test involves injecting into a remote process, which implies the target process must be running. | command text shows a process-spawning pattern | **PASS** |
| `not-process-injected` | Process | The execution failed due to the file being flagged as a virus, indicating the process injection did not occur. | command text shows a process-spawning pattern | **PASS** |
| `elevated-privilege-required` | (unclassified) | The YAML indicates elevation is not required locally, but it might be needed remotely; this is uncertain from the evidence. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1057 Test #2

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor for this test is 'command_prompt', indicating the use of cmd.exe. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `process-listing-obtained` | Information | The execution of 'tasklist' successfully listed running processes, as evidenced by the detailed process output. | no clear process-spawning pattern in command text | **MANUAL REVIEW** |

---

# Predicate cross-check — T1057 Test #3

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The test uses PowerShell to execute the Get-Process cmdlet. | YAML executor 'powershell' matches predicate | **PASS** |
| `process-listing-obtained` | Information | The execution evidence shows a list of processes obtained using the Get-Process cmdlet. | no clear process-spawning pattern in command text | **MANUAL REVIEW** |

---

# Predicate cross-check — T1057 Test #4

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-available` | Executor | The test uses PowerShell to execute the get-wmiObject command. | YAML executor 'powershell' matches predicate | **PASS** |
| `process-information-discovered` | Information | The execution evidence shows detailed process information was retrieved using get-wmiObject. | no clear process-spawning pattern in command text | **MANUAL REVIEW** |
| `elevated-privilege-required` | (unclassified) | The YAML does not specify if elevated privileges are required, but PowerShell commands sometimes need them. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1057 Test #5

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `command-prompt-available` | Executor | The test uses the command prompt to execute the WMIC command. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `not-process-listing-obtained` | Information | The execution failed with 'wmic' not recognized, so no process information was obtained. | no clear process-spawning pattern in command text | **MANUAL REVIEW** |
| `wmic-installed` | (unclassified) | The failure indicates WMIC is not available, but it's unclear if this is due to a missing installation or another issue. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1057 Test #6

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor for this test is 'command_prompt', indicating the use of cmd.exe. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `process-discovered` | Information | The execution evidence shows that the process 'lsass.exe' was successfully discovered using tasklist. | no clear process-spawning pattern in command text | **MANUAL REVIEW** |

---

# Predicate cross-check — T1057 Test #7

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `process-hacker-installed` | Environment | The YAML specifies that Process Hacker must be installed in a specific location as a dependency. | command text shows a process-spawning pattern | **PASS** |
| `not-process-hacker-executed` | Process | The execution evidence indicates that the command could not be run due to a file not found error, implying Process Hacker was not executed. | command text shows a process-spawning pattern | **PASS** |
| `elevated-privilege-required` | (unclassified) | The YAML specifies elevation is required, but the execution evidence does not confirm if this was a factor in the failure. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1057 Test #8

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `file-exists` | Environment | The YAML specifies that PCHunter must be present on the device, but the execution evidence shows the file was not found. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-process-spawned` | Process | The execution evidence indicates that the process could not be started due to a missing file. | command text shows a process-spawning pattern | **PASS** |
| `elevated-privilege-required` | (unclassified) | The YAML specifies elevation is required, but the execution evidence does not confirm if this was a factor in the failure. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1057 Test #9

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor for this test is 'command_prompt', indicating the use of cmd.exe. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `process-running` | Process | The test involves launching 'taskmgr.exe' to view running processes, indicating that the process manager is running. | no clear process-spawning pattern in command text | **MANUAL REVIEW** |
| `elevated-privilege` | (unclassified) | The YAML specifies 'elevation_required: false', but the exit code -2147467260 might indicate a permission issue. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1059.001 Test #17

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor for this test is 'command_prompt' running 'powershell.exe', so PowerShell must be invokable from the command prompt. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `user-has-interactive-session` | Privilege/User | The evidence shows the command was run interactively and output was displayed to the user, so an interactive session is required. | no explicit interactive-session evidence in YAML — flagged in methodology notes as typically inferred from execution artifacts rather than YAML structure | **MANUAL REVIEW** |
| `process-spawned-powershell` | Process | The evidence includes a ProcessId and ThreadId for the PowerShell process that executed the command. | YAML executor is 'command_prompt', predicate does not reference it; no clear process-spawning pattern in command text | **MANUAL REVIEW** |
| `powershell-command-executed` | Process | The test executed a PowerShell command and produced the expected output ('Hello, from PowerShell!'), confirming successful command execution. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `information-written-host-output` | Information | The command output ('Hello, from PowerShell!') was written to the host, as shown in the evidence. | no clear output-write pattern in command text | **MANUAL REVIEW** |
| `elevated-privilege` | (unclassified) | The YAML does not specify elevation_required for this test, and the evidence does not indicate whether admin rights were needed or used. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `obfuscated-powershell` | (unclassified) | The input argument is an obfuscated PowerShell command, but the effect of obfuscation is not directly observable in the evidence; flag for review if obfuscation-specific predicates are needed. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1070.004 Test #10

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `file-exists` | Information | The test requires the TeamViewer log file to exist before it can be deleted, as indicated by the dependency to create the file if it does not exist. | No matching rule for this predicate | **MANUAL REVIEW** |
| `file-deleted` | Information | The execution evidence shows that the TeamViewer log file was successfully deleted, as indicated by the exit code 0. | No matching rule for this predicate | **MANUAL REVIEW** |
| `elevation-required` | (unclassified) | The YAML does not specify elevation for this specific test, but similar tests in the YAML do, so this might need human review. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1070.004 Test #11

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires elevated privileges to clear the recycle bin, as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'Access is denied', indicating a failure due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `recycle-bin-cleared` | (unclassified) | The intended effect of clearing the recycle bin was not achieved due to access denial, so this effect is uncertain. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1070.004 Test #4

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `file-exists` | Information | The YAML specifies that the file to delete must exist on disk at the specified location as a prerequisite. | No matching rule for this predicate | **MANUAL REVIEW** |
| `cmd-invokable` | Executor | The executor for this test is 'command_prompt', indicating the use of cmd.exe. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `not-file-exists` | Information | The test aims to delete a file, and successful execution would result in the file no longer existing. | No matching rule for this predicate | **MANUAL REVIEW** |
| `access-denied` | (unclassified) | The evidence shows 'Could Not Find' message, which might indicate a missing file or access issue, but the exit code is 0, suggesting no error. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1070.004 Test #5

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `folder-exists` | Information | The YAML specifies that the folder must exist in order to be deleted, as indicated by the prereq_command. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-folder-exists` | Information | The intended effect of the test is to delete the specified folder, which would result in the folder no longer existing. | No matching rule for this predicate | **MANUAL REVIEW** |
| `execution-failed` | (unclassified) | The evidence shows 'The system cannot find the file specified', indicating the folder did not exist, leading to a failure in execution. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1070.004 Test #6

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `file-exists` | Information | The YAML specifies that the file must exist before it can be deleted, as indicated by the prereq_command. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-file-exists` | Information | The intended effect of the test is to delete the specified file, although the evidence shows it failed due to the file not existing. | No matching rule for this predicate | **MANUAL REVIEW** |
| `execution-failed` | (unclassified) | The evidence shows the command failed because the file did not exist, which contradicts the precondition. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1070.004 Test #7

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `folder-exists` | Information | The YAML specifies that the folder must exist in order to be deleted, as indicated by the prereq_command. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-folder-exists` | Information | The intended effect of the test is to delete the specified folder, but the evidence shows the folder did not exist, hence the effect is negated. | No matching rule for this predicate | **MANUAL REVIEW** |
| `execution-success` | (unclassified) | The exit code is 0, which typically indicates success, but the evidence shows the folder was not found, suggesting a discrepancy. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1070.004 Test #9

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `file-exists` | Information | The test requires a prefetch file to exist in the directory, as indicated by the error 'Cannot index into a null array'. | No matching rule for this predicate | **MANUAL REVIEW** |
| `user-is-admin` | Privilege/User | The executor specifies 'elevation_required: true', indicating administrative privileges are needed. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `not-file-exists` | Information | The intended effect of the test is to delete a prefetch file, reducing the count by one. | No matching rule for this predicate | **MANUAL REVIEW** |
| `execution-success` | (unclassified) | The exit code is 0, but the error suggests the operation did not succeed as intended. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1087.001 Test #10

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor for this test is 'command_prompt', indicating the need for CMD to be invokable. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `not-command-recognized` | Process | The evidence shows that 'query' is not recognized as a command, indicating a failure in command execution. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `user-is-admin` | (unclassified) | The test does not specify if administrative privileges are required, but CMD execution often implies user privilege context. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1087.001 Test #11

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `file-exists` | Information | The test requires the existence of the plink executable at the specified path. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-command-executed` | Process | The command failed to execute because plink.exe was not recognized as a command. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `elevated-privilege-required` | (unclassified) | The YAML specifies elevation_required as false, but the test might still require certain privileges to execute successfully. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1087.001 Test #8

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `executor-is-command-prompt` | Executor | The executor specified in the YAML is 'command_prompt', indicating the use of the Windows command prompt. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `accounts-enumerated` | Information | The evidence shows successful enumeration of user accounts and groups on the Windows system. | No matching rule for this predicate | **MANUAL REVIEW** |
| `credentials-discovered` | Information | The evidence includes stored credentials being listed, indicating discovery of credential information. | No matching rule for this predicate | **MANUAL REVIEW** |

---

# Predicate cross-check — T1087.001 Test #9

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor for this test is PowerShell, as indicated by the command execution context. | YAML executor 'powershell' matches predicate | **PASS** |
| `accounts-enumerated` | Information | The evidence shows successful enumeration of user accounts and groups, as indicated by the detailed account and group information output. | No matching rule for this predicate | **MANUAL REVIEW** |
| `elevated-privilege-required` | (unclassified) | The YAML does not specify elevation required for this specific test, but PowerShell enumeration often requires elevated privileges. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #10

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses 'reg.exe' via the command prompt to modify the registry. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry, as indicated by the 'Access is denied' error. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify the registry, but the 'Access is denied' error indicates this did not occur. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #11

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The test uses PowerShell to execute the command for modifying the registry. | YAML executor 'powershell' matches predicate | **PASS** |
| `user-has-write-access-to-registry` | Privilege/User | The test attempts to modify a registry path under HKCU, which requires write access. | no registry reference found in YAML command text | **FLAG** |
| `not-registry-key-created` | Environment | The evidence shows that the registry path does not exist, so the key was not created. | no registry reference found in YAML command text | **FLAG** |
| `exit-code-0` | (unclassified) | The exit code 0 suggests success, but the evidence indicates failure due to a missing path. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #12

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry, as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating that the registry modification was not successful due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify the registry to disable Task Manager, but this was not achieved due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #13

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses 'reg.exe' via the command prompt to modify the registry. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry key in HKCU, as indicated by the 'elevation_required: true' and the 'Access is denied' error. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `registry-key-modified` | (unclassified) | The intended effect of modifying the registry key was not achieved due to 'Access is denied' error. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #14

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry key under HKEY_LOCAL_MACHINE, as indicated by the 'elevation_required: true' and the 'Access is denied' error. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify the registry key to disable the Windows shutdown button, but the 'Access is denied' error indicates this did not occur. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #15

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry, as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating that the registry modification was not successful due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify the registry key to disable the Windows LogOff button, but this was not achieved due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #16

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry key under HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'Access is denied,' indicating the registry modification was not successful due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect of modifying the registry key to disable the change password feature was not achieved due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #17

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry, as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating that the registry modification was not successful due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | This predicate is uncertain because the evidence indicates the modification did not occur due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #18

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires elevation to modify registry keys under HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer, which typically requires administrative privileges. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `not-registry-run-key-set` | Environment | The registry modification to set the NoDesktop policy failed due to 'Access is denied', indicating the registry key was not set. | command references registry but no explicit hive path matched | **MANUAL REVIEW** |
| `command-prompt-invokable` | (unclassified) | The executor is command_prompt, but the failure suggests a privilege issue rather than an invocation issue. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #19

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires elevation to modify registry keys under HKEY_CURRENT_USER, which failed due to 'Access is denied'. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify a registry key, but the operation failed due to access denial, so this effect did not occur. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #1

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses 'reg.exe' via the command prompt to modify the registry. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `registry-key-modified` | Environment | The registry key 'HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced' was modified to set 'HideFileExt' to 1. | command references registry but no explicit hive path matched | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #20

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry, as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating that the registry modification was not successful due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect of modifying the registry key was not achieved due to access denial, so this effect is uncertain. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #21

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry key, as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating that the attempt to modify the registry was unsuccessful due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect of modifying the registry key was not achieved due to access denial, so this effect is uncertain. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #22

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry, as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating a failure due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect of modifying the registry key was not achieved due to access denial, so this effect is uncertain. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #23

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires elevation to modify registry keys under HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer, which typically requires administrative privileges. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `not-registry-run-key-set` | Environment | The registry modification attempt failed with 'Access is denied', indicating no changes were made to the registry. | command references registry but no explicit hive path matched | **MANUAL REVIEW** |
| `access-denied` | (unclassified) | The error message 'Access is denied' suggests a privilege issue, but it's unclear if this is due to lack of admin rights or another restriction. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #24

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry, as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating a failure due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify a registry key, but this did not occur due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #25

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires elevation as indicated by 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating a failure due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify a registry key, but this did not occur due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #26

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses the command prompt to execute the registry modification command. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry, as indicated by the 'Access is denied' error. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify a registry key, but the operation failed due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #27

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry, as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating that the registry modification was not successful due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect of modifying the registry key to hide the Windows clock was not achieved due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #28

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry, as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating that the registry modification was not successful due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify the registry key, but this did not occur due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #29

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry key under HKCU, as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating that the registry modification was not successful due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect of modifying the registry key was not achieved due to access denial, so this effect is uncertain. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #2

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor specified in the YAML is 'command_prompt', indicating the use of cmd.exe. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `user-is-admin` | Privilege/User | The test requires administrative rights as indicated by 'elevation_required: true'. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating a failure due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify a registry key, but this did not occur due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #30

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry, as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating that the registry modification was not successful due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify the registry key, but this did not occur due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #31

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry key under HKEY_CURRENT_USER, but the execution evidence shows 'Access is denied', indicating a lack of necessary privileges. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify a registry key, but the execution failed due to access denial, so this effect did not occur. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #32

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses the command prompt to execute registry modifications. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `registry-key-modified` | Environment | The registry keys HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced\ShowInfoTip and ShowCompColor were modified as part of the test. | registry hive reference found in command (hkcu\) | **PASS** |

---

# Predicate cross-check — T1112 Test #33

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses the command prompt to execute registry modifications. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify registry keys under HKCU\Software\Policies. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'Access is denied' errors, indicating a failure due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify registry keys, but this did not occur due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #34

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry under HKLM, as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating that the registry modification was not successful due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-written` | (unclassified) | The intended effect was to write a registry key, but this was not achieved due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #35

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry under HKLM, as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating that the attempt to modify the registry was unsuccessful due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-created` | (unclassified) | The intended effect was to create a registry key for service persistence in Safe Mode with Network, but this was not achieved due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #36

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses 'reg.exe' via the command prompt to modify the registry. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry under HKEY_CURRENT_USER. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `registry-key-modified` | Environment | The registry key 'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\PushNotifications' was modified to disable toast notifications. | command references registry but no explicit hive path matched | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #37

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses 'reg.exe' via the command prompt to modify the registry. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry under HKLM, as indicated by the 'elevation_required: true' and the 'Access is denied' error. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `registry-key-modified` | (unclassified) | The intended effect of modifying the registry key was not achieved due to 'Access is denied' error. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #38

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry key under HKLM, as indicated by the 'elevation_required: true' and the 'Access is denied' error. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify a registry key to suppress Windows Defender notifications, but the operation failed due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #39

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry key under HKLM, as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating that the registry modification was not successful due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect of modifying the registry key to allow RDP remote assistance was not achieved due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #3

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses 'reg.exe' via the command prompt to modify the registry. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the HKLM registry key, as indicated by 'elevation_required: true'. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating a failure due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify the registry key, but this did not occur due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #40

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses 'reg add' commands executed via the command prompt. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `registry-key-created` | Environment | The test creates a registry key at HKCU\Software\Microsoft\Windows\CurrentVersion\Run with the value 'NetWire'. | registry hive reference found in command (hkcu\) | **PASS** |
| `registry-key-created` | Environment | The test creates a registry key at HKCU\SOFTWARE\NetWire with values 'HostId' and 'Install Date'. | registry hive reference found in command (hkcu\) | **PASS** |

---

# Predicate cross-check — T1112 Test #41

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses 'reg.exe' via the command prompt to modify the registry. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `registry-key-created` | Environment | The test creates a registry key at 'HKCU\Software\AppDataLow\Software\Microsoft\3A861D62-51E0-15700F2219A4'. | registry hive reference found in command (hkcu\) | **PASS** |

---

# Predicate cross-check — T1112 Test #42

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `registry-key-exists` | Information | The test requires the 'MR9' Remote Desktop Connection history key to exist as a prerequisite. | command references registry but no explicit hive path matched | **MANUAL REVIEW** |
| `not-registry-key-exists` | Information | The test attempts to delete registry keys, but the evidence shows the keys were not found, indicating they do not exist. | command references registry but no explicit hive path matched | **MANUAL REVIEW** |
| `elevated-privilege-required` | (unclassified) | The test description mentions elevation is required, but the evidence does not confirm if this was a factor in the failure. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #43

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses the command prompt to execute registry modifications. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify HKLM registry keys. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows an error indicating invalid key name or syntax, suggesting access or syntax issues. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify a registry key, but the execution failed, so this effect is uncertain. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #44

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses the command prompt to execute registry modifications. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify registry keys, as indicated by the 'Access is denied' errors. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify registry keys, but the 'Access is denied' errors indicate this did not occur. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #45

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges as indicated by 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating a failure due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify a registry key, but this did not occur due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #46

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses the command prompt to execute the registry modification command. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `user-is-admin` | Privilege/User | The test modifies a registry key under HKEY_CURRENT_USER, which typically requires administrative privileges. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `registry-key-modified` | Environment | The registry key HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Winlogon was modified to enable multiple user sessions. | command references registry but no explicit hive path matched | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #47

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry key under HKLM, as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating that the action failed due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect of modifying the registry key was not achieved due to access denial, so this effect is uncertain. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #48

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry under HKLM, as indicated by the 'elevation_required: true' and the 'Access is denied' error. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify a registry key, but the operation failed due to access denial, so this effect did not occur. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #49

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses the command prompt to execute the registry modification command. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `user-is-admin` | Privilege/User | The test requires administrative privileges as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating a failure due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect of modifying the registry key did not occur due to access denial, so this effect is uncertain. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #4

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor for this test is PowerShell, as indicated by the command using 'Set-ItemProperty'. | YAML executor 'powershell' matches predicate | **PASS** |
| `user-is-admin` | Privilege/User | The test requires elevation, as indicated by 'elevation_required: true'. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `registry-key-modified` | Environment | The test modifies the registry key 'HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest' to store plaintext passwords. | no registry reference found in YAML command text | **FLAG** |

---

# Predicate cross-check — T1112 Test #50

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry, as indicated by 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating a failure due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect of modifying the registry key to enable RDP was not achieved due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #51

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry key under HKLM, as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating that the registry modification was not successful due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | This predicate is uncertain because the evidence indicates the operation failed due to access denial, so the registry key was not modified. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #52

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry key under HKLM, as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating that the registry modification was not successful due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | This predicate is uncertain because the evidence indicates the modification did not occur due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #53

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry key under HKLM, as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating that the registry modification was not successful due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | This effect is uncertain because the evidence indicates the operation failed due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #54

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry key under HKLM, as indicated by the 'elevation_required: true' and the 'Access is denied' error. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify a registry key, but the 'Access is denied' error indicates this did not occur. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #55

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses the command prompt to execute the registry modification command. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry key under HKLM, as indicated by the 'elevation_required: true' and the 'Access is denied' error. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `registry-key-modified` | (unclassified) | The intended effect of modifying the registry key was not achieved due to 'Access is denied' error, so this effect is uncertain. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #56

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry, as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating that the registry modification attempt was blocked due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect of modifying the registry key was not achieved due to access denial, so this effect is uncertain. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #57

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The test uses PowerShell to execute the command. | YAML executor 'powershell' matches predicate | **PASS** |
| `user-is-not-admin` | Privilege/User | The error 'Requested registry access is not allowed' indicates insufficient privileges, suggesting the user is not an admin. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `registry-key-write-failed` | (unclassified) | The evidence shows a failure to write to the registry, but it's unclear if this should be an effect or just a failed attempt. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #58

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses the command prompt to execute registry modifications. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `registry-key-modified` | Environment | The registry keys 'MaxConnectionsPerServer' and 'MaxConnectionsPer1_0Server' were modified to allow simultaneous downloads. | registry hive reference found in command (hkcu\) | **PASS** |

---

# Predicate cross-check — T1112 Test #59

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses the command prompt to execute registry modifications. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `registry-key-modified` | Environment | The registry keys for Internet Zone Protocol Defaults were modified to set 'http' and 'https' DWORD values to 0. | command references registry but no explicit hive path matched | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #5

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The test uses PowerShell to modify the registry, as indicated by the executor name in the YAML. | YAML executor 'powershell' matches predicate | **PASS** |
| `registry-key-modified` | Environment | The registry key HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains\bad-domain.com was modified to add a domain to the trusted sites zone, as evidenced by the execution output. | no registry reference found in YAML command text | **FLAG** |

---

# Predicate cross-check — T1112 Test #60

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The test uses PowerShell to modify registry values, indicating that PowerShell must be invokable. | YAML executor 'powershell' matches predicate | **PASS** |
| `registry-key-modified` | Environment | The test modifies the registry keys 'http' and 'https' under 'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\ProtocolDefaults' to weaken browser security settings. | command references registry but no explicit hive path matched | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #61

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses the command prompt to execute the registry modification command. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry key in HKLM, as indicated by the 'elevation_required: true' and the 'Access is denied' error. | elevation_required not set in YAML | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect of modifying the registry key was not achieved due to 'Access is denied' error, so this effect is uncertain. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #62

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry key under HKLM, as indicated by the 'elevation_required: true' and the 'Access is denied' error. | elevation_required not set in YAML | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify a registry key, but the operation failed due to access denial, so no registry modification occurred. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #63

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry key in HKLM, as indicated by the 'elevation_required: true' and the 'Access is denied' error. | elevation_required not set in YAML | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify a registry key, but the operation failed due to access denial, so this effect did not occur. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #64

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry key under HKLM, as indicated by the 'elevation_required: true' in the YAML. | elevation_required not set in YAML | **MANUAL REVIEW** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating that the registry modification was not successful due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | This predicate is flagged because the evidence shows the modification did not occur due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #65

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry key under HKLM, as indicated by the 'elevation_required: true' in the YAML. | elevation_required not set in YAML | **MANUAL REVIEW** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating that the registry modification was not successful due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | This effect is uncertain because the execution evidence indicates the operation failed due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #66

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses the command prompt to execute the registry modification command. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry key under HKCU. | elevation_required not set in YAML | **MANUAL REVIEW** |
| `registry-key-modified` | Environment | The registry key HKCU\Software\Microsoft\Windows\Windows Error Reporting\DontShowUI is modified to disable the ShowUI setting. | registry hive reference found in command (hkcu\) | **PASS** |

---

# Predicate cross-check — T1112 Test #67

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses the command prompt to execute the registry modification command. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry under HKCU. | elevation_required not set in YAML | **MANUAL REVIEW** |
| `registry-key-modified` | Environment | The registry key HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ProxyEnable is modified to enable proxy settings. | registry hive reference found in command (hkcu\) | **PASS** |

---

# Predicate cross-check — T1112 Test #68

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses the command prompt to execute the registry modification command. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `user-is-admin` | Privilege/User | The test requires elevation, indicating administrative privileges are needed. | elevation_required not set in YAML | **MANUAL REVIEW** |
| `registry-key-modified` | Environment | The registry key 'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ProxyServer' is modified to set up a proxy server. | registry hive reference found in command (hkcu\) | **PASS** |

---

# Predicate cross-check — T1112 Test #69

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses the command prompt to execute the registry modification command. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `registry-key-modified` | Environment | The registry key 'HKCU\Software\Microsoft\Terminal Server Client\AuthenticationLevelOverride' was modified to set the value to 0, as indicated by the successful execution message. | registry hive reference found in command (hkcu\) | **PASS** |

---

# Predicate cross-check — T1112 Test #6

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The test uses PowerShell to execute the registry modification command. | YAML executor 'powershell' matches predicate | **PASS** |
| `registry-key-modified` | Environment | The evidence shows a JavaScript block was added to the registry at HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings. | no registry reference found in YAML command text | **FLAG** |

---

# Predicate cross-check — T1112 Test #70

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry key under HKLM, as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating that the registry modification was not successful due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify the registry key to enable RDP, but this was not achieved due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #71

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry key in HKLM, as indicated by the 'elevation_required: true' and the 'Access is denied' error. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify the registry key to disable prefetch, but the operation failed due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #72

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor for this test is PowerShell, as indicated by the command using PowerShell cmdlets. | YAML executor 'powershell' matches predicate | **PASS** |
| `user-is-admin` | Privilege/User | The test requires elevation, as indicated by 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `registry-key-set` | Environment | The command modifies the registry key 'HKLM\Software\Policies\Microsoft\Windows NT\Terminal Services' to set the 'Shadow' value, indicating a persistent change. | no registry reference found in YAML command text | **FLAG** |
| `remote-firewall-rule-enabled` | (unclassified) | The command includes enabling a firewall rule on a remote machine, which is not directly captured in the current predicate categories. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #73

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `executor-is-command-prompt` | Executor | The test uses 'command_prompt' as the executor to run the command. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `user-is-admin` | Privilege/User | The test requires elevated privileges to execute the registry modification command. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `shimcache-flushed` | Environment | The command 'Rundll32.exe apphelp.dll,ShimFlushCache' is executed to flush the ShimCache. | No matching rule for this predicate | **MANUAL REVIEW** |
| `evidence-of-shimcache-flush` | (unclassified) | The evidence does not explicitly confirm the ShimCache was flushed, only that the command executed successfully. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #74

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires elevation to modify the registry key under HKLM, which typically requires administrative privileges. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'Access is denied', indicating the operation did not succeed due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify a registry key to disable RDP, but this did not occur due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #75

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry key under HKLM, as indicated by the 'elevation_required: true' and the 'Access is denied' error. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `registry-key-modified` | (unclassified) | The intended effect of modifying the registry key to enforce smart card authentication did not occur due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #76

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry key under HKLM, as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating that the registry modification was not successful due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect of modifying the registry key was not achieved due to access denial, so this effect is uncertain. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #77

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses the command prompt to execute the registry modification command. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry key under HKLM, as indicated by the 'elevation_required: true' and the 'Access is denied' error. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `registry-key-modified` | (unclassified) | The intended effect of modifying the registry key was not achieved due to 'Access is denied' error. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #78

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor specified in the YAML is 'command_prompt', indicating the use of cmd.exe. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `user-is-admin` | Privilege/User | The test requires elevation as indicated by 'elevation_required: true', suggesting administrative privileges are needed. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating a failure due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify a registry key, but this did not occur due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #79

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry, as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating that the registry modification was not successful due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify the registry key 'UseTPMPIN', but this was not achieved due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #7

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The test uses PowerShell to modify the registry execution policy. | YAML executor 'powershell' matches predicate | **PASS** |
| `user-is-not-admin` | Privilege/User | The evidence shows 'Access to the registry key is denied' indicating lack of administrative privileges. | elevation_required not set in YAML | **MANUAL REVIEW** |
| `execution-policy-bypass-attempted` | (unclassified) | The test attempted to change the execution policy to Bypass, but failed due to permission issues. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #80

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry key under HKLM, as indicated by the 'elevation_required: true' and the 'Access is denied' error. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `registry-key-modified` | (unclassified) | The intended effect of modifying the registry key was not achieved due to the 'Access is denied' error. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #81

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor specified in the YAML is 'command_prompt', indicating the use of cmd.exe. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `user-is-admin` | Privilege/User | The test requires elevation as indicated by 'elevation_required: true', implying administrative privileges are needed. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating a failure due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify a registry key, but this did not occur due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #82

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor specified in the YAML is 'command_prompt', indicating the use of cmd.exe. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `user-is-admin` | Privilege/User | The test requires elevation as indicated by 'elevation_required: true', but execution failed with 'Access is denied', suggesting admin privileges are needed. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify a registry key, but the operation failed due to access denial, so this effect did not occur. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #83

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry key under HKLM, as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating that the registry modification was not successful due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | This effect is uncertain because the evidence shows the operation failed due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #84

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry, as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating a failure due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect of modifying the registry key was not achieved due to access denial, so this effect is uncertain. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #85

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses the command prompt to execute the registry modification command. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry under HKLM, as indicated by the 'elevation_required: true' and the 'Access is denied' error. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `registry-key-modified` | (unclassified) | The intended effect of modifying the registry key did not occur due to 'Access is denied' error. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #86

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry under HKLM, as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating that the registry modification attempt failed due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify the registry key for RDP initial program, but this was not achieved due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #87

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry key under HKLM, as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'ERROR: Access is denied', indicating that the registry modification was not successful due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-modified` | (unclassified) | This effect is expected from the YAML description but was not achieved due to the access denied error. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #88

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The test uses the command prompt to execute the registry modification command. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry under HKLM, as indicated by the 'Access is denied' error. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify the registry, but the 'Access is denied' error indicates this did not occur. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #89

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify the registry under HKLM, as indicated by the 'elevation_required: true' and the 'Access is denied' error. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify the registry key for persistence, but the operation failed due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #8

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires administrative rights to modify the Local Machine registry, as indicated by 'elevation_required: true' and the 'Access is denied' errors. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `registry-key-modified` | (unclassified) | The intended effect of modifying the registry key was not achieved due to access denial, so this effect is not applicable. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #90

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test execution failed with 'Access is denied', indicating that administrative privileges are required to modify the registry in this manner. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `registry-key-modified` | (unclassified) | The intended effect was to modify a registry key, but the operation failed due to access denial, so this effect did not occur. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1112 Test #9

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The test uses PowerShell to modify registry keys, as indicated by the executor name 'powershell'. | YAML executor 'powershell' matches predicate | **PASS** |
| `user-is-admin` | Privilege/User | The test requires administrative privileges to modify HKLM registry keys, as indicated by the 'elevation_required: true' in the YAML. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'PermissionDenied' errors, indicating that registry access was denied due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `process-spawned` | (unclassified) | The evidence does not confirm if any process was successfully spawned due to the access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1136.001 Test #4

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor for this test is 'command_prompt', indicating the use of CMD. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `elevated-privilege` | Privilege/User | The YAML specifies 'elevation_required: true', indicating that elevated privileges are needed. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'Access is denied', indicating a failure due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `user-created` | (unclassified) | The intended effect of creating a user was not achieved due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1136.001 Test #5

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor specified in the YAML is PowerShell, indicating the need for PowerShell to be invokable. | YAML executor 'powershell' matches predicate | **PASS** |
| `elevated-privilege` | Privilege/User | The YAML specifies 'elevation_required: true', indicating that elevated privileges are needed to execute the command. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `access-denied` | Privilege/User | The execution evidence shows 'Access denied', indicating that the attempt to create a user was blocked due to insufficient privileges. | No matching rule for this predicate | **MANUAL REVIEW** |
| `user-created` | (unclassified) | The intended effect of creating a user did not occur due to access denial, so this effect is uncertain. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1136.001 Test #8

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The YAML specifies that elevation is required, and the execution evidence shows 'Access is denied', indicating a lack of necessary privileges. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `windows-admin-user-created` | (unclassified) | The intended effect of creating a new Windows admin user did not occur due to access denial. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1136.001 Test #9

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor for this test is PowerShell, as indicated by the 'name: powershell' in the YAML. | YAML executor 'powershell' matches predicate | **PASS** |
| `elevated-privilege` | Privilege/User | The YAML specifies 'elevation_required: true', indicating that elevated privileges are needed. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `not-user-created` | Information | The execution evidence shows a failure to resolve the remote name, preventing the user creation. | No matching rule for this predicate | **MANUAL REVIEW** |
| `network-access-required` | (unclassified) | The failure to resolve 'proxy.atomic-test.com' suggests a network dependency that was unmet. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1547.001 Test #1

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor for this test is 'command_prompt', indicating the attack requires the ability to invoke commands via cmd.exe. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `user-has-write-access-hkcu-run-key` | Privilege/User | The registry key targeted is under HKCU, so the user must have write access to their own registry hive. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-run-key-set` | Environment | The test adds a value ('Atomic Red Team') to HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run, establishing persistence via the Run key. | registry hive reference found in command (hkcu\) | **PASS** |
| `registry-key-written` | Information | A new registry value is written as part of the persistence mechanism, as described in the YAML and implied by successful execution. | registry hive reference found in command (hkcu\); command text shows an output/write pattern | **PASS** |
| `process-spawned` | (unclassified) | The test only modifies the registry and does not directly spawn a new process as part of the persistence action; process creation would occur on next logon, not during the test. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `file-created` | (unclassified) | No evidence in the YAML or execution output that a new file is created as part of this specific test; only a registry value is set. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1560.001 Test #10

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `plink-executable-missing` | Environment | The evidence indicates that the plink executable was not found at the expected path, which is a prerequisite for the test. | No matching rule for this predicate | **MANUAL REVIEW** |
| `command-not-found-error` | Process | The execution evidence shows a CommandNotFoundException for the plink executable, indicating a failure in process execution. | YAML executor is 'powershell', predicate does not reference it | **MANUAL REVIEW** |
| `file-not-found-error` | Information | The evidence indicates a failure to find the path 'C:\temp\loghost.txt', suggesting an issue with file access or creation. | No matching rule for this predicate | **MANUAL REVIEW** |
| `elevated-privilege-required` | (unclassified) | The YAML specifies elevation_required: true, but the evidence does not confirm if privilege elevation was attempted or required. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1560.001 Test #11

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `file-exists` | Information | The test requires a sample file for compression to be located at the specified location (C:\Temp\sam.hiv), but the evidence shows it was missing. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-file-compressed` | Information | The execution evidence indicates that the file compression did not occur due to the missing input file. | No matching rule for this predicate | **MANUAL REVIEW** |
| `executor-failure` | (unclassified) | The evidence shows an error during execution, but it's unclear if this should be a separate predicate or is covered by the 'not-file-compressed' effect. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1560.001 Test #12

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `user-is-admin` | Privilege/User | The test requires admin privileges as indicated by the precondition check for administrator role. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `appdata-folder-exists` | Information | The test requires the AppData folder to exist, as indicated by the precondition check. | No matching rule for this predicate | **MANUAL REVIEW** |
| `file-copy-failed` | Information | The evidence shows multiple 'Copy-Item' failures due to files being in use, indicating that some files could not be copied. | No matching rule for this predicate | **MANUAL REVIEW** |
| `zip-file-created` | Information | The test aims to create a ZIP archive of the AppData folder, although the evidence does not confirm successful creation due to errors. | No matching rule for this predicate | **MANUAL REVIEW** |
| `process-timeout` | (unclassified) | The process timed out, which may indicate incomplete execution, but it's unclear if this affects the final outcome. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1560.001 Test #1

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `rar-tool-installed` | Environment | The YAML specifies that the RAR tool must be installed at the specified location. | No matching rule for this predicate | **MANUAL REVIEW** |
| `command-failed` | Process | The execution evidence shows that the command failed with 'C:\Program' is not recognized as an internal or external command. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `file-compressed` | (unclassified) | The intended effect of compressing files was not achieved due to the command failure. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1560.001 Test #2

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `winrar-installed` | Environment | The test requires WinRAR to be installed at a specified location, as indicated by the dependency check for the RAR executable. | No matching rule for this predicate | **MANUAL REVIEW** |
| `file-compressed` | Information | The test compresses data into a RAR file, as evidenced by the creation of 'encrypted_file.txt' in the specified directory. | No matching rule for this predicate | **MANUAL REVIEW** |
| `path-not-found` | (unclassified) | The evidence mentions 'The system cannot find the path specified,' which may indicate an issue with the execution environment or path setup. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1560.001 Test #3

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `winzip-installed` | Environment | The YAML specifies that Winzip must be installed at the specified location. | No matching rule for this predicate | **MANUAL REVIEW** |
| `file-compressed` | Information | The evidence shows that a file named 'encrypted_file.txt' was created and presumably compressed using Winzip. | No matching rule for this predicate | **MANUAL REVIEW** |
| `directory-exists` | (unclassified) | The evidence mentions a directory '.\tmp\victim-files' already existing, but it's unclear if this is a precondition or an effect. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1560.001 Test #4

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `7zip-installed` | Environment | The YAML specifies that the 7zip tool must be installed at the specified location. | No matching rule for this predicate | **MANUAL REVIEW** |
| `file-compressed` | Information | The evidence shows that a file named 'encrypted_file.txt' was created, indicating data compression. | No matching rule for this predicate | **MANUAL REVIEW** |
| `password-protected-archive-created` | (unclassified) | The evidence does not confirm if the archive was password-protected as intended. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #10 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor is 'powershell', so the system must support invoking PowerShell commands. | YAML executor 'powershell' matches predicate | **PASS** |
| `file-exists-griffon-recon-vbs` | Information | The dependency in the YAML specifies that the Griffon recon VBScript must exist at the specified path before execution. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-process-spawned-cscript-griffon-recon` | Process | The evidence shows the script file was missing, so the cscript process for Griffon Recon was not spawned. | no clear process-spawning pattern in command text | **MANUAL REVIEW** |
| `not-system-info-discovered` | Information | No system information was collected or displayed due to the missing script file, as indicated by the input error. | No matching rule for this predicate | **MANUAL REVIEW** |
| `exit-code-0-despite-error` | (unclassified) | The exit code is 0 even though the script file was missing; this may indicate a wrapper or error-handling behavior that should be reviewed for accurate effect modeling. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #11 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor is 'command_prompt', indicating the attack requires the ability to invoke commands via cmd.exe. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `environment-variables-discovered` | Information | The evidence shows a full dump of environment variables, confirming that environment variable information was successfully gathered. | No matching rule for this predicate | **MANUAL REVIEW** |
| `process-spawned-cmd` | Process | The command was executed via cmd.exe, which implies a cmd process was spawned for this action. | YAML executor is 'command_prompt', predicate does not reference it; no clear process-spawning pattern in command text | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #14 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor is 'powershell', so the system must support invoking PowerShell commands. | YAML executor 'powershell' matches predicate | **PASS** |
| `network-connectivity-to-github` | Environment | The script attempts to download a file from 'raw.githubusercontent.com', so network connectivity to GitHub is required. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-information-system-info-discovered` | Information | The evidence shows that the download failed and 'winPEAS' was not recognized, so no system information was actually discovered. | No matching rule for this predicate | **MANUAL REVIEW** |
| `powershell-script-executed` | (unclassified) | The script attempted to execute, but due to download failure and missing command, it did not complete its intended function. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `file-downloaded-winpeas-ps1` | (unclassified) | The download did not succeed, so this effect did not occur, but it is a possible effect if the network were available. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `process-spawned-winpeas` | (unclassified) | The 'winPEAS' process was not spawned due to the command not being recognized; flagging for review in case partial execution is relevant. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #15 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor is PowerShell, as shown by the command block and the error messages referencing PowerShell cmdlets. | YAML executor 'powershell' matches predicate | **PASS** |
| `internet-connectivity` | Environment | The test attempts to download a script from GitHub, which requires outbound internet access; the failure indicates this was expected as a precondition. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-information-system-info-discovered` | Information | No system information was actually discovered or output due to the failure to download and run the intended script. | No matching rule for this predicate | **MANUAL REVIEW** |
| `process-spawned` | (unclassified) | A PowerShell process was started, but since the main payload did not execute, it's unclear if this should be considered a meaningful effect. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `user-is-admin` | (unclassified) | The test does not require elevation and there is no evidence of privilege escalation or requirement, so this is not included, but a human should confirm. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #16 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor is 'powershell', so the system must support invoking PowerShell commands. | YAML executor 'powershell' matches predicate | **PASS** |
| `internet-connectivity` | Environment | The script attempts to download a file from 'raw.githubusercontent.com', implying internet access is required for success. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-information-system-info-discovered` | Information | The evidence shows the download failed and the 'oldchecks' command was not found, so no system information was actually discovered. | No matching rule for this predicate | **MANUAL REVIEW** |
| `process-spawned` | (unclassified) | A PowerShell process was started, but since the main payload failed to download, it's unclear if any meaningful process state relevant to the attack was created. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `user-is-admin` | (unclassified) | Privilege elevation is not required for this test, but some WinPwn functions may require it; the evidence does not clarify if admin rights were needed or obtained. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #17 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor for this test is 'powershell', as shown in the YAML and the evidence (powershell.exe commands). | YAML executor 'powershell' matches predicate | **PASS** |
| `network-connectivity` | Environment | The test attempts to download a script from GitHub, which requires outbound network connectivity; the failure in evidence is due to lack of name resolution. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-information-system-info-discovered` | Information | The evidence shows that the script download failed and the 'otherchecks' command was not recognized, so no system information was actually discovered. | No matching rule for this predicate | **MANUAL REVIEW** |
| `process-spawned-powershell` | (unclassified) | A powershell process was started, but since the main payload did not execute, it's unclear if this should be considered a meaningful effect. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `file-downloaded-winpwn-script` | (unclassified) | The script was not downloaded due to network failure, so this effect did not occur. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `elevated-privilege` | (unclassified) | The YAML does not require elevation and the evidence does not indicate privilege escalation, but some WinPwn functions may require it in other contexts. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #18 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor is PowerShell, as shown by the command and error messages referencing PowerShell cmdlets. | YAML executor 'powershell' matches predicate | **PASS** |
| `network-connectivity-to-github` | Environment | The script attempts to download a PowerShell script from raw.githubusercontent.com, implying network access to GitHub is required. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-information-system-info-discovered` | Information | The evidence shows the download failed and the Generalrecon command was not found, so no system information was actually discovered. | No matching rule for this predicate | **MANUAL REVIEW** |
| `process-spawned-powershell` | (unclassified) | A PowerShell process was started, but since the main payload failed, it's unclear if this is meaningful for the attack chain. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `file-downloaded-winpwn-ps1` | (unclassified) | The download of WinPwn.ps1 was attempted but failed, so the file was not created; this is not an effect but could be relevant if the network requirement is met. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #19 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor for this test is PowerShell, as shown by the use of 'iex(new-object net.webclient)...' and 'Morerecon' PowerShell function. | YAML executor 'powershell' matches predicate | **PASS** |
| `network-connectivity` | Environment | The test attempts to download a script from 'raw.githubusercontent.com', implying that outbound network connectivity is required for success. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-information-system-info-discovered` | Information | The evidence shows that the download failed and the 'Morerecon' command was not recognized, so no system information was actually discovered or output. | No matching rule for this predicate | **MANUAL REVIEW** |
| `process-spawned-powershell` | (unclassified) | A PowerShell process was started, but since the main payload failed to download and execute, it's unclear if this should be considered a meaningful effect. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `user-is-standard` | (unclassified) | No evidence in the output about privilege level; the test does not require elevation, but actual user context is not confirmed. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #1 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor is 'command_prompt', so the ability to invoke commands via cmd.exe is required. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `system-information-discovered` | Information | The evidence shows detailed system information (OS, hardware, memory, network, etc.) was displayed, indicating successful discovery. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-read` | Information | The command 'reg query HKLM\SYSTEM\CurrentControlSet\Services\Disk\Enum' was executed and its output is present, showing registry read access. | registry hive reference found in command (hklm\) | **PASS** |
| `process-running` | (unclassified) | No evidence in the output that a long-lived or background process was created; only transient command execution. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `user-is-admin` | (unclassified) | No indication that administrative privileges were required or obtained; the commands succeeded without elevation. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `environment-variable-discovered` | (unclassified) | No evidence that environment variables were specifically targeted or output in this test. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `environment-changed` | (unclassified) | No persistent system/OS state change is indicated by the evidence; all actions are read-only. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #20 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor is PowerShell, as shown by the use of 'iex(new-object net.webclient)...' and the YAML specifying 'name: powershell'. | YAML executor 'powershell' matches predicate | **PASS** |
| `network-connectivity-required` | Environment | The test attempts to download a script from 'raw.githubusercontent.com', indicating that outbound network connectivity is required for success. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-information-discovered` | Information | The evidence shows that the download failed and the RBCD-Check command was not found, so no system or privilege information was actually discovered. | No matching rule for this predicate | **MANUAL REVIEW** |
| `rbcd-check-script-downloaded` | (unclassified) | Flagged because the script download failed, so this effect did not occur; if the download had succeeded, this would be an effect. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `rbcd-check-executed` | (unclassified) | Flagged because the RBCD-Check command was not recognized, so the intended enumeration did not occur. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `privilege-enumeration-performed` | (unclassified) | Flagged because the test's intent is to enumerate RBCD attack paths, but the evidence shows this did not happen due to missing script. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #21 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor is PowerShell, as shown by the command using 'iex' and 'Invoke-watson'. | YAML executor 'powershell' matches predicate | **PASS** |
| `network-connectivity-to-github` | Environment | The script attempts to download a PowerSharpPack script from 'raw.githubusercontent.com', which requires outbound network connectivity. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-information-windows-patches-discovered` | Information | The evidence shows the download failed and 'Invoke-watson' was not recognized, so no patch information was discovered or exfiltrated. | No matching rule for this predicate | **MANUAL REVIEW** |
| `process-spawned-powershell` | (unclassified) | A PowerShell process was likely spawned, but the evidence does not confirm any meaningful or persistent process effect beyond the failed script. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `user-is-standard` | (unclassified) | No evidence of privilege escalation or requirement for elevated rights, but the privilege context is not explicitly confirmed in the evidence. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #22 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor is PowerShell, as shown by the command using 'iex(new-object net.webclient)...' and 'Invoke-SharpUp'. | YAML executor 'powershell' matches predicate | **PASS** |
| `network-access-to-github` | Environment | The script attempts to download from 'raw.githubusercontent.com', implying network access to GitHub is required. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-information-system-info-discovered` | Information | The evidence shows the download failed and 'Invoke-SharpUp' was not recognized, so no system information was actually discovered. | No matching rule for this predicate | **MANUAL REVIEW** |
| `process-spawned-powershell` | (unclassified) | A PowerShell process was started, but since the main payload failed, it's unclear if this is meaningful for the attack chain. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `user-is-standard` | (unclassified) | No evidence of privilege escalation or requirement for admin rights, but the test does not specify user context explicitly. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #23 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor is PowerShell, as shown by the use of 'iex(new-object net.webclient)...' and 'Invoke-Seatbelt'. | YAML executor 'powershell' matches predicate | **PASS** |
| `network-access-to-github` | Environment | The script attempts to download from 'raw.githubusercontent.com', implying network access to GitHub is required for success. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-seatbelt-script-executed` | Process | The evidence shows 'Invoke-Seatbelt' was not recognized, so the Seatbelt script did not execute. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-system-information-collected` | Information | Because the Seatbelt script was not downloaded or run, no system information was collected as intended. | No matching rule for this predicate | **MANUAL REVIEW** |
| `exit-code-0` | (unclassified) | The exit code is 0 despite the failure, but this does not reflect successful information collection; flagging for human review in case the environment interprets exit codes differently. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #24 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor is PowerShell, as shown by the use of PowerShell commands in the YAML and evidence. | YAML executor 'powershell' matches predicate | **PASS** |
| `azurestealth-module-present` | Information | The YAML dependencies require the AzureStealth.ps1 module to exist, and the evidence shows failure due to its absence. | No matching rule for this predicate | **MANUAL REVIEW** |
| `azuread-module-installed` | Information | The YAML dependencies require the AzureAD module to be installed, and the evidence shows failure due to missing cmdlets. | No matching rule for this predicate | **MANUAL REVIEW** |
| `az-module-installed` | Information | The YAML dependencies require the Az module to be installed, and the evidence shows failure due to missing cmdlets. | No matching rule for this predicate | **MANUAL REVIEW** |
| `valid-azure-credentials-provided` | Privilege/User | The test requires valid Azure AD credentials, and the evidence shows failure due to invalid or missing username. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-azurestealth-module-imported` | Information | The evidence shows Import-Module failed due to missing AzureStealth.ps1, so the module was not imported. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-azure-credentials-obtained` | Privilege/User | The evidence shows failure to create a valid PSCredential object, so no credentials were obtained. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-azure-account-connected` | Environment | Connect-AzAccount failed due to missing cmdlet, so no Azure account session was established. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-azuread-connected` | Environment | Connect-AzureAD failed due to missing cmdlet, so no AzureAD session was established. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-azure-admins-discovered` | Information | Scan-AzureAdmins failed due to missing cmdlet, so no admin information was discovered. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `exit-code-0-despite-failures` | (unclassified) | The test exited with code 0 even though all commands failed; this may not reflect true success and should be reviewed. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #27 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor is 'command_prompt', so the ability to invoke commands via cmd.exe is required. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `not-system-info-discovered` | Information | All commands failed ('wmic' and 'Get-WmiObject' not recognized), so no system information was actually discovered. | No matching rule for this predicate | **MANUAL REVIEW** |
| `wmic-present` | (unclassified) | Flagged because the evidence shows 'wmic' is missing, but the YAML assumes it is present; this is a prerequisite that was not met. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `get-wmiobject-present` | (unclassified) | Flagged because 'Get-WmiObject' is not recognized, indicating PowerShell or the relevant module is missing; this is a prerequisite that was not met. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #28 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `command-prompt-invokable` | Executor | The executor for this test is 'command_prompt', so the ability to invoke commands via the Windows command prompt is required. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `system-information-discovered` | Information | The test is designed to collect and display system information, as described in the YAML and implied by the command 'systeminfo' and registry queries. | No matching rule for this predicate | **MANUAL REVIEW** |
| `access-denied-or-command-failed` | (unclassified) | The exit code is 1, which may indicate a failure or partial execution, but without more detailed error output, it's unclear if any information was actually retrieved. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #29 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor is 'command_prompt', so the ability to invoke cmd.exe is required. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `registry-key-read` | Information | The command queries the registry key 'HKEY_CURRENT_USER\Control Panel\International\Geo', and the evidence shows values were read. | command references registry but no explicit hive path matched | **MANUAL REVIEW** |
| `system-locale-discovered` | Information | The evidence shows the 'Nation' and 'Name' values (country code and name) were obtained, indicating system locale/geographic info was discovered. | No matching rule for this predicate | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #30 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor is 'command_prompt', so the ability to invoke cmd.exe is required. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `not-bios-info-discovered` | Information | The evidence shows 'ERROR: The system was unable to find the specified registry key or value', indicating BIOS information was not successfully discovered. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-read` | (unclassified) | The command attempted to read a registry key, but since the key was not found, it's unclear if this should be considered a successful read or not; flagged for human review. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #31 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor is 'command_prompt', so the ability to invoke commands via cmd.exe is required. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `file-exists-plink-exe` | Information | The YAML dependency requires that the plink.exe file exists at the specified path before execution. | No matching rule for this predicate | **MANUAL REVIEW** |
| `file-exists-cli-script` | Information | The command references a CLI script file, which must exist for the command to run as intended. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-process-spawned-plink` | Process | The evidence shows plink.exe was not recognized or executed, so no plink process was spawned. | no clear process-spawning pattern in command text | **MANUAL REVIEW** |
| `not-vm-info-discovered` | Information | Because plink.exe was not found, no ESXi VM information could be discovered or exfiltrated. | No matching rule for this predicate | **MANUAL REVIEW** |
| `access-denied-or-auth-failure` | (unclassified) | Exit code 255 could also indicate authentication or network failure, but the error message specifically points to missing plink.exe, so this is flagged for human review. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `network-connection-attempted` | (unclassified) | The command would attempt a network connection to the ESXi host if plink.exe were present, but this did not occur; flagging in case partial effects are relevant. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #32 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `file-exists-plink-exe` | Information | The YAML dependencies require that plink.exe exists at the specified path before execution; the error message confirms this was not true. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-process-spawned-plink` | Process | The evidence shows plink.exe was not recognized or executed, so no process was spawned. | no clear process-spawning pattern in command text | **MANUAL REVIEW** |
| `not-system-info-discovered-esxi` | Information | The system information discovery did not occur because the required tool was missing and the command failed. | No matching rule for this predicate | **MANUAL REVIEW** |
| `access-denied-or-auth-failure` | (unclassified) | Exit code 255 could also indicate authentication or network failure, but the error message specifically points to a missing executable. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #34 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor for this test is 'powershell', as indicated by the command using Get-CimInstance in PowerShell. | YAML executor 'powershell' matches predicate | **PASS** |
| `os-information-discovered` | Information | The test gathers and outputs operating system information (caption, version, service pack, architecture, etc.) using Get-CimInstance, as described in the YAML and implied by the successful execution (exit code 0). | No matching rule for this predicate | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #35 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor is 'command_prompt', so the ability to invoke cmd.exe is required. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `os-version-information-discovered` | Information | The 'ver' command outputs the Windows OS version, as confirmed by the evidence showing the version string. | No matching rule for this predicate | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #36 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor is 'command_prompt', so the ability to invoke commands via cmd.exe is required. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `user-is-admin` | Privilege/User | The YAML specifies 'elevation_required: true', indicating administrative privileges are needed to run vssadmin. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `process-spawned-vssadmin` | Process | The evidence shows vssadmin.exe was executed, so a vssadmin process was spawned. | no clear process-spawning pattern in command text | **MANUAL REVIEW** |
| `system-info-discovered` | Information | The test's purpose is to enumerate volume shadow copies, which is a form of system information discovery, even if no items were found. | No matching rule for this predicate | **MANUAL REVIEW** |
| `volume-shadow-copies-enumerated` | (unclassified) | No shadow copies were found (output: 'No items found that satisfy the query'), so this effect is not asserted. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #37 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `command-prompt-invokable` | Executor | The executor is 'command_prompt', so the ability to invoke cmd.exe is required. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `system-locale-information-discovered` | Information | The test gathers and outputs system locale and regional settings, as described in the YAML and implied by the command. | No matching rule for this predicate | **MANUAL REVIEW** |
| `file-created-tmp-a-txt` | Information | The command outputs locale details to %TMP%\a.txt, indicating a file is created as an artifact. | No matching rule for this predicate | **MANUAL REVIEW** |
| `powershell-invokable` | (unclassified) | The command uses 'powershell.exe' via cmd, but the executor is 'command_prompt'; flagging in case direct PowerShell invocation is a separate requirement. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `file-persisted-tmp-a-txt` | (unclassified) | The file %TMP%\a.txt is created, but the test does not specify if cleanup is always performed; persistence may be transient. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #38 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor is 'command_prompt' and the command is run via 'powershell.exe -c', requiring the ability to invoke commands from the Windows command prompt. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `filesystem-drives-enumerated` | Information | The output lists available drives (C, D) and their properties, indicating enumeration of filesystem drives. | No matching rule for this predicate | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #39 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor is 'command_prompt', so the ability to invoke cmd.exe is required. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `registry-key-readable` | Privilege/User | The test queries a registry key (HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion), so read access to this key is required. | registry hive reference found in command (hklm\) | **PASS** |
| `os-product-name-discovered` | Information | The evidence shows the ProductName value was successfully read from the registry, revealing the OS product name. | No matching rule for this predicate | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #40 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor is 'command_prompt', so the ability to invoke commands via cmd.exe is required. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `registry-key-readable` | Privilege/User | The test queries a registry key (HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion), so read access to this key is required. | registry hive reference found in command (hklm\) | **PASS** |
| `os-build-number-discovered` | Information | The evidence shows the CurrentBuildNumber value was successfully read and displayed, indicating the OS build number was discovered. | No matching rule for this predicate | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #7 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor is 'command_prompt', so the ability to invoke commands via cmd.exe is required. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `system-hostname-discovered` | Information | The evidence shows the system's hostname (DESKTOP-C1VFPEU) was displayed, indicating successful discovery of hostname information. | No matching rule for this predicate | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #9 (t1082_elevated)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor is 'command_prompt', so the ability to invoke commands via cmd.exe is required. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `registry-key-readable-hklm-software-microsoft-cryptography` | Information | The test queries the registry key HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography, so read access to this key is required. | command references registry but no explicit hive path matched | **MANUAL REVIEW** |
| `machine-guid-discovered` | Information | The evidence shows the MachineGuid value was successfully read and displayed, indicating the system's unique identifier was discovered. | No matching rule for this predicate | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #10 (t1082_normal)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor is 'powershell', so the system must support invoking PowerShell commands. | YAML executor 'powershell' matches predicate | **PASS** |
| `file-exists-griffon-recon-vbs` | Information | The dependency requires the Griffon Recon VBScript file to exist at the specified path before execution. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-process-spawned-cscript-griffon-recon` | Process | The evidence shows that cscript failed to load the script due to antivirus detection, so the process did not successfully run the intended script. | no clear process-spawning pattern in command text | **MANUAL REVIEW** |
| `access-denied-virus-detected` | Privilege/User | The error message indicates the operation was blocked because the file was detected as a virus or potentially unwanted software. | No matching rule for this predicate | **MANUAL REVIEW** |
| `system-info-discovered` | (unclassified) | Flagged because the evidence shows no system information was actually collected due to the antivirus block. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `file-read-griffon-recon-vbs` | (unclassified) | Flagged because the script file was not successfully read/executed; antivirus blocked access. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #11 (t1082_normal)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor is 'command_prompt', indicating the test requires the ability to invoke commands via cmd.exe. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `environment-variables-discovered` | Information | The evidence shows a full dump of environment variables, indicating successful discovery of environment variable information. | No matching rule for this predicate | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #14 (t1082_normal)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor is PowerShell, as shown by the use of PowerShell commands in the YAML and evidence. | YAML executor 'powershell' matches predicate | **PASS** |
| `network-connectivity` | Environment | The test attempts to download a script from GitHub, implying that outbound network connectivity is required. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-information-system-info-discovered` | Information | The evidence shows that the winPEAS script was not downloaded or executed, so no system information was actually discovered. | No matching rule for this predicate | **MANUAL REVIEW** |
| `process-spawned-winpeas` | (unclassified) | Flagged because the winPEAS process was not actually spawned due to the download failure. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `file-downloaded-winpeas-ps1` | (unclassified) | Flagged because the script was not downloaded; the evidence shows a network resolution failure. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `user-is-admin` | (unclassified) | Flagged because the test does not specify elevation is required, and the evidence does not clarify privilege context. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #15 (t1082_normal)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor is PowerShell, as shown by the command block and the use of PowerShell cmdlets. | YAML executor 'powershell' matches predicate | **PASS** |
| `network-connectivity-to-github` | Environment | The script attempts to download a file from raw.githubusercontent.com, implying network access to GitHub is required. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-information-system-info-discovered` | Information | The evidence shows the download failed and the itm4nprivesc command was not found, so no system information was actually discovered. | No matching rule for this predicate | **MANUAL REVIEW** |
| `process-spawned` | (unclassified) | While PowerShell was invoked, the evidence does not show that any meaningful process beyond the failed download and command error was spawned. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `user-is-admin` | (unclassified) | No evidence in the output indicates privilege escalation or admin context was required or obtained for this test. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #16 (t1082_normal)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor for this test is 'powershell', as shown in the YAML and the evidence (powershell command lines). | YAML executor 'powershell' matches predicate | **PASS** |
| `internet-connectivity` | Environment | The test attempts to download a script from 'raw.githubusercontent.com', which requires outbound internet access; the failure in the evidence is due to lack of connectivity. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-information-system-info-discovered` | Information | The evidence shows the test failed to download and run the intended script, so no system information was actually discovered or output. | No matching rule for this predicate | **MANUAL REVIEW** |
| `process-spawned` | (unclassified) | A powershell process was started, but since the script failed to download and execute, it's unclear if this should be considered a meaningful effect. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `user-is-admin` | (unclassified) | The test does not require elevation and there is no evidence of privilege escalation or admin context, so this is not asserted. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #17 (t1082_normal)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor is 'powershell', so the system must support PowerShell command execution. | YAML executor 'powershell' matches predicate | **PASS** |
| `internet-connectivity` | Environment | The script attempts to download a remote PowerShell script from GitHub, which requires outbound internet access. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-information-system-info-discovered` | Information | The evidence shows the remote script could not be downloaded and the 'otherchecks' command was not found, so no system information was actually discovered. | No matching rule for this predicate | **MANUAL REVIEW** |
| `process-spawned-powershell` | (unclassified) | A PowerShell process was started, but since the main payload failed, it's unclear if this is meaningful for downstream planning. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `user-is-standard` | (unclassified) | The test does not require elevation, but the actual privilege context is not confirmed in the evidence. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #18 (t1082_normal)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor is 'powershell', so the system must support invoking PowerShell commands. | YAML executor 'powershell' matches predicate | **PASS** |
| `network-connectivity-required` | Environment | The script attempts to download a remote PowerShell script from GitHub, requiring outbound network connectivity. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-information-system-info-discovered` | Information | The evidence shows the download failed and the Generalrecon command was not found, so no system information was actually discovered. | No matching rule for this predicate | **MANUAL REVIEW** |
| `process-spawned` | (unclassified) | A PowerShell process was started, but since the main payload failed to download and execute, it's unclear if this should be considered a meaningful effect. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `user-is-admin` | (unclassified) | The test does not require elevation and there is no evidence of privilege escalation or admin context, so this is not applicable. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #19 (t1082_normal)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor is PowerShell, as shown by the command using 'iex' and 'Morerecon'. | YAML executor 'powershell' matches predicate | **PASS** |
| `network-connectivity-required` | Environment | The test attempts to download a script from 'raw.githubusercontent.com', indicating a dependency on outbound network connectivity. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-information-system-info-discovered` | Information | The evidence shows the download failed and the 'Morerecon' command was not found, so no system information was actually discovered. | No matching rule for this predicate | **MANUAL REVIEW** |
| `process-spawned` | (unclassified) | A PowerShell process was likely started, but the evidence does not confirm any meaningful or persistent process effect beyond the failed command. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `user-is-admin` | (unclassified) | No evidence in the YAML or execution log indicates that elevated privileges were required or obtained for this specific test. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `file-created` | (unclassified) | No files were created or written as the script download and execution failed. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #1 (t1082_normal)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor is 'command_prompt', so the ability to invoke commands via cmd.exe is required. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `system-information-discovered` | Information | The evidence shows detailed system information (OS, hardware, memory, network, etc.) was displayed, indicating successful discovery. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-read` | Information | The command 'reg query HKLM\SYSTEM\CurrentControlSet\Services\Disk\Enum' was executed and its output is present, showing registry read access. | registry hive reference found in command (hklm\) | **PASS** |
| `process-running` | (unclassified) | No evidence of persistent or notable process state beyond normal command execution; not included. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `user-is-admin` | (unclassified) | No indication that administrative privileges were required or obtained for this test. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `environment-variable-discovered` | (unclassified) | No environment variable enumeration was performed in this specific test instance. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `environment-changed` | (unclassified) | No persistent system/OS state change occurred; all actions were read-only. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #20 (t1082_normal)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor for this test is 'powershell', as shown in the YAML and the evidence (powershell.exe commands). | YAML executor 'powershell' matches predicate | **PASS** |
| `internet-connectivity` | Environment | The test attempts to download a script from 'raw.githubusercontent.com', implying that internet access is required for success. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-information-system-info-discovered` | Information | The evidence shows that the download failed and the RBCD-Check command was not recognized, so no system information was actually discovered. | No matching rule for this predicate | **MANUAL REVIEW** |
| `rbcd-check-script-downloaded` | (unclassified) | Flagged because the script download failed due to lack of internet connectivity, so this effect did not occur. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `rbcd-check-process-spawned` | (unclassified) | Flagged because the RBCD-Check command was not recognized and did not execute, so no process was spawned. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `user-is-admin` | (unclassified) | Flagged because the test does not specify elevation is required, and the evidence does not indicate privilege escalation or admin context. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #21 (t1082_normal)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor is PowerShell, as shown by the command using 'iex' and 'Invoke-watson'. | YAML executor 'powershell' matches predicate | **PASS** |
| `network-connectivity-to-github` | Environment | The script attempts to download a PowerSharpPack script from 'raw.githubusercontent.com', implying network access is required for success. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-information-collected-missing-windows-patches` | Information | The evidence shows the download failed and 'Invoke-watson' was not recognized, so no patch information was collected. | No matching rule for this predicate | **MANUAL REVIEW** |
| `process-spawned-powershell` | (unclassified) | A PowerShell process was likely spawned, but the evidence does not confirm if any meaningful child process or script execution occurred beyond the failed download. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `user-is-standard` | (unclassified) | No evidence of privilege escalation or requirement for admin rights, but the privilege context is not explicitly confirmed in the evidence. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #22 (t1082_normal)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor is PowerShell, as shown by the command using 'iex' and 'Invoke-SharpUp'. | YAML executor 'powershell' matches predicate | **PASS** |
| `network-connectivity-required` | Environment | The test attempts to download a script from 'raw.githubusercontent.com', indicating a dependency on outbound network access. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-information-system-info-discovered` | Information | The evidence shows the download failed and the main reconnaissance command was not recognized, so no system information was actually discovered. | No matching rule for this predicate | **MANUAL REVIEW** |
| `process-spawned-powershell` | (unclassified) | A PowerShell process was likely spawned, but the main payload did not execute; flagging for review if this should be modeled as an effect. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `user-is-standard` | (unclassified) | No evidence of privilege escalation or requirement for admin rights, but unclear if the script would require it if it had executed. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #23 (t1082_normal)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor is PowerShell, as shown by the use of 'iex(new-object net.webclient)...' and 'Invoke-Seatbelt'. | YAML executor 'powershell' matches predicate | **PASS** |
| `internet-connectivity` | Environment | The test attempts to download a script from 'raw.githubusercontent.com', implying that internet access is required for success. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-information-system-surveyed` | Information | The evidence shows that the download failed and 'Invoke-Seatbelt' was not recognized, so no system information was actually collected. | No matching rule for this predicate | **MANUAL REVIEW** |
| `powershell-script-downloaded` | (unclassified) | Flagged because the script download failed due to lack of internet connectivity, so this effect did not occur. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `seatbelt-executed` | (unclassified) | Flagged because 'Invoke-Seatbelt' was not recognized and did not run, so this effect did not occur. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `system-information-collected` | (unclassified) | Flagged because the evidence shows no system information was actually gathered due to the failed script execution. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #24 (t1082_normal)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The executor is PowerShell, as shown by the use of PowerShell commands in the YAML and evidence. | YAML executor 'powershell' matches predicate | **PASS** |
| `azurestealth-module-present` | Information | The YAML dependencies require the AzureStealth.ps1 module to exist, and the evidence shows failure due to its absence. | No matching rule for this predicate | **MANUAL REVIEW** |
| `azuread-module-installed` | Information | The YAML dependencies require the AzureAD module to be installed for the test to proceed. | No matching rule for this predicate | **MANUAL REVIEW** |
| `az-module-installed` | Information | The YAML dependencies require the Az module to be installed for the test to proceed. | No matching rule for this predicate | **MANUAL REVIEW** |
| `valid-azuread-credentials-available` | Privilege/User | The test requires valid Azure AD credentials as input arguments, and the evidence shows failure due to invalid or missing username. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-azurestealth-module-imported` | Information | The evidence shows Import-Module failed due to missing AzureStealth.ps1, so the module was not imported. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-azure-credential-object-created` | Privilege/User | The evidence shows New-Object failed due to invalid username, so no credential object was created. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-azaccount-connected` | Privilege/User | The evidence shows Connect-AzAccount failed because the cmdlet was not found, so no Azure account connection was made. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-azuread-connected` | Privilege/User | The evidence shows Connect-AzureAD failed because the cmdlet was not found, so no Azure AD connection was made. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-azure-admins-scanned` | Information | The evidence shows Scan-AzureAdmins failed because the cmdlet was not found, so no admin scan was performed. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `output-folder-created-in-temp` | (unclassified) | YAML claims a folder with CSVs is created in temp on success, but evidence shows the test failed before this could occur. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `admin-user-information-discovered` | (unclassified) | YAML claims admin user info is discovered, but evidence shows the scan did not execute. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #27 (t1082_normal)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor is 'command_prompt', so the ability to invoke commands via cmd.exe is required. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `not-information-system-info-discovered` | Information | No system information was discovered because all commands failed ('wmic' and 'Get-WmiObject' not recognized), so the intended information effect did not occur. | No matching rule for this predicate | **MANUAL REVIEW** |
| `wmic-present` | (unclassified) | The evidence shows 'wmic' is not present, but the ART YAML assumes it is; this is a missing precondition that should be flagged for human review. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `get-wmiobject-present` | (unclassified) | The evidence shows 'Get-WmiObject' is not present, but the ART YAML assumes it is; this is a missing precondition that should be flagged for human review. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #28 (t1082_normal)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `command-prompt-invokable` | Executor | The executor for this test is 'command_prompt', so the ability to invoke commands via the Windows command prompt is required. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `system-information-discovered` | Information | The test attempts to collect system information using 'systeminfo' and registry queries, which, if successful, would result in system information being discovered. | No matching rule for this predicate | **MANUAL REVIEW** |
| `access-denied-or-command-failed` | (unclassified) | The exit code is 1, indicating failure; it is unclear if this was due to access denial, missing commands, or another error, so the actual effect may not be achieved. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #29 (t1082_normal)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor is 'command_prompt', so the ability to invoke commands via cmd.exe is required. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `registry-key-read` | Information | The command 'reg query "HKEY_CURRENT_USER\Control Panel\International\Geo"' reads registry values, as confirmed by the evidence showing Nation and Name values. | command references registry but no explicit hive path matched | **MANUAL REVIEW** |
| `system-locale-discovered` | Information | The evidence shows the discovery of country code and name (e.g., 'GB'), indicating system locale/geographic information was obtained. | No matching rule for this predicate | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #30 (t1082_normal)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor is 'command_prompt', so the ability to invoke commands via cmd.exe is required. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `system-bios-version-read` | Information | The evidence shows that the SystemBiosVersion registry value was successfully queried and returned a value (VBOX, VirtualBox, EDK II - 10000). | No matching rule for this predicate | **MANUAL REVIEW** |
| `video-bios-version-read-failed` | Information | The evidence includes 'ERROR: The system was unable to find the specified registry key or value' for the VideoBiosVersion query, indicating the attempt failed. | No matching rule for this predicate | **MANUAL REVIEW** |
| `registry-key-read` | (unclassified) | Generic registry read is implied, but the evidence is specific to BIOS keys; flagging in case broader registry access should be modeled. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #31 (t1082_normal)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor is 'command_prompt', so the ability to invoke commands via cmd is required. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `file-exists-plink-exe` | Information | The YAML dependency and the error message indicate that plink.exe must exist at the specified path for the command to succeed. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-process-spawned-plink` | Process | The error message shows plink.exe was not recognized, so the process was not spawned. | no clear process-spawning pattern in command text | **MANUAL REVIEW** |
| `not-vm-info-discovered` | Information | Because plink.exe was missing, no VM information could be discovered or exfiltrated. | No matching rule for this predicate | **MANUAL REVIEW** |
| `access-denied-or-auth-failure` | (unclassified) | Exit code 255 could also indicate authentication or network failure, but the error message specifically points to missing plink.exe. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `network-connection-attempted` | (unclassified) | The command would attempt a network connection to the ESXi host, but it's unclear if this was even attempted due to the missing binary. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #32 (t1082_normal)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `file-exists-plink-exe` | Information | The YAML dependencies require that plink.exe exists at the specified path before execution. | No matching rule for this predicate | **MANUAL REVIEW** |
| `not-process-spawned-plink` | Process | The evidence shows plink.exe was not recognized or executed, so no process was spawned. | no clear process-spawning pattern in command text | **MANUAL REVIEW** |
| `not-system-info-discovered-esxi` | Information | The command failed to run, so no ESXi system information was discovered or exfiltrated. | No matching rule for this predicate | **MANUAL REVIEW** |
| `access-denied-or-missing-dependency` | (unclassified) | The failure could be due to missing plink.exe or a PATH/environment issue; human review needed to distinguish root cause. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #34 (t1082_normal)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `powershell-invokable` | Executor | The YAML command uses PowerShell cmdlets (Get-CimInstance), so the system must support PowerShell execution. | YAML executor 'powershell' matches predicate | **PASS** |
| `os-information-discovered` | Information | The command queries and outputs operating system details (caption, version, service pack, architecture, etc.), indicating successful discovery of OS information. | No matching rule for this predicate | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #35 (t1082_normal)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor is 'command_prompt', indicating the command must be invokable via cmd.exe. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `os-version-information-discovered` | Information | The 'ver' command outputted the Windows version string, confirming that OS version information was obtained. | No matching rule for this predicate | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #36 (t1082_normal)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor is 'command_prompt', so the ability to invoke commands via cmd.exe is required. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `not-process-spawned-vssadmin` | Process | The evidence shows vssadmin was invoked but failed due to insufficient privileges, so no persistent vssadmin process or effect occurred. | no clear process-spawning pattern in command text | **MANUAL REVIEW** |
| `access-denied-vssadmin` | Privilege/User | The error message explicitly states that the command failed due to lack of elevated administrator privileges. | YAML elevation_required: true — confirms privilege precondition | **PASS** |
| `volume-shadow-copies-discovered` | (unclassified) | Flagged because the evidence shows the discovery did NOT occur due to access denial; this effect is not realized. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `user-is-admin` | (unclassified) | Flagged because the evidence suggests this was NOT true, but it is a relevant precondition for successful execution. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #37 (t1082_normal)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `command-prompt-invokable` | Executor | The executor is 'command_prompt' running a PowerShell command, so the ability to invoke command prompt is required. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `system-locale-information-discovered` | Information | The test gathers and outputs system locale and regional settings, as described in the YAML and implied by the command. | No matching rule for this predicate | **MANUAL REVIEW** |
| `file-created-tmp-a-txt` | Information | The command outputs locale details to %TMP%\a.txt, so a file is created as a result. | No matching rule for this predicate | **MANUAL REVIEW** |
| `powershell-invokable` | (unclassified) | The command is run via 'powershell.exe' from command prompt; it's unclear if direct PowerShell invocation is a separate precondition or always implied by command prompt access. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |
| `user-is-standard` | (unclassified) | No evidence of privilege escalation or access denial, but the privilege context is not explicitly stated in the evidence. | Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #38 (t1082_normal)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor is 'command_prompt' running a PowerShell command, so the ability to invoke commands via cmd is required. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `powershell-invokable` | Executor | The command uses 'powershell.exe -c', so PowerShell must be available and invokable from the command prompt. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `filesystem-drives-enumerated` | Information | The output lists available drives (C, D) and their usage, indicating enumeration of filesystem drives. | No matching rule for this predicate | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #39 (t1082_normal)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor is 'command_prompt', so the ability to invoke commands via cmd.exe is required. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `registry-key-readable` | Privilege/User | The test queries a registry key (HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion), so read access to this registry key is required. | registry hive reference found in command (hklm\) | **PASS** |
| `os-product-name-discovered` | Information | The evidence shows the ProductName value was successfully read and displayed, indicating the OS product name was discovered. | No matching rule for this predicate | **MANUAL REVIEW** |

---

# Predicate cross-check — T1082 Test #40 (t1082_normal)

| Candidate | Category | Evidence | Cross-check | Decision |
|---|---|---|---|---|
| `cmd-invokable` | Executor | The executor is 'command_prompt', so the ability to invoke cmd.exe is required. | YAML executor is 'command_prompt', predicate does not reference it | **MANUAL REVIEW** |
| `registry-key-readable` | Privilege/User | The test queries a registry key under HKLM, which requires at least standard user read access. | registry hive reference found in command (hklm\) | **PASS** |
| `os-build-number-discovered` | Information | The evidence shows the OS build number was successfully read from the registry and displayed. | No matching rule for this predicate | **MANUAL REVIEW** |