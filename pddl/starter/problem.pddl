;; ============================================================
;; problem.pddl
;; Starter chain: T1059.001 -> T1547.001 -> T1003.001 -> T1021.002
;;
;; Initial state = the environment/privilege facts that hold true
;; BEFORE any technique runs, based on the VM evidence collected so
;; far (localhost-scoped, DESKTOP-C1VFPEU, local admin account).
;;
;; lsass-memory-accessible is set true here ONLY so the planner can
;; walk the full four-step chain for this first validation pass. On
;; your real VM this was never actually true (all T1003.001 sub-tests
;; failed) - this is a deliberate placeholder loosening, not a claim
;; about the real environment. Flag this in your write-up if you keep
;; using this problem file beyond the initial pipeline check.
;; ============================================================

(define (problem starter-chain-p1)
  (:domain aurora-mini)

  (:init
    ;; --- Executor / baseline access ---
    (powershell-present)
    (cmd-invokable)

    ;; --- Privilege/User ---
    (user-has-write-access-hkcu-run-key)
    (user-has-admin-privileges)
    (remote-admin-token-unfiltered)

    ;; --- Environment ---
    (admin-share-reachable)
    (lsass-memory-accessible)   ;; PLACEHOLDER - see header note
  )

  (:goal (and
    (lateral-movement-achieved)
  ))
)
