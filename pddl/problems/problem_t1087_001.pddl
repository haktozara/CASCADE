;; T1087.001 Account Discovery - Test #8
(define (problem t1087-001-p1)
  (:domain aurora-mini)
  (:init (cmd-invokable))
  (:goal (and (accounts-enumerated) (credentials-discovered)))
)
