;; T1018 Remote System Discovery - two-path finding (Test #5 no-priv, Test #8 admin-gated)
;; This problem includes BOTH preconditions to confirm at least one path solves the goal.
(define (problem t1018-p1)
  (:domain aurora-mini)
  (:init (cmd-invokable) (powershell-invokable) (user-has-admin-privileges))
  (:goal (and (network-hosts-discovered)))
)
