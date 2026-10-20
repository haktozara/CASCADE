;; ============================================================
;; domain.pddl
;; Aurora-mini: five-category predicate scheme
;; (Executor, Process, Privilege/User, Information, Environment)
;;
;; Starter attack chain:
;;   T1059.001 -> T1547.001 -> T1003.001 -> T1021.002
;;
;; STATUS OF EACH ACTION:
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

    ;; --- Process category ---
    (process-running)                  ;; a process instance is running (T1059.001 effect)

    ;; --- Privilege/User category ---
    (user-has-write-access-hkcu-run-key)   ;; baseline precondition, true for virtually any
                                            ;; logged-in Windows user - included for category
                                            ;; completeness (T1547.001)
    (user-has-admin-privileges)            ;; local admin group membership confirmed
    (remote-admin-token-unfiltered)        ;; LocalAccountTokenFilterPolicy allows remote admin
                                            ;; token to pass (distinct from holding admin
                                            ;; privilege itself - causal A/B finding, T1021.002)

    ;; --- Information category ---
    (arbitrary-code-executed)          ;; capability demonstrated by T1059.001
    (registry-key-written)             ;; artifact-produced view of the T1547.001 write
    (credentials-obtained)             ;; PLACEHOLDER - T1003.001, no successful evidence

    ;; --- Environment category ---
    (registry-run-key-set)             ;; state-change view of the T1547.001 write
    (admin-share-reachable)            ;; target admin share (C$/ADMIN$) exists and is visible
    (admin-share-mapped)               ;; share successfully mapped/written to (T1021.002 effect)
    (lsass-memory-accessible)          ;; PLACEHOLDER - stands in for "no AV/Credential Guard
                                        ;; block", never observed true on the VM (T1003.001)

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
)
