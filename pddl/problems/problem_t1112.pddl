;; T1112 Modify Registry - converged cmd/powershell registry-write cluster
(define (problem t1112-p1)
  (:domain aurora-mini)
  (:init (cmd-invokable) (user-has-admin-privileges))
  (:goal (and (registry-key-modified)))
)
