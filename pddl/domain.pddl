;; ============================================================
;; domain.pddl
;; Aurora-mini: five-category predicate scheme
;; (Executor, Process, Privilege/User, Information, Environment)
;;
;; Starter attack chain:
;;   T1059.001 -> T1547.001 -> T1003.001 -> T1021.002
;;
;; STATUS OF EACH STARTER-CHAIN ACTION:
;;   T1059.001        - empirically grounded (Test #17, non-elevated,
;;                       obfuscated PowerShell -e flag)
;;   T1547.001        - empirically grounded (Test #1, Registry Run Key,
;;                       HKCU, elevation_required: false)
;;   T1003.001        - COARSE PLACEHOLDER. All 11 ART sub-tests on the
;;                       VM failed (Access is denied / missing payloads).
;;                       No successful-run evidence exists for this
;;                       technique. Predicates here are invented to let
;;                       the pipeline run end-to-end; treat as a stand-in
;;                       to be replaced (or kept as a documented
;;                       failure-mode finding) once you decide how to
;;                       write this up.
;;   T1021.002        - empirically grounded, combining Tests #1
;;                       (net use), #2 (New-PSDrive) and #4 (local admin
;;                       share write), which converge on the same
;;                       preconditions/effects. Test #3 (PsExec) is
;;                       excluded - failed only because PsExec.exe was
;;                       missing from ExternalPayloads, a tooling gap,
;;                       not a technique constraint.
;;
;; ------------------------------------------------------------
;; CORPUS EXTENSION (this pass): 12 additional techniques added below,
;; following the SAME convention as the starter chain - one action per
;; technique, backed by its cleanest empirically-validated test(s),
;; NOT one action per sub-test. Predicate names are canonicalised
;; across near-synonymous translator outputs (e.g. 7zip-installed /
;; winzip-installed -> archive-utility-installed) since the fidelity
;; metric (Section 3.7.3) compares ATT&CK technique IDs in the plan,
;; not predicate names, so this canonicalisation costs nothing on that
;; metric while keeping domain.pddl from fragmenting into near-dupes.
;; The corpus "user-is-admin" predicate is mapped onto the pre-existing
;; user-has-admin-privileges predicate below (same real-world fact,
;; not a new synonym).
;;
;; THREE TECHNIQUES DELIBERATELY HAVE NO ACTION: T1041, T1136.001,
;; T1055. This is a design choice, not an omission - all evidenced
;; sub-tests for each failed (T1055: 0/13, av-active-gated; T1041: 0/2,
;; network/tooling gaps; T1136.001: 3/4 access-denied + 1 ambiguous).
;; With no action available to produce their effect, Fast Downward
;; cannot find a plan for any goal requiring them - this correctly and
;; structurally yields Success Rate = 0 for these techniques without
;; inventing an unevidenced placeholder (contrast with T1003.001 above,
;; which pre-dates this convention and used a placeholder instead,
;; documented as such).
;; ------------------------------------------------------------
;;
;; SIMPLIFICATION: no host/agent typing. All predicates are 0-arity,
;; global facts, matching the localhost-scoped VM evidence collected
;; so far. Add ?h - host parameters later if you extend to genuine
;; multi-host scenarios.
;;
;; ASSUMPTION FLAGGED FOR REVIEW: set-registry-run-key requires
;; (arbitrary-code-executed) as a precondition. This is a chain-level
;; narrative link (T1059.001 must happen before T1547.001), not
;; something the T1547.001 ART evidence itself demonstrates - the
;; registry test succeeds independently of the PowerShell test. Decide
;; whether you want to defend this explicitly in your methodology or
;; remove it and let T1547.001 fire independently.
;; ============================================================

(define (domain aurora-mini)

  (:requirements :strips)

  (:predicates

    ;; --- Executor category ---
    (powershell-present)               ;; Environment-adjacent, kept with T1059.001 block below
    (interpreter-invokable)            ;; effect: powershell interpreter now invokable
    (cmd-invokable)                    ;; cmd.exe available (T1547.001, T1021.002 baseline)
    (powershell-invokable)             ;; powershell.exe available as an executor (distinct from
                                        ;; powershell-present/interpreter-invokable above, which
                                        ;; track the T1059.001 obfuscated-invocation chain
                                        ;; specifically; this is the general-purpose baseline used
                                        ;; across the discovery/collection/persistence corpus)

    ;; --- Process category ---
    (process-running)                  ;; a process instance is running (T1059.001 effect)

    ;; --- Privilege/User category ---
    (user-has-write-access-hkcu-run-key)   ;; baseline precondition, true for virtually any
                                            ;; logged-in Windows user - included for category
                                            ;; completeness (T1547.001)
    (user-has-admin-privileges)            ;; local admin group membership confirmed.
                                            ;; Corpus translator output "user-is-admin" is mapped
                                            ;; onto this SAME predicate throughout the extension
                                            ;; below (T1018, T1112) - same real-world fact, not a
                                            ;; new synonym.
    (remote-admin-token-unfiltered)        ;; LocalAccountTokenFilterPolicy allows remote admin
                                            ;; token to pass (distinct from holding admin
                                            ;; privilege itself - causal A/B finding, T1021.002)

    ;; --- Information category ---
    (arbitrary-code-executed)          ;; capability demonstrated by T1059.001
    (registry-key-written)             ;; artifact-produced view of the T1547.001 write; reused
                                        ;; as-is for T1053.005 (Test #7), same underlying fact
    (credentials-obtained)             ;; PLACEHOLDER - T1003.001, no successful evidence
    (system-information-discovered)    ;; canonical Information effect - collapses the corpus's
                                        ;; near-synonymous translator outputs (system-info-
                                        ;; discovered, system-information-collected, os-version-
                                        ;; information-discovered, bios-information-discovered,
                                        ;; system-locale-discovered, etc.) into one predicate,
                                        ;; since Section 3.7.3 fidelity compares technique IDs,
                                        ;; not predicate names (T1082)
    (registry-key-read)                ;; artifact-produced companion effect alongside
                                        ;; system-information-discovered (T1082 Test #1)
    (network-hosts-discovered)         ;; canonical effect - collapses network-arp-cache-
                                        ;; discovered and network-hosts-discovered (T1018)
    (network-service-discovered)       ;; T1046
    (process-listing-obtained)         ;; canonical effect - collapses process-listing-obtained
                                        ;; and process-discovered (T1057)
    (accounts-enumerated)              ;; T1087.001
    (credentials-discovered)           ;; T1087.001 - distinct from accounts-enumerated per the
                                        ;; ART evidence for Test #8, which reported both

    ;; --- Environment category ---
    (registry-run-key-set)             ;; state-change view of the T1547.001 write
    (admin-share-reachable)            ;; target admin share (C$/ADMIN$) exists and is visible
    (admin-share-mapped)               ;; share successfully mapped/written to (T1021.002 effect)
    (lsass-memory-accessible)          ;; PLACEHOLDER - stands in for "no AV/Credential Guard
                                        ;; block", never observed true on the VM (T1003.001)
    (file-exists)                      ;; generic file/tool-dependency precondition. Folded into
                                        ;; Environment per Table 1 (Aurora's File category folds
                                        ;; into Environment) - corrected corpus-wide from an
                                        ;; earlier Information mistagging (T1070.004)
    (registry-key-modified)            ;; T1112 - already the corpus-wide corrected convention
    (scheduled-task-created)           ;; T1053.005
    (archive-utility-installed)        ;; canonical precondition - collapses 7zip-installed /
                                        ;; winzip-installed (T1560.001); the specific tool stays
                                        ;; in the corpus justification text, not the predicate name
    (file-created)                     ;; T1560.001
    (file-deleted)                     ;; T1070.004 - CORRECTED from Information to Environment
                                        ;; during the nine-category reverse-fold exercise: per
                                        ;; Table 1's File->Environment fold rule, this is the same
                                        ;; category bug pattern already fixed for file-exists,
                                        ;; just not caught in that earlier pass - the ablation
                                        ;; process itself surfaced this as a residual scheme
                                        ;; inconsistency

    ;; --- Goal-only predicates for the 3 deliberately-unmodelled failure-mode
    ;;     techniques (T1041, T1136.001, T1055). Each is declared here so its
    ;;     corresponding problem file is syntactically valid, but NO action
    ;;     below has it as an effect - this is what makes Fast Downward
    ;;     correctly report "no solution found" for these goals, structurally
    ;;     encoding total technique failure rather than omitting the goal
    ;;     predicate entirely (which would instead cause a parse error).
    (data-exfiltrated)                 ;; T1041 - never produced (0/2 sub-tests succeeded)
    (local-account-created)            ;; T1136.001 - never produced (3/4 access-denied, 1 ambiguous)
    (process-injected)                 ;; T1055 - never produced (0/13 sub-tests succeeded)

    ;; --- Goal marker (Information) ---
    (lateral-movement-achieved)
  )

  ;; ------------------------------------------------------------
  ;; T1059.001 Test #17: obfuscated PowerShell (powershell.exe -e ...)
  ;; Non-elevated - no admin precondition required.
  ;; interpreter-invokable and process-running are UNCONSUMED effects
  ;; (nothing downstream reads them) - flagged as a methodological
  ;; observation on category load, not a bug.
  ;; ------------------------------------------------------------
  (:action exec-powershell-obfuscated
    :precondition (and (powershell-present))
    :effect (and
      (interpreter-invokable)
      (process-running)
      (arbitrary-code-executed)
    )
  )

  ;; ------------------------------------------------------------
  ;; T1547.001 Test #1: Registry Run Key persistence
  ;; REG ADD HKCU\...\Run /V "Atomic Red Team" ...
  ;; elevation_required: false in YAML - only HKCU write access needed.
  ;; registry-run-key-set (Environment) and registry-key-written
  ;; (Information) are split views of the same underlying write -
  ;; a recurring category-overlap pattern, see Discussion notes.
  ;; ------------------------------------------------------------
  (:action set-registry-run-key
    :precondition (and
      (cmd-invokable)
      (user-has-write-access-hkcu-run-key)
      (arbitrary-code-executed)   ;; ASSUMPTION - see header note
    )
    :effect (and
      (registry-run-key-set)
      (registry-key-written)
    )
  )

  ;; ------------------------------------------------------------
  ;; T1003.001 - COARSE PLACEHOLDER (all 11 ART sub-tests failed on VM)
  ;; Modeled as: would succeed given admin privilege, cmd access, and
  ;; an (invented) unblocked-LSASS-access environment state, following
  ;; on from persistence being established. No successful run backs
  ;; these preconditions/effects - replace once real evidence exists,
  ;; or keep as-is and write it up explicitly as a failure-mode finding
  ;; for the Privilege/User category.
  ;; ------------------------------------------------------------
  (:action dump-lsass-credentials
    :precondition (and
      (cmd-invokable)
      (user-has-admin-privileges)
      (lsass-memory-accessible)
      (registry-run-key-set)
    )
    :effect (and
      (credentials-obtained)
    )
  )

  ;; ------------------------------------------------------------
  ;; T1021.002 Tests #1/#2/#4 (net use / New-PSDrive / local admin
  ;; share write - converged into one action since all three share
  ;; the same preconditions and produce the same effect once the
  ;; token-filtering precondition is satisfied).
  ;; remote-admin-token-unfiltered is grounded in a causal A/B test:
  ;; identical command failed with "Access is denied" before
  ;; LocalAccountTokenFilterPolicy was set, succeeded immediately
  ;; after, nothing else changed.
  ;; Test #3 (PsExec) excluded - missing external payload, not a
  ;; technique constraint.
  ;; ------------------------------------------------------------
  (:action lateral-movement-admin-share
    :precondition (and
      (cmd-invokable)
      (user-has-admin-privileges)
      (remote-admin-token-unfiltered)
      (admin-share-reachable)
      (credentials-obtained)
    )
    :effect (and
      (admin-share-mapped)
      (lateral-movement-achieved)
    )
  )

  ;; ============================================================
  ;; CORPUS EXTENSION - 12 additional techniques (this pass)
  ;; ============================================================

  ;; ------------------------------------------------------------
  ;; T1057 Tests #2 (cmd, "process-listing-obtained") and #6 (cmd,
  ;; "process-discovered") converge - same executor, same underlying
  ;; fact (a process listing was produced), collapsed to one canonical
  ;; effect per the naming-consolidation rule.
  ;; ------------------------------------------------------------
  (:action discover-running-processes
    :precondition (and (cmd-invokable))
    :effect (and (process-listing-obtained))
  )

  ;; ------------------------------------------------------------
  ;; T1046 Test #10: PowerShell-based network service discovery.
  ;; Tests #3-8 are failure-mode data (tooling absent, network
  ;; unreachable, elevation-required ambiguity per the
  ;; elevation_required-unreliability finding) - not modelled as
  ;; actions, reported in the failure-mode table instead.
  ;; ------------------------------------------------------------
  (:action scan-network-services
    :precondition (and (powershell-invokable))
    :effect (and (network-service-discovered))
  )

  ;; ------------------------------------------------------------
  ;; T1082 Test #1 (elevated AND normal context both converge on the
  ;; identical predicate set - a genuine negative finding that this
  ;; particular discovery method has no privilege-gated branch,
  ;; contrasting with Test #36's vssadmin causal A/B pair, which DOES
  ;; show elevation-gating for a different sub-test of this same
  ;; technique). registry-key-read is an artifact-produced companion
  ;; effect alongside the canonical system-information-discovered.
  ;; ------------------------------------------------------------
  (:action discover-system-information
    :precondition (and (cmd-invokable))
    :effect (and
      (system-information-discovered)
      (registry-key-read)
    )
  )

  ;; ------------------------------------------------------------
  ;; T1018: TWO actions, reflecting a genuine two-path finding that
  ;; complements T1021.002's privilege-distinction result.
  ;; Test #5 succeeds with no privilege precondition at all (ARP cache
  ;; is locally-cached, requires no network round-trip or credential).
  ;; Test #8 requires admin privilege for a broader host discovery.
  ;; Both are canonicalised to the same effect (network-hosts-
  ;; discovered) since the fidelity metric compares technique IDs, not
  ;; predicate names - the privilege distinction lives in the
  ;; precondition, not a forked effect name.
  ;; Most other T1018 sub-tests (#1,#2,#16,#18,#19,#20,#21) are
  ;; environment/tooling-gap failures (no AD domain controller on the
  ;; standalone VM) - reported in the failure-mode table, not modelled.
  ;; ------------------------------------------------------------
  (:action discover-network-hosts-arp
    :precondition (and (cmd-invokable))
    :effect (and (network-hosts-discovered))
  )

  (:action discover-network-hosts-admin
    :precondition (and
      (powershell-invokable)
      (user-has-admin-privileges)
    )
    :effect (and (network-hosts-discovered))
  )

  ;; ------------------------------------------------------------
  ;; T1087.001 Test #8: command-prompt-based local account discovery,
  ;; which per the ART evidence surfaced both enumerated accounts AND
  ;; discoverable credential material - both reported as distinct
  ;; effects rather than collapsed, since the credential exposure is a
  ;; materially different consequence for a downstream planner.
  ;; ------------------------------------------------------------
  (:action discover-local-accounts
    :precondition (and (cmd-invokable))
    :effect (and
      (accounts-enumerated)
      (credentials-discovered)
    )
  )

  ;; ------------------------------------------------------------
  ;; T1112: converged from the large cluster of successful cmd/
  ;; PowerShell registry-modification sub-tests (#1,#5,#6,#58,#59,#60,
  ;; #66-69, etc). Gated by user-has-admin-privileges as a
  ;; conservative, evidence-consistent simplification: the majority of
  ;; this technique's ~90 sub-tests fail with access-denied specifically
  ;; WITHOUT admin privilege, so requiring it here is a safe upper
  ;; bound, even though a subset of successes (e.g. #1, #58) succeeded
  ;; without an explicit admin precondition being recorded (plausibly
  ;; because the VM session itself was already admin-elevated for those
  ;; runs). A finer HKCU-vs-HKLM privilege split was considered but not
  ;; modelled, to keep this action simple per project scope.
  ;; ------------------------------------------------------------
  (:action modify-registry-key
    :precondition (and
      (cmd-invokable)
      (user-has-admin-privileges)
    )
    :effect (and (registry-key-modified))
  )

  ;; ------------------------------------------------------------
  ;; T1070.004 Test #10: simple file-state effect, deleting a file
  ;; whose existence was itself a (now Environment-category, per the
  ;; corpus-wide file-exists correction) precondition.
  ;; ------------------------------------------------------------
  (:action delete-file
    :precondition (and (file-exists))
    :effect (and (file-deleted))
  )

  ;; ------------------------------------------------------------
  ;; T1560.001 Tests #3 (WinZip) and #4 (7-Zip) converge on the same
  ;; underlying fact (an archive utility being present enables file
  ;; creation via compression) - the specific tool is canonicalised
  ;; away into archive-utility-installed, since it is not something any
  ;; downstream action in this corpus needs to distinguish.
  ;; Tests #1/#2/#10/#11/#12 are failure-mode data (tooling absent,
  ;; missing payload, compression failure) - not modelled.
  ;; ------------------------------------------------------------
  (:action create-archive
    :precondition (and (archive-utility-installed))
    :effect (and (file-created))
  )

  ;; ------------------------------------------------------------
  ;; T1053.005: Test #7 (cmd-invokable) used as the primary basis since
  ;; it has the fuller, more informative predicate set; Test #2
  ;; (windows-platform precondition) converges on the same effect and
  ;; is treated as corroborating evidence, though its precondition is
  ;; flagged elsewhere as too weak/generic to fully explain why it
  ;; succeeded where most other sub-tests failed on access-denied - see
  ;; methodology notes. registry-key-written is REUSED from the
  ;; T1547.001 declaration above (same real-world fact: a registry
  ;; write occurred), not a new predicate.
  ;; The majority of this technique's sub-tests (#1,#3,#4,#6,#8,#9)
  ;; are Privilege/User failure-mode data (access-denied), #5 and #10
  ;; are environment/tooling gaps, and #12 is a downgraded-to-
  ;; unconfirmed ambiguous result - none of these are modelled as
  ;; actions, consistent with the T1003.001/T1055 failure-mode
  ;; treatment.
  ;; ------------------------------------------------------------
  (:action create-scheduled-task
    :precondition (and (cmd-invokable))
    :effect (and
      (scheduled-task-created)
      (registry-key-written)
    )
  )

  ;; ------------------------------------------------------------
  ;; NO ACTION MODELLED - T1041 (Exfiltration Over C2 Channel)
  ;; Both evidenced sub-tests failed (Test #1: proxy resolution
  ;; failure; Test #2: DNS query failure on an invalid character) -
  ;; total technique failure, reported in the failure-mode table.
  ;; ------------------------------------------------------------

  ;; ------------------------------------------------------------
  ;; NO ACTION MODELLED - T1136.001 (Create Local Account)
  ;; 3 of 4 evidenced sub-tests failed with access-denied under a
  ;; declared elevated-privilege precondition (a genuine Privilege/
  ;; User-category finding, not a translation artefact); the 4th
  ;; (#8) produced no effect and is ambiguous. Total technique failure
  ;; for planning purposes, reported in the failure-mode table.
  ;; ------------------------------------------------------------

  ;; ------------------------------------------------------------
  ;; NO ACTION MODELLED - T1055 (Process Injection)
  ;; 0/13 ART sub-tests achieved successful injection (11 blocked by
  ;; AV/EDR signature detection under the av-active precondition, 1
  ;; network-resolution failure, 1 access-denied). Total technique
  ;; failure, already an established finding - reported in the
  ;; failure-mode table, not modelled as an action.
  ;; ------------------------------------------------------------
)
