;; T1046 Network Service Scanning - Test #10
(define (problem t1046-p1)
  (:domain aurora-mini)
  (:init (powershell-invokable))
  (:goal (and (network-service-discovered)))
)
