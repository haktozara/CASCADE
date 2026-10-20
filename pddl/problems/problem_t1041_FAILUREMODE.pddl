;; T1041 Exfiltration Over C2 Channel - NO ACTION MODELLED (0/2 sub-tests succeeded:
;; Test #1 proxy resolution failure, Test #2 DNS query failure on invalid character).
;; Expected result: "Search stopped without finding a solution." This confirms
;; total-failure is structural - data-exfiltrated is declared in domain.pddl but
;; no action produces it, so no plan can ever reach this goal.
(define (problem t1041-p1-EXPECTED-UNSOLVABLE)
  (:domain aurora-mini)
  (:init (powershell-invokable) (file-exists))
  (:goal (and (data-exfiltrated)))
)
