;; T1560.001 Archive via Utility - Tests #3/#4 converge
(define (problem t1560-001-p1)
  (:domain aurora-mini)
  (:init (archive-utility-installed))
  (:goal (and (file-created)))
)
