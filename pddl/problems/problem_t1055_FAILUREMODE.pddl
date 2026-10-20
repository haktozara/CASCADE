;; T1055 Process Injection - NO ACTION MODELLED (0/13 sub-tests succeeded;
;; 11 blocked by AV/EDR signature detection, 1 network-resolution failure,
;; 1 access-denied).
;; Expected result: "Search stopped without finding a solution" - same structural
;; point as above.
(define (problem t1055-p1-EXPECTED-UNSOLVABLE)
  (:domain aurora-mini)
  (:init (powershell-invokable) (file-exists))
  (:goal (and (process-injected)))
)
