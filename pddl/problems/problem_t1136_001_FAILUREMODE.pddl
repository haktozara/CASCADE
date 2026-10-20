;; T1136.001 Create Local Account - NO ACTION MODELLED (3/4 sub-tests access-denied
;; under declared elevated-privilege, 1 ambiguous/no-effect).
;; Expected result: "Search stopped without finding a solution" - same structural
;; point as T1041 above.
(define (problem t1136-001-p1-EXPECTED-UNSOLVABLE)
  (:domain aurora-mini)
  (:init (cmd-invokable) (user-has-admin-privileges))
  (:goal (and (local-account-created)))
)
